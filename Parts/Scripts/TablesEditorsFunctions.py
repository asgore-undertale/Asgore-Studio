from PyQt5.QtWidgets import QTableWidgetItem
from Parts.Scripts.UsefulLittleFunctions import intToHex
from Parts.Vars import checkVersion, _ATE_VERSION_, _ATE_SEPARATOR_, _CSV_DELIMITER_

def deleteEmptyLines(tableContent : str):
    while '\n\n' in tableContent: tableContent = tableContent.replace('\n\n', '\n')
    return tableContent

def deleteTrash(tableContent : str, seperator : str):
    while seperator+'\n' in tableContent: tableContent = tableContent.replace(seperator+'\n', '\n')
    #while '\n\n' in tableContent: tableContent = tableContent.replace('\n\n', '\n')
    while tableContent[-1] == '\n': tableContent = tableContent[:-1]

    return tableContent

def eraseTable(Table, ROWS, COLS):
    for row in range(ROWS):
        for col in range(COLS):
            Table.setItem(row, col, QTableWidgetItem(''))

def add_row(Table, ROWS):
    Table.setRowCount(ROWSCOLS + 1)
    return ROWSCOLS + 1

def remove_row(Table, ROWS):
    if not ROWS: return
    Table.setRowCount(ROWS - 1)
    return ROWS - 1

def add_col(Table, COLS):
    Table.setColumnCount(COLSCOLS + 1)
    return COLS + 1

def remove_col(Table, COLS):
    if not COLS: return
    Table.setColumnCount(COLS - 1)
    return COLS - 1

def loadTBL(tablePath : str, Table, ROWS, COLS):
    if not tablePath: return
    eraseTable(Table, ROWS, COLS)
    
    tablePath = open(tablePath, 'r', encoding="utf-8", errors='replace').read()
    lines = tablePath.split('\n')
    
    for line in lines:
        if not line: continue
        parts = line.split('=')
        Table.setItem(int(parts[0][0], 16), int(parts[0][1], 16), QTableWidgetItem(parts[1]))

def loadList(tableList : list, Table, ROWS, COLS, increaseCells : bool):
    for r in range(len(tableList)):
        rowsnum = len(tableList[r])
        if rowsnum > ROWS and increaseCells:
            ROWS = rowsnum
            Table.setRowCount(rowsnum)
        
        for c in range(len(tableList[r])):
            cellsnum = len(tableList[r][c])
            if cellsnum > COLS and increaseCells:
                COLS = cellsnum
                Table.setColumnCount(cellsnum)
            
            Table.setItem(r, c, QTableWidgetItem(tableList[r][c]))

def ATEtoList(tablePath : str):
    tablePath = open(tablePath, 'r', encoding="utf-8", errors='replace').read()
    tablePath = deleteTrash(tablePath, _ATE_SEPARATOR_)
    
    tableList = []
    rows = tablePath.split('\n')
    
    for row in range(len(rows)):
        cells = rows[row].split(_ATE_SEPARATOR_)
        tableList.append(cells)
    
    return tableList

def loadATE(tablePath : str, Table, ROWS, COLS, increaseCells : bool):
    if not tablePath: return
    eraseTable(Table, ROWS, COLS)
    
    tableList = ATEtoList(tablePath)
    loadList(tableList, Table, ROWS, COLS, increaseCells)

def CSVtoList(tablePath : str):
    tableList = []
    rows = open(tablePath, 'r', encoding='utf8', errors='replace').read()
    rows = deleteTrash(rows, _CSV_DELIMITER_).split('\n')
    
    for r in range(len(rows)):
        parts = rows[r].split('"')
        switch, cellnum, row, cell = False, 0, [], ''
        if not parts[-1]: del parts[-1]
        if not parts[0]:
            del parts[0]
            switch = True
        
        for i in range(len(parts)):
            switch = not switch
            if not switch:
                cell += parts[i]
                continue
            if parts[i]:
                cellnum += parts[i].count(_CSV_DELIMITER_)
                if cell:
                    row.append(cell)
                    cell = ''
                for v in parts[i].split(_CSV_DELIMITER_): row.append(v)
            else:
                parts[i] = '"'
                cell += parts[i]
        row.append(cell)
        tableList.append(row)
    
    return tableList

def loadCSV(tablePath : str, Table, ROWS, COLS, increaseCells : bool):
    if not tablePath: return
    eraseTable(Table, ROWS, COLS)
    
    tableList = CSVtoList(tablePath)
    loadList(tableList, Table, ROWS, COLS, increaseCells)

def saveTBL(save_loc : str, Table):
    if not save_loc: return
    content = ''
    
    for row in range(Table.rowCount()):
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                content += f'{intToHex(row)[1]}{intToHex(col)[1]}={Table.item(row, col).text()}\n'
    
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(content)

def saveATE(save_loc : str, Table):
    if not save_loc: return
    content = f'\nVERSION="1.0"\nSEPARATOR="{_ATE_SEPARATOR_}"\n#####################\n'

    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                csv_row.append(Table.item(row, col).text())
            else: csv_row.append('')
 
        content += _ATE_SEPARATOR_.join(csv_row) + '\n'
    
    content = deleteTrash(content, _ATE_SEPARATOR_)
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(content)

def saveCSV(save_loc : str, Table):
    if not save_loc: return
    content = ''
    
    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if Table.item(row, col) and Table.item(row, col).text():
                cell = Table.item(row, col).text().replace('"', '""')
                if _CSV_DELIMITER_ in cell: cell = f'"{cell}"'
                csv_row.append(cell)
            else: csv_row.append('')
    
        content += _CSV_DELIMITER_.join(csv_row) + '\n'
        
    content = deleteTrash(content, _CSV_DELIMITER_)
    open(save_loc, 'w', encoding="utf-8", errors='replace').write(content)