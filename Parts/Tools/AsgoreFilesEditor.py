from PyQt5.QtWidgets import QApplication
from Parts.Scripts.UsefulLittleFunctions import openFile, saveFile
from Parts.Scripts.TablesEditorsFunctions import CSVtoList, loadList
from Parts.Scripts.LoadSaveFiles import *
from Parts.Scripts.LoadSaveFiles import filesTypesDescription
from Parts.Tools.TextConverter import convert
from sys import argv, exit
from os import path
import re, openpyxl, keyboard


fileContent = ''
textList, transList, oldTransList = '', '', ''
database, dataBaseDirectory, table = '', '', ''
sentencesNum, columnIndex = '', ''

def typeCommand():
    if not FilesEditorWindow.isActiveWindow(): return
    
    Text, c = FilesEditorWindow.textBox.toPlainText(), 0
    
    if '>' not in Text or '<' not in Text: return
    while '<c'+str(c)+'>' not in Text:
        if c == 30: return
        c += 1
    
    for i in range(Text.count('>')):
        if '<c'+str(c+i)+'>' not in FilesEditorWindow.translationBox.toPlainText() and '<c'+str(c+i)+'>' in Text:
            keyboard.write('<c'+str(c+i)+'>')
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

def getFilePath():
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    filePath = openFile([fileType(index)], FilesEditorWindow, 'ملف')
    return filePath

def loadFile(filePath = ''):
    if not filePath: filePath = getFilePath()
    if not filePath: return
    
    global fileContent, table, textList, transList, oldTransList, sentencesNum
    
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    
    handleText.current_item = 0
    columnIndex = FilesEditorWindow.columnIndexCell.getValue() -1
    textList, transList, oldTransList, fileContent, table, sentencesNum = loadByIndex(index, filePath, columnIndex)
    FilesEditorWindow.per.setText(f"{sentencesNum} \ {0}")
    
    if not textList: return
    FilesEditorWindow.textBox.setPlainText(textList[0])
    if not transList: return
    FilesEditorWindow.translationBox.setPlainText(transList[0])

def getFileSavePath():
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    filePath = saveFile([fileType(index)], FilesEditorWindow, 'ملف')
    return filePath
    
def save_file(filePath = ''):
    if not filePath: filePath = getFileSavePath()
    if not filePath: return
    
    global transList
    
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    
    transList[handleText.current_item] = FilesEditorWindow.translationBox.toPlainText()
    saveByIndex(index, filePath, fileContent, table, FilesEditorWindow.columnIndexCell.getValue() -1, textList, transList, oldTransList)

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
    
    setTranslation(dataBaseDirectory)
handleText.current_item = 0

def setTranslation(dataBaseDirectory):
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

def openInTablesEditor(textList, transList):
    tableList = list(map(lambda x: [x[0], x[1]], zip(textList, transList)))
    tableList.insert(0, ['النص الأصلي', 'الترجمة'])
    loadList(tableList, TableEditorWindow.Table, True)

app = QApplication(argv)
from Parts.Windows import FilesEditorWindow, TableEditorWindow

FilesEditorWindow.fileTypeComboBox.addItems(filesTypesDescription)

FilesEditorWindow.textButton.clicked.connect(lambda: openTextDataBase())
FilesEditorWindow.backButton.clicked.connect(lambda: handleText(False))
FilesEditorWindow.nextButton.clicked.connect(lambda: handleText(True))
FilesEditorWindow.saveButton.clicked.connect(lambda: save_file())
FilesEditorWindow.openButton.clicked.connect(lambda: loadFile())
FilesEditorWindow.openTableButton.clicked.connect(lambda: openInTablesEditor(textList, transList))
FilesEditorWindow.Convertbutton.clicked.connect(lambda: Convert())
FilesEditorWindow.ConvertAllbutton.clicked.connect(lambda: ConvertAll())
keyboard.add_hotkey("F3", lambda: typeCommand())

if __name__ == '__main__':
    FilesEditorWindow.show()
    exit(app.exec_())