from Parts.Scripts.UsefulLittleFunctions import tryTakeNum, saveFile, openFile
from Parts.Scripts.CreateFontTable import CreateAftFontTable
from Parts.Scripts.DrawFontTable import drawFontTable
from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from os import path

def saveFont():
    chars = FontsConverterWindow.charsCell.toPlainText()
    fontPath = openFont.fontPath
    if not chars or not fontPath: return
    
    Width = tryTakeNum(FontsConverterWindow.WidthCell.toPlainText(), 32)
    Height = tryTakeNum(FontsConverterWindow.HeightCell.toPlainText(), 32)
    fontSize = tryTakeNum(FontsConverterWindow.TtfSizeCell.toPlainText(), 28)
    if not Width or not Height or not fontSize: return
    
    fromRight = FontsConverterWindow.fromRightCheck.isChecked()
    isSmooth = (not FontsConverterWindow.smoothCheck.isChecked()) * 1
    monoSized = FontsConverterWindow.monoSizedCheck.isChecked()
    beforeFirstCol = tryTakeNum(FontsConverterWindow.beforeFirstColCell.toPlainText())
    beforeFirstRow = tryTakeNum(FontsConverterWindow.beforeFirstRowCell.toPlainText())
    BetweenCharsX = tryTakeNum(FontsConverterWindow.BetweenCharsXCell.toPlainText())
    BetweenCharsY = tryTakeNum(FontsConverterWindow.BetweenCharsYCell.toPlainText())
    charsPerRow = tryTakeNum(FontsConverterWindow.charsPerRowCell.toPlainText(), 8)
    if not charsPerRow: charsPerRow = 1
    
    tableContent = CreateAftFontTable(
        beforeFirstCol, beforeFirstRow, BetweenCharsX, BetweenCharsY, Width, Height,
        charsPerRow, chars, fontPath, fontSize, monoSized, fromRight
        )
    
    fontFileSavePath = saveFile(['aft'], FontsConverterWindow, 'ملف الخط')
    if not fontFileSavePath: return
    with open(fontFileSavePath, 'w', encoding="utf-8") as f:
        f.write(tableContent)
    
    if not fontPath: return
    imgFileSavePath = saveFile(['png'], FontsConverterWindow, 'صورة الخط')
    if not path.exists(fontPath) or not imgFileSavePath: return
    
    charsPerCol = (len(chars) // charsPerRow) + (((len(chars) % charsPerRow) > 0) * 1)
    imgSize = (beforeFirstCol + BetweenCharsX * (charsPerRow - 1) + Width * charsPerRow , beforeFirstRow + BetweenCharsY * (charsPerCol - 1) + Height * charsPerCol)
    
    drawFontTable(
        fontFileSavePath, chars, Width, Height, imgSize,
        fontPath, fontSize, isSmooth, imgFileSavePath
    )

def openFont():
    openFont.fontPath = openFile(['ttf', 'aff'], FontsConverterWindow, 'ملف خط ttf')
openFont.fontPath = ''


app = QApplication(argv)
from Parts.Windows import FontsConverterWindow

FontsConverterWindow.saveButton.clicked.connect(lambda: saveFont())
FontsConverterWindow.TtfButton.clicked.connect(lambda: openFont())

if __name__ == '__main__':
    FontsConverterWindow.show()
    exit(app.exec_())