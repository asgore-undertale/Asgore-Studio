from PyQt5.QtWidgets import QApplication
from Parts.Scripts.UsefulLittleFunctions import tryTakeNum, saveFile, openFile, splitTextByCommands, sentencesToText, checkForCommand
from Parts.Scripts.LineOffset import *
from Parts.Scripts.TakeFromTable import TakeFromTable
from Parts.Scripts.FitInBox import fit
# from Parts.Scripts.EmbedPygameInPyqt5 import embed
from sys import argv, exit
from time import sleep, time
from PIL import Image
from ctypes import windll
import keyboard
import pygame
'''
replacing pygame will cause a problem with saving window... for some reason
using arcade library will disable "keyboard library in the whole studio... for some reason
'''

def type_in_box(sentences, fontSize, per, boxWidth, boxHeight, linesNum, pxPerLine, charmap, newLine, newPage, display,
                lineBox, fromRight, boxAnimation):
    if FontPath.endswith('.ttf'): dialogue_font = pygame.font.Font(FontPath, fontSize)
    
    X, Y = borderThick, borderThick
    if fromRight: X += boxWidth
    _y, _x = Y, X
    
    PassTimes = 0
    TextColor = (225, 225, 225)
    BackgroundColor = 0
    SleepTime = 0
    ShakePoints = [(-7, -5), (5, 13), (-14, 6), (-7, 3), (0, 0)]
    
    for s in range(len(sentences)):
        if not s % (linesNum):
            waitForPress(display, s > 0)
            _y = Y
            drawBox(0, 0, boxWidth + borderThick * 2, boxHeight + borderThick * 2, BackgroundColor, boxAnimation, display)
        
        _x = X
        for c in range(len(sentences[s])):
            if PassTimes:
                PassTimes -= 1
                continue
            
            try:
                if checkForCommand('[^]', sentences[s], c):
                    waitForPress(display, True)
                    PassTimes = 2
                elif checkForCommand('[!]', sentences[s], c):
                    d = display.copy()
                    for point in ShakePoints:
                        display.blit(d, point)
                        pygame.display.update()
                        sleep(1/40)
                    PassTimes = 2
                elif checkForCommand(r'[\t#]', sentences[s], c):
                    TextColor = (225, 225, 225)
                    PassTimes = 4
                elif checkForCommand(r'[\b#]', sentences[s], c):
                    BackgroundColor = 0
                    PassTimes = 4
                elif checkForCommand(r'[\@]', sentences[s], c):
                    SleepTime = 0
                    PassTimes = 3
                    PassTimes = 2
                elif checkForCommand(r'[\$]', sentences[s], c):
                    char_height = charmap[list(charmap)[0]][3]
                    per = (fontSize * char_height / charmap['tallest'] - char_height) / charmap['tallest']
                    PassTimes = 3
                elif checkForCommand('[@', sentences[s], c) and sentences[s][c+8] == ']':
                    SleepTime = tryTakeNum(sentences[s][c+2:c+8], 0, False)
                    PassTimes = 8
                elif checkForCommand('[$', sentences[s], c) and sentences[s][c+5] == ']':
                    char_height = charmap[list(charmap)[0]][3]
                    font_size   = tryTakeNum(sentences[s][c+2:c+5], fontSize)
                    per = (font_size * char_height / charmap['tallest'] - char_height) / charmap['tallest']
                    PassTimes = 5
                elif checkForCommand('[t#', sentences[s], c) and sentences[s][c+9] == ']':
                    TextColor = (int(sentences[s][c+3], 16) * int(sentences[s][c+4], 16),
                        int(sentences[s][c+5], 16) * int(sentences[s][c+6], 16),
                        int(sentences[s][c+7], 16) * int(sentences[s][c+8], 16)
                        )
                    PassTimes = 9
                elif checkForCommand('[b#', sentences[s], c) and sentences[s][c+9] == ']':
                    BackgroundColor = (int(sentences[s][c+3], 16) * int(sentences[s][c+4], 16),
                        int(sentences[s][c+5], 16) * int(sentences[s][c+6], 16),
                        int(sentences[s][c+7], 16) * int(sentences[s][c+8], 16)
                        )
                    PassTimes = 9
                    
            except: pass
            if PassTimes: continue
            
            if lineBox: pygame.draw.rect(display, (255, 0, 0), (borderThick, _y, boxWidth, fontSize), 1)
            pygame.display.update()
            
            char = sentences[s][c]
            if FontPath.endswith('.ttf'):
                dialogue = dialogue_font.render(char, True, TextColor)
                char_width,  char_xadvance = dialogue.get_size()[0], 0
                
                if fromRight: _x -= char_width
                display.blit(dialogue, (_x, _y))
            else:
                if char not in charmap: continue
                char_x, char_y, char_height = charmap[char][0], charmap[char][1], charmap[char][3]
                
                charinfo = list(map(lambda x: int(x + (x * per)), charmap[char])) # ((x + (x * per)) % 1 > 0) * 1 + 
                
                char_width, char_height, char_xoffset = charinfo[2], charinfo[3], charinfo[4]
                char_yoffset, char_xadvance = charinfo[5], charinfo[6]
                if char_width > boxWidth: continue
                
                img = Image.open(ImgPath)
                croped_img = img.crop((char_x, char_y, char_x+charmap[char][2], char_y+charmap[char][3]))
                pySurface = pygame.image.fromstring(croped_img.tobytes(), croped_img.size, croped_img.mode)
                pySurface.fill(TextColor, special_flags=pygame.BLEND_MULT)
                
                pySurface = pygame.transform.scale(pySurface, (char_width, char_height))
                
                if fromRight: _x -= char_width
                display.blit(pySurface, (_x + char_xoffset, _y + char_yoffset))
            
            if fromRight: _x -= char_xadvance
            else: _x += char_width + char_xadvance
            
            pygame.display.update()
            pygameWait(display, SleepTime)
        
        _y += fontSize + pxPerLine

