from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView, QMainWindow, QLabel, QAction, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt
from Parts.Scripts.Un_Freeze_Arabic import Un_Freeze
from Parts.Scripts.FixTables import fixACT
from Parts.Scripts.TablesEditorsFunctions import *
from Parts.Scripts.TablesEditorsFunctions import _VERSION_, _SEPARATOR_
from Parts.Scripts.UsefulFunctions import intToHex, hexToString
import keyboard

app = QApplication(argv)
QApplication.setLayoutDirection(Qt.RightToLeft)
ROWS, COLS = 16, 16
nums = '0123456789ABCDEF'
startpoint1 = '20'
defultChars1 = ' !"#$%&' + "'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
userChars = 'ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼ'

def saveACT(save_loc : str):
    if not save_loc: return
    content = f'\nVERSION="1.0"\nSEPARATOR="{_SEPARATOR_}"\n#####################\nالحرف{_SEPARATOR_}أول{_SEPARATOR_}وسط{_SEPARATOR_}آخر{_SEPARATOR_}منفصل\n'
    
    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if not Table.item(row, col): continue
            if not Table.item(row, col).text(): continue
            content += f'{Table.item(row, col).text()}{_SEPARATOR_*4}{hexToString(intToHex(row)[1]+intToHex(col)[1])}\n'
    
    content = fixACT(delete_trash(content, _SEPARATOR_))
    content = deleteEmptyLines(content)
    
    open(save_loc, 'w', encoding="utf-8").write(content)
    QMessageBox.about(Table, "!!تم", "تم حفظ الجدول.")

def saveCSV(save_loc : str):
    if not save_loc: return
    content = f'الحرف{_SEPARATOR_}أول{_SEPARATOR_}وسط{_SEPARATOR_}آخر{_SEPARATOR_}منفصل\n'
    delimiter = ','
    
    for row in range(Table.rowCount()):
        for col in range(Table.columnCount()):
            if not Table.item(row, col): continue
            if not Table.item(row, col).text(): continue
            char = Table.item(row, col).text().replace(delimiter, f'"{delimiter}"')
            convert = hexToString(intToHex(row)[1]+intToHex(col)[1]).replace(delimiter, f'"{delimiter}"')
            content += f'{char}{_SEPARATOR_*4}{convert}\n'
    
    content = fixACT(delete_trash(content, _SEPARATOR_)).replace(_SEPARATOR_, delimiter)
    content = deleteEmptyLines(content)
    
    open(save_loc, 'w', encoding="utf-8").write(content)
    QMessageBox.about(Table, "!!تم", "تم حفظ الجدول.")

def setChars(startSpot, Chars):
    for i in range(len(Chars)):
        col = int(startSpot[1], 16) + i %  16
        row = int(startSpot[0], 16) + i // 16
        Table.setItem(row, col, QTableWidgetItem(Chars[i]))

def writeChar():
    global userChars
    checkUserChars()
    keyboard.write(userChars[writeChar.char])
    writeChar.char = writeChar.char + 1
    if writeChar.char == len(userChars): writeChar.char = 0
    nextChar.setText(f"الحرف التالي: {userChars[writeChar.char]}")
writeChar.char = 0

def previousChar():
    global userChars
    checkUserChars()
    if not writeChar.char: writeChar.char = len(userChars)
    writeChar.char -= 1
    nextChar.setText(f"الحرف التالي: {userChars[writeChar.char]}")

def resetCharCounter():
    global userChars
    writeChar.char = 0
    nextChar.setText(f"الحرف التالي: {userChars[writeChar.char]}")

def checkUserChars():
    global userChars
    if userChars == charsCell.toPlainText(): return
    if not charsCell.toPlainText(): return
    userChars = charsCell.toPlainText()
    writeChar.char = 0

def windowTrig(action):
    def check(text): return action.text() == text

    if check("فتح جدول حروف .tbl"): loadTBL(open_file('tbl', CharsTablesCreatorWindow), Table, ROWS, COLS)
    elif check("فتح جدول حروف .act"): loadATE(open_file('act', CharsTablesCreatorWindow), Table, ROWS, COLS, False)
    elif check("فتح جدول حروف .csv"): loadCSV(open_file('csv', CharsTablesCreatorWindow), Table, ROWS, COLS, False)
    elif check("حفظ جدول الحروف كـ .tbl"): saveTBL(save_file('tbl', CharsTablesCreatorWindow), Table)
    elif check("حفظ جدول الحروف كـ .act"): saveACT(save_file('act', CharsTablesCreatorWindow))
    elif check("حفظ جدول الحروف كـ .csv"): saveCSV(save_file('csv', CharsTablesCreatorWindow))
    elif check("مسح محتوى الجدول"): eraseTable(Table, ROWS, COLS)


#####################
CharsTablesCreatorWindow = QMainWindow()
CharsTablesCreatorWindow.setFixedSize(600, 600)
CharsTablesCreatorWindow.setWindowTitle("CharsTablesCreator")

label_font = QFont()
label_font.setPointSize(13)

Table = QTableWidget(CharsTablesCreatorWindow)
Table.setColumnCount(COLS)
Table.setRowCount(ROWS)
Table.setGeometry(QRect(0, 20, 600, 505))
Table.setLayoutDirection(Qt.LeftToRight)

bar = CharsTablesCreatorWindow.menuBar()

file = bar.addMenu("ملف")

file.addAction("فتح جدول حروف .tbl")
file.addAction("فتح جدول حروف .act")
file.addAction("فتح جدول حروف .csv")
file.addAction("حفظ جدول الحروف كـ .tbl")
file.addAction("حفظ جدول الحروف كـ .act")
file.addAction("حفظ جدول الحروف كـ .csv")
bar.addAction("مسح محتوى الجدول")

nextChar = QLabel(CharsTablesCreatorWindow)
nextChar.setGeometry(QRect(10, 523, 120, 40))
nextChar.setFont(label_font)
nextChar.setText(f"الحرف التالي: {userChars[0]}")

charsCell = QTextEdit(CharsTablesCreatorWindow)
charsCell.setGeometry(QRect(150, 529, 330, 66))
charsCell.setText(userChars)
charsLabel = QLabel(CharsTablesCreatorWindow)
charsLabel.setGeometry(QRect(460, 529, 130, 26))
charsLabel.setText("الحروف المراد إدخالها:")

bar.triggered[QAction].connect(windowTrig)
keyboard.on_press_key("F3", lambda _: writeChar())
keyboard.on_press_key("F4", lambda _: previousChar())
keyboard.on_press_key("F5", lambda _: resetCharCounter())

Table.setHorizontalHeaderLabels(list(nums))
Table.setVerticalHeaderLabels(list(nums))
header = Table.horizontalHeader()
for i in range(16): header.setSectionResizeMode(i, QHeaderView.Stretch)

setChars(startpoint1, defultChars1)
#####################

if __name__ == '__main__':
    CharsTablesCreatorWindow.show()
    exit(app.exec_())