from Parts.Scripts.AnalyzeText import analyzeText
from Parts.Scripts.SuggestDTE import suggestDTE
from Parts.Scripts.UsefulLittleFunctions import openFile, tryTakeNum
from PyQt5.QtWidgets import QApplication, QAction
from sys import argv, exit

app = QApplication(argv)
from Parts.Windows import TextAnalyzerWindow

def analyze():
    results = tryTakeNum(TextAnalyzerWindow.resultsNumCell.toPlainText())
    text, log = analyzeText(TextAnalyzerWindow.enteredBox.toPlainText(), results)
    TextAnalyzerWindow.resultBox.setPlainText(text)
    TextAnalyzerWindow.logBox.setPlainText(log)

def suggest():
    results = tryTakeNum(TextAnalyzerWindow.resultsNumCell.toPlainText())
    dteList, log = suggestDTE(TextAnalyzerWindow.enteredBox.toPlainText(), results)
    TextAnalyzerWindow.logBox.setPlainText(log)

def loadFile():
    FilePath = openFile(['*'], TextAnalyzerWindow, 'ملف نص')
    if not FilePath: return
    TextAnalyzerWindow.enteredBox.setPlainText(open(FilePath, 'r', encoding='utf8').read())


TextAnalyzerWindow.analyzeButton.clicked.connect(lambda: analyze())
TextAnalyzerWindow.openFileButton.clicked.connect(lambda: loadFile())
TextAnalyzerWindow.suggestDteButton.clicked.connect(lambda: suggest())

if __name__ == '__main__':
    TextAnalyzerWindow.show()
    exit(app.exec_())