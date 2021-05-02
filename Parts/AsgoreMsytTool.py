import re, openpyxl, keyboard
from sys import argv, exit
from os import path
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel, QFileDialog, QMessageBox

app = QApplication(argv)

#النافذة الرئيسية
textbox_font = QFont()
textbox_font.setPointSize(12)
label_font = QFont()
label_font.setPointSize(14)

MsytWindow = QMainWindow()
MsytWindow.setFixedSize(346, 326)

msyt_text = QTextEdit(MsytWindow)
msyt_text.setGeometry(QRect(13, 13, 321, 123))
msyt_text.setFont(textbox_font)
sheet_text = QTextEdit(MsytWindow)
sheet_text.setGeometry(QRect(13, 193, 321, 123))
sheet_text.setFont(textbox_font)

text_button = QPushButton(MsytWindow)
text_button.setGeometry(QRect(260, 145, 70, 40))
text_button.setText("فتح قاعدة\nبيانات نص")
next_button = QPushButton(MsytWindow)
next_button.setGeometry(QRect(302, 5, 20, 20))
next_button.setText(">")
back_button = QPushButton(MsytWindow)
back_button.setGeometry(QRect(322, 5, 20, 20))
back_button.setText("<")
open_button = QPushButton(MsytWindow)
open_button.setGeometry(QRect(180, 145, 70, 40))
open_button.setText("فتح ملف")
save_button = QPushButton(MsytWindow)
save_button.setGeometry(QRect(100, 145, 70, 40))
save_button.setText("حفظ الملف")

per = QLabel(MsytWindow)
per.setGeometry(QRect(13, 145, 90, 40))
per.setFont(label_font)

text_button.clicked.connect(lambda: openTextDataBase())
back_button.clicked.connect(lambda: script(False))
next_button.clicked.connect(lambda: script(True))
save_button.clicked.connect(lambda: save())
open_button.clicked.connect(lambda: openNewFile())
keyboard.on_press_key("F3", lambda _: typeC())

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
        line = line.replace('""', '').replace('\n', r'\n')
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

def script(boolen = True):
    if boolen:
        if script.current_item == centences_num:
            script.current_item = 0
            per.setText(f"{centences_num} \ {script.current_item}")
        else:
            script.current_item += 1
            per.setText(f"{centences_num} \ {script.current_item}")
    else:
        if script.current_item == 0:
            script.current_item = centences_num
            per.setText(f"{centences_num} \ {script.current_item}")
        else:
            script.current_item -= 1
            per.setText(f"{centences_num} \ {script.current_item}")
   
    if not centences_num: return
    global Text_content
    if sheet_text.toPlainText():
        Text_content = Text_content.replace('\n'+text_list[script.current_item-1]+'\n', '\n'+sheet_text.toPlainText()+'\n')  #لسبب ما لم يعمل التجميد والعكس هنا
        text_list[script.current_item-1] = sheet_text.toPlainText()
    
    msyt_text.setPlainText(text_list[script.current_item])
    sheet_text.setPlainText('')

    r = False
    if path.exists(dataBaseDirectory):
        _list = re.split('＜(.*?)＞', text_list[script.current_item])
        for item in range(len(_list)):
            for sheet in text_xlsx.sheetnames:
                text_table = text_xlsx.get_sheet_by_name(sheet)
                if not item % 2 and _list[item]:
                    for cell in range(2, len(text_table['A'])+1):
                        if text_table['A'+str(cell)].value == _list[item]:
                            sheet_text.setPlainText(sheet_text.toPlainText() + text_table['B'+str(cell)].value)
                            r = True
                            break
                    if r:
                        r = False
                        break

script.current_item = 0
Text_content, text_list, centences_num, file_path, text_xlsx = '', '', '', '', ''
dataBaseDirectory = r'OtherFiles/TextTable.xlsx'

def typeC():
    c = 0
    if '＞' in msyt_text.toPlainText():
        while '＜c'+str(c)+'＞' not in msyt_text.toPlainText(): c += 1
        for i in range(msyt_text.toPlainText().count('＞')):
            if '＜c'+str(c+i)+'＞' not in sheet_text.toPlainText() and '＜c'+str(c+i)+'＞' in msyt_text.toPlainText():
                keyboard.write('＜c'+str(c+i)+'＞')
                break

def openTextDataBase(Directory = ''):
    global dataBaseDirectory, text_xlsx
    if not Directory:
        Directory, _ = QFileDialog.getOpenFileName(MsytWindow, 'جداول إكسل', '' , '*.xlsx')

    if Directory != '' and path.exists(Directory):
        dataBaseDirectory = Directory
        text_xlsx = openpyxl.load_workbook(Directory)

def openNewFile():
    global Text_content, text_list, centences_num, file_path
    file_path, _ = QFileDialog.getOpenFileName(MsytWindow, 'Zelda .msyt file', '' , '*.msyt')
    if not file_path != '' or not path.exists(file_path): return
    file_content = open(file_path, 'r', encoding='utf-8').read()
    QMessageBox.about(MsytWindow, "!!", "تفحص نافذة الأوامر")
    
    Text_content = MsytToTxt(file_content)
    msyt_content_list = re.findall("\{\uffff(.*?)\uffff\}", Text_content.replace('\n', '\uffff'))#for regex
    for i in range(len(msyt_content_list)): msyt_content_list[i] = msyt_content_list[i].replace('\uffff', '\n')
    centences_num = msyt_content_list[0].count('\n')

    t = '\n' + msyt_content_list[0]
    text_list = t.split('\n')
    del text_list[0]

    openTextDataBase(dataBaseDirectory)
    script()
    script(False)

def save():
    if file_path: open(file_path, 'w', encoding='utf-8').write(TxtToMsyt(Text_content))
    QMessageBox.about(MsytWindow, "!!تهانينا", "تم حفظ الملف.")

if __name__ == '__main__':
    MsytWindow.show()
    exit(app.exec_())