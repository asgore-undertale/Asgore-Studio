from PyQt5.QtWidgets import QApplication
from Parts.Scripts.UsefulLittleFunctions import openFile, saveFile, tryTakeNum
from Parts.Scripts.TablesEditorsFunctions import CSVtoList
from Parts.Scripts.ConvertFiles import MsytToTxt, TxtToMsyt
from Parts.Vars import _CSV_DELIMITER_
from Parts.Tools.TextConverter import convert
from sys import argv, exit
from os import path
import re, openpyxl, keyboard, csv


file_content, file_path, text_list, trans_list, sentences_num, database, table = '', '', '', '', '', '', ''
before, after, columnIndex, dataBaseDirectory = '', '', '', ''

def fileType():
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    if index == 0: return 'msyt'
    if index == 1: return 'txt'
    if index == 2: return 'csv'

def typeCommand():
    if not FilesEditorWindow.isActiveWindow(): return
    
    Text, c = FilesEditorWindow.textBox.toPlainText(), 0
    
    if '＞' not in Text or '＜' not in Text: return
    while '＜c'+str(c)+'＞' not in Text:
        if c == 30: return
        c += 1
    
    for i in range(Text.count('＞')):
        if '＜c'+str(c+i)+'＞' not in FilesEditorWindow.translationBox.toPlainText() and '＜c'+str(c+i)+'＞' in Text:
            keyboard.write('＜c'+str(c+i)+'＞')
            break

def Convert():
    FilesEditorWindow.translationBox.setPlainText(convert(FilesEditorWindow.translationBox.toPlainText(), False))

def ConvertAll():
    for t in range(len(trans_list)):
        trans_list[t] = convert(trans_list[t], False)
    Convert()

def openTextDataBase():
    global dataBaseDirectory, database

    filePath = openFile(('xlsx', 'csv'), FilesEditorWindow, 'جدول نصوص')
    if not filePath: return
    
    dataBaseDirectory = filePath
    if dataBaseDirectory.endswith('.xlsx'):
        database = openpyxl.load_workbook(dataBaseDirectory)
    elif dataBaseDirectory.endswith('.csv'):
        database = CSVtoList(dataBaseDirectory)

def indexHandle(index, filePath, case):
    global file_content, before, after, columnIndex, text_list, trans_list, table
    if case:
        handleText.current_item = 0
        if index == 0:
            file_content = open(filePath, 'r', encoding='utf-8').read()
            before, after = '\n', '\n'
            Msyt()
        if index == 1:
            file_content = open(filePath, 'r', encoding='utf-8').read()
            before, after = '', FilesEditorWindow.endCommandCell.toPlainText()
            Kruptar()
        if index == 2:
            columnIndex = tryTakeNum(FilesEditorWindow.columnIndexCell.toPlainText()) -1
            CsvTable()
    else:
        if index == 0:
            for t in range(len(text_list)):
                file_content = file_content.replace(before+text_list[t]+after, before+trans_list[t]+after, 1)
            file_content = TxtToMsyt(file_content)
            open(filePath, 'w', encoding='utf-8').write(file_content)
        if index == 1:
            for t in range(len(text_list)):
                file_content = file_content.replace(before+text_list[t]+after, before+trans_list[t]+after, 1)
            open(filePath, 'w', encoding='utf-8').write(file_content)
        if index == 2:
            for t in range(len(text_list)):
                try: table[t][columnIndex] = trans_list[t]
                except: pass
            with open(filePath, 'w', newline='', encoding="utf-8", errors='replace') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in table:
                    spamwriter.writerow(row)

def loadFile():
    global file_path, text_list, trans_list
    file_path = openFile([fileType()], FilesEditorWindow, 'ملف')
    if not file_path: return
    
    indexHandle(FilesEditorWindow.fileTypeComboBox.currentIndex(), file_path, True)
    if not text_list: return
    
    trans_list = list(text_list)
    
    FilesEditorWindow.textBox.setPlainText(text_list[0])
    FilesEditorWindow.translationBox.setPlainText(text_list[0])
    
def save_file():
    global file_content, trans_list
    filePath = saveFile([fileType()], FilesEditorWindow, 'ملف')
    if not filePath: return
    
    trans_list[handleText.current_item] = FilesEditorWindow.translationBox.toPlainText()
    
    indexHandle(FilesEditorWindow.fileTypeComboBox.currentIndex(), filePath, False)

