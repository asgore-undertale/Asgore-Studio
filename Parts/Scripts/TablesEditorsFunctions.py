from PyQt5.QtWidgets import QTableWidgetItem
from Parts.Scripts.UsefulLittleFunctions import intToHex
from Parts.Vars import _ACT_SEPARATOR_, _CSV_DELIMITER_
import csv

def deleteEmptyLines(tableContent : str):
    while '\n\n' in tableContent: tableContent = tableContent.replace('\n\n', '\n')
    return tableContent

def deleteTrash(tableContent : str, seperator : str):
    try:
        while seperator+'\n' in tableContent: tableContent = tableContent.replace(seperator+'\n', '\n')
        #while '\n\n' in tableContent: tableContent = tableContent.replace('\n\n', '\n')
        while tableContent[-1] == '\n': tableContent = tableContent[:-1]
    except: pass
    return tableContent

def eraseTable(Table):
    for row in range(Table.rowCount()):
        for col in range(Table.columnCount()):
            Table.setItem(row, col, QTableWidgetItem(''))

def add_row(Table):
    Table.setRowCount(Table.rowCount() + 1)

def remove_row(Table):
    if not Table.rowCount(): return
    Table.setRowCount(Table.rowCount() - 1)

def add_col(Table):
    Table.setColumnCount(Table.columnCount() + 1)

def remove_col(Table):
    if not Table.columnCount(): return
    Table.setColumnCount(Table.columnCount() - 1)

def loadTBL(tablePath : str, Table):
    if not tablePath: return
    eraseTable(Table)
    
    tablePath = open(tablePath, 'r', encoding="utf-8", errors='replace').read()
    lines = tablePath.split('\n')
    
    for line in lines:
        if not line: continue
        parts = line.split('=')
        Table.setItem(int(parts[0][0], 16), int(parts[0][1], 16), QTableWidgetItem(parts[1]))

def loadList(tableList : list, Table, increaseCells : bool):
    rowsnum = len(tableList)
    if rowsnum > Table.rowCount() and increaseCells:
        Table.setRowCount(rowsnum)

    for r in range(len(tableList)):
        cellsnum = len(tableList[r])
        if cellsnum > Table.columnCount() and increaseCells:
            Table.setColumnCount(cellsnum)

        for c in range(len(tableList[r])):
            Table.setItem(r, c, QTableWidgetItem(tableList[r][c]))

def ATEtoList(tablePath : str):
    tablePath = open(tablePath, 'r', encoding="utf-8", errors='replace').read()
    tablePath = deleteTrash(tablePath, _ACT_SEPARATOR_)
    
    tableList = []
    rows = tablePath.split('\n')
    
    for row in range(len(rows)):
        cells = rows[row].split(_ACT_SEPARATOR_)
        tableList.append(cells)
    
    return tableList

def loadATE(tablePath : str, Table, increaseCells : bool):
    if not tablePath: return
    eraseTable(Table)
    
    tableList = ATEtoList(tablePath)
    loadList(tableList, Table, increaseCells)

def CSVtoList(tablePath : str):
    with open(tablePath, newline='', encoding='utf8', errors='replace') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"')
        return list(spamreader)

def loadCSV(tablePath : str, Table, increaseCells : bool):
    if not tablePath: return
    eraseTable(Table)
    
    tableList = CSVtoList(tablePath)
    loadList(tableList, Table, increaseCells)

def saveTBL(save_loc : str, Table):
    if not save_loc: return
    content = ''
    
    for row in range(Table.rowCount()):
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                for char in Table.item(row, col).text():
                    content += f'{intToHex(row)[1]}{intToHex(col)[1]}={char}\n'
    
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(content)

def saveATE(save_loc : str, Table):
    if not save_loc: return
    content = f'\nVERSION="1.0"\nSEPARATOR="{_ACT_SEPARATOR_}"\n#####################\n'

    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                csv_row.append(Table.item(row, col).text())
            else: csv_row.append('')
 
        content += _ACT_SEPARATOR_.join(csv_row) + '\n'
    
    content = deleteTrash(content, _ACT_SEPARATOR_)
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(content)

def saveCSV(save_loc : str, Table):
    if not save_loc: return
    
    with open(save_loc, 'w', newline='', encoding="utf-8", errors='replace') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in range(Table.rowCount()):
            csvRow = []
            for col in range(Table.columnCount()):
                if Table.item(row, col) and Table.item(row, col).text():
                    csvRow.append(Table.item(row, col).text())
            
            spamwriter.writerow(csvRow)
        
    a = open(save_loc, 'r', encoding="utf-8", errors='replace').read() # for some reason this is nessesary
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(
        deleteTrash(a, _CSV_DELIMITER_)
        )