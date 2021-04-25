from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel, QFileDialog, QMessageBox
from PyQt5.QtCore import QRect
from Parts.Scripts.CreateFontTable import CreateFontTable
from sys import argv, exit

def save():
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
    
    _file, _ = QFileDialog.getSaveFileName(FontsTablesCreatorWindow, 'جدول الحروف', '' , '*.ate')
    if _file == '/' or not _file: return
    
    open(_file, 'w', encoding="utf-8").write(tableContent)
    QMessageBox.about(FontsTablesCreatorWindow, "!!تهانينا", "تم حفظ الجدول.")


app = QApplication(argv)

FontsTablesCreatorWindow = QMainWindow()
FontsTablesCreatorWindow.setFixedSize(380, 350)

labelsWidth, labelsHeight = 200, 26

def y(num, height = 26, per = 10, first = 20):
    return first + (num * height) + ((num - 1) * per)

WidthCell = QTextEdit(FontsTablesCreatorWindow)
WidthCell.setGeometry(QRect(10, y(0), 180, 26))
WidthLabel = QLabel(FontsTablesCreatorWindow)
WidthLabel.setGeometry(QRect(170, y(0), labelsWidth, labelsHeight))
WidthLabel.setText("عرض الحروف الموحد:")
HeightCell = QTextEdit(FontsTablesCreatorWindow)
HeightCell.setGeometry(QRect(10, y(1), 180, 26))
HeightLabel = QLabel(FontsTablesCreatorWindow)
HeightLabel.setGeometry(QRect(170, y(1), labelsWidth, labelsHeight))
HeightLabel.setText("طول الحروف الموحد:")
charsPerRowCell = QTextEdit(FontsTablesCreatorWindow)
charsPerRowCell.setGeometry(QRect(10, y(2), 180, 26))
charsPerRowLabel = QLabel(FontsTablesCreatorWindow)
charsPerRowLabel.setGeometry(QRect(170, y(2), labelsWidth, labelsHeight))
charsPerRowLabel.setText("عدد الحروف في السطر الواحد:")
beforeFirstColCell = QTextEdit(FontsTablesCreatorWindow)
beforeFirstColCell.setGeometry(QRect(10, y(3), 180, 26))
beforeFirstColLabel = QLabel(FontsTablesCreatorWindow)
beforeFirstColLabel.setGeometry(QRect(170, y(3), labelsWidth, labelsHeight))
beforeFirstColLabel.setText("المسافة يسار العمود الاول:")
beforeFirstRowCell = QTextEdit(FontsTablesCreatorWindow)
beforeFirstRowCell.setGeometry(QRect(10, y(4), 180, 26))
beforeFirstRowLabel = QLabel(FontsTablesCreatorWindow)
beforeFirstRowLabel.setGeometry(QRect(170, y(4), labelsWidth, labelsHeight))
beforeFirstRowLabel.setText("المسافة فوق السطر الاول:")
BetweenCharsXCell = QTextEdit(FontsTablesCreatorWindow)
BetweenCharsXCell.setGeometry(QRect(10, y(5), 180, 26))
BetweenCharsXLabel = QLabel(FontsTablesCreatorWindow)
BetweenCharsXLabel.setGeometry(QRect(170, y(5), labelsWidth, labelsHeight))
BetweenCharsXLabel.setText("المسافة بين كل حرف أفقياً:")
BetweenCharsYCell = QTextEdit(FontsTablesCreatorWindow)
BetweenCharsYCell.setGeometry(QRect(10, y(6), 180, 26))
BetweenCharsYLabel = QLabel(FontsTablesCreatorWindow)
BetweenCharsYLabel.setGeometry(QRect(170, y(6), labelsWidth, labelsHeight))
BetweenCharsYLabel.setText("المسافة بين كل حرف عمودياً:")
charsCell = QTextEdit(FontsTablesCreatorWindow)
charsCell.setGeometry(QRect(10, y(7), 180, 80))
charsLabel = QLabel(FontsTablesCreatorWindow)
charsLabel.setGeometry(QRect(170, y(7), labelsWidth, labelsHeight))
charsLabel.setText("الحروف (بالترتيب من اليسار لليمين):")

save_button = QPushButton(FontsTablesCreatorWindow)
save_button.setGeometry(QRect(260, 300, 70, 40))
save_button.setText("حفظ الجدول")

save_button.clicked.connect(lambda: save())

if __name__ == '__main__':
    FontsTablesCreatorWindow.show()
    exit(app.exec_())