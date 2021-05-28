from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QCheckBox, QPushButton, QFileDialog, QMessageBox, QRadioButton
from PyQt5.QtCore import QRect, Qt
from Parts.Scripts.LineOffset import OffsetLine
from Parts.Scripts.CharmapCreator import CreateCharmap
from Parts.Scripts.Fit_in_box import fit
from Parts.Scripts.EmbedPygameInPyqt5 import embed
from os import path
from sys import argv, exit
from time import sleep
from PIL import Image
from ctypes import windll
import keyboard
import pygame

def type_in_box(textList, font_size, box_width, box_height, px_per_line, charmap, border_thick, newline, newpage, display, fontSize, lineBox, from_Right = False,
                x = 0, y = 0, sleep_time = 0, box_style = 0):
    if FileDirectory.endswith('.ttf'): dialogue_font = pygame.font.Font(FileDirectory, font_size)
    
    Y = y
    if from_Right: X = box_width + border_thick
    else: X = x
    
    for page in textList:
        _y = Y
        conversation(0, 0, box_width + border_thick * 2, box_height + border_thick * 2, 0, (255, 255, 255), border_thick, box_style, display)
        for line in page:
            _x = X
            for char in line:
                if FileDirectory.endswith('.ttf'):
                    dialogue = dialogue_font.render(char, True, (255, 255, 255))
                    char_width,  char_xadvance = dialogue.get_size()[0], 0
                    
                    if from_Right: _x -= char_width
                    display.blit(dialogue, (_x, _y)) # char_xoffset, char_yoffset
                else:
                    if char not in charmap: continue
                    char_x, char_y, char_width, char_height = charmap[char][0], charmap[char][1], charmap[char][2], charmap[char][3]
                    char_xoffset, char_yoffset, char_xadvance = charmap[char][4], charmap[char][5], charmap[char][6]
                    if char_width > box_width: continue

                    img = Image.open(pngDirectory)
                    croped_img = img.crop((char_x, char_y, char_x+char_width, char_y+char_height))
                    py_img = pygame.image.fromstring(croped_img.tobytes(), croped_img.size, croped_img.mode)
                    
                    if from_Right: _x -= char_width
                    display.blit(py_img, (_x + char_xoffset, _y + char_yoffset))
                
                if from_Right: _x -= char_xadvance
                else: _x += char_width + char_xadvance
                
                pygame.display.update()
                sleep(sleep_time)
            
            if lineBox: pygame.draw.rect(display, (255, 0, 0), (x, _y, box_width, fontSize), 1)
            pygame.display.update()
            
            _y += font_size + px_per_line
        
        while True:
            pygameCheck()
            if keyboard.is_pressed('enter'): break

def conversation(x, y, width, height, box_color, border_color, border_thick, box_style, display):
    frames = 100
    if box_style == 0:
        h = height
        for i in range(frames):
            w = width * (i + 1) / frames
            x = width / 2 - w / 2 
            pygame.draw.rect(display, box_color, (x, y, w, h))
            pygame.draw.rect(display, border_color, (x, y, w, h), border_thick)
            pygame.display.update()
            sleep(0.005)
    elif box_style == 1:
        for i in range(frames):
            w = width * (i + 1) / frames
            h = height * (i + 1) / frames
            x = width / 2 - w / 2 
            y = height / 2 - h / 2 
            pygame.draw.rect(display, box_color, (x, y, w, h))
            pygame.draw.rect(display, border_color, (x, y, w, h), border_thick)
            pygame.display.update()
            sleep(0.005)
    else: #if box_style == 2
        x, w = width / 2, 0
        for i in range(frames):
            h = height * (i + 1) / frames
            y = height / 2 - h / 2
            pygame.draw.rect(display, box_color, (x, y, w, h))
            pygame.draw.rect(display, border_color, (x, y, w, h), border_thick)
            pygame.display.update()
            sleep(0.0025)
        h = height
        for i in range(frames):
            w = width * (i + 1) / frames
            x = width / 2 - w / 2 
            pygame.draw.rect(display, box_color, (x, y, w, h))
            pygame.draw.rect(display, border_color, (x, y, w, h), border_thick)
            pygame.display.update()
            sleep(0.0025)

