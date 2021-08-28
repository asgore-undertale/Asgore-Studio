from PyQt5.QtWidgets import QApplication
from Parts.Scripts.UsefulLittleFunctions import openFile, saveFile, tryTakeNum
from Parts.Scripts.TablesEditorsFunctions import CSVtoList
from Parts.Scripts.ConvertFiles import MsytToTxt, TxtToMsyt
from Parts.Scripts.ExtractFromText import Extract
from Parts.Vars import _CSV_DELIMITER_
from Parts.Tools.TextConverter import convert
from sys import argv, exit
from os import path
import re, openpyxl, keyboard, csv


fileContent = ''
textList, transList, oldTransList = '', '', ''
database, dataBaseDirectory, table = '', '', ''
sentencesNum, columnIndex = '', ''

def fileType():
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    if index == 0: return 'msyt'
    if index == 1: return 'txt'
    if index == 2: return 'csv'
    if index == 3: return 'po'

def typeCommand():
    if not FilesEditorWindow.isActiveWindow(): return
    
    Text, c = FilesEditorWindow.textBox.toPlainText(), 0
    
    if '＞' not in Text or '＜' not in Text: return
    while '＜c'+str(c)+'＞' not in Text:
        if c == 30: return
        c += 1
    
    for i in range(Text.count('＞')):
        if '＜c'+str(c+i)+'＞' not in FilesEditorWindow.translationBox.toPlainText() and '＜c'+str(c+i)+'＞' in Text:
            keyboard.write('＜c'+str(c+i)+'＞')
            break

def Convert():
    FilesEditorWindow.translationBox.setPlainText(convert(FilesEditorWindow.translationBox.toPlainText(), False))

def ConvertAll():
    for t in range(len(transList)):
        transList[t] = convert(transList[t], False)
    Convert()

def openTextDataBase():
    global database

    filePath = openFile(('xlsx', 'csv'), FilesEditorWindow, 'جدول نصوص')
    if not filePath: return
    
    dataBaseDirectory = filePath
    if filePath.endswith('.xlsx'):
        database = openpyxl.load_workbook(filePath)
    elif filePath.endswith('.csv'):
        database = CSVtoList(filePath)

def indexHandle(index, filePath, case):
    global fileContent, columnIndex, textList, transList, oldTransList, table, sentencesNum
    if case:
        handleText.current_item = 0
        if index == 0:
            textList, transList = loadMsyt() # filePath
        if index == 1:
            textList, transList = loadKruptar() # filePath
        if index == 2:
            columnIndex = tryTakeNum(FilesEditorWindow.columnIndexCell.toPlainText()) -1
            textList, transList, table = loadCsvTable() # filePath
        if index == 3:
            textList, transList = loadPo() # filePath
            oldTransList = list(transList)
        
        sentencesNum = len(textList)-1
        FilesEditorWindow.per.setText(f"{sentencesNum} \ {0}")
    else:
        if index == 0: saveMsyt() # filePath, fileContent
        if index == 1: saveKruptar() # filePath, fileContent
        if index == 2: saveCsvTable() # filePath, table
        if index == 3: savePo() # filePath, fileContent

def loadFile():
    filePath = openFile([fileType()], FilesEditorWindow, 'ملف')
    if not filePath: return
    
    indexHandle(FilesEditorWindow.fileTypeComboBox.currentIndex(), filePath, True)
    
    if not textList: return
    FilesEditorWindow.textBox.setPlainText(textList[0])
    FilesEditorWindow.translationBox.setPlainText(transList[0])
    
def save_file():
    global transList
    filePath = saveFile([fileType()], FilesEditorWindow, 'ملف')
    if not filePath: return
    
    transList[handleText.current_item] = FilesEditorWindow.translationBox.toPlainText()
    
    indexHandle(FilesEditorWindow.fileTypeComboBox.currentIndex(), filePath, False)

def loadKruptar(): # filePath
    endcommand = FilesEditorWindow.endCommandCell.toPlainText()
    if not endcommand: return
    
    fileContent = open(filePath, 'r', encoding='utf-8', errors='replace').read()
    textList = fileContent.split(endcommand)
    del textList[-1]
    
    return textList, list(textList)

def saveKruptar(): # filePath, fileContent
    endCom = FilesEditorWindow.endCommandCell.toPlainText()
    for t in range(len(textList)):
        fileContent = fileContent.replace(textList[t] + endCom, transList[t] + endCom, 1)
    
    open(filePath, 'w', encoding='utf-8', errors='replace').write(fileContent)

