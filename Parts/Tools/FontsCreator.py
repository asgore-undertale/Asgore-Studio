from Parts.Scripts.UsefulLittleFunctions import tryTakeNum, saveFile, openFile
from Parts.Scripts.CreateFontTable import CreateFontTable
from Parts.Scripts.DrawFontTable import drawFontTable
from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from os import path

app = QApplication(argv)
from Parts.Windows import FontsCreatorWindow

def saveFont():
    chars = FontsCreatorWindow.charsCell.toPlainText()
    ttfPath = openTtf.ttfPath
    if not chars: return
    
    Width = tryTakeNum(FontsCreatorWindow.WidthCell.toPlainText(), 32)
    Height = tryTakeNum(FontsCreatorWindow.HeightCell.toPlainText(), 32)
    ttfSize = tryTakeNum(FontsCreatorWindow.TtfSizeCell.toPlainText(), 28)
    if not Width or not Height or not ttfSize: return
    
    fromRight = FontsCreatorWindow.fromRightCheck.isChecked()
    isSmooth = (not FontsCreatorWindow.smoothCheck.isChecked()) * 1
    beforeFirstCol = tryTakeNum(FontsCreatorWindow.beforeFirstColCell.toPlainText())
    beforeFirstRow = tryTakeNum(FontsCreatorWindow.beforeFirstRowCell.toPlainText())
    BetweenCharsX = tryTakeNum(FontsCreatorWindow.BetweenCharsXCell.toPlainText())
    BetweenCharsY = tryTakeNum(FontsCreatorWindow.BetweenCharsYCell.toPlainText())
    charsPerRow = tryTakeNum(FontsCreatorWindow.charsPerRowCell.toPlainText(), 8)
    if not charsPerRow: charsPerRow = 1
    
    tableContent = CreateFontTable(
        beforeFirstCol, beforeFirstRow, BetweenCharsX, BetweenCharsY, Width, Height,
        charsPerRow, chars
        )
    
    fontFileSavePath = saveFile(['aft'], FontsCreatorWindow, 'ملف الخط')
    if not fontFileSavePath: return
    with open(fontFileSavePath, 'w', encoding="utf-8") as f:
        f.write(tableContent)
    
    if not ttfPath: return
    imgFileSavePath = saveFile(['png'], FontsCreatorWindow, 'صورة الخط')
    if not path.exists(ttfPath) or not imgFileSavePath: return
    
    charsPerCol = (len(chars) // charsPerRow) # + int((len(chars) % charsPerRow > 0) * '1')
    if len(chars) % charsPerRow: charsPerCol += 1
    imgSize = (beforeFirstCol + BetweenCharsX * (charsPerRow - 1) + Width * charsPerRow , beforeFirstRow + BetweenCharsY * (charsPerCol - 1) + Height * charsPerCol)
    
    drawFontTable(
        fontFileSavePath, chars, Width, Height, imgSize,
        ttfPath, ttfSize, fromRight, isSmooth, imgFileSavePath
    )

def openTtf():
    openTtf.ttfPath = openFile(['ttf'], FontsCreatorWindow, 'ملف خط ttf')
openTtf.ttfPath = ''

FontsCreatorWindow.saveButton.clicked.connect(lambda: saveFont())
FontsCreatorWindow.TtfButton.clicked.connect(lambda: openTtf())

if __name__ == '__main__':
    FontsCreatorWindow.show()
    exit(app.exec_())