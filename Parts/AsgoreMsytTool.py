from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QGridLayout, QPushButton, QFileDialog, QMessageBox, QWidget, QHBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QFont
from sys import argv, exit
from os import path
import re, openpyxl, keyboard, csv

app = QApplication(argv)

#النافذة الرئيسية
textbox_font = QFont()
textbox_font.setPointSize(12)
label_font = QFont()
label_font.setPointSize(14)

MsytWindow = QMainWindow()
container = QWidget()
MsytWindow.resize(346, 326)

layout = QGridLayout()
container.setLayout(layout)
MsytWindow.setCentralWidget(container)

fileTypeComboBoxOptions = [
    "ملف زيلدا نفس البرية msyt.",
    "ملف نص مستخرج من الكروبتار"
]
fileTypeComboBox = QComboBox()
fileTypeComboBox.addItems(fileTypeComboBoxOptions)

msytBox = QTextEdit()
msytBox.setFont(textbox_font)
translationBox = QTextEdit()
translationBox.setFont(textbox_font)

minilayout = QHBoxLayout()
text_button = QPushButton()
text_button.setText("جدول نصوص")
open_button = QPushButton()
open_button.setText("فتح ملف")
save_button = QPushButton()
save_button.setText("حفظ الملف")

minilayout2 = QHBoxLayout()
next_button = QPushButton()
next_button.setText(">")
back_button = QPushButton()
back_button.setText("<")
per = QLabel()
per.setFont(label_font)

minilayout3 = QHBoxLayout()
endCommandCell = QTextEdit()
endCommandCell.setFixedSize(120, 26)
endCommandCell.setText("<END>")
endCommandLabel = QLabel()
endCommandLabel.setText("أمر نهاية الجملة:")

layout.addWidget(fileTypeComboBox, 0, 0)
layout.addLayout(minilayout2, 1, 0)
layout.addWidget(msytBox, 2, 0)
layout.addLayout(minilayout, 3, 0)
layout.addWidget(translationBox, 4, 0)
layout.addLayout(minilayout3, 5, 0)
minilayout.addWidget(open_button)
minilayout.addWidget(save_button)
minilayout.addWidget(text_button)
minilayout2.addWidget(back_button)
minilayout2.addWidget(per)
minilayout2.addWidget(next_button)
minilayout3.addWidget(endCommandLabel)
minilayout3.addWidget(endCommandCell)

text_button.clicked.connect(lambda: openTextDataBase())
back_button.clicked.connect(lambda: handleText(False))
next_button.clicked.connect(lambda: handleText(True))
save_button.clicked.connect(lambda: saveFile())
open_button.clicked.connect(lambda: openFile())
keyboard.on_press_key("F5", lambda _: typeCommand())

# ---------
file_content, text_list, trans_list, sentences_num, database = '', '', '', '', ''
before, after = '', ''
dataBaseDirectory = r'OtherFiles/Tables/TextTable.xlsx'

def fileType():
    index = fileTypeComboBox.currentIndex()
    if index == 0: return 'msyt'
    if index == 1: return 'txt'

def typeCommand():
    c = 0
    if '＞' in msytBox.toPlainText():
        while '＜c'+str(c)+'＞' not in msytBox.toPlainText(): c += 1
        for i in range(msytBox.toPlainText().count('＞')):
            if '＜c'+str(c+i)+'＞' not in translationBox.toPlainText() and '＜c'+str(c+i)+'＞' in msytBox.toPlainText():
                keyboard.write('＜c'+str(c+i)+'＞')
                break

def openTextDataBase(Directory = ''):
    global dataBaseDirectory, database
    if not Directory:
        Directory, _ = QFileDialog.getOpenFileName(MsytWindow, 'جداول إكسل', '' , '*.xlsx *.csv')

    if Directory and path.exists(Directory):
        dataBaseDirectory = Directory
        if dataBaseDirectory.endswith('.xlsx'):
            database = openpyxl.load_workbook(Directory)
        elif dataBaseDirectory.endswith('.csv'):
            file = open(Directory, 'r', encoding="utf-8")
            database = csv.DictReader(file)

