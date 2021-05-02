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

def type_in_box(textList, font_size, box_width, box_height, px_per_line, charmap, border_thick, newline, newpage, display, char_border = False, from_Right = False,
                x = 0, y = 0, sleep_time = 0, frames = 1, box_style = 0):
    Y = y
    if from_Right: X = box_width + border_thick
    else: X = x
    for page in textList:
        y = Y
        conversation(0, 0, box_width + border_thick * 2, box_height + border_thick * 2, 0, (255, 255, 255), border_thick, frames, box_style, display)
        for line in page:
            x = X
            for char in line:
                if char not in charmap: continue
                char_x, char_y, char_width, char_height = charmap[char][0], charmap[char][1], charmap[char][2], charmap[char][3]
                char_xoffset, char_yoffset, char_xadvance = charmap[char][4], charmap[char][5], charmap[char][6]
                if char_width > box_width: continue

                img = Image.open(pngDirectory)
                croped_img = img.crop((char_x, char_y, char_x+char_width, char_y+char_height))
                py_img = pygame.image.fromstring(croped_img.tobytes(), croped_img.size, croped_img.mode)

                if from_Right: x -= char_width
                display.blit(py_img, (x + char_xoffset, y + char_yoffset))
                if char_border:
                    pygame.draw.rect(display, (0, 255, 0), (x, y, char_width, font_size), 1)
                    pygame.draw.rect(display, (255, 0, 0), (x + char_xoffset, y + char_yoffset, char_width, char_height), 1)
                if from_Right: x -= char_xadvance
                else: x += char_width + char_xadvance
                
                pygame.display.update()
                sleep(sleep_time)
            y += font_size + px_per_line
        
        while True:
            pygameCheck()
            if keyboard.is_pressed('enter'): break

def conversation(x, y, width, height, box_color, border_color, border_thick, frames, box_style, display):
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

def fit_advance(text = '', box_width = 10, box_height = 10, px_per_line = 10, fnt_directory = '', img_directory = '', newline = '', newpage = '',
                before_command = '', after_command = '', from_Right = False, lineOfssef = 3,sleep_time = 0, frames = 1, border_thick = 10, box_style = 0):
    if not fnt_directory or not img_directory:
        QMessageBox.about(FitAdvancedWindow, "تذكر", "لا تنسى تحديد ملف وصورة الخط")
        return
    
    keyboard.on_press_key("F3", lambda _: pygame.image.save(textbox, "screenshot.png"))

    charmap = CreateCharmap(fnt_directory)
    
    font_size = charmap['height']
    lines_num = int(box_height / (font_size * 2 + px_per_line) * 2)
    fitted_text = fit(text, charmap, box_width, lines_num, newline, newpage, before_command, after_command)
    
    if newpage: pages = fitted_text.split(newpage)
    else: pages = [fitted_text]
    if newline: textList = [page.split(newline) for page in pages]
    else: textList = [pages]
    
    print_text = []
    for p in range(len(textList)):
        for l in range(len(textList[p])):
            textList[p][l] = OffsetLine(textList[p][l], charmap, box_width, lineOfssef)
        print_text.append('\n'.join(textList[p]))
    
    resultTextCell.setPlainText('\n\n'.join(print_text))
    
    pygame.init()
    pygame.display.set_caption('Fit in box (Advanced)')
    textbox = pygame.display.set_mode((int(box_width + border_thick * 2), int(box_height + border_thick * 2)))
    
    SetWindowPos = windll.user32.SetWindowPos
    SetWindowPos(pygame.display.get_wm_info()['window'], -1, 250, 250, 0, 0, 0x0001)
    
    type_in_box(textList, font_size, box_width, box_height, px_per_line, charmap, border_thick, newline, newpage, textbox, False, from_Right,
                border_thick, border_thick, sleep_time, frames, box_style)

    while True: pygameCheck()

def pygameCheck():
    for event in pygame.event.get():
        if event.type is pygame.QUIT: pygame.display.set_mode((1, 1), flags = pygame.HIDDEN)

def openPng(Directory = ''):
    global pngDirectory
    if not Directory: Directory, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'صورة الخط', '' , '*.jpg, *.png')
    if Directory and Directory != '/' and path.exists(Directory): pngDirectory = Directory
    
