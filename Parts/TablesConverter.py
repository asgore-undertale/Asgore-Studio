from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, QRadioButton, QComboBox, QLabel
from PyQt5.QtCore import QRect, Qt
from Parts.Scripts.CharmapToTable import *
from Parts.Scripts.Take_From_Table import *
from os import path
from sys import exit, argv

def openFile(type : str):
    _open, _ = QFileDialog.getOpenFileName(TablesConverterWindow, 'جدول الخط', '' , '*.'+type)
    if _open == '/' or not _open or not path.exists(_open): return
    return _open

def saveFile(type : str):
    _save, _ = QFileDialog.getSaveFileName(TablesConverterWindow, 'قاعدة بيانات النص', '' , '*.'+type)
    if _save == '/' or not _save: return
    return _save
    
def convertTable():
    try:
        From = fromComboBox.currentText()
        To = toComboBox.currentText()
        openDirectory = openFile(From)
        if openDirectory: saveDirectory = saveFile(To)
        if not openDirectory or not saveDirectory: return
        
        if From == 'act': charmap = TakeFromACT(openDirectory)
        if From == 'zts': charmap = TakeFromZTS(openDirectory)
        if From == 'fnt': charmap = TakeFromFNT(openDirectory)
        
        if To == 'act': table = charmapToACT(charmap)
        if To == 'zts': table = charmapToZTS(charmap)
        if To == 'aft': table = charmapToAFT(charmap)
        
        if not table: return
        open(saveDirectory, 'w', encoding='utf-8').write(table)
        QMessageBox.about(TablesConverterWindow, "!!تم", "!!تم")
    except: pass


app = QApplication(argv)

TablesConverterWindow = QMainWindow()
TablesConverterWindow.setFixedSize(300, 100)

convertButton = QPushButton(TablesConverterWindow)
convertButton.setGeometry(QRect(100, 50, 90, 40))
convertButton.setText("اختر جدول\nوحوّله")
convertButton.clicked.connect(lambda: convertTable())

comboLineWidth = 240
y = 10

fromComboBoxOptions = [
    "act",
    "fnt",
    "zts"
]
toComboBoxOptions = [
    "act",
    "aft",
    "zts"
]
fromComboBox = QComboBox(TablesConverterWindow)
fromComboBox.addItems(fromComboBoxOptions)
fromComboBox.setGeometry(QRect(comboLineWidth-35, y, 40, 25))
toComboBox = QComboBox(TablesConverterWindow)
toComboBox.addItems(toComboBoxOptions)
toComboBox.setGeometry(QRect(comboLineWidth-110, y, 40, 25))

fromLabel = QLabel(TablesConverterWindow)
fromLabel.setGeometry(QRect(comboLineWidth, y, 40, 25))
fromLabel.setText("تحويل:")
toLabel = QLabel(TablesConverterWindow)
toLabel.setGeometry(QRect(comboLineWidth-75, y, 30, 25))
toLabel.setText("إلى:")