def openFile():
    global file_content, before, after
    type = fileType()
    _open, _ = QFileDialog.getOpenFileName(MsytWindow, 'ملف', '' , '*.'+type)
    if not _open * (_open != '/') * (_open != '') * (path.exists(_open)): return
    file_content = open(_open, 'r', encoding='utf-8').read()
    
    index = fileTypeComboBox.currentIndex()
    if index == 0:
        Msyt()
        before, after = '\n', '\n'
    if index == 1:
        Kruptar()
        before, after = '', endCommandCell.toPlainText()
    
    msytBox.setPlainText(text_list[0])
    translationBox.setPlainText(text_list[0])
    
def saveFile():
    global file_content, trans_list
    type = fileType()
    _save, _ = QFileDialog.getSaveFileName(MsytWindow, 'ملف', '' , '*.'+type)
    if not _save * (_save != '/') * (_save != ''): return
    
    file_content = file_content.replace(before+trans_list[handleText.current_item]+after, before+translationBox.toPlainText()+after)
    trans_list[handleText.current_item] = translationBox.toPlainText()
    
    index = fileTypeComboBox.currentIndex()
    if index == 0: file_content = TxtToMsyt(file_content)
    if index == 1: pass
    
    open(_save, 'w', encoding='utf-8').write(file_content)
    QMessageBox.about(MsytWindow, "!!تهانينا", "تم حفظ الملف.")

def Kruptar():
    global text_list, trans_list, sentences_num
    endcommand = endCommandCell.toPlainText()
    if not endcommand: return
    text_list = file_content.split(endcommand)
    del text_list[-1]
    trans_list = list(text_list)
    sentences_num = len(text_list)-1
    
    openTextDataBase(dataBaseDirectory)
    
def Msyt():
    global file_content, text_list, trans_list, sentences_num
    file_content = MsytToTxt(file_content)
    msyt_content_list = re.findall("\{\uffff(.*?)\uffff\}", file_content.replace('\n', '\uffff'))#for regex
    for i in range(len(msyt_content_list)): msyt_content_list[i] = msyt_content_list[i].replace('\uffff', '\n')
    sentences_num = msyt_content_list[0].count('\n')

    t = '\n' + msyt_content_list[0]
    text_list = t.split('\n')
    del text_list[0]
    trans_list = list(text_list)

    openTextDataBase(dataBaseDirectory)
    QMessageBox.about(MsytWindow, "!!", "تفحص نافذة الأوامر")

def MsytToTxt(file_content):
    new_file_text, new_file_commands, new_file_dump = '', '', ''
    new_file_text_line, first_commands, last_commands = '', '', ''
    command_num = 0
    for line in file_content.split('\n'):
        if '- text:' in line:
            new_file_text_line += line.replace('      - text: ', '')
        elif '- control:' in line:
            new_file_text_line += '＜c' + str(command_num) + '＞'
            new_file_commands = new_file_commands.replace(']]', ']')
            new_file_commands += '[' + str(command_num) + ']]\n'
            command_num += 1
        elif '          ' in line:
            '''
            if 'animation' in line or 'sound' in line or 'sound2' in line or 'raw' in line:
                first_commands += '＜c' + str(command_num-1) + '＞'
                new_file_text_line = new_file_text_line.replace('＜c' + str(command_num-1) + '＞', '')
                elif 'auto_advance' in line or 'pause' in line or 'choice' in line or 'single_choice' in line:
                   last_commands += '＜c' + str(command_num-1) + '＞'
                  new_file_text_line = new_file_text_line.replace('＜c' + str(command_num-1) + '＞', '')
            '''
            new_file_commands = new_file_commands.replace(']]', ', ' + line.replace('          ', '') + ']]')
        else:
            if new_file_text_line:
                new_file_dump += '\t\t[-----------]\n'
                new_file_text += first_commands + new_file_text_line + last_commands + '\n'
                new_file_text_line, first_commands, last_commands = '', '', ''
            new_file_dump += line + '\n'
    
    new_file_content = '{\n'+new_file_text+'}\n\n' + '{\n'+new_file_commands+'}\n\n' + '{\n'+new_file_dump+'}'
    print(new_file_commands)
    return new_file_content

