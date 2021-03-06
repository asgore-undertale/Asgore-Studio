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
    filePath = openFile(['*'], TextConverterWindow, 'ملف')
    if not filePath: return
    TextConverterWindow.enteredBox.setPlainText(open(filePath, 'r', encoding='utf-8').read())

def openConvertTable():
    tablePath = openFile(('act', 'csv', 'tbl', 'zts', 'zta'), TextConverterOptionsWindow, 'جدول التحويل')
    if not tablePath: return
    global convertingTablePath, convertDatabase
    convertingTablePath = tablePath
    convertDatabase = TakeFromTable(convertingTablePath)

def openByteTable():
    tablePath = openFile(['tbl'], TextConverterOptionsWindow, 'تيبل')
    if not tablePath: return
    global byteTable
    byteTable = TakeFromTable(tablePath)

def getCustomScriptsList():
    return list(filter(lambda x: x.endswith('.py'), dirList(r'CustomScripts\TextConverterScripts')))

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

def takeFromCell(celltext):
    if TextConverterOptionsWindow.FixSlashes.isChecked():
        return fixSlashes(celltext)
    return celltext

def cell():
    cell._startCommand = takeFromCell(TextConverterOptionsWindow.startCommand.getValue())
    cell._endCommand = takeFromCell(TextConverterOptionsWindow.endCommand.getValue())
    cell._pageCommand = takeFromCell(TextConverterOptionsWindow.pageCommand.getValue())
    cell._lineCommand = takeFromCell(TextConverterOptionsWindow.lineCommand.getValue())
    cell._newpageCommand = takeFromCell(TextConverterOptionsWindow.newpageCommand.getValue())
    cell._newlineCommand = takeFromCell(TextConverterOptionsWindow.newlineCommand.getValue())
    cell._byte_1 = takeFromCell(TextConverterOptionsWindow.byte_1.getValue())
    cell._byte_2 = takeFromCell(TextConverterOptionsWindow.byte_2.getValue())
    cell._resultByteLength = takeFromCell(TextConverterOptionsWindow.resultByteLength.getValue())
    cell._readByteLength = takeFromCell(TextConverterOptionsWindow.readByteLength.getValue())
    cell._readByteLength2 = takeFromCell(TextConverterOptionsWindow.readByteLength2.getValue())
    cell._placeHolder = takeFromCell(TextConverterOptionsWindow.placeHolder.getValue())

def applyConverts(text):
    CustomScriptindex = TextConverterOptionsWindow.CustomScriptComboBox.currentIndex()
    HarakatOptionindex = TextConverterOptionsWindow.HarakatComboBox.currentIndex()
    UnicodeOptionindex = TextConverterOptionsWindow.unicodeComboBox.currentIndex()
    useBytesTable = TextConverterOptionsWindow.UseTable.isChecked()
    
    if CustomScriptindex > 1:
        text = applyCustomScripts(text) # Custom Script
    
    if UnicodeOptionindex == 1:
        text = convertBytes(text, cell._byte_1, cell._byte_2, (cell._readByteLength, cell._readByteLength2), cell._resultByteLength,
            'hextohex', byteTable, cell._placeHolder, useBytesTable) # Convert bytes
    elif UnicodeOptionindex == 2:
        text = convertBytes(text, cell._byte_1, cell._byte_2, (cell._readByteLength, cell._readByteLength2), cell._resultByteLength,
            'hextotext', byteTable, cell._placeHolder, useBytesTable) # Convert bytes
    
    if HarakatOptionindex:
        text = handleHarakat(text, HarakatOptionindex)# Handle Harakat
    if TextConverterOptionsWindow.RA_check.isChecked() or TextConverterOptionsWindow.C_check.isChecked():
        text = Freeze(text)# Freeze Arabic
    if TextConverterOptionsWindow.RT_check.isChecked():
        text = Reverse(text) # Reverse whole text
    if TextConverterOptionsWindow.RAO_check.isChecked():
        text = Reverse(text, False) # ‫Reverse Arabic only
    if TextConverterOptionsWindow.C_check.isChecked():
        text = Convert(text, convertDatabase, True)# Convert
    if TextConverterOptionsWindow.UC_check.isChecked():
        text = Convert(text, convertDatabase, False)# Unconvert
    if TextConverterOptionsWindow.UA_check.isChecked() or TextConverterOptionsWindow.UC_check.isChecked():
        text = Freeze(text, False)# UnFreeze Arabic
    
    if UnicodeOptionindex == 3:
        text = convertBytes(text, cell._byte_1, cell._byte_2, (cell._readByteLength, cell._readByteLength2), cell._resultByteLength,
            'texttohex', byteTable, cell._placeHolder, useBytesTable) # Convert bytes
    elif UnicodeOptionindex == 4:
        text = convertBytes(text, cell._byte_1, cell._byte_2, (cell._readByteLength, cell._readByteLength2), cell._resultByteLength,
            'unicodetotext', byteTable, cell._placeHolder, useBytesTable) # Convert bytes
    elif UnicodeOptionindex == 5:
        text = convertBytes(text, cell._byte_1, cell._byte_2, (cell._readByteLength, cell._readByteLength2), cell._resultByteLength,
            'texttounicode', byteTable, cell._placeHolder, useBytesTable) # Convert bytes
    
    return text

