from Parts.Scripts.AnalyzeText import analyzeText
from Parts.Scripts.SuggestDTE import suggestDTE
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
suggestDteButton = QPushButton()
analyzeButton.setText("اختزال\nالنص")
openFileButton.setText("فتح ملف\nنص")
suggestDteButton.setText("اقتراح\nثنائيات")

minilayout1 = QHBoxLayout()
resultsNumCell = QTextEdit()
resultsNumCell.setFixedSize(80, 26)
resultsNumCell.setText("25")
resultsNumLabel = QLabel()
resultsNumLabel.setText("عدد النتائج:")

layout.addLayout(minilayout2, 0, 0)
layout.addLayout(minilayout3, 0, 1)
layout.addLayout(minilayout1, 1, 0)
layout.addLayout(minilayout, 1, 1)
minilayout.addWidget(openFileButton)
minilayout.addWidget(analyzeButton)
minilayout.addWidget(suggestDteButton)
minilayout1.addWidget(resultsNumLabel)
minilayout1.addWidget(resultsNumCell)
minilayout2.addWidget(enteredLabel)
minilayout2.addWidget(enteredBox)
minilayout2.addWidget(resultLabel)
minilayout2.addWidget(resultBox)
minilayout3.addWidget(logLabel)
minilayout3.addWidget(logBox)


analyzeButton.clicked.connect(lambda: analyze())
openFileButton.clicked.connect(lambda: openFile())
suggestDteButton.clicked.connect(lambda: suggest())

def analyze():
    try: results = int(resultsNumCell.toPlainText())
    except: results = 0
    text, _ = analyzeText(enteredBox.toPlainText(), results)
    resultBox.setPlainText(text)
    logBox.setPlainText(_)

def openFile():
    fileName, _ = QFileDialog.getOpenFileName(AnalyzeWindow, 'ملف نص', '' , '*')
    if path.exists(fileName) and fileName != '/' and fileName:
        enteredBox.setPlainText(open(fileName, 'r', encoding='utf-8').read())
        QMessageBox.about(AnalyzeWindow, "!!تهانيّ", "تم اختيار ملف النص.")

def suggest():
    try: results = int(resultsNumCell.toPlainText())
    except: results = 0
    dteList, _ = suggestDTE(enteredBox.toPlainText(), results)
    
    logBox.setPlainText(_)