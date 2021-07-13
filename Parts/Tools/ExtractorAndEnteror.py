from openpyxl.styles import PatternFill, Alignment, Font
from PyQt5.QtWidgets import QApplication, QMessageBox
from sys import argv, exit
from os import path, mkdir, makedirs
import openpyxl

from Parts.Scripts.UsefulLittleFunctions import selectFolder, openFile, dirList, byteInCell, bytesToString
from Parts.Vars import checkVersion, _ATE_VERSION_, _CSV_DELIMITER_
from Parts.Scripts.TablesEditorsFunctions import CSVtoList
from Parts.Scripts.ExtractFromText import Extract
from Parts.Scripts.LineOffset import OffsetTextWithSpaces
from Parts.Tools.TextConverter import convert

textTablePath = r'OtherFiles/Tables/TextTable.xlsx'
extractedTextTablePath = r'OtherFiles/Tables/ExtractedTextTable.xlsx'
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
    if not path.exists(inputFolder):
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف كل العمليات،\nالمجلد الحاوي للملفات غير موجود.")
        return
    if not path.exists(outputFolder):
        mkdir(outputFolder)
    
    return True

def prepareTextAndTranslation(text, translation, convertBool):
    if not text: return
    if not translation: translation = ''
    if convertBool: translation = convert(translation, False)
    
    if EnteringWindow.tooLongCheck.isChecked():
        if len(translation.encode().hex()) > len(text.encode().hex()): return
    
    return translation

def getTextListFromTable(textTablePath, convertBool):
    textList = []
    if textTablePath.endswith('.csv'):
        csvTable = CSVtoList(textTablePath)
        for row in csvTable:
            try:
                text = row[0]
                translation = row[1]
            except: continue
            
            translation = prepareTextAndTranslation(text, translation, convertBool)
            if translation == None: continue
            textList.append([text, translation])
    
    elif textTablePath.endswith('.xlsx'):
        textXlsx = openpyxl.load_workbook(textTablePath)
        for sheet in textXlsx.sheetnames:
            textTable = textXlsx.get_sheet_by_name(sheet)
            for cell in range(2, len(textTable['A'])+1):
                text = textTable['A'+str(cell)].value
                translation = textTable['B'+str(cell)].value
                
                translation = prepareTextAndTranslation(text, translation, convertBool)
                if translation == None: continue
                textList.append([text, translation])
    
    return sorted(textList, key=lambda x: len(str(x[0])), reverse=True)

def putInXlsx(text, sheet, cell, isbold = False, isAlignted = False, fill = False):
    sheet[cell].value = text
    sheet[cell].font = Font(bold=isbold)
    if isAlignted: sheet[cell].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    if fill: sheet[cell].fill = PatternFill(fill_type='solid', start_color=fill, end_color=fill)

def enter(convertBool = True):
    if not prepareToEnter(): return
    
    filesList = dirList(inputFolder)
    if not filesList:
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف كل العمليات،\nلا توجد أي ملفات للإدخال إليها.")
        return
    
    if EnteringWindow.databaseCheck.isChecked():
        if not path.exists(textTablePath):
            QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف كل العمليات،\nقاعدة بيانات النصوص غير موجودة.")
            return
        
        textList = getTextListFromTable(textTablePath, convertBool)
    else:
        text = EnteringWindow.textBox.toPlainText()
        if not text: return
        translation = prepareTextAndTranslation(text, EnteringWindow.translationBox.toPlainText(), convertBool)
        if translation == None: return
        textList = [[text, translation]]
    
    before = byteInCell(EnteringWindow.beforeText.toPlainText())
    after = byteInCell(EnteringWindow.afterText.toPlainText())
    
    
    for filename in filesList:
        with open(filename, 'rb') as f:
            fileContent = f.read()
        
        textListLength, deletedText = len(textList), 0
        for i in range(textListLength):
            i -= deletedText
            
            text, translation = before + textList[i][0] + after, before + textList[i][1] + after
            byteText = text.encode()
            
            if EnteringWindow.translationOffsetCheck.isChecked():
                spacesNum = (len(text.encode().hex()) - len(translation.encode().hex())) // 2
                translation = OffsetTextWithSpaces(translation, 0, EnteringWindow.Offset.currentIndex(), spacesNum)
            
            if byteText not in fileContent: continue
            fileContent = fileContent.replace(byteText, translation.encode(), 1)
            del textList[i]
            deletedText += 1
        
        savePath = filename.replace(inputFolder, outputFolder, 1)
        makedirs(path.dirname(savePath), exist_ok=True) # للتأكد من عدم حصول أي مشكلة بسبب عبث المستخدم لأن العملية تأخذ وقتاً
        with open(savePath, 'wb') as f:
            f.write(fileContent)
        if textList:
            content = ''
            for item in textList:
                content += str(item) + '\n'
            StudioWindow.AddReportWindow('لم يتم إيجاده', content)
    
    QMessageBox.about(EnteringWindow, "!!تهانيّ", "انتهى الإدخال.")

def extract():
    before = byteInCell(EnteringWindow.beforeText.toPlainText()).encode()
    after  = byteInCell(EnteringWindow.afterText.toPlainText()).encode()
    if not before or not after:
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف العملية،\nاملأ حقلي: ما يسبق النصوص، ما يلحقها.")
        return
    filesList = dirList(inputFolder)
    if not len(filesList):
        QMessageBox.about(EnteringWindow, "!!خطأ", "تم إيقاف العملية،\nلا توجد أي ملفات للاستخراج منها.")
        return
    
    mini = byteInCell(EnteringWindow.minText.toPlainText())
    maxi = byteInCell(EnteringWindow.maxText.toPlainText())
    
    if extractedTextTablePath.endswith('.csv'):
        with open(extractedTextTablePath, 'w', encoding='utf8', errors='replace') as database: # 'wb'
            content = ''
            
            for filename in filesList:
                with open(filename, 'rb') as f:
                    fileContent = f.read()
                
                extracted = Extract(fileContent, before, after, True, mini, maxi)
                if len(extracted):
                    content += f'<-- {filename} -->\n'
                    for item in extracted:
                        item = item.decode(encoding='utf8', errors='replace')
                        if _CSV_DELIMITER_ in item:
                            item = f'"{item}"'.replace('\n', '"\n"').replace('\r', '"\r"')
                            item = f'"{item}"'.replace('"\r""\n"', '"\r\n"').replace('"\n""\r"', '"\n\r"')
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
            
            extracted = Extract(fileContent, before, after, True, mini, maxi)
            if len(extracted):
                putInXlsx(filename, sheet, 'A'+str(row), True, True, 'D112D1')
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