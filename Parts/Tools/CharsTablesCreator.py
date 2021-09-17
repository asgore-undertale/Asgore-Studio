from PyQt5.QtWidgets import QApplication, QAction, QTableWidgetItem
from Parts.Scripts.FixTables import sortACT, fixCharmap
from Parts.Scripts.TablesEditorsFunctions import *
from Parts.Scripts.TakeFromTable import TakeFromTable
from Parts.Scripts.UsefulLittleFunctions import intToHex, hexToString, openFile, saveFile, stringToHex
from Parts.Vars import _ACT_VERSION_, _A_SEPARATOR_, _CSV_DELIMITER_, FreezedArabicChars, ASCII, _ACT_DESC_, _AFT_DESC_
from sys import argv, exit
import keyboard, csv

def tableToCharmap(Table):
    charmap = {}
    for row in range(Table.rowCount()):
        csv_row = []
        for col in range(Table.columnCount()):
            if not Table.item(row, col): continue
            if not Table.item(row, col).text(): continue
            charmap[Table.item(row, col).text()] = hexToString(intToHex(row)[1]+intToHex(col)[1])
    return charmap

def loadTable(tablePath : str, Table):
    if not tablePath: return
    eraseTable(Table)
    charmap = TakeFromTable(tablePath)
    
    for k, v in charmap.items():
        if not v: continue
        Table.setItem(int(stringToHex(v)[0], 16), int(stringToHex(v)[1], 16), QTableWidgetItem(k))

def saveACT(save_loc : str, Table):
    if not save_loc: return
    
    charmap = fixCharmap(tableToCharmap(Table))
    content = ''
    
    for k, v in charmap.items():
        content += f'{k}{_A_SEPARATOR_*4}{v}\n'
    
    content = deleteEmptyLines(deleteTrash(content, _A_SEPARATOR_))
    content = sortACT(content, _A_SEPARATOR_)
    content = _ACT_DESC_.replace('[_SEPARATOR_]', _A_SEPARATOR_) + content

    open(save_loc, 'w', encoding="utf-8").write(content)


def saveCSV(save_loc : str, Table):
    if not save_loc: return
    
    charmap = fixCharmap(tableToCharmap(Table))
    content = ''
    
    for k, v in charmap.items():
        content += f'{k}{_A_SEPARATOR_*4}{v}\n'
    
    content = deleteEmptyLines(deleteTrash(content, _A_SEPARATOR_))
    content = sortACT(content, _A_SEPARATOR_)
    content = _ACT_DESC_.replace('[_SEPARATOR_]', _A_SEPARATOR_) + content
    
    with open(save_loc, 'w', newline='', encoding="utf-8", errors='replace') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in content.split('\n'):
            spamwriter.writerow(row.split(_A_SEPARATOR_))

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

    if check("فتح جدول حروف .tbl"): loadTBL(openFile(['tbl'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("فتح جدول حروف .act"): loadTable(openFile(['act'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("فتح جدول حروف .csv"): loadTable(openFile(['csv'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("حفظ جدول الحروف كـ .tbl"): saveTBL(saveFile(['tbl'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("حفظ جدول الحروف كـ .act"): saveACT(saveFile(['act'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("حفظ جدول الحروف كـ .csv"): saveCSV(saveFile(['csv'], CharsTablesCreatorWindow), CharsTablesCreatorWindow.Table)
    elif check("مسح محتوى الجدول"): eraseTable(CharsTablesCreatorWindow.Table)


app = QApplication(argv)
from Parts.Windows import CharsTablesCreatorWindow


userChars = FreezedArabicChars

CharsTablesCreatorWindow.nextChar.setText(f"الحرف التالي: {FreezedArabicChars[0]}")
CharsTablesCreatorWindow.charsCell.setText(FreezedArabicChars)

CharsTablesCreatorWindow.bar.triggered[QAction].connect(windowTrig)
keyboard.add_hotkey("F3", lambda: writeChar())
keyboard.add_hotkey("F4", lambda: previousChar())
keyboard.add_hotkey("F5", lambda: resetCharCounter())

setChars('20', ASCII)

if __name__ == '__main__':
    CharsTablesCreatorWindow.show()
    exit(app.exec_())