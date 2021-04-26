from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, QRadioButton
from PyQt5.QtCore import QRect, Qt
from Parts.Scripts.ConvertTables import *
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
    if XmlToAteRadio.isChecked():
        openDirectory = openFile('fnt')
        saveDirectory = saveFile('ate')
        
        tableContent = open(openDirectory, 'r', encoding='utf-8').read()
        open(saveDirectory, 'w', encoding='utf-8').write(XmlToAte(tableContent))
    
    QMessageBox.about(TablesConverterWindow, "!!تم", "!!تم")
    

app = QApplication(argv)

windowWidth = 300
radioWidth = windowWidth - 20

TablesConverterWindow = QMainWindow()
TablesConverterWindow.setFixedSize(windowWidth, 100)

tableButton = QPushButton(TablesConverterWindow)
tableButton.setGeometry(QRect(20, 50, 100, 40))
tableButton.setText("اختر جدول\nوحوّله")

tableButton.clicked.connect(lambda: convertTable())

XmlToAteRadio = QRadioButton("تحويل جدول BMFont Xml إلى جداول آسغور Ate", TablesConverterWindow)
XmlToAteRadio.setGeometry(QRect(10, 10, radioWidth, 26))
XmlToAteRadio.setLayoutDirection(Qt.RightToLeft)