def loadPo(): # filePath
    fileContent = open(filePath, 'r', encoding='utf-8', errors='replace').read() + '\n\n'
    
    textList = Extract(fileContent, 'msgid "', '"\nmsgstr')
    transList = Extract(fileContent, 'msgstr "', '"\n\n')
    textList = list(map(lambda x: x.replace('\\n', '\n').replace('"\n"', ''), textList))
    transList = list(map(lambda x: x.replace('\\n', '\n').replace('"\n"', ''), transList))
    del textList[0], transList[0]
    
    return textList, transList

def savePo(): # filePath, fileContent
    for t in range(len(textList)):
        fileContent = fileContent.replace(f'msgstr "{oldTransList[t]}"\n\n', f'msgstr "{transList[t]}"\n\n', 1)
    open(filePath, 'w', encoding='utf-8', errors='replace').write(fileContent)

def loadCsvTable(): # filePath
    if columnIndex < 0: return
    
    with open(filePath, newline='', encoding='utf8', errors='replace') as csvfile:
        table = list(csv.reader(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"'))
    
    textList = []
    for row in table:
        try: textList.append(row[columnIndex])
        except: pass
    
    return textList, list(textList), table

def saveCsvTable(): # filePath, table
    for t in range(len(textList)):
        try: table[t][columnIndex] = transList[t]
        except: pass
    with open(filePath, 'w', newline='', encoding="utf-8", errors='replace') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in table:
            spamwriter.writerow(row)

def loadMsyt(): # filePath
    global textList, transList, sentencesNum
    
    fileContent = open(filePath, 'r', encoding='utf-8', errors='replace').read()
    
    fileContent, reportContent = MsytToTxt(fileContent)
    msyt_content_list = Extract(fileContent, '{\n', '\n}')
    textList = msyt_content_list[0].split('\n')
    
    StudioWindow.Report('أوامر ملف .msyt', reportContent)
    
    return textList, list(textList)

def saveMsyt(): # filePath, fileContent
    for t in range(len(textList)):
        fileContent = fileContent.replace(f'\n{textList[t]}\n', f'\n{transList[t]}\n', 1)
    open(filePath, 'w', encoding='utf-8', errors='replace').write(TxtToMsyt(fileContent))

def handleText(direction = True):
    if not sentencesNum: return
    
    if direction:
        handleText.current_item = (handleText.current_item + 1) % (sentencesNum + 1)
        index = ((not handleText.current_item) * sentencesNum) + ((handleText.current_item > 0) * (handleText.current_item - 1))
    else:
        handleText.current_item = ((not handleText.current_item) * sentencesNum) + ((handleText.current_item > 0) * (handleText.current_item - 1))
        index = (handleText.current_item + 1) % (sentencesNum + 1)
    
    FilesEditorWindow.per.setText(f"{sentencesNum} \ {handleText.current_item}")
    
    transList[index] = FilesEditorWindow.translationBox.toPlainText()
    
    FilesEditorWindow.textBox.setPlainText(textList[handleText.current_item])
    FilesEditorWindow.translationBox.setPlainText(transList[handleText.current_item])
    
    setTranslation() # dataBaseDirectory
handleText.current_item = 0

def setTranslation(): # dataBaseDirectory
    if not path.exists(dataBaseDirectory): return
    
    if dataBaseDirectory.endswith('.xlsx'):
        for sheet in database.sheetnames:
            text_table = database.get_sheet_by_name(sheet)
            for cell in range(2, len(text_table['A'])+1):
                if text_table['A'+str(cell)].value != transList[handleText.current_item]:
                    continue
                FilesEditorWindow.translationBox.setPlainText(text_table['B'+str(cell)].value)
                return
    
    elif dataBaseDirectory.endswith('.csv'):
        for row in database:
            try:
                text = row[0]
                translation = row[1]
            except: continue
            
            if text != transList[handleText.current_item]:
                continue
            FilesEditorWindow.translationBox.setPlainText(translation)
            return


app = QApplication(argv)
from Parts.Windows import FilesEditorWindow, StudioWindow

FilesEditorWindow.textButton.clicked.connect(lambda: openTextDataBase())
FilesEditorWindow.backButton.clicked.connect(lambda: handleText(False))
FilesEditorWindow.nextButton.clicked.connect(lambda: handleText(True))
FilesEditorWindow.saveButton.clicked.connect(lambda: save_file())
FilesEditorWindow.openButton.clicked.connect(lambda: loadFile())
FilesEditorWindow.Convertbutton.clicked.connect(lambda: Convert())
FilesEditorWindow.ConvertAllbutton.clicked.connect(lambda: ConvertAll())
keyboard.add_hotkey("F3", lambda: typeCommand())

if __name__ == '__main__':
    FilesEditorWindow.show()
    exit(app.exec_())