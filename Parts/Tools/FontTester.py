from PyQt5.QtWidgets import QApplication
from Parts.Windows import FontTesterWindow, FontTesterOptionsWindow, StudioWindow
from Parts.Classes.DialogBox import DialogBox
from Parts.Scripts.UsefulLittleFunctions import openFile, Split
from Parts.Scripts.LineOffset import *
from Parts.Scripts.TakeFromTable import TakeFromTable
from Parts.Scripts.ExtractFromText import Extract
from Parts.Scripts.FitInBox import fit
# from Parts.Scripts.EmbedPygameInPyqt5 import embed
from sys import argv
from os import path
import keyboard, pygame, random

app = QApplication(argv)
pygame.init()

def testFont(text, fontSize, boxWidth, boxHeight, borderS, pxPerLine, newLine, newPage, beforeCom, afterCom, RTL,
            showBoxes, boxAnimation, lineOffset, offsetWith, offsetCom):
    
    if not path.exists(FontPath) or not boxWidth or not boxHeight or not fontSize: return
    
    charmap = TakeFromTable(FontPath, text, fontSize)
    per = fontSize / charmap['tallest']
    
    linesNum = (boxHeight + pxPerLine) // (fontSize + pxPerLine)
    fittedText = fit(text, multiCharmapbyPer(charmap, per), boxWidth, linesNum, newLine, newPage, beforeCom, afterCom)
    
    Pages = [Split(i, newLine) for i in Split(fittedText, newPage)]
    
    if lineOffset >= 0:
        offsetedText = ''
        for p in range(len(Pages)):
            for l in range(len(Pages[p])):
                if offsetWith == 0:
                    Pages[p][l] = OffsetLineWithSpaces(Pages[p][l], charmap, boxWidth, lineOffset)
                if offsetWith == 1 and offsetCom:
                    Pages[p][l] = OffsetLineWithCommands(Pages[p][l], charmap, boxWidth, lineOffset, offsetCom)
        
                offsetedText += Pages[p][l]
    else:
        offsetedText = fittedText
    
    FontTesterWindow.resultTextBox.setPlainText(offsetedText)
    
    if not ImgPath and (not FontPath.endswith('.ttf') or FontPath.endswith('.aff')): return
    
    textbox = openWin(boxWidth + (borderS * 2), boxHeight + (borderS * 2))
    
    dialogbox = DialogBox(textbox, 0, 0, boxWidth, boxHeight, pxPerLine, [0, (255, 255, 255)], borderS, 'enter', 0.01, (255, 255, 255),
        FontPath, fontSize, ImgPath, charmap, RTL, showBoxes)
    dialogbox.write(Pages)

    while True: dialogbox.pygameCheck(textbox)

def multiCharmapbyPer(charmap, per):
    dict = {}
    for k, v in charmap.items():
        if not isinstance(v, tuple): continue # for 'tallest' var
        dict[k] = list(map(lambda x: int(x * per), v[0:7])) # [0:7] for 'drawdata'
    return dict

def openWin(boxWidth, boxHeight):
    WindowSize = (boxWidth, boxHeight)
    pygame.display.set_caption('Font Tester')
    return pygame.display.set_mode(WindowSize)

def fixMsytList(textList):
    for i in range(len(textList)):
        if textList[i][0] == '"' and textList[i][-1] == '"': textList[i] = textList[i][1:-1]
    return textList

def loadMsyt(fileContent):
    textList = []
    parts = fileContent.split('\n    contents:\n')
    for part in parts[1:len(parts)]:
        extractedList = Extract(part, '      - text: ', '\n')
        textList.append(''.join(fixMsytList(extractedList)))
    fileContent = '\n'.join(textList)
    
    linesNum = 3
    fontSize = FontTesterOptionsWindow.fontSizeCell.getValue()
    pixelsPerLine = FontTesterOptionsWindow.pixelsPerCell.getValue()
    
    FontTesterOptionsWindow.fontSizeCell.setValue(fontSize)
    FontTesterOptionsWindow.pixelsPerCell.setValue(pixelsPerLine)
    FontTesterOptionsWindow.boxWidthCell.setValue(50 * fontSize)
    FontTesterOptionsWindow.boxHeightCell.setValue((fontSize * linesNum) + (pixelsPerLine * (linesNum - 1)))
    FontTesterOptionsWindow.newLineCell.setValue('\\n')
    FontTesterOptionsWindow.newPageCell.setValue('\n')
    
    return fileContent

def loadFile():
    FilePath = openFile(['*'], FontTesterWindow, 'ملف')
    if not FilePath: return
    fileContent = open(FilePath, 'r', encoding='utf8', errors='replace').read()
    
    if FilePath.endswith('.msyt'):
        fileContent = loadMsyt(fileContent)
    
    FontTesterWindow.enteredTextBox.setPlainText(fileContent)

def openFont():
    global FontPath, ImgPath
    _fontPath = openFile(('aft', 'fnt', 'ttf', 'aff'), FontTesterWindow, 'الخط')
    if _fontPath: FontPath = _fontPath
    
    if FontPath.endswith('.ttf') or FontPath.endswith('.aff'): return
    
    _imgPath = openFile(('jpg', 'png'), FontTesterWindow, 'صورة الخط')
    if _imgPath: ImgPath = _imgPath

def start():
    fontSize = FontTesterOptionsWindow.fontSizeCell.getValue()
    boxWidth = FontTesterOptionsWindow.boxWidthCell.getValue()
    boxHeight = FontTesterOptionsWindow.boxHeightCell.getValue()
    pixelsPer = FontTesterOptionsWindow.pixelsPerCell.getValue()
    
    text = FontTesterWindow.enteredTextBox.toPlainText()
    newLineCom = FontTesterOptionsWindow.newLineCell.getValue()
    newPageCom = FontTesterOptionsWindow.newPageCell.getValue()
    beforeCom = FontTesterOptionsWindow.beforeComCell.getValue()
    afterCom = FontTesterOptionsWindow.afterComCell.getValue()
    offsetCom = FontTesterOptionsWindow.offsetComCell.getValue()
    RTL = FontTesterOptionsWindow.fromRightCheck.isChecked()
    showBoxes = FontTesterOptionsWindow.BoxesCheck.isChecked()
    
    offset = FontTesterOptionsWindow.offsetComboBox.currentIndex() -1
    offsetWith = FontTesterOptionsWindow.offsetWithComboBox.currentIndex()
    
    testFont(
        text, fontSize, boxWidth, boxHeight, 10, pixelsPer, newLineCom,
        newPageCom, beforeCom, afterCom, RTL,
        showBoxes, False, offset, offsetWith, offsetCom
        )

FontPath = r'OtherFiles\Fonts\AftFont.aft' * path.exists(r'OtherFiles\Fonts\AftFont.aft')
ImgPath = r'OtherFiles\Fonts\AftFont.png' * path.exists(r'OtherFiles\Fonts\AftFont.png')

FontTesterWindow.fontButton.clicked.connect(lambda: openFont())
FontTesterWindow.startButton.clicked.connect(lambda: start())
FontTesterWindow.openButton.clicked.connect(lambda: loadFile())
FontTesterWindow.infoButton.clicked.connect(
    lambda: StudioWindow.Report('أوامر مجرب الخطوط', open('Parts/TextFiles/FontTester commands.txt', 'r', encoding='utf-8', errors='replace').read())
    )