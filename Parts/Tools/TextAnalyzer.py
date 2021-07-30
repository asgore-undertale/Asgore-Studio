from Parts.Scripts.AnalyzeText import analyzeText
from Parts.Scripts.SuggestDTE import suggestDTE
from Parts.Scripts.UsefulLittleFunctions import openFile, saveFile, tryTakeNum
from PyQt5.QtWidgets import QApplication, QAction
from sys import argv, exit

app = QApplication(argv)
from Parts.Windows import TextAnalyzerWindow

def analyze():
    resultsNum = tryTakeNum(TextAnalyzerWindow.resultsNumCell.toPlainText())
    text, log = analyzeText(TextAnalyzerWindow.enteredBox.toPlainText(), TextAnalyzerWindow.ignoredDtesCell.toPlainText(), resultsNum)
    TextAnalyzerWindow.resultBox.setPlainText(text)
    TextAnalyzerWindow.logBox.setPlainText(log)

def suggest():
    resultsNum = tryTakeNum(TextAnalyzerWindow.resultsNumCell.toPlainText())
    mergedCharFromLen = tryTakeNum(TextAnalyzerWindow.mergedCharLenFromCell.toPlainText())
    mergedCharToLen = tryTakeNum(TextAnalyzerWindow.mergedCharLenToCell.toPlainText())
    dteList, log = suggestDTE(TextAnalyzerWindow.enteredBox.toPlainText(),
        TextAnalyzerWindow.ignoredCharsCell.toPlainText() + '\n\r',
        (mergedCharFromLen, mergedCharToLen), resultsNum
        )
    TextAnalyzerWindow.logBox.setPlainText(log)

def loadFile():
    FilePath = openFile(['*'], TextAnalyzerWindow, 'ملف نص')
    if not FilePath: return
    TextAnalyzerWindow.enteredBox.setPlainText(open(FilePath, 'r', encoding='utf8').read())

def saveLog():
    FilePath = saveFile(['txt'], TextAnalyzerWindow, 'ملف الإحصاءات')
    if not FilePath: return
    open(FilePath, 'w', encoding='utf8').write(TextAnalyzerWindow.logBox.toPlainText())


TextAnalyzerWindow.saveLog.clicked.connect(lambda: saveLog())
TextAnalyzerWindow.analyzeButton.clicked.connect(lambda: analyze())
TextAnalyzerWindow.openFileButton.clicked.connect(lambda: loadFile())
TextAnalyzerWindow.suggestDteButton.clicked.connect(lambda: suggest())

if __name__ == '__main__':
    TextAnalyzerWindow.show()
    exit(app.exec_())