def Kruptar():
    global text_list, sentences_num
    
    endcommand = FilesEditorWindow.endCommandCell.toPlainText()
    if not endcommand: return
    
    text_list = file_content.split(endcommand)
    del text_list[-1]
    
    sentences_num = len(text_list)-1
    FilesEditorWindow.per.setText(f"{sentences_num} \ {0}")

def CsvTable():
    global text_list, file_path, columnIndex, sentences_num, table
    
    if columnIndex < 0: return
    
    with open(file_path, newline='', encoding='utf8', errors='replace') as csvfile:
        table = list(csv.reader(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"'))
    
    text_list = []
    for row in table:
        try: text_list.append(row[columnIndex])
        except: pass
    
    sentences_num = len(text_list)-1
    FilesEditorWindow.per.setText(f"{sentences_num} \ {0}")
    
def Msyt():
    global file_content, text_list, sentences_num
    
    file_content = MsytToTxt(file_content)
    msyt_content_list = re.findall("\{\uffff(.*?)\uffff\}", file_content.replace('\n', '\uffff'))#for regex
    msyt_content_list = [x.replace('\uffff', '\n') for x in msyt_content_list]
    
    text_list = msyt_content_list[0].split('\n')
    
    sentences_num = len(text_list) -1
    FilesEditorWindow.per.setText(f"{sentences_num} \ {0}")

def handleText(direction = True):
    if not sentences_num: return
    
    if direction:
        handleText.current_item += 1
        handleText.current_item = handleText.current_item % (sentences_num +1)
        FilesEditorWindow.per.setText(f"{sentences_num} \ {handleText.current_item}")
        
        index = handleText.current_item -1
        if index == -1:
            index = sentences_num
    else:
        handleText.current_item -= 1
        if handleText.current_item == -1:
            handleText.current_item = sentences_num
        FilesEditorWindow.per.setText(f"{sentences_num} \ {handleText.current_item}")
        
        index = handleText.current_item +1
        index = index % (sentences_num +1)
    
    trans_list[index] = FilesEditorWindow.translationBox.toPlainText()
    
    FilesEditorWindow.textBox.setPlainText(text_list[handleText.current_item])
    FilesEditorWindow.translationBox.setPlainText(trans_list[handleText.current_item])

    if not path.exists(dataBaseDirectory): return
    parts = re.split('＜(.*?)＞', trans_list[handleText.current_item])
    
    for item in range(len(parts)):
        if item % 2 or not parts[item]: continue
        
        if dataBaseDirectory.endswith('.xlsx'):
            r = False
            for sheet in database.sheetnames:
                text_table = database.get_sheet_by_name(sheet)
                for cell in range(2, len(text_table['A'])+1):
                    if text_table['A'+str(cell)].value != parts[item]: continue
                    FilesEditorWindow.translationBox.setPlainText(
                        trans_list[handleText.current_item].replace(parts[item], text_table['B'+str(cell)].value, 1)
                        )
                    r = True
                    break
                if r: break
        
        elif dataBaseDirectory.endswith('.csv'):
            for row in database:
                try:
                    text = row[0]
                    translation = row[1]
                except: continue
                
                if not text or text != parts[item]: continue
                if not translation: translation = ''
                
                FilesEditorWindow.translationBox.setPlainText(trans_list[handleText.current_item].replace(text, translation, 1))
                break
handleText.current_item = 0


app = QApplication(argv)
from Parts.Windows import FilesEditorWindow

FilesEditorWindow.textButton.clicked.connect(lambda: openTextDataBase())
FilesEditorWindow.backButton.clicked.connect(lambda: handleText(False))
FilesEditorWindow.nextButton.clicked.connect(lambda: handleText(True))
FilesEditorWindow.saveButton.clicked.connect(lambda: save_file())
FilesEditorWindow.openButton.clicked.connect(lambda: loadFile())
FilesEditorWindow.Convertbutton.clicked.connect(lambda: Convert())
FilesEditorWindow.ConvertAllbutton.clicked.connect(lambda: ConvertAll())
keyboard.add_hotkey("F3", lambda: typeCommand())

if __name__ == '__main__':
    FilesEditorWindow.show()
    exit(app.exec_())