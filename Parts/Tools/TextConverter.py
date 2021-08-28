import re, pyautogui, pyperclip, keyboard, time
from PyQt5.QtWidgets import QApplication, QMessageBox
from sys import argv, exit
from os import path

from Parts.Scripts.UsefulLittleFunctions import *
from Parts.Scripts.FreezeArabic import Freeze
from Parts.Scripts.ConvertBytes import convertBytes
from Parts.Scripts.ReverseText import Reverse
from Parts.Scripts.ConvertText import Convert
from Parts.Scripts.HandleHarakat import handleHarakat
from Parts.Scripts.TakeFromTable import TakeFromTable


def opentextFile():
    filePath = openFile(('act', 'zts'), TextConverterWindow, 'جدول التحويل')
    if not filePath: return
    TextConverterWindow.enteredBox.setPlainText(open(filePath, 'r', encoding='utf-8').read())

def openConvertTable():
    tablePath = openFile(('act', 'zts'), TextConverterOptionsWindow, 'جدول التحويل')
    if not tablePath: return
    global convertingTablePath, convertDatabase
    convertingTablePath = tablePath
    convertDatabase = TakeFromTable(convertingTablePath)

def getCustomScriptsList():
    return list(filter(lambda x: x.endswith('.py'), dirList(r'Parts\CustomScripts')))

def loadCustomScripts():
    CustomScriptindex = TextConverterOptionsWindow.CustomScriptComboBox.currentIndex()
    if CustomScriptindex: return
    
    CustomScript = []
    for script in getCustomScriptsList(): 
        try:
            exec(f"from {ToModulePath(script)} import Name", globals())
            CustomScript.append(Name)
        except Exception as e: print(e)
    
    TextConverterOptionsWindow.CustomScriptComboBox.blockSignals(True)
    TextConverterOptionsWindow.CustomScriptComboBox.clear()
    TextConverterOptionsWindow.CustomScriptComboBox.AddItems(['تحديث القائمة', '...'])
    TextConverterOptionsWindow.CustomScriptComboBox.AddCheckBoxItems(CustomScript)
    TextConverterOptionsWindow.CustomScriptComboBox.setCurrentIndex(1)
    TextConverterOptionsWindow.CustomScriptComboBox.blockSignals(False)

def applyCustomScripts(text):
    scripts = getCustomScriptsList()
    indexes = TextConverterOptionsWindow.CustomScriptComboBox.check_items()
    for index in indexes:
        try:
            exec(f"from {ToModulePath(scripts[index-2])} import Script", globals())
            text = Script(text)
        except Exception as e: print(e)
    
    return text

def cell():
    cell._startCommand  = byteInCell(TextConverterOptionsWindow.startCommand.toPlainText())
    cell._endCommand    = byteInCell(TextConverterOptionsWindow.endCommand.toPlainText())
    cell._pageCommand   = byteInCell(TextConverterOptionsWindow.pageCommand.toPlainText())
    cell._lineCommand   = byteInCell(TextConverterOptionsWindow.lineCommand.toPlainText())
    cell._convertedByte = byteInCell(TextConverterOptionsWindow.convertedByte.toPlainText())
    
    if not TextConverterOptionsWindow.FixSlashes.isChecked(): return
    cell._startCommand  = fixSlashes(cell._startCommand)
    cell._endCommand    = fixSlashes(cell._endCommand)
    cell._pageCommand   = fixSlashes(cell._pageCommand)
    cell._lineCommand   = fixSlashes(cell._lineCommand)
    cell._convertedByte = fixSlashes(cell._convertedByte)

def applyConverts(text):
    CustomScriptindex = TextConverterOptionsWindow.CustomScriptComboBox.currentIndex()
    HarakatOptionindex = TextConverterOptionsWindow.HarakatComboBox.currentIndex()
    if CustomScriptindex > 1: text = applyCustomScripts(text)# Custom Script
    if HarakatOptionindex: text = handleHarakat(text, HarakatOptionindex)# Handle Harakat
    if TextConverterOptionsWindow.RA_check.isChecked() or TextConverterOptionsWindow.C_check.isChecked(): text = Freeze(text)# Freeze Arabic
    if TextConverterOptionsWindow.RT_check.isChecked(): text = Reverse(text) # Reverse whole text
    if TextConverterOptionsWindow.RAO_check.isChecked(): text = Reverse(text, False) # ‫Reverse Arabic only
    if TextConverterOptionsWindow.C_check.isChecked(): text = Convert(text, convertDatabase, True)# Convert
    if TextConverterOptionsWindow.UC_check.isChecked(): text = Convert(text, convertDatabase, False)# Unconvert
    if TextConverterOptionsWindow.UA_check.isChecked() or TextConverterOptionsWindow.UC_check.isChecked(): text = Freeze(text, False)# UnFreeze Arabic
    if TextConverterOptionsWindow.CB_check.isChecked(): text = convertBytes(text, cell._convertedByte)# Convert bytes
    return text