def fit_advance(text = '', fontSize = 16, box_width = 10, box_height = 10, px_per_line = 10, fnt_directory = '', img_directory = '', newline = '', newpage = '',
                before_command = '', after_command = '', from_Right = False, lineBox = False, lineOfssef = 3,sleep_time = 0, border_thick = 10, box_style = 0):
    if (not fnt_directory or not img_directory) and not fnt_directory.endswith('.ttf'):
        QMessageBox.about(FitAdvancedWindow, "تذكر", "لا تنسى تحديد ملف وصورة الخط")
        return
    
    charmap = CreateCharmap(fnt_directory, text, fontSize, FileDirectory.split('.')[-1])
    
    lines_num = int(box_height / (fontSize * 2 + px_per_line) * 2)
    fitted_text = fit(text, charmap, box_width, lines_num, newline, newpage, before_command, after_command)
    
    resultTextCell.setPlainText(fitted_text)
    
    if newpage: pages = fitted_text.split(newpage)
    else: pages = [fitted_text]
    if newline: textList = [page.split(newline) for page in pages]
    else: textList = [pages]
    
    pygame.display.set_caption('Fit in box (Advanced)')
    textbox = pygame.display.set_mode((int(box_width + border_thick * 2), int(box_height + border_thick * 2)))
    
    SetWindowPos = windll.user32.SetWindowPos
    SetWindowPos(pygame.display.get_wm_info()['window'], -1, 250, 250, 0, 0, 0x0001)
    
    type_in_box(textList, fontSize, box_width, box_height, px_per_line, charmap, border_thick, newline, newpage, textbox, fontSize, lineBox, from_Right,
                border_thick, border_thick, sleep_time, box_style)

    while True: pygameCheck()

def pygameCheck():
    for event in pygame.event.get():
        if event.type is pygame.QUIT: pygame.display.set_mode((1, 1), flags = pygame.HIDDEN)

def openFont(Directory = ''):
    global pngDirectory, FileDirectory
    Directory, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'جدول الخط', '' , '*.aft *.ttf')
    if Directory and Directory != '/' and path.exists(Directory): FileDirectory = Directory
    
    if FileDirectory.endswith('.ttf'): return
    
    if Directory: Directory, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'صورة الخط', '' , '*.jpg *.png')
    if Directory and Directory != '/' and path.exists(Directory): pngDirectory = Directory

def start():
    if fontSizeCell.toPlainText(): fontSize = int(float(fontSizeCell.toPlainText()))
    else: fontSize = 1
    if boxWidthCell.toPlainText(): boxWidth = float(boxWidthCell.toPlainText())
    else: boxWidth = 180
    if boxHeightCell.toPlainText(): boxHeight = float(boxHeightCell.toPlainText())
    else: boxHeight = 60
    if pixelsPerCell.toPlainText(): pixelsPer = float(pixelsPerCell.toPlainText())
    else: pixelsPer = 0
    if timePerCharCell.toPlainText(): timePerChar = float(timePerCharCell.toPlainText())
    else: timePerChar = 0
    if borderThickCell.toPlainText(): borderThick = float(borderThickCell.toPlainText())
    else: borderThick = 10
    if boxAnimationCell.toPlainText(): boxAnimation = int(float(boxAnimationCell.toPlainText()))
    else: boxAnimation = 2
    
    if offset0Radio.isChecked(): offset = 0
    elif offset1Radio.isChecked(): offset = 1
    elif offset2Radio.isChecked(): offset = 2
    elif offset3Radio.isChecked(): offset = 3
    else: offset = -1
    
    fit_advance(enteredTextCell.toPlainText(), fontSize, boxWidth, boxHeight, pixelsPer, FileDirectory, pngDirectory, newLineCell.toPlainText(), newPageCell.toPlainText(), beforeComCell.toPlainText(), afterComCell.toPlainText(), fromRightCheck.isChecked(), lineBoxCheck.isChecked(), offset, timePerChar, borderThick, boxAnimation)

