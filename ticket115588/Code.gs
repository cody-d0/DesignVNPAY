// ═══════════════════════════════════════════════
// Google Apps Script — Phiếu Thu Backend
// Sheet = Single Source of Truth
// Copy toàn bộ file này vào Apps Script editor
// ═══════════════════════════════════════════════

const SHEET_NAME = 'Receipts';
const HEADERS = ['id','room','dateFrom','dateTo','name','el','wa','wi','rentMonths','rent','total','paid','paidAt','ts'];

// ── SETUP: Chạy 1 lần để tạo sheet + header ──
function setupSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) sheet = ss.insertSheet(SHEET_NAME);
  
  sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]);
  sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
  sheet.setFrozenRows(1);
  HEADERS.forEach((_, i) => sheet.autoResizeColumn(i + 1));
  
  Logger.log('✅ Sheet "Receipts" đã được tạo với ' + HEADERS.length + ' cột');
}

// ── POST Handler ──
function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(10000);
  
  try {
    const body = JSON.parse(e.postData.contents);
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    if (!sheet) return jsonOut({ success: false, error: 'Sheet not found' });
    
    // ── save (upsert single receipt) ──
    if (body.action === 'save') {
      const r = body.receipt;
      if (!r || !r.id) return jsonOut({ success: false, error: 'Missing receipt' });
      
      const rowData = HEADERS.map(h => r[h] !== undefined ? r[h] : '');
      const existingRow = findRow(sheet, r.id, r.room);
      
      if (existingRow > 0) {
        sheet.getRange(existingRow, 1, 1, HEADERS.length).setValues([rowData]);
      } else {
        sheet.appendRow(rowData);
      }
      return jsonOut({ success: true, action: 'saved', id: r.id });
    }
    
    // ── saveAll (bulk sync) ──
    if (body.action === 'saveAll') {
      const receipts = body.receipts || [];
      receipts.forEach(r => {
        const rowData = HEADERS.map(h => r[h] !== undefined ? r[h] : '');
        const existingRow = findRow(sheet, r.id, r.room);
        if (existingRow > 0) {
          sheet.getRange(existingRow, 1, 1, HEADERS.length).setValues([rowData]);
        } else {
          sheet.appendRow(rowData);
        }
      });
      return jsonOut({ success: true, action: 'saveAll', saved: receipts.length });
    }
    
    // ── delete (single receipt) ──
    if (body.action === 'delete') {
      const existingRow = findRow(sheet, body.id, body.room);
      if (existingRow > 0) {
        sheet.deleteRow(existingRow);
        return jsonOut({ success: true, action: 'deleted' });
      }
      return jsonOut({ success: true, action: 'deleted', note: 'not found' });
    }
    
    // ── deleteAll (bulk delete — all data or by room) ──
    if (body.action === 'deleteAll') {
      return doDeleteAll(sheet, body.room);
    }
    
    return jsonOut({ success: false, error: 'Unknown action' });
    
  } catch (err) {
    return jsonOut({ success: false, error: err.toString() });
  } finally {
    lock.releaseLock();
  }
}

// ── GET Handler ──
function doGet(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    if (!sheet) return jsonOut({ success: false, error: 'Sheet not found' });
    
    // Support deleteAll via GET (fallback for no-cors POST issues)
    if (e.parameter.action === 'deleteAll') {
      const lock = LockService.getScriptLock();
      lock.tryLock(10000);
      try {
        const result = doDeleteAll(sheet, e.parameter.room);
        return result;
      } finally {
        lock.releaseLock();
      }
    }
    
    const rows = sheet.getDataRange().getValues();
    if (rows.length <= 1) return jsonOut({ success: true, data: [] });
    
    const headers = rows[0];
    const room = e.parameter.room;
    const receipts = [];
    
    for (let i = 1; i < rows.length; i++) {
      const obj = {};
      headers.forEach((h, idx) => {
        let val = rows[i][idx];
        if (['el','wa','wi','rentMonths','rent','total'].includes(h)) val = Number(val) || 0;
        if (h === 'paid') val = val === true || val === 'true';
        obj[h] = val;
      });
      if (!room || obj.room === room) receipts.push(obj);
    }
    
    receipts.sort((a, b) => (b.ts || '').localeCompare(a.ts || ''));
    return jsonOut({ success: true, data: receipts, total: receipts.length });
    
  } catch (err) {
    return jsonOut({ success: false, error: err.toString() });
  }
}

// ── deleteAll helper (used by both GET and POST) ──
function doDeleteAll(sheet, room) {
  const lastRow = sheet.getLastRow();
  if (lastRow <= 1) return jsonOut({ success: true, action: 'deleteAll', deleted: 0 });
  
  if (!room) {
    // Delete ALL data rows at once (keep header)
    sheet.deleteRows(2, lastRow - 1);
    return jsonOut({ success: true, action: 'deleteAll', deleted: lastRow - 1 });
  }
  
  // Delete by room (bottom-up)
  const data = sheet.getDataRange().getValues();
  let deleted = 0;
  for (let i = data.length - 1; i >= 1; i--) {
    if (String(data[i][1]) === String(room)) {
      sheet.deleteRow(i + 1);
      deleted++;
    }
  }
  return jsonOut({ success: true, action: 'deleteAll', deleted });
}

// ── Helpers ──
function findRow(sheet, id, room) {
  const data = sheet.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (String(data[i][0]) === String(id) && String(data[i][1]) === String(room)) return i + 1;
  }
  return -1;
}

function jsonOut(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
