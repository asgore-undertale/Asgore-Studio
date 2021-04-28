from sys import argv, exit
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QMessageBox, QAction
from Parts.Scripts.TablesEditorsFunctions import *
from Parts.Scripts.TablesEditorsFunctions import _VERSION_, _SEPARATOR_

app = QApplication(argv)
ROWS, COLS = 100, 40

def saveATE(save_loc : str):
    content = f'\nVERSION="1.0"\nSEPARATOR="{_SEPARATOR_}"\n#####################\n'

    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if Table.item(row, col): csv_row.append(Table.item(row, col).text())
            else: csv_row.append('')
 
        content += _SEPARATOR_.join(csv_row) + '\n'
    
    content = delete_trash(content)
    
    open(save_loc, 'w', encoding="utf-8").write(content)
    QMessageBox.about(Table, "!!تم", "تم حفظ الجدول.")

def saveCSV(save_loc : str):
    content = f'الحرف{_SEPARATOR_}أول{_SEPARATOR_}وسط{_SEPARATOR_}آخر{_SEPARATOR_}منفصل\n'
    
    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if not Table.item(row, col): continue
            content += f'{Table.item(row, col).text()},,,,{hexToString(intToHex(row)+intToHex(col))}\n'
    
    content = delete_trash(content)
    
    open(save_loc, 'w', encoding="utf-8").write(content)
    QMessageBox.about(Table, "!!تم", "تم حفظ الجدول.")

def windowTrig(action):
    def check(text): return action.text() == text
    
    if check("فتح جدول حروف .tbl"): loadTBL(open_file('tbl', TableEditorWindow), Table, ROWS, COLS)
    elif check("فتح جدول حروف .ate"): loadATE(open_file('ate', TableEditorWindow), Table, ROWS, COLS, True)
    elif check("حفظ جدول الحروف كـ .tbl"): saveTBL(save_file('tbl', TableEditorWindow), Table)
    elif check("حفظ جدول الحروف كـ .ate"): saveATE(save_file('ate', TableEditorWindow))
    elif check("حفظ جدول الحروف كـ .csv"): saveCSV(save_file('csv', TableEditorWindow))
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

file.addAction("فتح جدول حروف .tbl")
file.addAction("فتح جدول حروف .ate")
file.addAction("حفظ جدول الحروف كـ .tbl")
file.addAction("حفظ جدول الحروف كـ .ate")
file.addAction("حفظ جدول الحروف كـ .csv")
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