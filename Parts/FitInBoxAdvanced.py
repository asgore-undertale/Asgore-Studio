from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QCheckBox, QPushButton, QFileDialog, QMessageBox, QComboBox, QWidget, QGridLayout
from PyQt5.QtCore import QRect, Qt
from Parts.Scripts.LineOffset import *
from Parts.Scripts.Take_From_Table import Take_From_Table
from Parts.Scripts.Fit_in_box import fit
from Parts.Scripts.EmbedPygameInPyqt5 import embed
from os import path
from sys import argv, exit
from time import sleep
from PIL import Image
from ctypes import windll
import keyboard
import pygame

def type_in_box(textList, font_size, box_width, box_height, px_per_line, charmap, border_thick, newline, newpage, display, fontSize,
                lineBox = False, from_Right = False, boxAnimation = False, x = 0, y = 0):
    if FileDirectory.endswith('.ttf'): dialogue_font = pygame.font.Font(FileDirectory, font_size)
    
    Y = y
    if from_Right: X = box_width + border_thick
    else: X = x
    
    for page in textList:
        _y = Y
        conversation(0, 0, box_width + border_thick * 2, box_height + border_thick * 2, 0, (255, 255, 255), border_thick, boxAnimation, display)
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
            
            if lineBox: pygame.draw.rect(display, (255, 0, 0), (x, _y, box_width, fontSize), 1)
            pygame.display.update()
            
            _y += font_size + px_per_line
        
        while True:
            pygameCheck(display)
            if keyboard.is_pressed('enter'): break

def conversation(x, y, width, height, box_color, border_color, border_thick, boxAnimation, display):
    if not boxAnimation:
        pygame.draw.rect(display, box_color, (x, y, width, height))
        pygame.draw.rect(display, border_color, (x, y, width, height), border_thick)
        pygame.display.update()
        return
        
    frames = 100
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
                before_command = '', after_command = '', from_Right = False, lineBox = False, boxAnimation = False, lineOffset = 3, offsetWith = 0, offsetCommand = ''):
    if (not fnt_directory or not img_directory) and not fnt_directory.endswith('.ttf'):
        QMessageBox.about(FitAdvancedWindow, "تذكر", "لا تنسى اختيار الخط")
        return
    
    border_thick = 10
    charmap = Take_From_Table(fnt_directory, text, fontSize)
    
    lines_num = int(box_height / (fontSize * 2 + px_per_line) * 2)
    fitted_text = fit(text, charmap, box_width, lines_num, newline, newpage, before_command, after_command)
    
    if newpage: pages = fitted_text.split(newpage)
    else: pages = [fitted_text]
    if newline: textList = [page.split(newline) for page in pages]
    else: textList = [pages]
    
    if lineOffset >= 0:
        if offsetWith == 0:
            for p in range(len(textList)):
                for l in range(len(textList[p])):
                    textList[p][l] = OffsetLineWithSpaces(textList[p][l], charmap, box_width, lineOffset)
        if offsetWith == 1:
            if offsetCommand:
                for p in range(len(textList)):
                    for l in range(len(textList[p])):
                        textList[p][l] = OffsetLineWithCommands(textList[p][l], charmap, box_width, lineOffset, offsetCommand)
        
        fitted_text = newpage.join([newline.join(page) for page in textList])
    
    resultTextBox.setPlainText(fitted_text)
    
    pygame.display.set_caption('Font Tester')
    textbox = pygame.display.set_mode((int(box_width + border_thick * 2), int(box_height + border_thick * 2)))
    
    SetWindowPos = windll.user32.SetWindowPos
    SetWindowPos(pygame.display.get_wm_info()['window'], -1, 250, 250, 0, 0, 0x0001)
    
    type_in_box(textList, fontSize, box_width, box_height, px_per_line, charmap, border_thick, newline, newpage, textbox, fontSize,
                lineBox, from_Right, boxAnimation, border_thick, border_thick)

    while True: pygameCheck(textbox)

def pygameCheck(display):
    for event in pygame.event.get():
        if event.type is pygame.QUIT: pygame.display.set_mode((1, 1), flags = pygame.HIDDEN)
        elif event.type == pygame.KEYDOWN:
            all_keys = pygame.key.get_pressed()
            if all_keys[pygame.K_LCTRL] and all_keys[pygame.K_s]:
                    pygame.image.save(display, save_file('png', FitAdvancedWindow))