FileDirectory, pngDirectory = '', ''

app = QApplication(argv)
pygame.init()

FitAdvancedWindow = QMainWindow()
FitAdvancedWindow.setFixedSize(700, 390)

labelsWidth, labelsHeight = 130, 26

def y(num, height = 26, per = 10, first = 20):
    return first + (num * height) + ((num - 1) * per)

fontSizeCell = QTextEdit(FitAdvancedWindow)
fontSizeCell.setGeometry(QRect(240, y(0), 70, 26))
fontSizeLabel = QLabel(FitAdvancedWindow)
fontSizeLabel.setGeometry(QRect(320, y(0), labelsWidth, labelsHeight))
fontSizeLabel.setText("حجم الخط:")
borderThickCell = QTextEdit(FitAdvancedWindow)
borderThickCell.setGeometry(QRect(240, y(1), 70, 26))
borderThickLabel = QLabel(FitAdvancedWindow)
borderThickLabel.setGeometry(QRect(320, y(1), labelsWidth, labelsHeight))
borderThickLabel.setText("ثخن جدار المربع:")
boxWidthCell = QTextEdit(FitAdvancedWindow)
boxWidthCell.setGeometry(QRect(240, y(2), 70, 26))
boxWidthLabel = QLabel(FitAdvancedWindow)
boxWidthLabel.setGeometry(QRect(320, y(2), labelsWidth, labelsHeight))
boxWidthLabel.setText("عرض المربع:")
boxHeightCell = QTextEdit(FitAdvancedWindow)
boxHeightCell.setGeometry(QRect(240, y(3), 70, 26))
boxHeightLabel = QLabel(FitAdvancedWindow)
boxHeightLabel.setGeometry(QRect(320, y(3), labelsWidth, labelsHeight))
boxHeightLabel.setText("ارتفاع المربع:")
pixelsPerCell = QTextEdit(FitAdvancedWindow)
pixelsPerCell.setGeometry(QRect(240, y(4), 70, 26))
pixelsPerLabel = QLabel(FitAdvancedWindow)
pixelsPerLabel.setGeometry(QRect(320, y(4), labelsWidth, labelsHeight))
pixelsPerLabel.setText("البيكسلات بين كل سطر:")
newLineCell = QTextEdit(FitAdvancedWindow)
newLineCell.setGeometry(QRect(240, y(5), 70, 26))
newLineLabel = QLabel(FitAdvancedWindow)
newLineLabel.setGeometry(QRect(320, y(5), labelsWidth, labelsHeight))
newLineLabel.setText("أمر سطر جديد:")
newPageCell = QTextEdit(FitAdvancedWindow)
newPageCell.setGeometry(QRect(10, y(0), 70, 26))
newPageLabel = QLabel(FitAdvancedWindow)
newPageLabel.setGeometry(QRect(90, y(0), labelsWidth, labelsHeight))
newPageLabel.setText("أمر صفحة جديدة:")
beforeComCell = QTextEdit(FitAdvancedWindow)
beforeComCell.setGeometry(QRect(10, y(1), 70, 26))
beforeComLabel = QLabel(FitAdvancedWindow)
beforeComLabel.setGeometry(QRect(90, y(1), labelsWidth, labelsHeight))
beforeComLabel.setText("ما قبل الأوامر:")
afterComCell = QTextEdit(FitAdvancedWindow)
afterComCell.setGeometry(QRect(10, y(2), 70, 26))
afterComLabel = QLabel(FitAdvancedWindow)
afterComLabel.setGeometry(QRect(90, y(2), labelsWidth, labelsHeight))
afterComLabel.setText("ما بعدها:")
timePerCharCell = QTextEdit(FitAdvancedWindow)
timePerCharCell.setGeometry(QRect(10, y(3), 70, 26))
timePerCharLabel = QLabel(FitAdvancedWindow)
timePerCharLabel.setGeometry(QRect(90, y(3), labelsWidth, labelsHeight))
timePerCharLabel.setText("الزمن بين كل حرف بالثواني:")
boxAnimationCell = QTextEdit(FitAdvancedWindow)
boxAnimationCell.setGeometry(QRect(10, y(4), 70, 26))
boxAnimationLabel = QLabel(FitAdvancedWindow)
boxAnimationLabel.setGeometry(QRect(90, y(4), labelsWidth, labelsHeight))
boxAnimationLabel.setText("أنميشن المربع (0-2):")

