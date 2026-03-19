# Template: API Caller

Script gọi APIs có retry, rate limiting, và pagination.

## Khi nào dùng

- Fetch data từ REST/GraphQL APIs
- Sync data giữa services
- Webhook processors
- API migration tools

## Node.js Skeleton

```javascript
#!/usr/bin/env node
'use strict';

/**
 * API Client with retry, rate limiting, and pagination.
 */

// ─── Rate Limiter ───────────────────────────────────────────
class RateLimiter {
  constructor(maxPerSecond = 10) {
    this.minInterval = 1000 / maxPerSecond;
    this.lastCall = 0;
    this.queue = [];
  }

  async acquire() {
    const now = Date.now();
    const wait = Math.max(0, this.minInterval - (now - this.lastCall));
    if (wait > 0) await new Promise(r => setTimeout(r, wait));
    this.lastCall = Date.now();
  }
}

// ─── Retry Logic ────────────────────────────────────────────
async function withRetry(fn, {
  maxAttempts = 3,
  baseDelay = 1000,
  maxDelay = 30000,
  retryOn = [429, 500, 502, 503, 504],
} = {}) {
  let lastError;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await fn();
    } catch (err) {
      lastError = err;

      // Check if retryable
      const status = err.status || err.statusCode;
      if (status && !retryOn.includes(status)) throw err;

      if (attempt === maxAttempts) throw err;

      // Exponential backoff with jitter
      let delay = Math.min(baseDelay * Math.pow(2, attempt - 1), maxDelay);
      delay += Math.random() * delay * 0.1; // 10% jitter

      // Respect Retry-After header
      if (err.retryAfter) {
        delay = Math.max(delay, err.retryAfter * 1000);
      }

      console.warn(`  ⚠️  Attempt ${attempt}/${maxAttempts} failed (${err.message}). Retry in ${Math.round(delay)}ms`);
      await new Promise(r => setTimeout(r, delay));
    }
  }
  throw lastError;
}

// ─── API Client ─────────────────────────────────────────────
class ApiClient {
  constructor({ baseUrl, token, rateLimit = 10 }) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.headers = {
      'Content-Type': 'application/json',
      ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    };
    this.limiter = new RateLimiter(rateLimit);
    this.stats = { requests: 0, retries: 0, errors: 0 };
  }

  async request(method, path, { body, query, timeout = 30000 } = {}) {
    await this.limiter.acquire();

    const url = new URL(path, this.baseUrl);
    if (query) {
      Object.entries(query).forEach(([k, v]) => {
        if (v !== undefined) url.searchParams.set(k, String(v));
      });
    }

    this.stats.requests++;

    return withRetry(async () => {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), timeout);

      try {
        const res = await fetch(url.toString(), {
          method,
          headers: this.headers,
          body: body ? JSON.stringify(body) : undefined,
          signal: controller.signal,
        });

        if (!res.ok) {
          const error = new Error(`${method} ${path}: ${res.status} ${res.statusText}`);
          error.status = res.status;
          if (res.headers.get('retry-after')) {
            error.retryAfter = parseInt(res.headers.get('retry-after'), 10);
          }
          throw error;
        }

        return await res.json();
      } finally {
        clearTimeout(timer);
      }
    });
  }

  get(path, opts)    { return this.request('GET', path, opts); }
  post(path, opts)   { return this.request('POST', path, opts); }
  put(path, opts)    { return this.request('PUT', path, opts); }
  delete(path, opts) { return this.request('DELETE', path, opts); }

  // ─── Pagination ─────────────────────────────────────────
  async *paginate(path, { pageSize = 100, pageParam = 'page', sizeParam = 'per_page' } = {}) {
    let page = 1;
    let hasMore = true;

    while (hasMore) {
      const data = await this.get(path, {
        query: { [pageParam]: page, [sizeParam]: pageSize },
      });

      const items = Array.isArray(data) ? data : data.items || data.data || [];
      yield* items;

      hasMore = items.length >= pageSize;
      page++;
    }
  }
}

// ─── Usage ──────────────────────────────────────────────────
async function main() {
  const client = new ApiClient({
    baseUrl: process.env.API_URL || 'https://api.example.com',
    token: process.env.API_TOKEN,
    rateLimit: 5,
  });

  // Paginated fetch
  const allItems = [];
  for await (const item of client.paginate('/v1/items', { pageSize: 50 })) {
    allItems.push(item);
    if (allItems.length % 100 === 0) {
      console.log(`  Fetched ${allItems.length} items...`);
    }
  }

  console.log(`✅ Total: ${allItems.length} items`);
  console.log(`📊 Stats: ${JSON.stringify(client.stats)}`);
}

main().catch(err => {
  console.error('💥', err.message);
  process.exit(1);
});
```

## Bash Skeleton — curl-Based

```bash
#!/usr/bin/env bash
set -euo pipefail

API_URL="${API_URL:?Set API_URL}"
API_TOKEN="${API_TOKEN:?Set API_TOKEN}"

# ─── Rate-limited curl ──────────────────────────────────────
api_call() {
  local method="$1" endpoint="$2"
  shift 2

  local response
  response=$(curl -s -w "\n%{http_code}" \
    -X "$method" \
    -H "Authorization: Bearer $API_TOKEN" \
    -H "Content-Type: application/json" \
    "$@" \
    "${API_URL}${endpoint}")

  local body="${response%$'\n'*}"
  local code="${response##*$'\n'}"

  if [[ "$code" -ge 400 ]]; then
    echo "API Error $code: $body" >&2
    return 1
  fi

  echo "$body"
  sleep 0.1  # Simple rate limit
}

# Usage: api_call GET /v1/items
# Usage: api_call POST /v1/items -d '{"name":"test"}'
```
