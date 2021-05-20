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
import pygame
import threading

geoDirectory, pngDirectory = '', ''
pygameXoffset, pygameYoffset = 10, 180

def type_in_box(textList, font_size, box_width, box_height, px_per_line, charmap, newline, newpage, display, char_border = False, from_Right = False,
                x = 0, y = 0, sleep_time = 0):
    Y = y
    if from_Right: X = box_width + x
    else: X = x
    for page in textList:
        setPygame(display, int(box_width + Y * 2), int(box_height + Y * 2), Y)
        embed(FitAdvancedWindow, embedLabel, display, pygameXoffset, pygameYoffset)
        y = Y
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
                
                embed(FitAdvancedWindow, embedLabel, display, pygameXoffset, pygameYoffset)
            y += font_size + px_per_line
        sleep(sleep_time)

def fit_advance(text = '', box_width = 10, box_height = 10, px_per_line = 10, fnt_directory = '', img_directory = '', newline = '', newpage = '',
                before_command = '', after_command = '', from_Right = False, lineOffset = 3, sleep_time = 0, border_thick = 10):
    if not fnt_directory or not img_directory:
        QMessageBox.about(FitAdvancedWindow, "تذكر", "لا تنسى اختيار الخط")
        return

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
            textList[p][l] = OffsetLine(textList[p][l], charmap, box_width, lineOffset)
        print_text.append(newline.join(textList[p]))
    
    resultTextCell.setPlainText(newpage.join(print_text))
    
    pygame.init()
    textbox = pygame.Surface((int(box_width + border_thick * 2), int(box_height + border_thick * 2)))
    
    type_in_box(textList, font_size, box_width, box_height, px_per_line, charmap, newline, newpage, textbox, False, from_Right,
                border_thick, border_thick, sleep_time)

def setPygame(display, pygameWidth, pygameHeight, border_thick):
    pygame.draw.rect(display, 0, (0, 0, pygameWidth, pygameHeight))
    pygame.draw.rect(display, 255, (0, 0, pygameWidth, pygameHeight), border_thick)

def openFont():
    global pngDirectory, geoDirectory
    d1, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'صورة الخط', '' , '*.jpg, *.png')
    d2, _ = QFileDialog.getOpenFileName(FitAdvancedWindow, 'جدول الخط', '' , '*.ate')
    if d1 and d1 != '/' and path.exists(d1): pngDirectory = d1
    if d2 and d2 != '/' and path.exists(d2): geoDirectory = d2

def start():
    if boxWidthCell.toPlainText(): boxWidth = int(float(boxWidthCell.toPlainText()))
    else: boxWidth = 190
    if boxHeightCell.toPlainText(): boxHeight = int(float(boxHeightCell.toPlainText()))
    else: boxHeight = 180
    if pixelsPerCell.toPlainText(): pixelsPer = int(float(pixelsPerCell.toPlainText()))
    else: pixelsPer = 0
    if timePerPageCell.toPlainText(): timePerPage = int(float(timePerPageCell.toPlainText()))
    else: timePerPage = 0
    if borderThickCell.toPlainText(): borderThick = int(float(borderThickCell.toPlainText()))
    else: borderThick = 10
    
    if offset0Radio.isChecked(): offset = 0
    elif offset1Radio.isChecked(): offset = 1
    elif offset2Radio.isChecked(): offset = 2
    elif offset3Radio.isChecked(): offset = 3
    else: offset = -1
    
    fit_advance(enteredTextCell.toPlainText(), boxWidth, boxHeight, pixelsPer, geoDirectory, pngDirectory, newLineCell.toPlainText(), newPageCell.toPlainText(), beforeComCell.toPlainText(), afterComCell.toPlainText(), fromRightCheck.isChecked(), offset, timePerPage, borderThick)

app = QApplication(argv)

FitAdvancedWindow = QMainWindow()
FitAdvancedWindow.setFixedSize(700, 390)
embedLabel = QLabel(FitAdvancedWindow)

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
beforeComCell.setGeometry(QRect(240, y(6), 70, 26))
beforeComLabel = QLabel(FitAdvancedWindow)
beforeComLabel.setGeometry(QRect(320, y(6), labelsWidth, labelsHeight))
beforeComLabel.setText("ما قبل الأوامر:")
afterComCell = QTextEdit(FitAdvancedWindow)
afterComCell.setGeometry(QRect(240, y(7), 70, 26))
afterComLabel = QLabel(FitAdvancedWindow)
afterComLabel.setGeometry(QRect(320, y(7), labelsWidth, labelsHeight))
afterComLabel.setText("ما بعدها:")
timePerPageCell = QTextEdit(FitAdvancedWindow)
timePerPageCell.setGeometry(QRect(240, y(8), 70, 26))
timePerPageLabel = QLabel(FitAdvancedWindow)
timePerPageLabel.setGeometry(QRect(320, y(8), labelsWidth, labelsHeight))
timePerPageLabel.setText("الزمن بين كل صفحة بالثواني:")

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
fromRightCheck.setGeometry(QRect(80, 10, 145, 26))
fromRightCheck.setLayoutDirection(Qt.RightToLeft)
offsetRadio = QRadioButton("اترك النص على حاله", FitAdvancedWindow)
offsetRadio.setGeometry(QRect(10, 35, 210, 26))
offsetRadio.setLayoutDirection(Qt.RightToLeft)
offset0Radio = QRadioButton("النص في البداية واملأ بعده فراغات", FitAdvancedWindow)
offset0Radio.setGeometry(QRect(10, 60, 210, 26))
offset0Radio.setLayoutDirection(Qt.RightToLeft)
offset1Radio = QRadioButton("النص في النهاية واملأ قبله فراغات", FitAdvancedWindow)
offset1Radio.setGeometry(QRect(10, 85, 210, 26))
offset1Radio.setLayoutDirection(Qt.RightToLeft)
offset2Radio = QRadioButton("النص في الوسط واملأ قبله فراغات", FitAdvancedWindow)
offset2Radio.setGeometry(QRect(10, 110, 210, 26))
offset2Radio.setLayoutDirection(Qt.RightToLeft)
offset3Radio = QRadioButton("النص في الوسط واملأ قبله وبعده فراغات", FitAdvancedWindow)
offset3Radio.setGeometry(QRect(10, 135, 210, 26))
offset3Radio.setLayoutDirection(Qt.RightToLeft)

fontButton = QPushButton(FitAdvancedWindow)
fontButton.setGeometry(QRect(360, 338, 80, 40))
fontButton.setText("اختر الخط")
startButton = QPushButton(FitAdvancedWindow)
startButton.setGeometry(QRect(260, 338, 80, 40))
startButton.setText("بدء")

fontButton.clicked.connect(lambda: openFont())
startButton.clicked.connect(lambda: start())

if __name__ == '__main__':
    FitAdvancedWindow.show()
    exit(app.exec_())