enteredTextLabel = QLabel(FitAdvancedWindow)
enteredTextLabel.setGeometry(QRect(580, 5, 81, 20))
enteredTextLabel.setText("النص الداخل:")
resultTextLabel_2 = QLabel(FitAdvancedWindow)
resultTextLabel_2.setGeometry(QRect(580, 185, 81, 20))
resultTextLabel_2.setText("النص الناتج:")

enteredTextCell = QTextEdit(FitAdvancedWindow)
enteredTextCell.setGeometry(QRect(480, 30, 200, 150))
enteredTextCell.setPlainText('السلام عليكم')
resultTextCell = QTextEdit(FitAdvancedWindow)
resultTextCell.setGeometry(QRect(480, 210, 200, 150))

fromRightCheck = QCheckBox("تدفق النص من اليمين", FitAdvancedWindow)
fromRightCheck.setGeometry(QRect(300, 225, 145, 26))
fromRightCheck.setLayoutDirection(Qt.RightToLeft)
lineBoxCheck = QCheckBox("صناديق الأسطر", FitAdvancedWindow)
lineBoxCheck.setGeometry(QRect(150, 225, 145, 26))
lineBoxCheck.setLayoutDirection(Qt.RightToLeft)

offsetRadio = QRadioButton("اترك النص على حاله", FitAdvancedWindow)
offsetRadio.setGeometry(QRect(220, 258, 210, 26))
offsetRadio.setLayoutDirection(Qt.RightToLeft)
offset0Radio = QRadioButton("النص في البداية واملأ بعده فراغات", FitAdvancedWindow)
offset0Radio.setGeometry(QRect(220, 283, 210, 26))
offset0Radio.setLayoutDirection(Qt.RightToLeft)
offset1Radio = QRadioButton("النص في النهاية واملأ قبله فراغات", FitAdvancedWindow)
offset1Radio.setGeometry(QRect(220, 308, 210, 26))
offset1Radio.setLayoutDirection(Qt.RightToLeft)
offset2Radio = QRadioButton("النص في الوسط واملأ قبله فراغات", FitAdvancedWindow)
offset2Radio.setGeometry(QRect(220, 333, 210, 26))
offset2Radio.setLayoutDirection(Qt.RightToLeft)
offset3Radio = QRadioButton("النص في الوسط واملأ قبله وبعده فراغات", FitAdvancedWindow)
offset3Radio.setGeometry(QRect(220, 358, 210, 26))
offset3Radio.setLayoutDirection(Qt.RightToLeft)

fontButton = QPushButton(FitAdvancedWindow)
fontButton.setGeometry(QRect(30, 290, 100, 40))
fontButton.setText("الخط")
startButton = QPushButton(FitAdvancedWindow)
startButton.setGeometry(QRect(30, 340, 100, 40))
startButton.setText("بدء")

fontButton.clicked.connect(lambda: openFont())
startButton.clicked.connect(lambda: start())

if __name__ == '__main__':
    FitAdvancedWindow.show()
    exit(app.exec_())