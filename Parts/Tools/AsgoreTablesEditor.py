from Parts.Scripts.TablesEditorsFunctions import *
from Parts.Scripts.UsefulLittleFunctions import openFile, saveFile
from PyQt5.QtWidgets import QApplication, QAction
from sys import argv, exit

app = QApplication(argv)
from Parts.Windows import TableEditorWindow

def windowTrig(action):
    action = action.text()
    Table = TableEditorWindow.Table
    ROWS, COLS = TableEditorWindow.ROWS, TableEditorWindow.COLS
    
    if   action == "فتح جدول .ate": loadATE(openFile(('ate', 'aft', 'act'), TableEditorWindow), Table, ROWS, COLS, True)
    elif action == "فتح جدول .csv": loadCSV(openFile(['csv'], TableEditorWindow), Table, ROWS, COLS, True)
    elif action == "حفظ الجدول كـ .ate": saveATE(saveFile(('ate', 'aft', 'act'), TableEditorWindow), Table)
    elif action == "حفظ الجدول كـ .csv": saveCSV(saveFile(['csv'], TableEditorWindow), Table)
    elif action == "إضافة صف": ROWS = add_row(Table, ROWS)
    elif action == "حذف صف": ROWS = remove_row(Table, ROWS)
    elif action == "إضافة عمود": COLS = add_col(Table, COLS)
    elif action == "حذف عمود": COLS = remove_col(Table, COLS)
    elif action == "مسح محتوى الجدول": eraseTable(Table, ROWS, COLS)
    
    TableEditorWindow.ROWS, TableEditorWindow.COLS = ROWS, COLS

TableEditorWindow.bar.triggered[QAction].connect(windowTrig)

if __name__ == '__main__':
    TableEditorWindow.show()
    exit(app.exec_())