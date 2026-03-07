/**
 * DemoKit v2 — Micro-lib for interactive HTML demos
 * Zero dependencies. Web Components + Functional API.
 * Auto-injects CSS on load.
 *
 * WEB COMPONENTS (declarative):
 *   <dk-callout type="tip|warn|good">     Styled callout block
 *   <dk-code label="...">                 Code block with label
 *   <dk-grid cols="2|3">                  Responsive grid
 *   <dk-box color="..." title="..."       Styled box with colored border
 *           border="top|left">
 *   <dk-panel title="...">                Panel container
 *   <dk-toggle summary="...">             Collapsible section
 *   <dk-counter value="..." label="...">  Big counter display
 *
 * JS API (imperative):
 *   DK.init(opts?)          Build nav from data-title, wire sections
 *   DK.go(i)                Navigate to section i
 *   DK.onSection(i, fn)     Lazy-init callback when section i shown
 *   DK.panel(el, opts)      Button-group → result panel
 *   DK.steps(el, opts)      Step animation, returns run()
 *   DK.graph(el, opts)      Draggable node-edge graph, returns controller
 *   DK.fileTree(el, opts)   Interactive file tree with click-to-check
 *   DK.toggle(id)           Show/hide element
 *   DK.editor(el, opts)     Code textarea + run button
 *   DK.compare(el, opts)    Side-by-side comparison boxes
 *   DK.el(id)               getElementById shorthand
 */
