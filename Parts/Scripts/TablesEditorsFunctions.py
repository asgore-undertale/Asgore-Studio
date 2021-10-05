from PyQt5.QtWidgets import QTableWidgetItem
from Parts.Scripts.UsefulLittleFunctions import intToHex, hexToString, stringToHex
from Parts.Scripts.FixTables import sortACT, fixCharmap, takeFromArabic
from Parts.Vars import _A_SEPARATOR_, _CSV_DELIMITER_, _ACT_DESC_, checkVersion
import csv

# HexTable = [[''] * 16] * 16 # lines have same id
HexTable = [
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    ]

def deleteEmptyLines(tableContent : str):
    while '\n\n' in tableContent: tableContent = tableContent.replace('\n\n', '\n')
    return tableContent

def deleteTrash(tableContent : str, seperator : str):
    try:
        tries = 20
        for i in range(tries):
            while (seperator*(tries-i))+'\n' in tableContent: tableContent = tableContent.replace(seperator+'\n', '\n')
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

def tablelistToCharmap(List):
    charmap = {}
    for r in range(len(List)):
        csv_row = []
        for c in range(len(List[r])):
            if not List[r][c]: continue
            charmap[List[r][c]] = intToHex(r)[1]+intToHex(c)[1]
    return charmap

def tableToCharmap(Table):
    charmap = {}
    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if not Table.item(row, col): continue
            if not Table.item(row, col).text(): continue
            charmap[Table.item(row, col).text()] = intToHex(row)[1]+intToHex(col)[1]
    return charmap

def loadList(tableList : list, Table, increaseCells : bool):
    eraseTable(Table)
    
    rowsnum = len(tableList)
    if rowsnum > Table.rowCount() and increaseCells:
        Table.setRowCount(rowsnum)

    for r in range(len(tableList)):
        cellsnum = len(tableList[r])
        if cellsnum > Table.columnCount() and increaseCells:
            Table.setColumnCount(cellsnum)

        for c in range(len(tableList[r])):
            Table.setItem(r, c, QTableWidgetItem(tableList[r][c]))

def TBLtoList(tablePath : str):
    tablePath = open(tablePath, 'r', encoding="utf-8", errors='replace').read()
    rows = tablePath.split('\n')
    tableList = []
    
    for row in rows:
        if not row: continue
        tableList.append(row.split('='))
    
    return tableList

def TBLtoHexList(tablePath : str):
    tablePath = open(tablePath, 'r', encoding="utf-8", errors='replace').read()
    rows = tablePath.split('\n')
    tableList = list(HexTable)
    
    for row in range(len(rows)):
        if not rows[row]: continue
        parts = rows[row].split('=')
        tableList[int(parts[0][0], 16)][int(parts[0][1], 16)] = parts[1]
    
    return tableList

def ATEtoList(tablePath : str):
    tablePath = open(tablePath, 'r', encoding="utf-8", errors='replace').read()
    rows = tablePath.split('\n')
    tableList = []
    
    for row in range(len(rows)):
        if not rows[row]: continue
        cells = rows[row].split(_A_SEPARATOR_)
        tableList.append(cells)
    
    return tableList

def ACTtoList(tablePath : str):
    tablePath = open(tablePath, 'r', encoding="utf-8", errors='replace').read()
    rows = tablePath.split('\n')
    tableList = list(HexTable)
    charmap = {}
    
    VERSION = rows[1][9:-1]
    SEPARATOR = rows[2][11:-1]
    checkVersion(VERSION, 0)
    
    for r in range(5, len(rows)):
        if not rows[r]: continue
        row = rows[r].split(SEPARATOR)
        for i in range(5 - len(row)): row.append('')
        charmap = takeFromArabic(charmap, row)
    
    for k, v in charmap.items():
        if not v or not k: continue
        tableList[int(stringToHex(v)[0], 16)][int(stringToHex(v)[1], 16)] = k
    
    return tableList

def CSVtoList(tablePath : str):
    with open(tablePath, newline='', encoding='utf8', errors='replace') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"')
        return list(spamreader)

def loadTBL(tablePath : str, Table, increaseCells = False):
    if not tablePath: return
    eraseTable(Table)
    
    tableList = TBLtoList(tablePath)
    loadList(tableList, Table, increaseCells)


def loadTBLHex(tablePath : str, Table, increaseCells = False):
    if not tablePath: return
    eraseTable(Table)
    
    tableList = TBLtoHexList(tablePath)
    loadList(tableList, Table, increaseCells)

def loadATE(tablePath : str, Table, increaseCells = False):
    if not tablePath: return
    eraseTable(Table)
    
    tableList = ATEtoList(tablePath)
    loadList(tableList, Table, increaseCells)

def loadACT(tablePath : str, Table, increaseCells = False):
    if not tablePath: return
    eraseTable(Table)
    
    tableList = ACTtoList(tablePath)
    loadList(tableList, Table, increaseCells)

def loadCSV(tablePath : str, Table, increaseCells = False):
    if not tablePath: return
    eraseTable(Table)
    
    tableList = CSVtoList(tablePath)
    loadList(tableList, Table, increaseCells)

def saveTBLHex(save_loc : str, Table):
    if not save_loc: return
    content = ''
    charmap = tableToCharmap(Table)
    
    for k, v in charmap.items():
        content += f'{v}={k}\n'
    
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(content)

def saveTBL(save_loc : str, Table):
    if not save_loc: return
    content = ''

    for r in range(Table.rowCount()):
        if not Table.item(r, 0) or not Table.item(r, 0).text(): continue
        if not Table.item(r, 1) or not Table.item(r, 1).text(): continue
        content += f'{Table.item(r, 0).text()}={Table.item(r, 1).text()}\n'
    
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(content)

def saveATE(save_loc : str, Table):
    if not save_loc: return
    content = ''

    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                csv_row.append(Table.item(row, col).text())
            else: csv_row.append('')
 
        content += _A_SEPARATOR_.join(csv_row) + '\n'
    
    content = deleteTrash(content, _A_SEPARATOR_)
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(content)

def saveACT(save_loc : str, Table):
    if not save_loc: return
    
    charmap = fixCharmap(tableToCharmap(Table))
    content = ''
    
    for k, v in charmap.items():
        content += f'\n{k}{_A_SEPARATOR_*4}{hexToString(v)}'
    
    content = deleteEmptyLines(deleteTrash(content, _A_SEPARATOR_))
    content = sortACT(content, _A_SEPARATOR_)
    content = _ACT_DESC_.replace('[_SEPARATOR_]', _A_SEPARATOR_) + content

    open(save_loc, 'w', encoding="utf-8").write(content)

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

def saveCSVHex(save_loc : str, Table): # CSV Converting table
    if not save_loc: return
    
    charmap = fixCharmap(tableToCharmap(Table))
    content = ''
    
    for k, v in charmap.items():
        content += f'\n{k}{_A_SEPARATOR_*4}{hexToString(v)}'
    
    content = deleteEmptyLines(deleteTrash(content, _A_SEPARATOR_))
    content = sortACT(content, _A_SEPARATOR_)
    content = _ACT_DESC_.replace('[_SEPARATOR_]', _A_SEPARATOR_) + content
    
    with open(save_loc, 'w', newline='', encoding="utf-8", errors='replace') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in content.split('\n'):
            spamwriter.writerow(row.split(_A_SEPARATOR_))