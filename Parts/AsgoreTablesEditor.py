from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QMessageBox, QAction
from Parts.Scripts.TablesEditorsFunctions import *
from Parts.Scripts.TablesEditorsFunctions import _VERSION_, _SEPARATOR_
from sys import argv, exit

app = QApplication(argv)
ROWS, COLS = 100, 40

def windowTrig(action):
    def check(text): return action.text() == text
    
    if check("فتح جدول .ate"): loadATE(open_file('ate', TableEditorWindow), Table, ROWS, COLS, True)
    elif check("فتح جدول .csv"): loadCSV(open_file('csv', TableEditorWindow), Table, ROWS, COLS, True)
    elif check("حفظ الجدول كـ .ate"): saveATE(save_file('ate', TableEditorWindow), Table)
    elif check("حفظ الجدول كـ .csv"): saveCSV(save_file('csv', TableEditorWindow), Table)
    elif check("إضافة صف"): add_row(Table, ROWS)
    elif check("حذف صف"): remove_row(Table, ROWS)
    elif check("إضافة عمود"): add_col(Table, COLS)
    elif check("حذف عمود"): remove_col(Table, COLS)
    elif check("مسح محتوى الجدول"): eraseTable(Table, ROWS, COLS)

#####################
TableEditorWindow = QMainWindow()
TableContainer = QWidget()
layout = QVBoxLayout()

TableContainer.setWindowTitle(f"Asgore Tables {_VERSION_}v")
Table = QTableWidget()
Table.setColumnCount(COLS)
Table.setRowCount(ROWS)

bar = TableEditorWindow.menuBar()

file = bar.addMenu("ملف")
options = bar.addMenu("خيارات الجدول")

file.addAction("فتح جدول .ate")
file.addAction("فتح جدول .csv")
file.addAction("حفظ الجدول كـ .ate")
file.addAction("حفظ الجدول كـ .csv")
options.addAction("إضافة صف")
options.addAction("حذف صف")
options.addAction("إضافة عمود")
options.addAction("حذف عمود")
bar.addAction("مسح محتوى الجدول")

bar.triggered[QAction].connect(windowTrig)

#####################

layout.addWidget(Table)
TableContainer.setLayout(layout)
TableEditorWindow.setCentralWidget(TableContainer)

if __name__ == '__main__':
    TableEditorWindow.show()
    exit(app.exec_())