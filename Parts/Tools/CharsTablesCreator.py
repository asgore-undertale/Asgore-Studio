from PyQt5.QtWidgets import QApplication, QAction, QTableWidgetItem
from Parts.Scripts.FixTables import sortACT
from Parts.Scripts.TablesEditorsFunctions import *
from Parts.Scripts.UsefulLittleFunctions import intToHex, hexToString, openFile, saveFile
from Parts.Vars import _ATE_VERSION_, _ATE_SEPARATOR_, _CSV_DELIMITER_
from sys import argv, exit
import keyboard


def saveACT(save_loc : str, Table):
    if not save_loc: return
    content = ''
    
    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if not Table.item(row, col): continue
            if not Table.item(row, col).text(): continue
            content += f'{Table.item(row, col).text()}{_ATE_SEPARATOR_*4}{hexToString(intToHex(row)[1]+intToHex(col)[1])}\n'
    
    content = sortACT(deleteTrash(content, _ATE_SEPARATOR_))
    content = deleteEmptyLines(content)
    content = f'\nVERSION="{_ATE_VERSION_}"\nSEPARATOR="{_ATE_SEPARATOR_}"\n#####################\nالحرف{_ATE_SEPARATOR_}أول{_ATE_SEPARATOR_}وسط{_ATE_SEPARATOR_}آخر{_ATE_SEPARATOR_}منفصل\n' + content

    open(save_loc, 'w', encoding="utf-8").write(content)

def saveCSV(save_loc : str, Table):
    if not save_loc: return
    content = ''

    for row in range(Table.rowCount()):
        for col in range(Table.columnCount()):
            if not Table.item(row, col): continue
            if not Table.item(row, col).text(): continue
            char = Table.item(row, col).text().replace('"', '""')
            if _CSV_DELIMITER_ in char: char = f'"{char}"'
            convert = hexToString(intToHex(row)[1]+intToHex(col)[1]).replace(_CSV_DELIMITER_, f'"{_CSV_DELIMITER_}"')
            content += f'{char}{_ATE_SEPARATOR_*4}{convert}\n'
    
    content = sortACT(deleteTrash(content, _ATE_SEPARATOR_), _ATE_SEPARATOR_).replace(_ATE_SEPARATOR_, _CSV_DELIMITER_)
    content = deleteEmptyLines(content)
    content = f'الحرف{_ATE_SEPARATOR_}أول{_ATE_SEPARATOR_}وسط{_ATE_SEPARATOR_}آخر{_ATE_SEPARATOR_}منفصل\n' + content

    open(save_loc, 'w', encoding="utf-8").write(content)

def setChars(startSpot, Chars):
    for i in range(len(Chars)):
        col = int(startSpot[1], 16) + i %  16
        row = int(startSpot[0], 16) + i // 16
        CharsTablesCreatorWindow.Table.setItem(row, col, QTableWidgetItem(Chars[i]))

def writeChar():
    if not CharsTablesCreatorWindow.isActiveWindow(): return
    checkUserChars()
    keyboard.write(userChars[writeChar.current])
    
    writeChar.current += 1
    if writeChar.current == len(userChars): writeChar.current = 0
    CharsTablesCreatorWindow.nextChar.setText(f"الحرف التالي: {userChars[writeChar.current]}")
writeChar.current = 0

def previousChar():
    if not CharsTablesCreatorWindow.isActiveWindow(): return
    checkUserChars()
    
    if not writeChar.current: writeChar.current = len(userChars)
    writeChar.current -= 1
    CharsTablesCreatorWindow.nextChar.setText(f"الحرف التالي: {userChars[writeChar.current]}")

def resetCharCounter():
    if not CharsTablesCreatorWindow.isActiveWindow(): return
    writeChar.current = 0
    CharsTablesCreatorWindow.nextChar.setText(f"الحرف التالي: {userChars[writeChar.current]}")

def checkUserChars():
    global userChars
    if userChars == CharsTablesCreatorWindow.charsCell.toPlainText(): return
    if not CharsTablesCreatorWindow.charsCell.toPlainText(): return
    
    userChars = CharsTablesCreatorWindow.charsCell.toPlainText()
    writeChar.current = 0

def windowTrig(action):
    def check(text): return action.text() == text

    if check("فتح جدول حروف .tbl"): loadTBL(openFile(['tbl'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table, ROWS, COLS)
    elif check("فتح جدول حروف .act"): loadATE(openFile(['act'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table, ROWS, COLS, False)
    elif check("فتح جدول حروف .csv"): loadCSV(openFile(['csv'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table, ROWS, COLS, False)
    elif check("حفظ جدول الحروف كـ .tbl"): saveTBL(saveFile(['tbl'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("حفظ جدول الحروف كـ .act"): saveACT(saveFile(['act'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("حفظ جدول الحروف كـ .csv"): saveCSV(saveFile(['csv'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("مسح محتوى الجدول"): eraseTable(CharsTablesCreatorWindow.Table, ROWS, COLS)


app = QApplication(argv)
from Parts.Windows import CharsTablesCreatorWindow


ROWS, COLS = 16, 16
defultChars = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
userChars = 'ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼ'


CharsTablesCreatorWindow.nextChar.setText(f"الحرف التالي: {userChars[0]}")
CharsTablesCreatorWindow.charsCell.setText(userChars)

CharsTablesCreatorWindow.bar.triggered[QAction].connect(windowTrig)
keyboard.add_hotkey("F3", lambda: writeChar())
keyboard.add_hotkey("F4", lambda: previousChar())
keyboard.add_hotkey("F5", lambda: resetCharCounter())

setChars('20', defultChars)

if __name__ == '__main__':
    CharsTablesCreatorWindow.show()
    exit(app.exec_())