def TxtToMsyt(file_content):
    msyt_content_list = re.findall("\{\uffff(.*?)\uffff\}", file_content.replace('\n', '\uffff'))#for regex
    for i in range(len(msyt_content_list)): msyt_content_list[i] = msyt_content_list[i].replace('\uffff', '\n')
    if len(msyt_content_list) == 2: msyt_content_list.insert(1, '')
    
    TxtToMsyt.new_file_content = msyt_content_list[2]
    
    t = '\n' + msyt_content_list[0]
    text_list = t.split('\n')
    del text_list[0]
    
    def edit_line(line):
        if line[0] != '＜': line = '      - text: ' + line
        line = line.replace('\n', '\n      - text: ').replace('＞', '＞      - text: ')
        line = line.replace('＞      - text: ＜', '＞＜').replace('＞      - text: \n', '＞\n')
        line = line.replace('＞      - text: ', '＞\n      - text: ').replace('＜', '\n＜')
        line = line.replace('""', '')
        TxtToMsyt.new_file_content = TxtToMsyt.new_file_content.replace('\t\t[-----------]', line, 1)
    
    list(map(edit_line, text_list))
    
    commands_list = re.findall("\[(.*?)\]", msyt_content_list[1])
    for i in range(len(commands_list)):
        j = '\n      - control:' + commands_list[i].replace(str(i)+', ', ', ').replace(', ', '\n          ')
        TxtToMsyt.new_file_content = TxtToMsyt.new_file_content.replace('＜c' + str(i) + '＞', j)
    
    TxtToMsyt.new_file_content = TxtToMsyt.new_file_content.replace('\n      - text: \n', '\n')
    TxtToMsyt.new_file_content = TxtToMsyt.new_file_content.replace('\n\n\n      - control:', '\n      - control:').replace('\n\n      - control:\n', '\n      - control:\n')
    TxtToMsyt.new_file_content = TxtToMsyt.new_file_content.replace('}\n\n{\n', '')
    return TxtToMsyt.new_file_content

def handleText(boolen = True):
    global file_content
    if not sentences_num: return
    
    if boolen:
        handleText.current_item += 1
        handleText.current_item = handleText.current_item % (sentences_num +1)
        per.setText(f"{sentences_num} \ {handleText.current_item}")
    else:
        if handleText.current_item == 0:
            handleText.current_item = sentences_num
            per.setText(f"{sentences_num} \ {handleText.current_item}")
        else:
            handleText.current_item -= 1
            per.setText(f"{sentences_num} \ {handleText.current_item}")
    
    if boolen:
        index = handleText.current_item -1
        if index == -1:
            index = sentences_num
    else:
        index = handleText.current_item +1
        index = index % (sentences_num +1)
    
    file_content = file_content.replace(before+trans_list[index]+after, before+translationBox.toPlainText()+after)
    trans_list[index] = translationBox.toPlainText()
    
    msytBox.setPlainText(text_list[handleText.current_item])
    translationBox.setPlainText(trans_list[handleText.current_item])

    if not path.exists(dataBaseDirectory): return
    _list = re.split('＜(.*?)＞', trans_list[handleText.current_item])
    for item in range(len(_list)):
        if item % 2 or not _list[item]: continue
        
        if dataBaseDirectory.endswith('.xlsx'):
            r = False
            for sheet in database.sheetnames:
                text_table = database.get_sheet_by_name(sheet)
                for cell in range(2, len(text_table['A'])+1):
                    if text_table['A'+str(cell)].value != _list[item]: continue
                    if translationBox.toPlainText() == trans_list[handleText.current_item]:
                        translationBox.setPlainText('')
                    translationBox.setPlainText(translationBox.toPlainText() + text_table['B'+str(cell)].value)
                    r = True
                    break
                if r: break
        
        elif dataBaseDirectory.endswith('.csv'):
            for row in database:
                item0, item1 = row[list(row)[0]], row[list(row)[1]]
                if isinstance(item0, list):
                    text = item0[0]
                    translation = item1[1]
                elif isinstance(item1, list):
                    text = item0
                    translation = item1[0]
                else:
                    text = item0
                    translation = item1
                
                if not text: break
                if not translation: translation = ''
                if text != _list[item]: continue
                if translationBox.toPlainText() == trans_list[handleText.current_item]:
                    translationBox.setPlainText('')
                translationBox.setPlainText(translationBox.toPlainText() + translation)
                break
            openTextDataBase(dataBaseDirectory)
handleText.current_item = 0

if __name__ == '__main__':
    MsytWindow.show()
    exit(app.exec_())