def openFont(Directory = ''):
    global pngDirectory, FileDirectory
    Directory, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'جدول الخط', '' , '*.aft *.ttf')
    if Directory and Directory != '/' and path.exists(Directory): FileDirectory = Directory
    
    if FileDirectory.endswith('.ttf'): return
    
    if Directory: Directory, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'صورة الخط', '' , '*.jpg *.png')
    if Directory and Directory != '/' and path.exists(Directory): pngDirectory = Directory

def save_file(type : str, window):
    _save, _ = QFileDialog.getSaveFileName(window, 'صورة', '' , '*.'+type)
    return _save * (_save != '/') * (_save != '')

def start():
    if fontSizeCell.toPlainText(): fontSize = int(float(fontSizeCell.toPlainText()))
    else: fontSize = 1
    if boxWidthCell.toPlainText(): boxWidth = float(boxWidthCell.toPlainText())
    else: boxWidth = 180
    if boxHeightCell.toPlainText(): boxHeight = float(boxHeightCell.toPlainText())
    else: boxHeight = 60
    if pixelsPerCell.toPlainText(): pixelsPer = float(pixelsPerCell.toPlainText())
    else: pixelsPer = 0
    offset = offsetComboBox.currentIndex() -1
    offsetWith = offsetWithComboBox.currentIndex()
    
    fit_advance(enteredTextBox.toPlainText(), fontSize, boxWidth, boxHeight, pixelsPer, FileDirectory, pngDirectory, newLineCell.toPlainText(), newPageCell.toPlainText(), beforeComCell.toPlainText(), afterComCell.toPlainText(), fromRightCheck.isChecked(), lineBoxCheck.isChecked(), boxAnimationCheck.isChecked(), offset, offsetWith, offsetCommandCell.toPlainText())

FileDirectory, pngDirectory = '', ''

app = QApplication(argv)
pygame.init()

FitAdvancedWindow = QMainWindow()
container = QWidget()
FitAdvancedWindow.resize(240, 420)

layout = QGridLayout()
container.setLayout(layout)
FitAdvancedWindow.setCentralWidget(container)

enteredTextBox = QTextEdit()
resultTextBox = QTextEdit()
enteredTextBox.setPlainText('تجربة الخط')

enteredTextLabel = QLabel()
resultTextLabel = QLabel()
enteredTextLabel.setText("   النص الداخل:")
resultTextLabel.setText("   النص الناتج:")

minilayout = QGridLayout()
startButton = QPushButton()
fontButton = QPushButton()
startButton.setText("بدء")
fontButton.setText("الخط")

layout.addWidget(enteredTextLabel, 0, 0)
layout.addWidget(enteredTextBox, 1, 0)
layout.addWidget(resultTextLabel, 2, 0)
layout.addWidget(resultTextBox, 3, 0)
layout.addLayout(minilayout, 4, 0)
minilayout.addWidget(startButton, 0, 1)
minilayout.addWidget(fontButton, 0, 0)


FitAdvancedOptionsWindow = QMainWindow()
FitAdvancedOptionsWindow.setFixedSize(480, 330)

labelsWidth, labelsHeight = 145, 26

def y(num, height = 26, per = 10, first = 20):
    return first + (num * height) + ((num - 1) * per)

