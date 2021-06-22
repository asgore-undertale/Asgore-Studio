from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from Parts.Scripts.UsefulFunctions import intToHex, hexToString
from os import path
import csv

_VERSION_ = 1.0
_SEPARATOR_ = "█"
_CSVDELIMITER_ = ','

def check_version(ver : int):
    if ver > _VERSION_: return True

def open_file(type : str, window, text = 'جدول حروف'):
    _open, _ = QFileDialog.getOpenFileName(window, text, '' , '*.'+type)
    return _open * (_open != '/') * (_open != '') * (path.exists(_open))

def save_file(type : str, window, text = 'جدول حروف'):
    _save, _ = QFileDialog.getSaveFileName(window, text, '' , '*.'+type)
    return _save * (_save != '/') * (_save != '')

def deleteEmptyLines(table : str):
    while '\n\n' in table: table = table.replace('\n\n', '\n')
    return table

def delete_trash(table : str, seperator : str):
    while seperator+'\n' in table: table = table.replace(seperator+'\n', '\n')
    #while '\n\n' in table: table = table.replace('\n\n', '\n')
    while table[-1] == '\n': table = table[:-1]

    return table

def loadTBL(table : str, Table, ROWS, COLS):
    if not table: return
    eraseTable(Table, ROWS, COLS)
    
    table = open(table, 'r', encoding="utf-8").read()
    lines = table.split('\n')
    
    for line in lines:
        if not line: continue
        parts = line.split('=')
        Table.setItem(int(parts[0][0], 16), int(parts[0][1], 16), QTableWidgetItem(parts[1]))

def loadATE(table : str, Table, ROWS, COLS, increaseCells : bool):
    if not table: return
    eraseTable(Table, ROWS, COLS)
    
    table = open(table, 'r', encoding="utf-8").read()
    table = delete_trash(table, _SEPARATOR_)
    rows = table.split('\n')
    
    if len(rows) > ROWS and increaseCells:
        ROWS = len(rows) - 4
        Table.setRowCount(ROWS)
    
    VERSION = float(rows[1][9:-1])
    if check_version(VERSION): QMessageBox.about(Table, "!!تحذير", f"النسخة {VERSION} غير مدعومة.\n(سيتم فتح الملف على أي حال.)")
    SEPARATOR = rows[2][11:-1]
    
    for row in range(4, len(rows)):
        cols = rows[row].split(SEPARATOR)
        if len(cols) > COLS and increaseCells:
            COLS = len(cols)
            Table.setColumnCount(COLS)
        for col in range(len(cols)):
            Table.setItem(row-4, col, QTableWidgetItem(cols[col]))

def loadCSV(table : str, Table, ROWS, COLS, increaseCells : bool):
    if not table: return
    eraseTable(Table, ROWS, COLS)
    
    table = open(table, 'r', encoding="utf-8")# .read()
    # table = delete_trash(table, _CSVDELIMITER_)
    csvContent = csv.DictReader(table) # thank you library
    
    rownum, cellnum = 0, 0
    i, j = 1, 0
    for row in csvContent:
        if len(row) > j: j = len(row)
        i += 1
        if i > ROWS and increaseCells:
            ROWS = i
            Table.setRowCount(ROWS)
        if j > COLS and increaseCells:
            COLS = j
            Table.setColumnCount(COLS)
        
        if rownum == 0:
            for cell in row:
                if isinstance(cell, list):
                    for item in cell:
                        Table.setItem(rownum, cellnum, QTableWidgetItem(item))
                        cellnum += 1
                    continue
                Table.setItem(rownum, cellnum, QTableWidgetItem(cell))
                cellnum += 1
            rownum, cellnum = rownum+1, 0
        for cell in row:
            text = row[cell]
            if isinstance(text, list):
                for item in text:
                    Table.setItem(rownum, cellnum, QTableWidgetItem(item))
                    cellnum += 1
                continue
            Table.setItem(rownum, cellnum, QTableWidgetItem(text))
            cellnum += 1
        rownum, cellnum = rownum+1, 0

def saveTBL(save_loc : str, Table):
    if not save_loc: return
    content = ''
    
    for row in range(Table.rowCount()):
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                content += f'{intToHex(row)[1]}{intToHex(col)[1]}={Table.item(row, col).text()}\n'
    
    open(save_loc, 'w', encoding="utf-8").write(content)
    QMessageBox.about(Table, "!!تم", "تم حفظ الجدول.")

def saveATE(save_loc : str, Table):
    if not save_loc: return
    content = f'\nVERSION="1.0"\nSEPARATOR="{_SEPARATOR_}"\n#####################\n'

    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                csv_row.append(Table.item(row, col).text())
            else: csv_row.append('')
 
        content += _SEPARATOR_.join(csv_row) + '\n'
    
    content = delete_trash(content, _SEPARATOR_)
    
    open(save_loc, 'w', encoding="utf-8").write(content)
    QMessageBox.about(Table, "!!تم", "تم حفظ الجدول.")

def saveCSV(save_loc : str, Table):
    if not save_loc: return
    content = f'الحرف{_SEPARATOR_}أول{_SEPARATOR_}وسط{_SEPARATOR_}آخر{_SEPARATOR_}منفصل\n'
    
    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                csv_row.append(Table.item(row, col).text().replace(_CSVDELIMITER_, f'"{_CSVDELIMITER_}"'))
            else: csv_row.append('')
    
        content += _CSVDELIMITER_.join(csv_row) + '\n'
        
    content = delete_trash(content, _CSVDELIMITER_)
    
    open(save_loc, 'w', encoding="utf-8").write(content)
    QMessageBox.about(Table, "!!تم", "تم حفظ الجدول.")

def eraseTable(Table, ROWS, COLS):
    for row in range(ROWS):
        for col in range(COLS):
            Table.setItem(row, col, QTableWidgetItem(''))

def add_row(Table, ROWS):
    ROWS += 1
    Table.setRowCount(ROWS)

def remove_row(Table, ROWS):
    if not ROWS: return
    ROWS -= 1
    Table.setRowCount(ROWS)

def add_col(Table, COLS):
    COLS += 1
    Table.setColumnCount(COLS)

def remove_col(Table, COLS):
    if not COLS: return
    COLS -= 1
    Table.setColumnCount(COLS)