def drawBox(x, y, width, height, boxColor, boxAnimation, display):
    if not boxAnimation:
        pygame.draw.rect(display, boxColor, (x, y, width, height))
        pygame.draw.rect(display, borderColor, (x, y, width, height), borderThick)
        pygame.display.update()
        return
        
    frames = 100
    x, w = width / 2, 0
    for i in range(frames):
        h = height * (i + 1) / frames
        y = height / 2 - h / 2
        pygame.draw.rect(display, boxColor, (x, y, w, h))
        pygame.draw.rect(display, borderColor, (x, y, w, h), borderThick)
        pygame.display.update()
        sleep(0.0025)
    h = height
    for i in range(frames):
        w = width * (i + 1) / frames
        x = width / 2 - w / 2 
        pygame.draw.rect(display, boxColor, (x, y, w, h))
        pygame.draw.rect(display, borderColor, (x, y, w, h), borderThick)
        pygame.display.update()
        sleep(0.0025)

def testFont(text, fontSize, boxWidth, boxHeight, pxPerLine, newLine, newPage, beforeCom, afterCom, fromRight,
            lineBox, boxAnimation, lineOffset, offsetWith, offsetCom):
    
    if not FontPath: return
    
    charsinfo = {}
    charmap = TakeFromTable(FontPath, text, fontSize)
    char_height = charmap[list(charmap)[0]][3]
    per = (fontSize * char_height / charmap['tallest'] - char_height) / charmap['tallest']
    for k, v in charmap.items():
        if not isinstance(v, tuple): break
        charsinfo[k] = list(map(lambda x: int(x + (x * per)), v))
    
    linesNum = (boxHeight + pxPerLine) // (fontSize + pxPerLine)
    fittedText = fit(text, charsinfo, boxWidth, linesNum, newLine, newPage, beforeCom, afterCom)
    
    sentences = splitTextByCommands((newPage, newLine), fittedText)
    offsetedText = ''
    
    if lineOffset >= 0:
        if offsetWith == 0:
            for s in range(len(sentences)):
                sentences[s] = OffsetLineWithSpaces(sentences[s], charmap, boxWidth, lineOffset)
        if offsetWith == 1 and offsetCom:
            for s in range(len(sentences)):
                sentences[s] = OffsetLineWithCommands(sentences[s], charmap, boxWidth, lineOffset, offsetCom)
    
    text = sentencesToText(sentences, newLine, newPage, linesNum)
    
    FontTesterWindow.resultTextBox.setPlainText(text)
    
    if not ImgPath and not FontPath.endswith('.ttf'): return
    
    WindowSize = (int(boxWidth + borderThick * 2), int(boxHeight + borderThick * 2))
    pygame.display.set_caption('Font Tester')
    textbox = pygame.display.set_mode(WindowSize)
    
    SetWindowPos = windll.user32.SetWindowPos
    SetWindowPos(pygame.display.get_wm_info()['window'], -1, 500, 500, 0, 0, 0x0001)
    
    type_in_box(sentences, fontSize, per, boxWidth, boxHeight, linesNum, pxPerLine, charmap, newLine, newPage, textbox,
                lineBox, fromRight, boxAnimation)

    while True: pygameCheck(textbox)

