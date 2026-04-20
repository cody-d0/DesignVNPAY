// ═══════════════════════════════════════════════
// Google Apps Script — Phiếu Thu Backend v2
// Sheet = Single Source of Truth
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
  Logger.log('Done');
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);
  try {
    var body = JSON.parse(e.postData.contents);
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    if (!sheet) return out({success:false, error:'No sheet'});

    if (body.action === 'save') {
      var r = body.receipt;
      if (!r || !r.id) return out({success:false, error:'No id'});
      var row = HEADERS.map(function(h){ return r[h] !== undefined ? r[h] : ''; });
      var existing = findRow(sheet, r.id, r.room);
      if (existing > 0) {
        sheet.getRange(existing, 1, 1, HEADERS.length).setValues([row]);
      } else {
        sheet.appendRow(row);
      }
      return out({success:true, action:'saved', id:r.id});
    }

    if (body.action === 'saveAll') {
      var receipts = body.receipts || [];
      for (var j = 0; j < receipts.length; j++) {
        var r2 = receipts[j];
        var row2 = HEADERS.map(function(h){ return r2[h] !== undefined ? r2[h] : ''; });
        var ex = findRow(sheet, r2.id, r2.room);
        if (ex > 0) {
          sheet.getRange(ex, 1, 1, HEADERS.length).setValues([row2]);
        } else {
          sheet.appendRow(row2);
        }
      }
      return out({success:true, action:'saveAll', saved:receipts.length});
    }

    if (body.action === 'delete') {
      var found = findRow(sheet, body.id, body.room);
      if (found > 0) sheet.deleteRow(found);
      return out({success:true, action:'deleted'});
    }

    if (body.action === 'deleteAll') {
      return clearSheet(sheet, body.room);
    }

    return out({success:false, error:'Unknown action'});
  } catch(err) {
    return out({success:false, error:String(err)});
  } finally {
    lock.releaseLock();
  }
}

function doGet(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    if (!sheet) return out({success:false, error:'No sheet'});

    // deleteAll via GET (fallback)
    if (e.parameter.action === 'deleteAll') {
      var lock = LockService.getScriptLock();
      lock.tryLock(10000);
      try {
        return clearSheet(sheet, e.parameter.room);
      } finally {
        lock.releaseLock();
      }
    }

    // delete single via GET (fallback)
    if (e.parameter.action === 'delete' && e.parameter.id) {
      var lock2 = LockService.getScriptLock();
      lock2.tryLock(10000);
      try {
        var f = findRow(sheet, e.parameter.id, e.parameter.room);
        if (f > 0) sheet.deleteRow(f);
        return out({success:true, action:'deleted'});
      } finally {
        lock2.releaseLock();
      }
    }

    // List all receipts
    var rows = sheet.getDataRange().getValues();
    if (rows.length <= 1) return out({success:true, data:[]});

    var headers = rows[0];
    var room = e.parameter.room;
    var result = [];

    for (var i = 1; i < rows.length; i++) {
      var obj = {};
      for (var c = 0; c < headers.length; c++) {
        var val = rows[i][c];
        var h = headers[c];
        if (h==='el'||h==='wa'||h==='wi'||h==='rentMonths'||h==='rent'||h==='total') val = Number(val)||0;
        if (h==='paid') val = (val===true||val==='true');
        obj[h] = val;
      }
      if (!room || obj.room === room) result.push(obj);
    }

    result.sort(function(a,b){ return (b.ts||'').localeCompare(a.ts||''); });
    return out({success:true, data:result, total:result.length});

  } catch(err) {
    return out({success:false, error:String(err)});
  }
}

function clearSheet(sheet, room) {
  var lastRow = sheet.getLastRow();
  if (lastRow <= 1) return out({success:true, action:'deleteAll', deleted:0});

  if (!room) {
    // Delete all data rows at once
    var count = lastRow - 1;
    sheet.deleteRows(2, count);
    return out({success:true, action:'deleteAll', deleted:count});
  }

  // Delete by room (bottom-up)
  var data = sheet.getDataRange().getValues();
  var deleted = 0;
  for (var i = data.length - 1; i >= 1; i--) {
    if (String(data[i][1]) === String(room)) {
      sheet.deleteRow(i + 1);
      deleted++;
    }
  }
  return out({success:true, action:'deleteAll', deleted:deleted});
}

function findRow(sheet, id, room) {
  var data = sheet.getDataRange().getValues();
  for (var i = 1; i < data.length; i++) {
    if (String(data[i][0]) === String(id) && String(data[i][1]) === String(room)) return i + 1;
  }
  return -1;
}

function out(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
