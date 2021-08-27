from openpyxl.styles import PatternFill, Alignment, Font
from PyQt5.QtWidgets import QApplication, QMessageBox
from sys import argv, exit
from os import path, mkdir, makedirs
import openpyxl

from Parts.Scripts.UsefulLittleFunctions import *
from Parts.Vars import _CSV_DELIMITER_, Returns
from Parts.Scripts.TablesEditorsFunctions import CSVtoList
from Parts.Scripts.ExtractFromText import Extract
from Parts.Scripts.LineOffset import OffsetTextWithSpaces
from Parts.Tools.TextConverter import convert

textTablePath = r'OtherFiles/Tables/TextTable.csv'
extractedTextTablePath = r'OtherFiles/Tables/ExtractedTextTable.csv'
inputFolder, outputFolder = r'OtherFiles/_FilesFolder/', r'OtherFiles/_AfterEnteringFolder/'

def openTextTable():
    tablePath = openFile(('xlsx', 'csv'), EnteringWindow, 'جدول النص')
    if not tablePath: return
    global textTablePath
    textTablePath = tablePath

def openExtractedTextTable():
    tablePath = openFile(('xlsx', 'csv'), EnteringWindow, 'جدول الاستخراج')
    if not tablePath: return
    global extractedTextTablePath
    extractedTextTablePath = tablePath

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

def prepareToEnter():
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
    
    elif textTablePath.endswith('.xlsx'):
        textXlsx = openpyxl.load_workbook(textTablePath)
        for sheet in textXlsx.sheetnames:
            textTable = textXlsx.get_sheet_by_name(sheet)
            for cell in range(2, len(textTable['A'])+1):
                text = textTable['A'+str(cell)].value
                translation = textTable['B'+str(cell)].value
                
                translation, tooLong = prepareTextAndTranslation(text, translation, convertBool)
                if tooLong: tooLongList.append([tooLong, hexLength(tooLong[1]) - hexLength(tooLong[0])])
                if translation != None: textList.append([text, translation])
    
    if EnteringWindow.sortedCheck.isChecked():
        return textList, tooLongList
    else:
        return sorted(textList, key=lambda x: len(str(x[0])), reverse=True), tooLongList

def putInXlsx(text, sheet, cell, isbold = False, isAlignted = False, fill = False):
    sheet[cell].value = text
    sheet[cell].font = Font(bold=isbold)
    if isAlignted: sheet[cell].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    if fill: sheet[cell].fill = PatternFill(fill_type='solid', start_color=fill, end_color=fill)

def offsetTranslation(text, translation):
    offsetType = EnteringWindow.OffsetType.currentIndex()
    if offsetType == 0:
        spacesNum = hexLength(text) - hexLength(translation)
    if offsetType == 1:
        spacesNum = len(text) - len(translation)
    
    return OffsetTextWithSpaces(translation, 0, EnteringWindow.Offset.currentIndex(), spacesNum)

def enter(convertBool = True):
    if not prepareToEnter(): return
    
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
    
    before = byteInCell(EnteringWindow.beforeText.toPlainText())
    after = byteInCell(EnteringWindow.afterText.toPlainText())
    
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

def extract():
    before = byteInCell(EnteringWindow.beforeText.toPlainText()).encode()
    after  = byteInCell(EnteringWindow.afterText.toPlainText()).encode()
    if (not before or not after) and not EnteringWindow.asciiCheck.isChecked():
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف العملية،\nاملأ حقلي: ما يسبق النصوص، ما يلحقها.")
        return
    filesList = dirList(inputFolder)
    if not len(filesList):
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف العملية،\nلا توجد أي ملفات للاستخراج منها.")
        return
    
    mini = tryTakeNum(byteInCell(EnteringWindow.minText.toPlainText()), False)
    maxi = tryTakeNum(byteInCell(EnteringWindow.maxText.toPlainText()), False)
    
    if extractedTextTablePath.endswith('.csv'):
        with open(extractedTextTablePath, 'w', encoding='utf8', errors='replace') as database:
            content = ''
            
            for filename in filesList:
                with open(filename, 'rb') as f:
                    fileContent = f.read()
                
                extracted = Extract(fileContent, before, after, False, mini, maxi, EnteringWindow.asciiCheck.isChecked())
                if not extracted: break
                
                content += f'<-- {filename} -->,-\n'
                for item in extracted:
                    item = item.decode(encoding='utf8', errors='replace').replace('"', '""')
                    if _CSV_DELIMITER_ in item:
                        item = f'"{item}"'
                        for r in Returns:
                            item = item.replace(r, f'"{r}"')
                    content += item + '\n'
                
            database.write(content)
        
    elif extractedTextTablePath.endswith('.xlsx'):
        extracted_xlsx = openpyxl.load_workbook(extractedTextTablePath)
        sheet = extracted_xlsx.get_sheet_by_name("Main")
        row = 2
        
        sheet.delete_cols(1, 2)
        putInXlsx("النص الأصلي", sheet, 'A1', True, True, 'ff8327')
        
        for filename in filesList:
            with open(filename, 'rb') as f:
                fileContent = f.read()
            
            extracted = Extract(fileContent, before, after, False, mini, maxi, EnteringWindow.asciiCheck.isChecked())
            if len(extracted):
                putInXlsx(filename, sheet, 'A'+str(row), True, True, 'D112D1')
                putInXlsx('-', sheet, 'B'+str(row), True, True, 'D112D1')
                row += 1
                
                for item in extracted:
                    putInXlsx(bytesToString(item), sheet, 'A'+str(row))
                    row += 1
        
        extracted_xlsx.save(extractedTextTablePath)
    QMessageBox.about(EnteringWindow, "!!تهانيّ", "انتهى الاستخراج.")

app = QApplication(argv)
from Parts.Windows import EnteringWindow, TextConverterOptionsWindow, StudioWindow

EnteringWindow.textTableButton.clicked.connect(lambda: openTextTable())
EnteringWindow.extractTableButton.clicked.connect(lambda: openExtractedTextTable())
EnteringWindow.enterButton.clicked.connect(lambda: enter(False))
EnteringWindow.extractButton.clicked.connect(lambda: extract())
EnteringWindow.enterConvertButton.clicked.connect(lambda: enter())
EnteringWindow.fromFolder.clicked.connect(lambda: selectInputFolder())
EnteringWindow.toFolder.clicked.connect(lambda: selectOutputFolder())

if __name__ == '__main__':
    EnteringWindow.show()
    exit(app.exec_())