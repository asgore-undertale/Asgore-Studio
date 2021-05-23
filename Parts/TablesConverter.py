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
    if XmlToaftRadio.isChecked():
        openDirectory, saveDirectory = openFile('fnt'), saveFile('aft')
        open(saveDirectory, 'w', encoding='utf-8').write(XmlToAft(open(openDirectory, 'r', encoding='utf-8').read()))
    
    elif ZtsToActRadio.isChecked():
        openDirectory, saveDirectory = openFile('zts'), saveFile('act')
        open(saveDirectory, 'w', encoding='utf-8').write(ZtsToAct(open(openDirectory, 'r', encoding='utf-8').read()))

    else: return
    QMessageBox.about(TablesConverterWindow, "!!تم", "!!تم")


app = QApplication(argv)

windowWidth = 300
radioWidth = windowWidth - 20

TablesConverterWindow = QMainWindow()
TablesConverterWindow.setFixedSize(windowWidth, 120)

tableButton = QPushButton(TablesConverterWindow)
tableButton.setGeometry(QRect(20, 70, 100, 40))
tableButton.setText("اختر جدول\nوحوّله")

tableButton.clicked.connect(lambda: convertTable())

XmlToaftRadio = QRadioButton("تحويل جدول BMFont Xml إلى جداول خطوط آسغور aft", TablesConverterWindow)
XmlToaftRadio.setGeometry(QRect(10, 10, radioWidth, 26))
XmlToaftRadio.setLayoutDirection(Qt.RightToLeft)
ZtsToActRadio = QRadioButton("تحويل جدول zts إلى جداول تحويل آسغور Act", TablesConverterWindow)
ZtsToActRadio.setGeometry(QRect(10, 30, radioWidth, 26))
ZtsToActRadio.setLayoutDirection(Qt.RightToLeft)