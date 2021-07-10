import re, pyautogui, pyperclip, keyboard, time
from PyQt5.QtWidgets import QApplication, QMessageBox
from sys import argv, exit
from os import path

from Parts.Scripts.UsefulLittleFunctions import *
from Parts.Scripts.FreezeArabic import Freeze
from Parts.Scripts.ExtractFromText import Extract
from Parts.Scripts.ConvertBytes import convertBytes
from Parts.Scripts.ReverseText import Reverse
from Parts.Scripts.ConvertText import Convert
from Parts.Scripts.HandleHarakat import handleHarakat
from Parts.Scripts.TakeFromTable import TakeFromTable


convertingTablePath = r'OtherFiles/Tables/CharsConvertingTable.act'

if path.exists(convertingTablePath): convert_database = TakeFromTable(convertingTablePath)
else: convert_database = {}


def opentextFile():
    filePath = openFile(('act', 'zts'), TextConverterWindow, 'جدول التحويل')
    if not filePath: return
    TextConverterWindow.enteredBox.setPlainText(open(filePath, 'r', encoding='utf-8').read())

def openConvertTable():
    tablePath = openFile(('act', 'zts'), TextConverterOptionsWindow, 'جدول التحويل')
    if not tablePath: return
    global convertingTablePath
    convertingTablePath = tablePath

def cell():
    cell._startCommand  = byteInCell(TextConverterOptionsWindow.startCommand.toPlainText())
    cell._endCommand    = byteInCell(TextConverterOptionsWindow.endCommand.toPlainText())
    cell._pageCommand   = byteInCell(TextConverterOptionsWindow.pageCommand.toPlainText())
    cell._lineCommand   = byteInCell(TextConverterOptionsWindow.lineCommand.toPlainText())
    cell._beforeText    = byteInCell(TextConverterOptionsWindow.beforeText.toPlainText())
    cell._afterText     = byteInCell(TextConverterOptionsWindow.afterText.toPlainText())
    cell._convertedByte = byteInCell(TextConverterOptionsWindow.convertedByte.toPlainText())

def lastConvertingStep(text):
    HarakatOptionindex = TextConverterOptionsWindow.HarakatComboBox.currentIndex()
    if HarakatOptionindex: text = handleHarakat(text, HarakatOptionindex)#Handle Harakat
    if TextConverterOptionsWindow.RA_check.isChecked() or TextConverterOptionsWindow.C_check.isChecked(): text = Freeze(text)#Freeze Arabic
    if TextConverterOptionsWindow.C_check.isChecked(): text = Convert(text, convert_database, True)#Convert
    if TextConverterOptionsWindow.RT_check.isChecked(): text = Reverse(text) #Reverse whole text
    if TextConverterOptionsWindow.RAO_check.isChecked(): text = Reverse(text, False) #‫Reverse Arabic only
    if TextConverterOptionsWindow.UC_check.isChecked(): text = Convert(text, convert_database, False)#Unconvert
    if TextConverterOptionsWindow.UA_check.isChecked() or TextConverterOptionsWindow.UC_check.isChecked(): text = Freeze(text, False)#UnFreeze Arabic
    if TextConverterOptionsWindow.CB_check.isChecked(): text = convertBytes(text, cell._convertedByte)#Convert bytes
    return text

def convert(text):
    if not text: return
    if (TextConverterOptionsWindow.C_check.isChecked() or TextConverterOptionsWindow.UC_check.isChecked()) and not path.exists(convertingTablePath):
        QMessageBox.about(TextConverter, "!!خطأ", "قاعدة بيانات التحويل غير موجودة")
        return
        
    cell()
    
    if TextConverterOptionsWindow.Ext_check.isChecked():#Extract from text
        if not cell._beforeText or not cell._afterText:
            QMessageBox.about(EnteringWindow, "!!خطأ", "املأ حقلي: ما قبل النصوص، ما بعدها.\nعلى الأقل للاستخراج.")
            return
        
        mini = byteInCell(TextConverterOptionsWindow.miniText.toPlainText())
        maxi = byteInCell(TextConverterOptionsWindow.maxText.toPlainText())
        text = Extract(text, cell._beforeText, cell._afterText, True, mini, maxi, TextConverterOptionsWindow.EnglishOnlyCheck.isChecked())
        text = '\n'.join(text)
        if not text: return
    
    textPagesList = Split(text, cell._pageCommand)
    
    for p in range(len(textPagesList)):
        if TextConverterOptionsWindow.DDL_check.isChecked(): textPagesList[p] = DeleteDuplicatedLines(textPagesList[p], cell._lineCommand) #Delete Duplicated lines
        if TextConverterOptionsWindow.SSL_check.isChecked(): textPagesList[p] = SortLines(textPagesList[p], cell._lineCommand) #Sort short to long
        if TextConverterOptionsWindow.SLS_check.isChecked(): textPagesList[p] = SortLines(textPagesList[p], cell._lineCommand, False) #Sort long to short
    
        linesList = Split(textPagesList[p], cell._lineCommand)
        
        for l in range(len(linesList)):
            linesList[l] = splitByBeforeAfterAndDo(
                linesList[l], cell._startCommand, cell._endCommand , lastConvertingStep,
                TextConverterOptionsWindow.RT_check.isChecked() or TextConverterOptionsWindow.RAO_check.isChecked()
                )
        textPagesList[p] = cell._lineCommand.join(linesList)
    text = cell._pageCommand.join(linesList)
    
    return text

def convertFiles():
    folderPath = selectFolder(EnteringWindow)
    if not folderPath: return
    files = dirList(folderPath)
    
    for file in files:
        content = open(file, 'r', encoding='utf-8').read()
        if not content: continue
        open(file, 'w', encoding='utf-8').write(convert(content))
    
    QMessageBox.about(EnteringWindow, "!!تهانينا", "انتهى تحويل الملفات.")

def convertByHotkey():
    # if not TextConverter.isActiveWindow(): return
    pyperclip.copy('')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(.01)  # لنضمن ألا يسبق البرنامج ctrl-c
    pyperclip.copy(convert(pyperclip.paste()))
    pyautogui.hotkey('ctrl', 'v')


app = QApplication(argv)
from Parts.Windows import TextConverterWindow, TextConverterOptionsWindow


TextConverterWindow.convertButton.clicked.connect(
    lambda: TextConverterWindow.resultBox.setPlainText(convert(TextConverterWindow.enteredBox.toPlainText()))
    )
TextConverterWindow.openFileButton.clicked.connect(lambda: opentextFile())
TextConverterWindow.ConvertFilesButton.clicked.connect(lambda: convertFiles())
TextConverterOptionsWindow.C_databaseButton.clicked.connect(lambda: openConvertTable())

keyboard.add_hotkey("ctrl+b", lambda: convertByHotkey())

if __name__ == '__main__':
    TextConverterWindow.show()
    exit(app.exec_())