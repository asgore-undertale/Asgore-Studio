from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, QRadioButton, QComboBox, QLabel
from PyQt5.QtCore import QRect, Qt
from Parts.Scripts.ConvertTables import *
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
    if XmlToaftRadio.isChecked():
        openDirectory, saveDirectory = openFile('fnt'), saveFile('aft')
        open(saveDirectory, 'w', encoding='utf-8').write(XmlToAft(open(openDirectory, 'r', encoding='utf-8').read()))

    else:
        From = fromComboBox.currentText()
        To = toComboBox.currentText()
        openDirectory, saveDirectory = openFile(From), saveFile(To)
        
        if From == 'act': charmap = TakeFromACT(openDirectory)
        if From == 'zts': charmap = TakeFromZTS(openDirectory)
        
        if To == 'act': table = charmapToACT(charmap)
        if To == 'zts': table = charmapToZTS(charmap)
        
        open(saveDirectory, 'w', encoding='utf-8').write(table)
        
    QMessageBox.about(TablesConverterWindow, "!!تم", "!!تم")


app = QApplication(argv)

windowWidth = 300
radioWidth = windowWidth - 20

TablesConverterWindow = QMainWindow()
TablesConverterWindow.setFixedSize(windowWidth, 130)

convertButton = QPushButton(TablesConverterWindow)
convertButton.setGeometry(QRect(100, 80, 90, 40))
convertButton.setText("اختر جدول\nوحوّله")
convertButton.clicked.connect(lambda: convertTable())

XmlToaftRadio = QRadioButton("تحويل جدول BMFont Xml إلى جداول خطوط آسغور aft", TablesConverterWindow)
XmlToaftRadio.setGeometry(QRect(10, 10, radioWidth, 26))
XmlToaftRadio.setLayoutDirection(Qt.RightToLeft)

comboLineWidth = 240

fromLabel = QLabel(TablesConverterWindow)
fromLabel.setGeometry(QRect(comboLineWidth, 40, 40, 25))
fromLabel.setText("تحويل:")
toLabel = QLabel(TablesConverterWindow)
toLabel.setGeometry(QRect(comboLineWidth-75, 40, 30, 25))
toLabel.setText("إلى:")

fromComboBoxOptions = [
    "act",
    "zts"
]
toComboBoxOptions = [
    "act",
    "zts"
]
fromComboBox = QComboBox(TablesConverterWindow)
fromComboBox.addItems(fromComboBoxOptions)
fromComboBox.setGeometry(QRect(comboLineWidth-35, 40, 40, 25))
toComboBox = QComboBox(TablesConverterWindow)
toComboBox.addItems(fromComboBoxOptions)
toComboBox.setGeometry(QRect(comboLineWidth-110, 40, 40, 25))