def waitForPress(display, wait):
    pressed = False
    while wait:
        pygameCheck(display)
        if keyboard.is_pressed('enter'): pressed = True
        else:
            if pressed: break

def pygameCheck(display):
    for event in pygame.event.get():
        if event.type is pygame.QUIT: pygame.display.set_mode((1, 1), flags = pygame.HIDDEN)
        elif event.type == pygame.KEYDOWN:
            all_keys = pygame.key.get_pressed()
            if not all_keys[pygame.K_LCTRL] or not all_keys[pygame.K_s]: continue
            
            savePath = saveFile(['png'], FontTesterWindow, 'صورة')
            if savePath: pygame.image.save(display, savePath)

def pygameWait(display, waitTime = 0):
    if waitTime: start = time()
    while waitTime:
        if waitTime and time() - start > waitTime: break
        pygameCheck(display)

def loadFile():
    FilePath = openFile(['*'], FontTesterWindow, 'ملف')
    if not FilePath: return
    FontTesterWindow.enteredTextBox.setPlainText(open(FilePath, 'r', encoding='utf8').read())

def openFont():
    global FontPath, ImgPath
    FontPath = openFile(('aft', 'fnt', 'ttf'), FontTesterWindow, 'الخط')
    if FontPath.endswith('.ttf'): return
    ImgPath  = openFile(('jpg', 'png'), FontTesterWindow, 'صورة الخط')

def start():
    fontSize  = tryTakeNum(FontTesterOptionsWindow.fontSizeCell.toPlainText(), 16)
    boxWidth  = tryTakeNum(FontTesterOptionsWindow.boxWidthCell.toPlainText(), 180)
    boxHeight = tryTakeNum(FontTesterOptionsWindow.boxHeightCell.toPlainText(), 60)
    pixelsPer = tryTakeNum(FontTesterOptionsWindow.pixelsPerCell.toPlainText(), 60)
    
    text         = FontTesterWindow.enteredTextBox.toPlainText()
    newLineCom   = FontTesterOptionsWindow.newLineCell.toPlainText()
    newPageCom   = FontTesterOptionsWindow.newPageCell.toPlainText()
    beforeCom    = FontTesterOptionsWindow.beforeComCell.toPlainText()
    afterCom     = FontTesterOptionsWindow.afterComCell.toPlainText()
    offsetCom    = FontTesterOptionsWindow.offsetComCell.toPlainText()
    fromRight    = FontTesterOptionsWindow.fromRightCheck.isChecked()
    lineBox      = FontTesterOptionsWindow.lineBoxCheck.isChecked()
    boxAnimation = FontTesterOptionsWindow.boxAnimationCheck.isChecked()
    
    offset     = FontTesterOptionsWindow.offsetComboBox.currentIndex() -1
    offsetWith = FontTesterOptionsWindow.offsetWithComboBox.currentIndex()
    
    testFont(
        text, fontSize, boxWidth, boxHeight, pixelsPer, newLineCom,
        newPageCom, beforeCom, afterCom, fromRight,
        lineBox, boxAnimation, offset, offsetWith, offsetCom
        )

FontPath, ImgPath = '', ''
borderThick, borderColor = 10, (255, 255, 255)

app = QApplication(argv)
from Parts.Windows import FontTesterWindow, FontTesterOptionsWindow
pygame.init()

FontTesterWindow.fontButton.clicked.connect(lambda: openFont())
FontTesterWindow.startButton.clicked.connect(lambda: start())
FontTesterWindow.openButton.clicked.connect(lambda: loadFile())