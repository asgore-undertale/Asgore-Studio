from Parts.Scripts.UsefulLittleFunctions import saveFile, openFile
from Parts.Scripts.CreateFontTable import CreateAftFontTable
from Parts.Scripts.DrawFontTable import drawFontTable
from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from os import path

def saveFont():
    chars = FontsConverterWindow.charsCell.getValue()
    fontPath = openFont.fontPath
    if not chars or not fontPath: return
    
    Width = FontsConverterWindow.WidthCell.getValue()
    Height = FontsConverterWindow.HeightCell.getValue()
    fontSize = FontsConverterWindow.TtfSizeCell.getValue()
    if not Width or not Height or not fontSize: return
    
    fromRight = FontsConverterWindow.fromRightCheck.isChecked()
    isSmooth = (not FontsConverterWindow.smoothCheck.isChecked()) * 1
    monoSized = FontsConverterWindow.monoSizedCheck.isChecked()
    beforeFirstCol = FontsConverterWindow.beforeFirstColCell.getValue()
    beforeFirstRow = FontsConverterWindow.beforeFirstRowCell.getValue()
    BetweenCharsX = FontsConverterWindow.BetweenCharsXCell.getValue()
    BetweenCharsY = FontsConverterWindow.BetweenCharsYCell.getValue()
    charsPerRow = FontsConverterWindow.charsPerRowCell.getValue()
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
    imgSize = (beforeFirstCol + BetweenCharsX * (((charsPerRow * (charsPerCol > 1)) + (len(chars) * (charsPerCol == 1))) - 1) + (Width * ((charsPerRow * (charsPerCol > 1)) + (len(chars) * (charsPerCol == 1)))),
        beforeFirstRow + BetweenCharsY * (charsPerCol - 1) + Height * charsPerCol)
    
    drawFontTable(
        fontFileSavePath, chars, Width, Height, imgSize,
        fontPath, fontSize, isSmooth, fromRight, monoSized, imgFileSavePath
    )

def openFont():
    Path = openFile(['ttf', 'aff'], FontsConverterWindow, 'ملف خط ttf')
    if not Path: return
    openFont.fontPath = Path
openFont.fontPath = ''


app = QApplication(argv)
from Parts.Windows import FontsConverterWindow

FontsConverterWindow.saveButton.clicked.connect(lambda: saveFont())
FontsConverterWindow.TtfButton.clicked.connect(lambda: openFont())

if __name__ == '__main__':
    FontsConverterWindow.show()
    exit(app.exec_())