from PyQt5.QtWidgets import QApplication
from Parts.Scripts.UsefulLittleFunctions import saveFile, openFile
from Parts.Scripts.CharmapToTable import *
from Parts.Scripts.TakeFromTable import *
from sys import exit, argv

def convertTable():
    From = TablesConverterWindow.fromComboBox.currentText()
    To = TablesConverterWindow.toComboBox.currentText()
    
    openDirectory = openFile([From], TablesConverterWindow)
    if not openDirectory: return
    saveDirectory = saveFile([To], TablesConverterWindow)
    if not saveDirectory: return
    
    table = charmapToTable(TakeFromTable(openDirectory), To)
    if not table: return
    
    with open(saveDirectory, 'w', encoding='utf-8') as f:
        f.write(table)


app = QApplication(argv)
from Parts.Windows import TablesConverterWindow

TablesConverterWindow.convertButton.clicked.connect(lambda: convertTable())

if __name__ == '__main__':
    TablesConverterWindow.show()
    exit(app.exec_())