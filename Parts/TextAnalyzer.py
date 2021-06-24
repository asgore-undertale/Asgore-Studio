from Parts.Scripts.AnalyzeText import AnalyzeText
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from sys import argv, exit
from os import path

AnalyzeWindow = QMainWindow()
AnalyzeWindow.resize(200, 200)
container = QWidget()

layout = QGridLayout()
container.setLayout(layout)
AnalyzeWindow.setCentralWidget(container)


minilayout3 = QVBoxLayout()
logBox = QTextEdit(AnalyzeWindow)
logLabel = QLabel()
logLabel.setText("   الإحصاءات:")

minilayout2 = QVBoxLayout()
enteredBox = QTextEdit(AnalyzeWindow)
resultBox = QTextEdit(AnalyzeWindow)
enteredBox.setPlainText('تجربة الاختزال')

enteredLabel = QLabel()
resultLabel = QLabel()
enteredLabel.setText("   النص الداخل:")
resultLabel.setText("   النص الناتج:")

minilayout = QHBoxLayout()
analyzeButton = QPushButton()
openFileButton = QPushButton()
openConvertFilesButton = QPushButton()
analyzeButton.setText("اختزال\nالنص")
openFileButton.setText("فتح ملف\nنص")

layout.addLayout(minilayout2, 0, 0)
layout.addLayout(minilayout3, 0, 1)
layout.addLayout(minilayout, 1, 1)
minilayout.addWidget(openFileButton)
minilayout.addWidget(analyzeButton)
minilayout2.addWidget(enteredLabel)
minilayout2.addWidget(enteredBox)
minilayout2.addWidget(resultLabel)
minilayout2.addWidget(resultBox)
minilayout3.addWidget(logLabel)
minilayout3.addWidget(logBox)


analyzeButton.clicked.connect(lambda: analyze(enteredBox.toPlainText()))
openFileButton.clicked.connect(lambda: openFile())

def analyze(text):
    text, _ = AnalyzeText(text)
    resultBox.setPlainText(text)
    logBox.setPlainText(_)

def openFile():
    fileName, _ = QFileDialog.getOpenFileName(AnalyzeWindow, 'ملف نص', '' , '*')
    if path.exists(fileName) and fileName != '/' and fileName:
        enteredBox.setPlainText(open(fileName, 'r', encoding='utf-8').read())
        QMessageBox.about(AnalyzeWindow, "!!تهانيّ", "تم اختيار ملف النص.")