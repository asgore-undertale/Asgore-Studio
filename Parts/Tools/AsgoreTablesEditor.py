from Parts.Scripts.TablesEditorsFunctions import *
from Parts.Scripts.UsefulLittleFunctions import openFile, saveFile
from PyQt5.QtWidgets import QApplication, QAction
from sys import argv, exit

app = QApplication(argv)
from Parts.Windows import TableEditorWindow

Table = TableEditorWindow.Table

def windowTrig(action):
    action = action.text()
    
    if   action == "فتح جدول .ate": loadATE(openFile(('ate', 'aft', 'act'), TableEditorWindow), Table, True)
    elif action == "فتح جدول .csv": loadCSV(openFile(['csv'], TableEditorWindow), Table, True)
    elif action == "فتح جدول .tbl": loadTBL(openFile(['tbl'], TableEditorWindow), Table, True)
    elif action == "حفظ الجدول كـ .ate": saveATE(saveFile(('ate', 'aft', 'act'), TableEditorWindow), Table)
    elif action == "حفظ الجدول كـ .csv": saveCSV(saveFile(['csv'], TableEditorWindow), Table)
    elif action == "حفظ الجدول كـ .tbl": saveTBL(saveFile(['tbl'], TableEditorWindow), Table)
    elif action == "إضافة صف": add_row(Table)
    elif action == "حذف صف": remove_row(Table)
    elif action == "إضافة عمود": add_col(Table)
    elif action == "حذف عمود": remove_col(Table)
    elif action == "مسح محتوى الجدول": eraseTable(Table)

TableEditorWindow.bar.triggered[QAction].connect(windowTrig)

if __name__ == '__main__':
    TableEditorWindow.show()
    exit(app.exec_())