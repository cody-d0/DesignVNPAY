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
  
  // Set headers
  sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]);
  
  // Bold + freeze header
  sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
  sheet.setFrozenRows(1);
  
  // Auto-resize columns
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
    if (!sheet) return jsonOut({ success: false, error: 'Sheet not found. Run setupSheet() first.' });
    
    // ── ACTION: save (upsert single receipt) ──
    if (body.action === 'save') {
      const r = body.receipt;
      if (!r || !r.id) return jsonOut({ success: false, error: 'Missing receipt data' });
      
      const rowData = HEADERS.map(h => r[h] !== undefined ? r[h] : '');
      const existingRow = findRow(sheet, r.id, r.room);
      
      if (existingRow > 0) {
        sheet.getRange(existingRow, 1, 1, HEADERS.length).setValues([rowData]);
      } else {
        sheet.appendRow(rowData);
      }
      
      return jsonOut({ success: true, action: 'saved', id: r.id });
    }
    
    // ── ACTION: saveAll (bulk sync from localStorage) ──
    if (body.action === 'saveAll') {
      const receipts = body.receipts || [];
      let saved = 0;
      
      receipts.forEach(r => {
        const rowData = HEADERS.map(h => r[h] !== undefined ? r[h] : '');
        const existingRow = findRow(sheet, r.id, r.room);
        
        if (existingRow > 0) {
          sheet.getRange(existingRow, 1, 1, HEADERS.length).setValues([rowData]);
        } else {
          sheet.appendRow(rowData);
        }
        saved++;
      });
      
      return jsonOut({ success: true, action: 'saveAll', saved: saved });
    }
    
    // ── ACTION: delete (single receipt) ──
    if (body.action === 'delete') {
      const existingRow = findRow(sheet, body.id, body.room);
      if (existingRow > 0) {
        sheet.deleteRow(existingRow);
        return jsonOut({ success: true, action: 'deleted' });
      }
      return jsonOut({ success: false, error: 'Not found' });
    }
    
    // ── ACTION: deleteAll (clear by room or everything) ──
    if (body.action === 'deleteAll') {
      const room = body.room;
      const data = sheet.getDataRange().getValues();
      const roomCol = 1; // 'room' column index
      
      // Delete matching rows from bottom to top (to preserve row indices)
      let deleted = 0;
      for (let i = data.length - 1; i >= 1; i--) {
        if (!room || String(data[i][roomCol]) === String(room)) {
          sheet.deleteRow(i + 1);
          deleted++;
        }
      }
      
      return jsonOut({ success: true, action: 'deleteAll', deleted: deleted });
    }
    
    return jsonOut({ success: false, error: 'Unknown action: ' + body.action });
    
  } catch (err) {
    return jsonOut({ success: false, error: err.toString() });
  } finally {
    lock.releaseLock();
  }
}

// ── GET Handler (list receipts — Sheet is source of truth) ──
function doGet(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    if (!sheet) return jsonOut({ success: false, error: 'Sheet not found' });
    
    const rows = sheet.getDataRange().getValues();
    if (rows.length <= 1) return jsonOut({ success: true, data: [] });
    
    const headers = rows[0];
    const room = e.parameter.room;
    const receipts = [];
    
    for (let i = 1; i < rows.length; i++) {
      const obj = {};
      headers.forEach((h, idx) => {
        let val = rows[i][idx];
        // Convert numeric fields
        if (['el','wa','wi','rentMonths','rent','total'].includes(h)) val = Number(val) || 0;
        if (h === 'paid') val = val === true || val === 'true';
        obj[h] = val;
      });
      
      if (!room || obj.room === room) {
        receipts.push(obj);
      }
    }
    
    // Sort newest first
    receipts.sort((a, b) => (b.ts || '').localeCompare(a.ts || ''));
    
    return jsonOut({ success: true, data: receipts, total: receipts.length });
    
  } catch (err) {
    return jsonOut({ success: false, error: err.toString() });
  }
}

// ── Helpers ──
function findRow(sheet, id, room) {
  const data = sheet.getDataRange().getValues();
  const idCol = 0;   // 'id' column
  const roomCol = 1; // 'room' column
  
  for (let i = 1; i < data.length; i++) {
    if (String(data[i][idCol]) === String(id) && String(data[i][roomCol]) === String(room)) {
      return i + 1; // 1-indexed row
    }
  }
  return -1;
}

function jsonOut(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
