from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel, QFileDialog, QMessageBox, QCheckBox
from PyQt5.QtCore import QRect, Qt
from Parts.Scripts.CreateFontTable import CreateFontTable
from Parts.Scripts.drawFontTable import drawFontTable
from sys import argv, exit

def save():
    if fromRightCheck.isChecked(): fromRight = True
    else: fromRight = False
    if smoothCheck.isChecked(): smooth = 0
    else: smooth = 1
    if TtfSizeCell.toPlainText(): ttfSize = int(float(TtfSizeCell.toPlainText()))
    else: ttfSize = 28
    if beforeFirstColCell.toPlainText(): beforeFirstCol = int(float(beforeFirstColCell.toPlainText()))
    else: beforeFirstCol = 0
    if beforeFirstRowCell.toPlainText(): beforeFirstRow = int(float(beforeFirstRowCell.toPlainText()))
    else: beforeFirstRow = 0
    if BetweenCharsXCell.toPlainText(): BetweenCharsX = int(float(BetweenCharsXCell.toPlainText()))
    else: BetweenCharsX = 0
    if BetweenCharsYCell.toPlainText(): BetweenCharsY = int(float(BetweenCharsYCell.toPlainText()))
    else: BetweenCharsY = 0
    if WidthCell.toPlainText(): Width = int(float(WidthCell.toPlainText()))
    else: Width = 0
    if HeightCell.toPlainText(): Height = int(float(HeightCell.toPlainText()))
    else: Height = 0
    if charsPerRowCell.toPlainText(): charsPerRow = int(float(charsPerRowCell.toPlainText()))
    else: charsPerRow = 0
    
    tableContent = CreateFontTable(beforeFirstCol, beforeFirstRow, BetweenCharsX, BetweenCharsY, Width, Height, charsPerRow, charsCell.toPlainText())
    
    _file, _ = QFileDialog.getSaveFileName(FontsCreatorWindow, 'جدول الخط', '' , '*.ate')
    if _file == '/' or not _file: return
    open(_file, 'w', encoding="utf-8").write(tableContent)
    
    if TtfNameCell.toPlainText():
        _file2, _ = QFileDialog.getSaveFileName(FontsCreatorWindow, 'صورة الخط', '' , '*.png')
        if _file2 == '/' or not _file2: return
        open(_file2, 'w', encoding="utf-8").write(tableContent)
        
        charsPerCol = len(charsCell.toPlainText()) // charsPerRow
        if len(charsCell.toPlainText()) % charsPerRow: charsPerCol += 1
        imgSize = (beforeFirstCol + BetweenCharsX * (charsPerRow - 1) + Width * charsPerRow , beforeFirstRow + BetweenCharsY * (charsPerCol - 1) + Height * charsPerCol)
        drawFontTable(_file, charsCell.toPlainText(), Width, Height, imgSize, TtfNameCell.toPlainText(), ttfSize, fromRight, smooth, _file2)
    
    QMessageBox.about(FontsCreatorWindow, "!!تهانينا", "تم حفظ الخط.")


app = QApplication(argv)

FontsCreatorWindow = QMainWindow()
FontsCreatorWindow.setFixedSize(380, 460)

labelsWidth, labelsHeight = 200, 26

def y(num, height = 26, per = 10, first = 20):
    return first + (num * height) + ((num - 1) * per)