def sortText(text):
    textPagesList = Split(text, cell._pageCommand)
    for p in range(len(textPagesList)):
        if TextConverterOptionsWindow.DDL_check.isChecked():
            textPagesList[p] = DeleteDuplicatedLines(textPagesList[p], cell._lineCommand) #Delete Duplicated lines
            
        sortOptionindex = TextConverterOptionsWindow.sortComboBox.currentIndex()
        if sortOptionindex == 1:
            textPagesList[p] = SortLines(textPagesList[p], cell._lineCommand, 'length') #Sort short to long
        elif sortOptionindex == 2:
            textPagesList[p] = SortLines(textPagesList[p], cell._lineCommand, 'length', True) #Sort long to short
        elif sortOptionindex == 3:
            textPagesList[p] = SortLines(textPagesList[p], cell._lineCommand) #Sort Alphabetic
            
        if TextConverterOptionsWindow.RL_check.isChecked():
            textPagesList[p] = cell._lineCommand.join(textPagesList[p].split(cell._lineCommand)[::-1]) #Reverse Lines
    text = cell._pageCommand.join(textPagesList)
    
    if TextConverterOptionsWindow.RP_check.isChecked():  text = cell._pageCommand.join(text.split(cell._pageCommand)[::-1]) #Reverse Pages
    
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
    
    text = sortText(text)
    
    if cell._newpageCommand and cell._pageCommand:
        text = text.replace(cell._pageCommand, cell._newpageCommand)
    if cell._newlineCommand and cell._lineCommand:
        text = text.replace(cell._lineCommand, cell._newlineCommand)
    
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

def convertSelectedText():
    pyperclip.copy('')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(.05)  # لنضمن ألا يسبق البرنامج ctrl-c
    pyperclip.copy(convert(pyperclip.paste()))
    pyautogui.hotkey('ctrl', 'v')

def PasteAndConvert():
    time.sleep(.05)
    pyperclip.copy(convert(pyperclip.paste()))
    pyautogui.hotkey('ctrl', 'v')

def AutoConvert():
    if not TextConverterOptionsWindow.AutoConvertCheck.isChecked(): return
    TextConverterWindow.resultBox.setPlainText(convert(TextConverterWindow.enteredBox.toPlainText()))

# -------------------------------------------------->

app = QApplication(argv)
from Parts.Windows import TextConverterWindow, TextConverterOptionsWindow


loadCustomScripts()
convertDatabase, byteTable = {}, {}
convertingTablePath = r'OtherFiles/Tables/CharsConvertingTable.act'
if path.exists(convertingTablePath): convertDatabase = TakeFromTable(convertingTablePath)

TextConverterWindow.convertButton.clicked.connect(
    lambda: TextConverterWindow.resultBox.setPlainText(convert(TextConverterWindow.enteredBox.toPlainText()))
    )
TextConverterWindow.openFileButton.clicked.connect(lambda: opentextFile())
TextConverterWindow.ConvertFilesButton.clicked.connect(lambda: convertFiles())
TextConverterOptionsWindow.C_databaseButton.clicked.connect(lambda: openConvertTable())
TextConverterOptionsWindow.bytesTableButton.clicked.connect(lambda: openByteTable())
TextConverterOptionsWindow.CustomScriptComboBox.currentIndexChanged.connect(loadCustomScripts)
TextConverterWindow.enteredBox.textChanged.connect(AutoConvert)

keyboard.add_hotkey("ctrl+b", lambda: convertSelectedText())
keyboard.add_hotkey("ctrl+shift+b", lambda: PasteAndConvert())
keyboard.add_hotkey("ctrl+p", lambda: keyboard.write(TextConverterOptionsWindow.newpageCommand.getValue()))
keyboard.add_hotkey("ctrl+l", lambda: keyboard.write(TextConverterOptionsWindow.newlineCommand.getValue()))

if __name__ == '__main__':
    TextConverterWindow.show()
    exit(app.exec_())
