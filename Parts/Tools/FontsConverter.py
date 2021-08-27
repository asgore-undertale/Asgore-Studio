from Parts.Scripts.UsefulLittleFunctions import tryTakeNum, saveFile, openFile
from Parts.Scripts.CreateFontTable import CreateFontTable
from Parts.Scripts.DrawFontTable import drawFontTable
from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from os import path

app = QApplication(argv)
from Parts.Windows import FontsConverterWindow

def saveFont():
    chars = FontsConverterWindow.charsCell.toPlainText()
    ttfPath = openTtf.ttfPath
    if not chars: return
    
    Width = tryTakeNum(FontsConverterWindow.WidthCell.toPlainText(), 32)
    Height = tryTakeNum(FontsConverterWindow.HeightCell.toPlainText(), 32)
    ttfSize = tryTakeNum(FontsConverterWindow.TtfSizeCell.toPlainText(), 28)
    if not Width or not Height or not ttfSize: return
    
    fromRight = FontsConverterWindow.fromRightCheck.isChecked()
    isSmooth = (not FontsConverterWindow.smoothCheck.isChecked()) * 1
    beforeFirstCol = tryTakeNum(FontsConverterWindow.beforeFirstColCell.toPlainText())
    beforeFirstRow = tryTakeNum(FontsConverterWindow.beforeFirstRowCell.toPlainText())
    BetweenCharsX = tryTakeNum(FontsConverterWindow.BetweenCharsXCell.toPlainText())
    BetweenCharsY = tryTakeNum(FontsConverterWindow.BetweenCharsYCell.toPlainText())
    charsPerRow = tryTakeNum(FontsConverterWindow.charsPerRowCell.toPlainText(), 8)
    if not charsPerRow: charsPerRow = 1
    
    tableContent = CreateFontTable(
        beforeFirstCol, beforeFirstRow, BetweenCharsX, BetweenCharsY, Width, Height,
        charsPerRow, chars
        )
    
    fontFileSavePath = saveFile(['aft'], FontsConverterWindow, 'ملف الخط')
    if not fontFileSavePath: return
    with open(fontFileSavePath, 'w', encoding="utf-8") as f:
        f.write(tableContent)
    
    if not ttfPath: return
    imgFileSavePath = saveFile(['png'], FontsConverterWindow, 'صورة الخط')
    if not path.exists(ttfPath) or not imgFileSavePath: return
    
    charsPerCol = (len(chars) // charsPerRow)
    if len(chars) % charsPerRow: charsPerCol += 1
    imgSize = (beforeFirstCol + BetweenCharsX * (charsPerRow - 1) + Width * charsPerRow , beforeFirstRow + BetweenCharsY * (charsPerCol - 1) + Height * charsPerCol)
    
    drawFontTable(
        fontFileSavePath, chars, Width, Height, imgSize,
        ttfPath, ttfSize, fromRight, isSmooth, imgFileSavePath
    )

def openTtf():
    openTtf.ttfPath = openFile(['ttf'], FontsConverterWindow, 'ملف خط ttf')
openTtf.ttfPath = ''

FontsConverterWindow.saveButton.clicked.connect(lambda: saveFont())
FontsConverterWindow.TtfButton.clicked.connect(lambda: openTtf())

if __name__ == '__main__':
    FontsConverterWindow.show()
    exit(app.exec_())