def openGeo(Directory = ''):
    global geoDirectory
    if not Directory: Directory, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'جدول الخط', '' , '*.ate')
    if Directory and Directory != '/' and path.exists(Directory): geoDirectory = Directory

def start():
    if boxWidthCell.toPlainText(): boxWidth = float(boxWidthCell.toPlainText())
    else: boxWidth = 1
    if boxHeightCell.toPlainText(): boxHeight = float(boxHeightCell.toPlainText())
    else: boxHeight = 1
    if pixelsPerCell.toPlainText(): pixelsPer = float(pixelsPerCell.toPlainText())
    else: pixelsPer = 0
    if timePerCharCell.toPlainText(): timePerChar = float(timePerCharCell.toPlainText())
    else: timePerChar = 0
    if framesNumCell.toPlainText(): framesNum = int(float(framesNumCell.toPlainText()))
    else: framesNum = 100
    if borderThickCell.toPlainText(): borderThick = float(borderThickCell.toPlainText())
    else: borderThick = 10
    if boxAnimationCell.toPlainText(): boxAnimation = int(float(boxAnimationCell.toPlainText()))
    else: boxAnimation = 2
    
    if offset0Radio.isChecked(): offset = 0
    elif offset1Radio.isChecked(): offset = 1
    elif offset2Radio.isChecked(): offset = 2
    elif offset3Radio.isChecked(): offset = 3
    else: offset = -1
    
    fit_advance(enteredTextCell.toPlainText(), boxWidth, boxHeight, pixelsPer, geoDirectory, pngDirectory, newLineCell.toPlainText(), newPageCell.toPlainText(), beforeComCell.toPlainText(), afterComCell.toPlainText(), fromRightCheck.isChecked(), offset, timePerChar, framesNum, borderThick, boxAnimation)

geoDirectory, pngDirectory = '', ''

app = QApplication(argv)

FitAdvancedWindow = QMainWindow()
FitAdvancedWindow.setFixedSize(700, 390)

labelsWidth, labelsHeight = 130, 26

def y(num, height = 26, per = 10, first = 20):
    return first + (num * height) + ((num - 1) * per)

borderThickCell = QTextEdit(FitAdvancedWindow)
borderThickCell.setGeometry(QRect(240, y(0), 70, 26))
borderThickLabel = QLabel(FitAdvancedWindow)
borderThickLabel.setGeometry(QRect(320, y(0), labelsWidth, labelsHeight))
borderThickLabel.setText("ثخن جدار المربع:")
boxWidthCell = QTextEdit(FitAdvancedWindow)
boxWidthCell.setGeometry(QRect(240, y(1), 70, 26))
boxWidthLabel = QLabel(FitAdvancedWindow)
boxWidthLabel.setGeometry(QRect(320, y(1), labelsWidth, labelsHeight))
boxWidthLabel.setText("عرض المربع:")
boxHeightCell = QTextEdit(FitAdvancedWindow)
boxHeightCell.setGeometry(QRect(240, y(2), 70, 26))
boxHeightLabel = QLabel(FitAdvancedWindow)
boxHeightLabel.setGeometry(QRect(320, y(2), labelsWidth, labelsHeight))
boxHeightLabel.setText("ارتفاع المربع:")
pixelsPerCell = QTextEdit(FitAdvancedWindow)
pixelsPerCell.setGeometry(QRect(240, y(3), 70, 26))
pixelsPerLabel = QLabel(FitAdvancedWindow)
pixelsPerLabel.setGeometry(QRect(320, y(3), labelsWidth, labelsHeight))
pixelsPerLabel.setText("البيكسلات بين كل سطر:")
newLineCell = QTextEdit(FitAdvancedWindow)
newLineCell.setGeometry(QRect(240, y(4), 70, 26))
newLineLabel = QLabel(FitAdvancedWindow)
newLineLabel.setGeometry(QRect(320, y(4), labelsWidth, labelsHeight))
newLineLabel.setText("أمر سطر جديد:")
newPageCell = QTextEdit(FitAdvancedWindow)
newPageCell.setGeometry(QRect(240, y(5), 70, 26))
newPageLabel = QLabel(FitAdvancedWindow)
newPageLabel.setGeometry(QRect(320, y(5), labelsWidth, labelsHeight))
newPageLabel.setText("أمر صفحة جديدة:")
beforeComCell = QTextEdit(FitAdvancedWindow)
beforeComCell.setGeometry(QRect(10, y(0), 70, 26))
beforeComLabel = QLabel(FitAdvancedWindow)
beforeComLabel.setGeometry(QRect(90, y(0), labelsWidth, labelsHeight))
beforeComLabel.setText("ما قبل الأوامر:")
afterComCell = QTextEdit(FitAdvancedWindow)
afterComCell.setGeometry(QRect(10, y(1), 70, 26))
afterComLabel = QLabel(FitAdvancedWindow)
afterComLabel.setGeometry(QRect(90, y(1), labelsWidth, labelsHeight))
afterComLabel.setText("ما بعدها:")
timePerCharCell = QTextEdit(FitAdvancedWindow)
timePerCharCell.setGeometry(QRect(10, y(2), 70, 26))
timePerCharLabel = QLabel(FitAdvancedWindow)
timePerCharLabel.setGeometry(QRect(90, y(2), labelsWidth, labelsHeight))
timePerCharLabel.setText("الزمن بين كل حرف بالثواني:")
framesNumCell = QTextEdit(FitAdvancedWindow)
framesNumCell.setGeometry(QRect(10, y(3), 70, 26))
framesNumLabel = QLabel(FitAdvancedWindow)
framesNumLabel.setGeometry(QRect(90, y(3), labelsWidth, labelsHeight))
framesNumLabel.setText("عدد الإطارات:")
boxAnimationCell = QTextEdit(FitAdvancedWindow)
boxAnimationCell.setGeometry(QRect(10, y(4), 70, 26))
boxAnimationLabel = QLabel(FitAdvancedWindow)
boxAnimationLabel.setGeometry(QRect(90, y(4), labelsWidth, labelsHeight))
boxAnimationLabel.setText("أنميشن المربع (0-2):")