def convert(text, thisTool = True):
    if not text: return ''
    if (TextConverterOptionsWindow.C_check.isChecked() or TextConverterOptionsWindow.UC_check.isChecked()) and not path.exists(convertingTablePath):
        QMessageBox.about(TextConverterWindow, "!!خطأ", "جدول التحويل غير موجود")
        return
        
    cell()
    
    sentences = splitTextBySoperators(text, (cell._pageCommand, cell._lineCommand))
    for s in range(len(sentences)):
        if s % 2: continue
        sentences[s] = splitByBeforeAfterComAndDo(
            sentences[s], cell._startCommand, cell._endCommand , applyConverts,
            TextConverterOptionsWindow.RT_check.isChecked() or TextConverterOptionsWindow.RAO_check.isChecked()
            )
    text = ''.join(sentences)
    
    
    textPagesList = Split(text, cell._pageCommand)
    for p in range(len(textPagesList)):
        if TextConverterOptionsWindow.DDL_check.isChecked(): textPagesList[p] = DeleteDuplicatedLines(textPagesList[p], cell._lineCommand) #Delete Duplicated lines
        if TextConverterOptionsWindow.SSL_check.isChecked(): textPagesList[p] = SortLines(textPagesList[p], cell._lineCommand) #Sort short to long
        if TextConverterOptionsWindow.SLS_check.isChecked(): textPagesList[p] = SortLines(textPagesList[p], cell._lineCommand, False) #Sort long to short
        if TextConverterOptionsWindow.RL_check.isChecked():  textPagesList[p] = cell._lineCommand.join(textPagesList[p].split(cell._lineCommand)[::-1]) #Reverse Lines
    text = cell._pageCommand.join(textPagesList)
    if TextConverterOptionsWindow.RP_check.isChecked():  text = cell._pageCommand.join(text.split(cell._pageCommand)[::-1]) #Reverse Pages
    
    if thisTool and TextConverterOptionsWindow.AutoCopyCheck.isChecked():
        pyperclip.copy(text)
    
    return text

def convertFiles():
    folderPath = selectFolder(TextConverterWindow)
    if not folderPath: return
    files = dirList(folderPath)
    
    for file in files:
        content = open(file, 'r', encoding='utf-8').read()
        if not content: continue
        open(file, 'w', encoding='utf-8').write(convert(content))
    
    QMessageBox.about(TextConverterWindow, "!!تهانينا", "انتهى تحويل الملفات.")

def convertByHotkey():
    # if not TextConverter.isActiveWindow(): return
    pyperclip.copy('')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(.01)  # لنضمن ألا يسبق البرنامج ctrl-c
    pyperclip.copy(convert(pyperclip.paste()))
    pyautogui.hotkey('ctrl', 'v')

# -------------------------------------------------->

app = QApplication(argv)
from Parts.Windows import TextConverterWindow, TextConverterOptionsWindow


loadCustomScripts()
convertDatabase = {}
convertingTablePath = r'OtherFiles/Tables/CharsConvertingTable.act'
if path.exists(convertingTablePath): convertDatabase = TakeFromTable(convertingTablePath)

TextConverterWindow.convertButton.clicked.connect(
    lambda: TextConverterWindow.resultBox.setPlainText(convert(TextConverterWindow.enteredBox.toPlainText()))
    )
TextConverterWindow.openFileButton.clicked.connect(lambda: opentextFile)
TextConverterWindow.ConvertFilesButton.clicked.connect(lambda: convertFiles)
TextConverterOptionsWindow.C_databaseButton.clicked.connect(lambda: openConvertTable)
TextConverterOptionsWindow.CustomScriptComboBox.currentIndexChanged.connect(loadCustomScripts)

keyboard.add_hotkey("ctrl+b", lambda: convertByHotkey())

if __name__ == '__main__':
    TextConverterWindow.show()
    exit(app.exec_())