TtfNameCell = QTextEdit(FontsCreatorWindow)
TtfNameCell.setGeometry(QRect(10, y(0), 180, 26))
TtfNameLabel = QLabel(FontsCreatorWindow)
TtfNameLabel.setGeometry(QRect(170, y(0), labelsWidth, labelsHeight))
TtfNameLabel.setText("اسم خط ttf:")
TtfSizeCell = QTextEdit(FontsCreatorWindow)
TtfSizeCell.setGeometry(QRect(10, y(1), 180, 26))
TtfSizeLabel = QLabel(FontsCreatorWindow)
TtfSizeLabel.setGeometry(QRect(170, y(1), labelsWidth, labelsHeight))
TtfSizeLabel.setText("حجم خط ttf:")
WidthCell = QTextEdit(FontsCreatorWindow)
WidthCell.setGeometry(QRect(10, y(2), 180, 26))
WidthLabel = QLabel(FontsCreatorWindow)
WidthLabel.setGeometry(QRect(170, y(2), labelsWidth, labelsHeight))
WidthLabel.setText("عرض الحروف الموحد:")
HeightCell = QTextEdit(FontsCreatorWindow)
HeightCell.setGeometry(QRect(10, y(3), 180, 26))
HeightLabel = QLabel(FontsCreatorWindow)
HeightLabel.setGeometry(QRect(170, y(3), labelsWidth, labelsHeight))
HeightLabel.setText("طول الحروف الموحد:")
charsPerRowCell = QTextEdit(FontsCreatorWindow)
charsPerRowCell.setGeometry(QRect(10, y(4), 180, 26))
charsPerRowLabel = QLabel(FontsCreatorWindow)
charsPerRowLabel.setGeometry(QRect(170, y(4), labelsWidth, labelsHeight))
charsPerRowLabel.setText("عدد الحروف في السطر الواحد:")
beforeFirstColCell = QTextEdit(FontsCreatorWindow)
beforeFirstColCell.setGeometry(QRect(10, y(5), 180, 26))
beforeFirstColLabel = QLabel(FontsCreatorWindow)
beforeFirstColLabel.setGeometry(QRect(170, y(5), labelsWidth, labelsHeight))
beforeFirstColLabel.setText("المسافة يسار العمود الاول:")
beforeFirstRowCell = QTextEdit(FontsCreatorWindow)
beforeFirstRowCell.setGeometry(QRect(10, y(6), 180, 26))
beforeFirstRowLabel = QLabel(FontsCreatorWindow)
beforeFirstRowLabel.setGeometry(QRect(170, y(6), labelsWidth, labelsHeight))
beforeFirstRowLabel.setText("المسافة فوق السطر الاول:")
BetweenCharsXCell = QTextEdit(FontsCreatorWindow)
BetweenCharsXCell.setGeometry(QRect(10, y(7), 180, 26))
BetweenCharsXLabel = QLabel(FontsCreatorWindow)
BetweenCharsXLabel.setGeometry(QRect(170, y(7), labelsWidth, labelsHeight))
BetweenCharsXLabel.setText("المسافة بين كل حرف أفقياً:")
BetweenCharsYCell = QTextEdit(FontsCreatorWindow)
BetweenCharsYCell.setGeometry(QRect(10, y(8), 180, 26))
BetweenCharsYLabel = QLabel(FontsCreatorWindow)
BetweenCharsYLabel.setGeometry(QRect(170, y(8), labelsWidth, labelsHeight))
BetweenCharsYLabel.setText("المسافة بين كل حرف عمودياً:")
fromRightCheck = QCheckBox("إزاحة الحروف ليمين الخانة", FontsCreatorWindow)
fromRightCheck.setGeometry(QRect(10, y(9), 180, 26))
fromRightCheck.setLayoutDirection(Qt.RightToLeft)
smoothCheck = QCheckBox("نعومة الخط", FontsCreatorWindow)
smoothCheck.setGeometry(QRect(190, y(9), 180, 26))
smoothCheck.setLayoutDirection(Qt.RightToLeft)
charsCell = QTextEdit(FontsCreatorWindow)
charsCell.setGeometry(QRect(10, y(10), 180, 80))
charsLabel = QLabel(FontsCreatorWindow)
charsLabel.setGeometry(QRect(170, y(10), labelsWidth, labelsHeight))
charsLabel.setText("الحروف (بالترتيب من اليسار لليمين):")

save_button = QPushButton(FontsCreatorWindow)
save_button.setGeometry(QRect(260, 410, 70, 40))
save_button.setText("حفظ الجدول")

save_button.clicked.connect(lambda: save())

if __name__ == '__main__':
    FontsCreatorWindow.show()
    exit(app.exec_())