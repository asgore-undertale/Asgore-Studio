from PyQt5.QtWidgets import QApplication, QMessageBox
from sys import argv, exit
from os import path, mkdir, makedirs

from Parts.Scripts.UsefulLittleFunctions import *
from Parts.Vars import _CSV_DELIMITER_, Returns
from Parts.Scripts.TablesEditorsFunctions import CSVtoList
from Parts.Scripts.ExtractFromText import Extract
from Parts.Scripts.LineOffset import OffsetTextWithSpaces
from Parts.Tools.TextConverter import convert
from Parts.Scripts.LoadSaveFiles import fileType, loadByIndex

textTablePath = r'OtherFiles/Tables/TextTable.csv'
inputFolder, outputFolder = r'OtherFiles/_FilesFolder/', r'OtherFiles/_AfterEnteringFolder/'

def openTextTable():
    tablePath = openFile(['csv'], EnteringWindow, 'جدول النص')
    if not tablePath: return
    global textTablePath
    textTablePath = tablePath

def selectInputFolder():
    folderPath = selectFolder(EnteringWindow)
    if not folderPath: return
    global inputFolder
    inputFolder = folderPath

def selectOutputFolder():
    folderPath = selectFolder(EnteringWindow)
    if not folderPath: return
    global outputFolder
    outputFolder = folderPath

def detectEnteringErrors():
    if TextConverterOptionsWindow.C_check.isChecked() or TextConverterOptionsWindow.UC_check.isChecked():
        from Parts.Tools.TextConverter import convertingTablePath
        if not path.exists(convertingTablePath):
            QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف كل العمليات،\nقاعدة بيانات التحويل غير موجودة.")
            return
    if EnteringWindow.databaseCheck.isChecked():
        if not path.exists(textTablePath):
            QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف كل العمليات،\nجدول النصوص غير موجود.")
            return
    if not path.exists(inputFolder):
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف كل العمليات،\nالمجلد الحاوي للملفات غير موجود.")
        return
    if not path.exists(outputFolder):
        mkdir(outputFolder)
    
    return True

def detectExportingErrors(before, after, filesNum):
    if (not before or not after) and not EnteringWindow.asciiCheck.isChecked() and not EnteringWindow.filesEditorCheck.isChecked():
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف العملية،\nاملأ حقلي: ما يسبق النصوص، ما يلحقها.")
        return
    if not filesNum:
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف العملية،\nلا توجد أي ملفات للاستخراج منها.")
        return
    return True

def prepareTextAndTranslation(text, translation, convertBool):
    if not text: return None, None
    if not translation: translation = ''
    if convertBool: translation = convert(translation, False)
    
    if EnteringWindow.tooLongCheck.isChecked():
        if hexLength(translation) > hexLength(text):
            return None, [text, translation]
    
    return translation, None

def getTextListFromTable(textTablePath, convertBool):
    textList, tooLongList = [], []
    if textTablePath.endswith('.csv'):
        csvTable = CSVtoList(textTablePath)
        for row in csvTable:
            try:
                text = row[0]
                translation = row[1]
            except: continue
            
            translation, tooLong = prepareTextAndTranslation(text, translation, convertBool)
            if tooLong: tooLongList.append([tooLong, hexLength(tooLong[1]) - hexLength(tooLong[0])])
            if translation != None:
                textList.append([text, translation])
    
    if EnteringWindow.sortedCheck.isChecked():
        return textList, tooLongList
    else:
        return sorted(textList, key=lambda x: len(str(x[0])), reverse=True), tooLongList

def offsetTranslation(text, translation):
    offsetType = EnteringWindow.OffsetType.currentIndex()
    if offsetType == 0:
        spacesNum = hexLength(text) - hexLength(translation)
    if offsetType == 1:
        spacesNum = len(text) - len(translation)
    
    return OffsetTextWithSpaces(translation, 0, EnteringWindow.Offset.currentIndex(), spacesNum)

