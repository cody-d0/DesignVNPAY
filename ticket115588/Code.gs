// ═══════════════════════════════════════════════
// Google Apps Script — Phiếu Thu v3
// ALL operations via doGet (100% reliable)
// ═══════════════════════════════════════════════

var SHEET_NAME = 'Receipts';
var HEADERS = ['id','room','dateFrom','dateTo','name','el','wa','wi','rentMonths','rent','total','paid','paidAt','ts'];

function setupSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) sheet = ss.insertSheet(SHEET_NAME);
  sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]);
  sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
  sheet.setFrozenRows(1);
  Logger.log('Done - sheet created');
}

function doGet(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(15000);
  
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    if (!sheet) return out({success:false, error:'Run setupSheet() first'});
    
    var action = e.parameter.action || 'list';
    
    // ── SAVE ──
    if (action === 'save') {
      var id = e.parameter.id;
      var room = e.parameter.room;
      if (!id || !room) return out({success:false, error:'Missing id/room'});
      
      var row = [];
      for (var h = 0; h < HEADERS.length; h++) {
        row.push(e.parameter[HEADERS[h]] || '');
      }
      
      var existing = findRow(sheet, id, room);
      if (existing > 0) {
        sheet.getRange(existing, 1, 1, HEADERS.length).setValues([row]);
      } else {
        sheet.appendRow(row);
      }
      return out({success:true, action:'saved', id:id});
    }
    
    // ── DELETE single ──
    if (action === 'delete') {
      var f = findRow(sheet, e.parameter.id, e.parameter.room);
      if (f > 0) sheet.deleteRow(f);
      return out({success:true, action:'deleted'});
    }
    
    // ── DELETE ALL ──
    if (action === 'deleteAll') {
      var lastRow = sheet.getLastRow();
      if (lastRow > 1) sheet.deleteRows(2, lastRow - 1);
      return out({success:true, action:'deleteAll', deleted: Math.max(0, lastRow - 1)});
    }
    
    // ── LIST (default) ──
    var rows = sheet.getDataRange().getValues();
    if (rows.length <= 1) return out({success:true, data:[]});
    
    var headers = rows[0];
    var result = [];
    
    for (var i = 1; i < rows.length; i++) {
      var obj = {};
      for (var c = 0; c < headers.length; c++) {
        var val = rows[i][c];
        var key = headers[c];
        if (key==='el'||key==='wa'||key==='wi'||key==='rentMonths'||key==='rent'||key==='total') val = Number(val)||0;
        if (key==='paid') val = (val===true||val==='true'||val===true);
        obj[key] = val;
      }
      result.push(obj);
    }
    
    result.sort(function(a,b){ return (b.ts||'').localeCompare(a.ts||''); });
    return out({success:true, data:result});
    
  } catch(err) {
    return out({success:false, error:String(err)});
  } finally {
    lock.releaseLock();
  }
}

function doPost(e) {
  // Redirect POST to GET handler for compatibility
  return doGet(e);
}

function findRow(sheet, id, room) {
  if (!id) return -1;
  var data = sheet.getDataRange().getValues();
  for (var i = 1; i < data.length; i++) {
    if (String(data[i][0]) === String(id) && String(data[i][1]) === String(room)) return i + 1;
  }
  return -1;
}

function out(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
