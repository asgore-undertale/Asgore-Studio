from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QCheckBox, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import QRect, Qt
from Parts.Scripts.Un_Freeze_Arabic import Un_Freeze
from Parts.FitInBoxAdvancedScripts.CharmapCreator import CreateCharmap
from Parts.FitInBoxAdvancedScripts.Fit_in_box import fit
from os import path
from sys import argv, exit
from time import sleep
from PIL import Image
import keyboard
import pygame

def type_in_box(text, font_size, box_width, box_height, px_per_line, charmap, border_thick, newline, newpage, display, char_border = False, from_Right = False,
                x = 0, y = 0, sleep_time = 0, frames = 1, box_style = 0):
    X, Y = x, y
    if newpage: pages = text.split(newpage)
    else: pages = [text]
    if newline: splited_pages = [page.split(newline) for page in pages]
    else: splited_pages = [pages]
    
    for page in splited_pages:
        conversation(0, 0, box_width + border_thick * 2, box_height + border_thick * 2, 0, (255, 255, 255), border_thick, frames, box_style, display)
        for line in page:
            if from_Right: x = box_width
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
            x = X
        y = Y
        
        run = True
        while True:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.display.set_mode((1, 1), flags = pygame.HIDDEN)
                if keyboard.is_pressed('enter'):
                    run = False
                    break

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
    elif box_style == 2:
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
                before_command = '', after_command = '', from_Right = False, sleep_time = 0, frames = 1, border_thick = 10, box_style = 0):
    if not fnt_directory or not img_directory:
        QMessageBox.about(FitAdvancedWindow, "تذكر", "لا تنسى تحديد ملف وصورة الخط")
        return
    
    keyboard.on_press_key("F3", lambda _: pygame.image.save(textbox, "screenshot.png"))
    print('\nPress enter to see the next page.')
    print('Press F3 to save an image.')
    print('-----------------------------------')

    charmap = CreateCharmap(fnt_directory)
    
    font_size = charmap['height']
    lines_num = int(box_height / (font_size * 2 + px_per_line) * 2)
    fitted_text = fit(Un_Freeze(text), charmap, box_width, lines_num, newline, newpage, before_command, after_command)
    
    print_text = fitted_text
    if newpage: print_text = print_text.replace(newpage, '\n\n')
    if newline: print_text = print_text.replace(newline, '\n')
    print('\n' + print_text)
    
    pygame.init()
    pygame.display.set_caption('Fit in box (Advanced)')
    textbox = pygame.display.set_mode((int(box_width + border_thick * 2), int(box_height + border_thick * 2)))

    type_in_box(fitted_text, font_size, box_width, box_height, px_per_line, charmap, border_thick, newline, newpage, textbox, False, from_Right,
                border_thick, border_thick, sleep_time, frames, box_style)

    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.display.set_mode((1, 1), flags = pygame.HIDDEN)

def openPng(Directory = ''):
    global pngDirectory
    if not Directory: Directory, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'جداول إكسل', '' , '*.jpg, *.png')
    if Directory != '' and path.exists(Directory): pngDirectory = Directory
    
def openGeo(Directory = ''):
    global geoDirectory
    if not Directory: Directory, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'جداول إكسل', '' , '*.ate')
    if Directory != '' and path.exists(Directory): geoDirectory = Directory

def start():
    if boxWidthCell.toPlainText(): boxWidth = float(boxWidthCell.toPlainText())
    else: boxWidth = 1
    if boxHeightCell.toPlainText(): boxHeight = float(boxHeightCell.toPlainText())
    else: boxHeight = 1
    if pixelsPerCell.toPlainText(): pixelsPer = float(pixelsPerCell.toPlainText())
    else: pixelsPer = 0
    if timePerCharCell.toPlainText(): timePerChar = float(timePerCharCell.toPlainText())
    else: timePerChar = 0
    if framesNumCell.toPlainText(): framesNum = float(framesNumCell.toPlainText())
    else: framesNum = 100
    if borderThickCell.toPlainText(): borderThick = float(borderThickCell.toPlainText())
    else: borderThick = 10
    if boxAnimationCell.toPlainText(): boxAnimation = float(boxAnimationCell.toPlainText())
    else: boxAnimation = 2

    fit_advance(textCell.toPlainText(), boxWidth, boxHeight, pixelsPer, geoDirectory, pngDirectory, newLineCell.toPlainText(), newPageCell.toPlainText(), beforeComCell.toPlainText(), afterComCell.toPlainText(), fromRightCheck.isChecked(), timePerChar, framesNum, borderThick, boxAnimation)

geoDirectory, pngDirectory = '', ''

app = QApplication(argv)

FitAdvancedWindow = QMainWindow()
FitAdvancedWindow.setFixedSize(460, 280)

labelsWidth, labelsHeight = 130, 26

def y(num, height = 26, per = 10, first = 20):
    return first + (num * height) + ((num - 1) * per)

textCell = QTextEdit(FitAdvancedWindow)
textCell.setGeometry(QRect(240, y(0), 150, 26))
textLabel = QLabel(FitAdvancedWindow)
textLabel.setGeometry(QRect(320, y(0), labelsWidth, labelsHeight))
textLabel.setText("النص:")
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
borderThickCell = QTextEdit(FitAdvancedWindow)
borderThickCell.setGeometry(QRect(10, y(4), 70, 26))
borderThickLabel = QLabel(FitAdvancedWindow)
borderThickLabel.setGeometry(QRect(90, y(4), labelsWidth, labelsHeight))
borderThickLabel.setText("ثخن جدار المربع:")
boxAnimationCell = QTextEdit(FitAdvancedWindow)
boxAnimationCell.setGeometry(QRect(10, y(5), 70, 26))
boxAnimationLabel = QLabel(FitAdvancedWindow)
boxAnimationLabel.setGeometry(QRect(90, y(5), labelsWidth, labelsHeight))
boxAnimationLabel.setText("أنميشن المربع (0-2):")

fromRightCheck = QCheckBox("تدفق النص من اليمين", FitAdvancedWindow)
fromRightCheck.setGeometry(QRect(120, 238, 140, 26))
fromRightCheck.setLayoutDirection(Qt.RightToLeft)

pngButton = QPushButton(FitAdvancedWindow)
pngButton.setGeometry(QRect(280, 230, 70, 40))
pngButton.setText("صورة الخط")
geoButton = QPushButton(FitAdvancedWindow)
geoButton.setGeometry(QRect(360, 230, 80, 40))
geoButton.setText("جدول معلومات\nالخط")
startButton = QPushButton(FitAdvancedWindow)
startButton.setGeometry(QRect(30, 230, 60, 40))
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