def enter(convertBool = True):
    if not detectEnteringErrors(): return
    
    filesList = dirList(inputFolder)
    if not filesList:
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف كل العمليات،\nلا توجد أي ملفات للإدخال إليها.")
        return
    
    textList, tooLongList = [], []
    
    if EnteringWindow.databaseCheck.isChecked():
        textList, tooLongList = getTextListFromTable(textTablePath, convertBool)
    else:
        text = EnteringWindow.textBox.toPlainText()
        if text:
            translation, tooLong = prepareTextAndTranslation(text, EnteringWindow.translationBox.toPlainText(), convertBool)
            if translation != None: textList = [[text, translation]]
    
    before = EnteringWindow.beforeText.getValue()
    after = EnteringWindow.afterText.getValue()
    
    for filename in filesList:
        with open(filename, 'rb') as f:
            fileContent = f.read()
        
        textListLength, deletedText = len(textList), 0
        for i in range(textListLength):
            i -= deletedText
            
            text, translation = before+textList[i][0]+after, before+textList[i][1]+after
            byteText = text.encode()
            if byteText not in fileContent: continue
            
            if EnteringWindow.translationOffsetCheck.isChecked():
                translation = offsetTranslation(text, translation)
            
            fileContent = fileContent.replace(byteText, translation.encode(), 1)
            del textList[i]
            deletedText += 1
        
        savePath = filename.replace(inputFolder, outputFolder, 1)
        makedirs(path.dirname(savePath), exist_ok=True)
        
        with open(savePath, 'wb') as f:
            f.write(fileContent)
    
    if textList:
        reportContent = '\n'.join(list(map(str, textList)))
        StudioWindow.Report('لم يتم إيجاده', reportContent)
    if tooLongList:
        reportContent = '\n'.join(list(map(str, tooLongList)))
        StudioWindow.Report('أطول من الأصلي بقيم الهيكس', reportContent)
    
    QMessageBox.about(EnteringWindow, "!!تهانيّ", "انتهى الإدخال.")

def fixExtractedItem(item):
    if isinstance(item, bytes):
        item = item.decode(encoding='utf8', errors='replace')
    item = item.replace('"', '""')
    
    if _CSV_DELIMITER_ in item or '"' in item:
        item = f'"{item}"'
        for r in Returns:
            item = item.replace(r, f'"{r}"')
    return item

def getExtractedLists(filepath, fileTypeindex, columnIndex, before, after, mini, maxi):
    if EnteringWindow.filesEditorCheck.isChecked():
        if not filepath.endswith('.'+fileType(fileTypeindex)): return None, None
        extractedTextList, extractedTransList, _, _, _, _ = loadByIndex(fileTypeindex, filepath, columnIndex)
        
        if EnteringWindow.asciiCheck.isChecked():
            extractedTextList = list(map(filterAscii, extractedTextList))
            extractedTextList = list(filter(lambda a: a, extractedTextList))
        
        if mini or maxi:
            for i in range(len(extractedTextList)):
                extractedTextList[i] = minimax(extractedTextList[i], mini, maxi)
            extractedTextList = list(filter(lambda a: a, extractedTextList))
    else:
        with open(filepath, 'rb') as f:
            fileContent = f.read()
        extractedTextList = Extract(fileContent, before, after, False, mini, maxi, EnteringWindow.asciiCheck.isChecked())
        extractedTransList = ['' for i in range(len(extractedTextList))]
    
    return extractedTextList, extractedTransList

def extract():
    before = EnteringWindow.beforeText.toPlainText().encode()
    after  = EnteringWindow.afterText.toPlainText().encode()
    filesList = dirList(inputFolder)
    fileTypeindex = FilesEditorWindow.fileTypeComboBox.currentIndex()
    columnIndex = FilesEditorWindow.columnIndexCell.getValue() -1
    
    if not detectExportingErrors(before, after, len(filesList)): return
    
    mini = EnteringWindow.minText.getValue()
    maxi = EnteringWindow.maxText.getValue()
    
    tablePath = saveFile(['csv'], EnteringWindow, 'جدول الاستخراج')
    if not tablePath: return
    
    with open(tablePath, 'w', encoding='utf8', errors='replace') as database:
        content = ''
        
        for filepath in filesList:
            extractedTextList, extractedTransList = getExtractedLists(
                filepath, fileTypeindex, columnIndex, before, after, mini, maxi
                )
            if not extractedTextList: continue
            
            content += f'<-- {filepath} -->,-\n'
            for i in range(len(extractedTextList)):
                content += f'{fixExtractedItem(extractedTextList[i])},{fixExtractedItem(extractedTransList[i])}\n'
            
        database.write(content)
    
    QMessageBox.about(EnteringWindow, "!!تهانيّ", "انتهى الاستخراج.")

app = QApplication(argv)
from Parts.Windows import EnteringWindow, TextConverterOptionsWindow, StudioWindow, FilesEditorWindow

EnteringWindow.textTableButton.clicked.connect(lambda: openTextTable())
EnteringWindow.enterButton.clicked.connect(lambda: enter(False))
EnteringWindow.extractButton.clicked.connect(lambda: extract())
EnteringWindow.enterConvertButton.clicked.connect(lambda: enter())
EnteringWindow.fromFolder.clicked.connect(lambda: selectInputFolder())
EnteringWindow.toFolder.clicked.connect(lambda: selectOutputFolder())

if __name__ == '__main__':
    EnteringWindow.show()
    exit(app.exec_())