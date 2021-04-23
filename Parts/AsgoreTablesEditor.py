from sys import argv, exit
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QFileDialog, QMessageBox

app = QApplication(argv)
_VERSION_ = 1.0
ROWS, COLS = 100, 10

def check_version(ver : int):
    if ver > _VERSION_: return True

def open_file(type : str):
    _file, _ = QFileDialog.getOpenFileName(Table, 'Asgore Tables', '' , '*.'+type)
    if not _file != '/' or not _file: return
    return _file

def save_file(type : str):
    _file, _ = QFileDialog.getSaveFileName(Table, 'قاعدة بيانات النص', '' , '*.'+type)
    if not _file != '/': return
    return _file

def delete_trash(table : str, x = 10):
    for i in range(1, x):
        i = x - i
        while '█'*i + '\n' in table: table = table.replace('█'*i + '\n', '\n')
    for i in range(1, x):
        i = x - i
        while '\n'*i + '\n' in table: table = table.replace('\n'*i + '\n', '\n')
    return table

def load_table(ate_file : str): #table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
    if not ate_file: return
    global ROWS, COLS
    
    table = open(ate_file, 'r', encoding="utf-8").read()
    table = delete_trash(table)
    rows = table.split('\n')
    
    if len(rows) > ROWS:
        ROWS = len(rows) - 4
        Table.setRowCount(ROWS)
    
    VERSION = float(rows[1][9:-1])
    if check_version(VERSION): QMessageBox.about(Table, "!!تحذير", f"النسخة {VERSION} غير مدعومة.\n(سيتم فتح الملف على أي حال.)")
    SEPARATOR = rows[2][11:-1]
    
    for row in range(4, len(rows)):
        cols = rows[row].split(SEPARATOR)
        if len(cols) > COLS:
            COLS = len(cols)
            Table.setColumnCount(COLS)
        for col in range(len(cols)):
            Table.setItem(row-4, col, QTableWidgetItem(cols[col]))

def save_table(save_loc : str):
    content = '\nVERSION="1.0"\nSEPARATOR="█"\n#####################\n'

    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if Table.item(row, col): csv_row.append(Table.item(row, col).text())
            else: csv_row.append('')
 
        content += '█'.join(csv_row) + '\n'
    
    content = delete_trash(content)
    
    open(save_loc, 'w', encoding="utf-8").write(content)
    QMessageBox.about(Table, "!!تم", f"تم حفظ الجدول.")

def add_row():
    global ROWS
    ROWS += 1
    Table.setRowCount(ROWS)

def remove_row():
    global ROWS
    if ROWS == 0: return
    ROWS -= 1
    Table.setRowCount(ROWS)

def add_col():
    global COLS
    COLS += 1
    Table.setColumnCount(COLS)

def remove_col():
    global COLS
    if COLS == 0: return
    COLS -= 1
    Table.setColumnCount(COLS)

#####################
TableEditorWindow = QWidget()
layout = QVBoxLayout()

TableEditorWindow.setWindowTitle(f"Asgore Tables {_VERSION_}v")
TableEditorWindow.resize(340, 400)
Table = QTableWidget()
Table.setColumnCount(COLS)
Table.setRowCount(ROWS)

row_p_button = QPushButton()
row_p_button.setText("+ صف")
row_m_button = QPushButton()
row_m_button.setText("- صف")
col_p_button = QPushButton()
col_p_button.setText("+ عمود")
col_m_button = QPushButton()
col_m_button.setText("- عمود")

load_button = QPushButton()
load_button.setText("فتح")
save_button = QPushButton()
save_button.setText("حفظ")


load_button.clicked.connect(lambda: load_table(open_file('ate')))
save_button.clicked.connect(lambda: save_table(save_file('ate')))
row_p_button.clicked.connect(lambda: add_row())
row_m_button.clicked.connect(lambda: remove_row())
col_p_button.clicked.connect(lambda: add_col())
col_m_button.clicked.connect(lambda: remove_col())

#####################

layout.addWidget(row_p_button)
layout.addWidget(row_m_button)
layout.addWidget(col_p_button)
layout.addWidget(col_m_button)
layout.addWidget(Table)
layout.addWidget(load_button)
layout.addWidget(save_button)
TableEditorWindow.setLayout(layout)

if __name__ == '__main__':
    TableEditorWindow.show()
    exit(app.exec_())