;(function () {
  'use strict';

  // ═══════════════════════════════════════════════════════
  // 1. CSS — auto-loaded from external demo-kit.css
  // ═══════════════════════════════════════════════════════
  var scriptEl = document.currentScript;
  var basePath = scriptEl ? scriptEl.src.replace(/demo-kit\.js$/, '') : 'assets/';
  var linkEl = document.createElement('link');
  linkEl.rel = 'stylesheet';
  linkEl.href = basePath + 'demo-kit.css';
  linkEl.id = 'dk-css';
  document.head.appendChild(linkEl);

  // ═══════════════════════════════════════════════════════
  // 2. DK NAMESPACE
  // ═══════════════════════════════════════════════════════
  var DK = {};
  var _cb = {};
  var _inited = {};
  var _uid = 0;
  function uid() { return 'dk' + (++_uid); }

  // ═══════════════════════════════════════════════════════
  // 3. NAVIGATION
  // ═══════════════════════════════════════════════════════

  DK.init = function (opts) {
    opts = opts || {};
    var sections = document.querySelectorAll('.section');
    if (!sections.length) return;

    if (opts.css) {
      var extra = document.createElement('style');
      extra.textContent = opts.css;
      document.head.appendChild(extra);
    }

    var nav = document.createElement('nav');
    nav.className = 'nav';
    sections.forEach(function (s, i) {
      var btn = document.createElement('button');
      btn.className = 'nav-btn' + (i === 0 ? ' active' : '');
      btn.textContent = s.dataset.title || 'Section ' + i;
      btn.addEventListener('click', function () { DK.go(i); });
      nav.appendChild(btn);
      if (i === 0) s.classList.add('active');
      else s.classList.remove('active');
    });
    document.body.insertBefore(nav, document.body.firstChild);
  };

  DK.go = function (i) {
    var sections = document.querySelectorAll('.section');
    var btns = document.querySelectorAll('.nav-btn');
    sections.forEach(function (s, idx) { s.classList.toggle('active', idx === i); });
    btns.forEach(function (b, idx) { b.classList.toggle('active', idx === i); });
    window.scrollTo(0, 0);
    if (_cb[i] && !_inited[i]) {
      _inited[i] = true;
      _cb[i]();
    }
  };

  DK.onSection = function (i, fn) { _cb[i] = fn; };

  // ═══════════════════════════════════════════════════════
  // 4. PANEL — button-group → result
  // ═══════════════════════════════════════════════════════

  DK.panel = function (el, opts) {
    var title = opts.title || '';
    var buttons = opts.buttons || [];
    var render = opts.render;
    var defaultIdx = opts.defaultIndex != null ? opts.defaultIndex : 0;
    var id = uid();

    el.innerHTML =
      '<div class="panel">' +
        '<div class="panel-t">' + title + '</div>' +
        '<div class="btn-row" id="' + id + '_b"></div>' +
        '<div class="result" id="' + id + '_r"></div>' +
      '</div>';

    var btnRow = document.getElementById(id + '_b');
    var resultEl = document.getElementById(id + '_r');

    buttons.forEach(function (label, i) {
      var btn = document.createElement('button');
      btn.className = 'btn btn-sm' + (i === defaultIdx ? ' active' : '');
      btn.textContent = label;
      btn.addEventListener('click', function () {
        btnRow.querySelectorAll('.btn').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        render(i, resultEl);
      });
      btnRow.appendChild(btn);
    });

    if (render) render(defaultIdx, resultEl);
    return resultEl;
  };

  // ═══════════════════════════════════════════════════════
  // 5. STEPS — step-by-step animation
  // ═══════════════════════════════════════════════════════

  DK.steps = function (el, opts) {
    var data = opts.data || [];
    var result = opts.result || '';
    var delay = opts.delay || 1000;
    var onStep = opts.onStep || null;
    var id = uid();

    var listEl = document.createElement('div');
    listEl.className = 'step-list';
    listEl.id = id + '_list';
    el.appendChild(listEl);

    var resultEl = null;
    if (result) {
      resultEl = document.createElement('div');
      resultEl.className = 'result';
      resultEl.id = id + '_result';
      resultEl.style.color = 'var(--green)';
      el.appendChild(resultEl);
    }

    return function run() {
      if (resultEl) resultEl.textContent = '';
      listEl.innerHTML = data.map(function (s, i) {
        return '<div class="step-item" id="' + id + '_s' + i + '">' +
          '<div class="step-num">' + (i + 1) + '</div>' +
          '<div class="step-text">' + s.text + '</div>' +
        '</div>';
      }).join('');

      var si = 0;
      function next() {
        if (si >= data.length) {
          if (resultEl && result) resultEl.textContent = result;
          return;
        }
        var stepEl = document.getElementById(id + '_s' + si);
        stepEl.classList.add('active');
        if (onStep) onStep(si, data[si]);
        si++;
        setTimeout(next, delay);
      }
      setTimeout(next, 300);
    };
  };

  // ═══════════════════════════════════════════════════════
  // 6. GRAPH — draggable node-edge visualization
  // ═══════════════════════════════════════════════════════

  DK.graph = function (el, opts) {
    var nodes = opts.nodes || [];
    var edges = opts.edges || [];
    var onClick = opts.onClick || null;
    var height = opts.height || 460;
    var id = uid();

    el.classList.add('live-graph');
    el.style.height = height + 'px';
    el.innerHTML =
      '<svg class="edges" id="' + id + '_svg"></svg>' +
      '<div class="node-info" id="' + id + '_info" style="display:none;"></div>';

    var svg = document.getElementById(id + '_svg');
    var infoEl = document.getElementById(id + '_info');

    nodes.forEach(function (n) {
      var size = n.size || (n.type === 'Project' ? 56 : n.type === 'Screen' ? 50 : 46);
      var nodeEl = document.createElement('div');
      nodeEl.className = 'node';
      nodeEl.style.width = size + 'px';
      nodeEl.style.height = size + 'px';
      nodeEl.style.left = (n.x - size / 2) + 'px';
      nodeEl.style.top = (n.y - size / 2) + 'px';
      nodeEl.style.background = n.color + '18';
      nodeEl.style.border = '2px solid ' + n.color;
      nodeEl.style.color = n.color;
      nodeEl.style.fontSize = size < 50 ? '.6rem' : '.65rem';
      var short = n.id.length > 6 ? n.id.slice(0, 5) + '\u2026' : n.id;
      nodeEl.innerHTML = short + '<span class="node-lbl">' + n.id + '</span>';
      nodeEl.dataset.id = n.id;
      nodeEl.addEventListener('mousedown', function (ev) {
        _dragStart(ev, n, el, nodes, edges, svg);
      });
      if (onClick) {
        nodeEl.addEventListener('click', function () { onClick(n, infoEl); });
      }
      el.appendChild(nodeEl);
    });

    _drawEdges(el, nodes, edges, svg);

    return {
      highlight: function (nodeIds) {
        el.querySelectorAll('.node').forEach(function (nd) {
          var match = !nodeIds || nodeIds.indexOf(nd.dataset.id) >= 0;
          nd.style.opacity = match ? '1' : '0.12';
          nd.style.boxShadow = (match && nodeIds) ? ('0 0 16px ' + nd.style.borderColor) : 'none';
        });
        svg.querySelectorAll('line').forEach(function (l) {
          var match = !nodeIds || (nodeIds.indexOf(l.dataset.from) >= 0 && nodeIds.indexOf(l.dataset.to) >= 0);
          l.setAttribute('stroke', match ? '#a78bfaaa' : '#a78bfa11');
          l.setAttribute('stroke-width', match ? '2.5' : '1');
        });
        el.querySelectorAll('.edge-lbl').forEach(function (l) {
          var match = !nodeIds || (nodeIds.indexOf(l.dataset.from) >= 0 && nodeIds.indexOf(l.dataset.to) >= 0);
          l.style.opacity = match ? '1' : '0.1';
        });
      },
      reset: function () { this.highlight(null); },
      redraw: function () { _drawEdges(el, nodes, edges, svg); },
      showInfo: function (html, duration) {
        infoEl.innerHTML = html;
        infoEl.style.display = 'block';
        if (duration !== 0) {
          setTimeout(function () { infoEl.style.display = 'none'; }, duration || 5000);
        }
      },
      svg: svg,
      infoEl: infoEl
    };
  };

  function _drawEdges(container, nodes, edges, svg) {
    svg.innerHTML = '';
    container.querySelectorAll('.edge-lbl').forEach(function (l) { l.remove(); });
    edges.forEach(function (e) {
      var fn = null, tn = null;
      for (var i = 0; i < nodes.length; i++) {
        if (nodes[i].id === e.from) fn = nodes[i];
        if (nodes[i].id === e.to) tn = nodes[i];
      }
      if (!fn || !tn) return;

      var line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', fn.x); line.setAttribute('y1', fn.y);
      line.setAttribute('x2', tn.x); line.setAttribute('y2', tn.y);
      line.setAttribute('stroke', '#a78bfa33');
      line.setAttribute('stroke-width', '1.5');
      line.dataset.from = e.from;
      line.dataset.to = e.to;
      svg.appendChild(line);

      var ang = Math.atan2(tn.y - fn.y, tn.x - fn.x);
      var sz = (tn.size || (tn.type === 'Project' ? 56 : tn.type === 'Screen' ? 50 : 46)) / 2 + 4;
      var ex = tn.x - Math.cos(ang) * sz;
      var ey = tn.y - Math.sin(ang) * sz;
      var a1x = ex - 8 * Math.cos(ang - 0.4);
      var a1y = ey - 8 * Math.sin(ang - 0.4);
      var a2x = ex - 8 * Math.cos(ang + 0.4);
      var a2y = ey - 8 * Math.sin(ang + 0.4);
      var arrow = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
      arrow.setAttribute('points', ex + ',' + ey + ' ' + a1x + ',' + a1y + ' ' + a2x + ',' + a2y);
      arrow.setAttribute('fill', '#a78bfa66');
      svg.appendChild(arrow);

      var lbl = document.createElement('div');
      lbl.className = 'edge-lbl';
      lbl.textContent = e.label;
      lbl.style.left = ((fn.x + tn.x) / 2 - 28) + 'px';
      lbl.style.top = ((fn.y + tn.y) / 2 - 8) + 'px';
      lbl.dataset.from = e.from;
      lbl.dataset.to = e.to;
      container.appendChild(lbl);
    });
  }

  function _dragStart(ev, node, container, nodes, edges, svg) {
    ev.preventDefault();
    var rect = container.getBoundingClientRect();
    var offX = ev.clientX - rect.left - node.x;
    var offY = ev.clientY - rect.top - node.y;

    function onMove(e) {
      node.x = Math.max(30, Math.min(rect.width - 30, e.clientX - rect.left - offX));
      node.y = Math.max(30, Math.min(rect.height - 30, e.clientY - rect.top - offY));
      var el = container.querySelector('[data-id="' + node.id + '"]');
      var sz = parseInt(el.style.width);
      el.style.left = (node.x - sz / 2) + 'px';
      el.style.top = (node.y - sz / 2) + 'px';
      _drawEdges(container, nodes, edges, svg);
    }
    function onUp() {
      document.removeEventListener('mousemove', onMove);
      document.removeEventListener('mouseup', onUp);
    }
    document.addEventListener('mousemove', onMove);
    document.addEventListener('mouseup', onUp);
  }

  // ═══════════════════════════════════════════════════════
  // 7. FILE TREE — interactive click-to-check
  // ═══════════════════════════════════════════════════════

  DK.fileTree = function (el, opts) {
    var files = opts.files || [];
    var onCheck = opts.onCheck || function () {};
    var id = uid();
    var checked = 0;
    var matches = [];

    el.classList.add('file-tree');
    el.innerHTML = files.map(function (f, i) {
      return '<div>\u{1F4C4} <span id="' + id + '_' + i + '">' + f.path + '</span></div>';
    }).join('');

    files.forEach(function (f, i) {
      var span = document.getElementById(id + '_' + i);
      span.addEventListener('click', function () {
        if (span.classList.contains('checked')) return;
        span.classList.add('checked');
        checked++;
        if (f.match) {
          matches.push(f.name || f.path);
          span.style.color = 'var(--green)';
          span.textContent += ' \u2705 C\u00d3 d\u00f9ng!';
        } else {
          span.textContent += ' \u2014 kh\u00f4ng d\u00f9ng';
        }
        onCheck(checked, files.length, matches);
      });
    });
  };

  // ═══════════════════════════════════════════════════════
  // 8. HELPERS
  // ═══════════════════════════════════════════════════════

  DK.toggle = function (id) {
    var el = typeof id === 'string' ? document.getElementById(id) : id;
    if (el) el.style.display = el.style.display === 'none' ? 'block' : 'none';
  };

  DK.editor = function (el, opts) {
    var code = opts.code || '';
    var onRun = opts.onRun;
    var placeholder = opts.placeholder || '';
    var lang = opts.lang || '';
    var id = uid();

    el.innerHTML =
      '<textarea class="qi" id="' + id + '_in" rows="' + (opts.rows || 4) + '"' +
        (placeholder ? ' placeholder="' + placeholder + '"' : '') +
      '>' + code + '</textarea>' +
      '<div style="margin-top:.4rem;">' +
        '<button class="btn" id="' + id + '_run">\u25B6 Run</button>' +
        (lang ? ' <span style="color:var(--muted);font-size:.7rem;">' + lang + '</span>' : '') +
      '</div>' +
      '<div class="result" id="' + id + '_out"></div>';

    var inputEl = document.getElementById(id + '_in');
    var outputEl = document.getElementById(id + '_out');

    document.getElementById(id + '_run').addEventListener('click', function () {
      var result = onRun(inputEl.value);
      if (typeof result === 'string') outputEl.textContent = result;
      else if (result && result.nodeType) {
        outputEl.innerHTML = '';
        outputEl.appendChild(result);
      }
    });

    return { input: inputEl, output: outputEl };
  };

  DK.compare = function (el, opts) {
    var left = opts.left || {};
    var right = opts.right || {};

    function renderSide(side) {
      var borderStyle = side.color ? 'border-top:3px solid var(--' + side.color + ');' : '';
      var titleColor = side.color ? ' style="color:var(--' + side.color + ');"' : '';
      return '<div class="box" style="' + borderStyle + '">' +
        (side.title ? '<h4' + titleColor + '>' + side.title + '</h4>' : '') +
        (side.content || '') +
      '</div>';
    }

    el.innerHTML = '<div class="cmp">' + renderSide(left) + renderSide(right) + '</div>';
  };

  DK.el = function (id) { return document.getElementById(id); };

  // ═══════════════════════════════════════════════════════
  // 9. WEB COMPONENTS
  // ═══════════════════════════════════════════════════════

  // <dk-callout type="tip|warn|good"> content </dk-callout>
  customElements.define('dk-callout', class extends HTMLElement {
    connectedCallback() {
      this.classList.add(this.getAttribute('type') || 'tip');
    }
  });

  // <dk-code label="..."> syntax highlighted content </dk-code>
  customElements.define('dk-code', class extends HTMLElement {
    connectedCallback() {
      var self = this;
      // Defer: connectedCallback fires before children are parsed when script is in <head>
      setTimeout(function() {
        var label = self.getAttribute('label');
        var content = self.innerHTML.replace(/^\s*\n/, '').replace(/\n\s*$/, '');
        self.innerHTML = '<pre class="sql">' +
          (label ? '<span class="lbl">' + label + '</span>' : '') +
          content + '</pre>';
      }, 0);
    }
  });

  // <dk-grid cols="2|3"> children </dk-grid>
  // Styling handled by CSS attribute selectors
  customElements.define('dk-grid', class extends HTMLElement {
    connectedCallback() { /* CSS handles cols via dk-grid[cols="2"] */ }
  });

  // <dk-box color="red" title="..." border="top|left"> content </dk-box>
  customElements.define('dk-box', class extends HTMLElement {
    connectedCallback() {
      this.classList.add('box');
      var color = this.getAttribute('color');
      var title = this.getAttribute('title');
      var border = this.getAttribute('border') || 'top';
      if (color) {
        this.style[border === 'left' ? 'borderLeft' : 'borderTop'] = '3px solid var(--' + color + ')';
      }
      if (title) {
        var h4 = document.createElement('h4');
        h4.style.color = color ? 'var(--' + color + ')' : '';
        h4.innerHTML = title;
        this.insertBefore(h4, this.firstChild);
      }
    }
  });

  // <dk-panel title="..."> content </dk-panel>
  customElements.define('dk-panel', class extends HTMLElement {
    connectedCallback() {
      this.classList.add('panel');
      var title = this.getAttribute('title');
      if (title) {
        var t = document.createElement('div');
        t.className = 'panel-t';
        t.textContent = title;
        this.insertBefore(t, this.firstChild);
      }
    }
  });

  // <dk-toggle summary="..."> hidden content </dk-toggle>
  customElements.define('dk-toggle', class extends HTMLElement {
    connectedCallback() {
      var self = this;
      // Defer: connectedCallback fires before children are parsed when script is in <head>
      setTimeout(function() {
        var summary = self.getAttribute('summary') || 'Details';
        var content = self.innerHTML;
        self.innerHTML =
          '<div class="box" style="cursor:pointer;">' +
            '<div class="dk-t-hdr" style="display:flex;justify-content:space-between;align-items:center;">' +
              '<strong style="font-size:.85rem;">' + summary + '</strong>' +
              '<span style="color:var(--muted);font-size:.75rem;">\u25BC</span>' +
            '</div>' +
            '<div class="dk-t-body" style="display:none;margin-top:.6rem;">' + content + '</div>' +
          '</div>';
        var hdr = self.querySelector('.dk-t-hdr');
        hdr.addEventListener('click', function () {
          var body = hdr.nextElementSibling;
          var arrow = hdr.querySelector('span');
          if (body.style.display === 'none') {
            body.style.display = 'block';
            arrow.textContent = '\u25B2';
          } else {
            body.style.display = 'none';
            arrow.textContent = '\u25BC';
          }
        });
      }, 0);
    }
  });

  // <dk-counter value="..." label="...">
  customElements.define('dk-counter', class extends HTMLElement {
    connectedCallback() {
      this.innerHTML =
        '<div class="counter">' + (this.getAttribute('value') || '0') + '</div>' +
        (this.getAttribute('label') ? '<div class="counter-label">' + this.getAttribute('label') + '</div>' : '');
    }
    static get observedAttributes() { return ['value']; }
    attributeChangedCallback(name, oldVal, newVal) {
      if (name === 'value') {
        var c = this.querySelector('.counter');
        if (c) c.textContent = newVal;
      }
    }
  });

  // ═══════════════════════════════════════════════════════
  // EXPOSE
  // ═══════════════════════════════════════════════════════
  window.DK = DK;

})();
