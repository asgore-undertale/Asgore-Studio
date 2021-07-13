from PyQt5.QtWidgets import QApplication
from Parts.Scripts.UsefulLittleFunctions import openFile, saveFile
from Parts.Scripts.TablesEditorsFunctions import CSVtoList
from Parts.Scripts.ConvertFiles import MsytToTxt, TxtToMsyt
from Parts.Tools.TextConverter import convert
from sys import argv, exit
from os import path
import re, openpyxl, keyboard


file_content, text_list, trans_list, sentences_num, database = '', '', '', '', ''
before, after, dataBaseDirectory = '', '', ''

def fileType():
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    if index == 0: return 'msyt'
    if index == 1: return 'txt'

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

def loadFile():
    global file_content, before, after
    filePath = openFile([fileType()], FilesEditorWindow, 'ملف')
    if not filePath: return
    file_content = open(filePath, 'r', encoding='utf-8').read()
    
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    if index == 0:
        before, after = '\n', '\n'
        Msyt()
    if index == 1:
        before, after = '', FilesEditorWindow.endCommandCell.toPlainText()
        Kruptar()
    
    FilesEditorWindow.textBox.setPlainText(text_list[0])
    FilesEditorWindow.translationBox.setPlainText(text_list[0])
    
def save_file():
    global file_content, trans_list
    filePath = saveFile([fileType()], FilesEditorWindow, 'ملف')
    if not filePath: return
    
    file_content = file_content.replace(
        before+trans_list[handleText.current_item]+after,
        before+FilesEditorWindow.translationBox.toPlainText()+after
        )
    trans_list[handleText.current_item] = FilesEditorWindow.translationBox.toPlainText()
    
    index = FilesEditorWindow.fileTypeComboBox.currentIndex()
    if index == 0: file_content = TxtToMsyt(file_content)
    if index == 1: pass
    
    open(filePath, 'w', encoding='utf-8').write(file_content)

def Kruptar():
    global text_list, trans_list, sentences_num
    
    endcommand = FilesEditorWindow.endCommandCell.toPlainText()
    if not endcommand: return
    
    text_list = file_content.split(endcommand)
    del text_list[-1]
    trans_list = list(text_list)
    
    sentences_num = len(text_list)-1
    FilesEditorWindow.per.setText(f"{sentences_num} \ {0}")
    
def Msyt():
    global file_content, text_list, trans_list, sentences_num
    
    file_content = MsytToTxt(file_content)
    msyt_content_list = re.findall("\{\uffff(.*?)\uffff\}", file_content.replace('\n', '\uffff'))#for regex
    msyt_content_list = [x.replace('\uffff', '\n') for x in msyt_content_list]
    
    text_list = msyt_content_list[0].split('\n')
    trans_list = list(text_list)
    
    sentences_num = len(text_list) -1
    FilesEditorWindow.per.setText(f"{sentences_num} \ {0}")

def handleText(direction = True):
    global file_content
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