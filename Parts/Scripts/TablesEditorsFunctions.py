from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from Parts.Scripts.UsefulFunctions import intToHex, hexToString
from os import path

_VERSION_ = 1.0
_SEPARATOR_ = "█"

def check_version(ver : int):
    if ver > _VERSION_: return True

def open_file(type : str, window):
    _open, _ = QFileDialog.getOpenFileName(window, 'جدول حروف', '' , '*.'+type)
    if _open == '/' or not _open or not path.exists(_open): return
    return _open

def save_file(type : str, window):
    _save, _ = QFileDialog.getSaveFileName(window, 'جدول حروف', '' , '*.'+type)
    if _save == '/' or not _save: return
    return _save

def delete_trash(table : str, x = 10):
    '''
    for i in range(1, x):
        i = x - i
        while _SEPARATOR_ *i + '\n' in table: table = table.replace(_SEPARATOR_*i + '\n', '\n')
    for i in range(1, x):
        i = x - i
        while '\n'*i + '\n' in table: table = table.replace('\n'*i + '\n', '\n')
    '''
    table = table.split('\n')
    while not table[-1]: del table[-1]
    table = '\n'.join(table)
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
    table = delete_trash(table)
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

def saveTBL(save_loc : str, Table):
    content = ''
    
    for row in range(Table.rowCount()):
        for col in range(Table.columnCount()):
            if Table.item(row, col): content += f'{intToHex(row)}{intToHex(col)}={Table.item(row, col).text()}\n'
    
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