label = QLabel(FitAdvancedWindow)
label.setGeometry(QRect(580, 5, 81, 20))
label.setText("النص الداخل:")
label_2 = QLabel(FitAdvancedWindow)
label_2.setGeometry(QRect(580, 185, 81, 20))
label_2.setText("النص الناتج:")

enteredTextCell = QTextEdit(FitAdvancedWindow)
enteredTextCell.setGeometry(QRect(480, 30, 200, 150))
resultTextCell = QTextEdit(FitAdvancedWindow)
resultTextCell.setGeometry(QRect(480, 210, 200, 150))

fromRightCheck = QCheckBox("تدفق النص من اليمين", FitAdvancedWindow)
fromRightCheck.setGeometry(QRect(300, 225, 145, 26))
fromRightCheck.setLayoutDirection(Qt.RightToLeft)
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

geoButton = QPushButton(FitAdvancedWindow)
geoButton.setGeometry(QRect(30, 240, 100, 40))
geoButton.setText("جدول الخط")
pngButton = QPushButton(FitAdvancedWindow)
pngButton.setGeometry(QRect(30, 290, 100, 40))
pngButton.setText("صورة الخط")
startButton = QPushButton(FitAdvancedWindow)
startButton.setGeometry(QRect(30, 340, 100, 40))
startButton.setText("بدء")

pngButton.clicked.connect(lambda: openPng())
geoButton.clicked.connect(lambda: openGeo())
startButton.clicked.connect(lambda: start())

if __name__ == '__main__':
    FitAdvancedWindow.show()
    exit(app.exec_())

#fnt_directory, img_directory = r'tests\The Legend of Zelda A Link to the Past\table.txt', r'tests\The Legend of Zelda A Link to the Past\unknown.png'
#text = 'Long ago, in the[gr] beautiful kingdom of hyrule surrounded by mountains and forests...'
#fit_advance(text, 180, 65, 5, fnt_directory, img_directory, '[br]', '[page]', '[', ']', False, 0.03, 10, 100, 2)

#text = 'خط الميترويد يحييكم'
#fnt_directory, img_directory = r'tests\Mitroid\font.fiba', r'tests\Mitroid\unknown.png'
#fit_advance(text, 180, 65, 5, fnt_directory, img_directory, '[br]', '[page]', '[', ']', True, 0.03, 100, 10, 2)