fontSizeCell = QTextEdit(FitAdvancedOptionsWindow)
fontSizeCell.setGeometry(QRect(240, y(0), 70, 26))
fontSizeCell.setText("16")
fontSizeLabel = QLabel(FitAdvancedOptionsWindow)
fontSizeLabel.setGeometry(QRect(320, y(0), labelsWidth, labelsHeight))
fontSizeLabel.setText("حجم الخط:")
boxWidthCell = QTextEdit(FitAdvancedOptionsWindow)
boxWidthCell.setGeometry(QRect(240, y(1), 70, 26))
boxWidthCell.setText("180")
boxWidthLabel = QLabel(FitAdvancedOptionsWindow)
boxWidthLabel.setGeometry(QRect(320, y(1), labelsWidth, labelsHeight))
boxWidthLabel.setText("عرض المربع:")
boxHeightCell = QTextEdit(FitAdvancedOptionsWindow)
boxHeightCell.setGeometry(QRect(240, y(2), 70, 26))
boxHeightCell.setText("60")
boxHeightLabel = QLabel(FitAdvancedOptionsWindow)
boxHeightLabel.setGeometry(QRect(320, y(2), labelsWidth, labelsHeight))
boxHeightLabel.setText("ارتفاع المربع:")
pixelsPerCell = QTextEdit(FitAdvancedOptionsWindow)
pixelsPerCell.setGeometry(QRect(240, y(3), 70, 26))
pixelsPerCell.setText("1")
pixelsPerLabel = QLabel(FitAdvancedOptionsWindow)
pixelsPerLabel.setGeometry(QRect(320, y(3), labelsWidth, labelsHeight))
pixelsPerLabel.setText("البيكسلات بين كل سطر:")
newLineCell = QTextEdit(FitAdvancedOptionsWindow)
newLineCell.setGeometry(QRect(240, y(4), 70, 26))
newLineCell.setText("<line>")
newLineLabel = QLabel(FitAdvancedOptionsWindow)
newLineLabel.setGeometry(QRect(320, y(4), labelsWidth, labelsHeight))
newLineLabel.setText("أمر سطر جديد:")
newPageCell = QTextEdit(FitAdvancedOptionsWindow)
newPageCell.setGeometry(QRect(240, y(5), 70, 26))
newPageCell.setText("<page>")
newPageLabel = QLabel(FitAdvancedOptionsWindow)
newPageLabel.setGeometry(QRect(320, y(5), labelsWidth, labelsHeight))
newPageLabel.setText("أمر صفحة جديدة:")
beforeComCell = QTextEdit(FitAdvancedOptionsWindow)
beforeComCell.setGeometry(QRect(240, y(6), 70, 26))
beforeComCell.setText("[")
beforeComLabel = QLabel(FitAdvancedOptionsWindow)
beforeComLabel.setGeometry(QRect(320, y(6), labelsWidth, labelsHeight))
beforeComLabel.setText("ما قبل الأوامر:")
afterComCell = QTextEdit(FitAdvancedOptionsWindow)
afterComCell.setGeometry(QRect(240, y(7), 70, 26))
afterComCell.setText("]")
afterComLabel = QLabel(FitAdvancedOptionsWindow)
afterComLabel.setGeometry(QRect(320, y(7), labelsWidth, labelsHeight))
afterComLabel.setText("ما بعدها:")
offsetCommandCell = QTextEdit(FitAdvancedOptionsWindow)
offsetCommandCell.setGeometry(QRect(240, y(8), 70, 26))
offsetCommandCell.setText("(px)")
offsetCommandLabel = QLabel(FitAdvancedOptionsWindow)
offsetCommandLabel.setGeometry(QRect(320, y(8), labelsWidth, labelsHeight))
offsetCommandLabel.setText("أمر الإزاحة:")

offsetComboBoxOptions = ["اترك النص على حاله", "النص في البداية واملأ ما بعده", "النص في النهاية واملأ ما قبله",
    "النص في الوسط واملأ ما قبله", "النص في الوسط واملأ ما قبله وبعده"]
offsetComboBox = QComboBox(FitAdvancedOptionsWindow)
offsetComboBox.setGeometry(20, 35, 200, 30)
offsetComboBox.addItems(offsetComboBoxOptions)
offsetComboBox.setInsertPolicy(QComboBox.NoInsert)
# offsetComboBox.setEditable(True)
offsetWithComboBoxOptions = ["الفراغات", "الأوامر"]
offsetWithComboBox = QComboBox(FitAdvancedOptionsWindow)
offsetWithComboBox.setGeometry(20, 105, 200, 30)
offsetWithComboBox.addItems(offsetWithComboBoxOptions)
offsetWithComboBox.setInsertPolicy(QComboBox.NoInsert)

offsetComboBoxLabel = QLabel(FitAdvancedOptionsWindow)
offsetComboBoxLabel.setGeometry(QRect(130, 10, 80, 20))
offsetComboBoxLabel.setText("الإزاحة:")
offsetWithComboBoxLabel = QLabel(FitAdvancedOptionsWindow)
offsetWithComboBoxLabel.setGeometry(QRect(130, 80, 80, 20))
offsetWithComboBoxLabel.setText("باستعمال:")

fromRightCheck = QCheckBox("تدفق النص من اليمين", FitAdvancedOptionsWindow)
fromRightCheck.setGeometry(QRect(80, 250, 145, 26))
fromRightCheck.setLayoutDirection(Qt.RightToLeft)
boxAnimationCheck = QCheckBox("أنميشن مربع الحوار", FitAdvancedOptionsWindow)
boxAnimationCheck.setGeometry(QRect(80, 275, 145, 26))
boxAnimationCheck.setLayoutDirection(Qt.RightToLeft)
lineBoxCheck = QCheckBox("صناديق الأسطر", FitAdvancedOptionsWindow)
lineBoxCheck.setGeometry(QRect(80, 300, 145, 26))
lineBoxCheck.setLayoutDirection(Qt.RightToLeft)

fontButton.clicked.connect(lambda: openFont())
startButton.clicked.connect(lambda: start())