from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Parts.Classes import CheckableComboBox

textboxFont = QFont()
textboxFont.setPointSize(10)
labelFont = QFont()
labelFont.setPointSize(9)
perFont = QFont()
perFont.setPointSize(14)

#<-------------------------------------------[النافذة الأم]------------------------------------------->
class StudioMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # version ([rewrite studio].[add new tool].[big update].[small updates and fixes])
        self.setWindowTitle("Asgore Studio 2.0.2.59")
 
        self.mdiArea = QMdiArea()
        self.setCentralWidget(self.mdiArea)
        
        self.createBars()
        self.createMenus()
        self.createActions()
        
        self.importantInfo = ('- للكتابة بالبايتات في الحقول الصغيرة اكتب [b] وبعدها البايتات.\n'
            '(هذا في المدخل وخيارات التحويل فقط) (ولا تضع فراغات)\n'
            '- لا تفتح ملفات الاكسل أثناء تشغيل الأداة.\n'
            '- ترتيب وحذف السطور يعمل لكل صفحة على حدة.\n'
            '- اضغط F3 في محرّر الملفات لإضافة <c>.\n'
            '- اضغط ctrl+B لتحويل النص المحدد.\n'
            '- في منشئ جداول الحروف اضغط F3 لكتابة الحرف التالي وF4 للعودة حرفاً للوراء وF5 للعودة لأول حرف.\n' #
            "- اضغط ctrl+S لالتقاط صورة لمربع الحوار في مجرب الخطوط")
    
    def createBars(self):
        self.bar = self.menuBar()
    
    def createMenus(self):
        self.tools = self.bar.addMenu("الأدوات")
        self.windows = self.bar.addMenu("النوافذ")
    
    def createActions(self):
        self.bar.addAction("معلومات مهمة")
        self.bar.addAction("عني")
        self.windows.addAction("تكبير النوافذ وصفها")
        self.windows.addAction("تصغير النوافذ")
        self.windows.addAction("إغلاق كافة النوافذ")
        self.tools.addAction("جداول آسغور")
        self.tools.addAction("مختزل النصوص")
        self.tools.addAction("محرّر الملفات")
        self.tools.addAction("منشئ جداول الحروف")
        self.tools.addAction("محوّل الجداول")
        self.tools.addAction("محوّل الخطوط")
        self.tools.addAction("مجرب الخطوط")
        self.tools.addAction("إعدادات مجرب الخطوط")
        self.tools.addAction("محوّل النصوص")
        self.tools.addAction("خيارات محوّل النصوص")
        self.tools.addAction("المدخل والمستخرج")

    def newChild(self, widget, container, title):
        if container not in self.mdiArea.subWindowList():
            container.setWindowTitle(title)
            self.mdiArea.addSubWindow(container)
        widget.show()

    def Report(self, title, reportText):
        ReportWindow = QMdiSubWindow()
        ReportWindow.setWindowTitle(title)
        
        text = QTextEdit(ReportWindow)
        text.setPlainText(reportText)
        ReportWindow.setWidget(text)
        
        self.mdiArea.addSubWindow(ReportWindow)
        ReportWindow.show()

StudioWindow = StudioMotherWindow()


#<-------------------------------------------[جداول آسغور]------------------------------------------->
class TableEditorMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ROWS, self.COLS = 1000, 100
        
        TableContainer = QWidget()
        layout = QVBoxLayout()
        
        self.Table = QTableWidget()
        self.Table.setColumnCount(self.COLS)
        self.Table.setRowCount(self.ROWS)

        self.bar = self.menuBar()
        
        file = self.bar.addMenu("ملف")
        options = self.bar.addMenu("خيارات الجدول")
        
        file.addAction("فتح جدول .ate")
        file.addAction("فتح جدول .csv")
        file.addAction("حفظ الجدول كـ .ate")
        file.addAction("حفظ الجدول كـ .csv")
        options.addAction("إضافة صف")
        options.addAction("حذف صف")
        options.addAction("إضافة عمود")
        options.addAction("حذف عمود")
        self.bar.addAction("مسح محتوى الجدول")
        
        layout.addWidget(self.Table)
        TableContainer.setLayout(layout)
        self.setCentralWidget(TableContainer)

TableEditorWindow = TableEditorMotherWindow()


#<-------------------------------------------[مختزل النصوص]------------------------------------------->
class TextAnalyzerMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        container = QWidget()
        layout = QGridLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        logLayout = QVBoxLayout()
        self.logBox = QTextEdit()
        logLabel = QLabel()
        logLabel.setText("   الإحصاءات:")

        boxesLayout = QVBoxLayout()
        self.enteredBox = QTextEdit()
        self.resultBox = QTextEdit()
        self.enteredBox.setPlainText('تجربة الاختزال')

        enteredLabel = QLabel()
        resultLabel = QLabel()
        enteredLabel.setText("   النص الداخل:")
        resultLabel.setText("   النص الناتج:")

        buttonsLayout = QVBoxLayout()
        self.saveLog = QPushButton()
        self.analyzeButton = QPushButton()
        self.openFileButton = QPushButton()
        self.suggestDteButton = QPushButton()
        self.saveLog.setText("حفظ الإحصاءات في ملف")
        self.analyzeButton.setText("اختزال النص")
        self.openFileButton.setText("فتح ملف نص")
        self.suggestDteButton.setText("اقتراح حروف مدمجة")

        varsLayout = QGridLayout()
        minivarsLayout = QGridLayout()
        self.resultsNumCell = QTextEdit()
        self.resultsNumCell.setFixedSize(40, 26)
        self.resultsNumCell.setText("25")
        resultsNumLabel = QLabel()
        resultsNumLabel.setText("عدد النتائج:")
        self.mergedCharLenFromCell = QTextEdit()
        self.mergedCharLenFromCell.setFixedSize(40, 26)
        self.mergedCharLenFromCell.setText("2")
        mergedCharLenFromLabel = QLabel()
        mergedCharLenFromLabel.setText("طول الاختزال المقترح من:")
        self.mergedCharLenToCell = QTextEdit()
        self.mergedCharLenToCell.setFixedSize(40, 26)
        self.mergedCharLenToCell.setText("2")
        mergedCharLenToLabel = QLabel()
        mergedCharLenToLabel.setText("لـ:")
        self.ignoredCharsCell = QTextEdit()
        self.ignoredCharsCell.setFixedSize(255, 30)
        ignoredCharsLabel = QLabel()
        ignoredCharsLabel.setText("الحروف المتجاهلة في الاقتراح:")
        self.ignoredDtesCell = QTextEdit()
        self.ignoredDtesCell.setFixedSize(255, 30)
        ignoredDtesLabel = QLabel()
        ignoredDtesLabel.setText("الاختزالات المتجاهلة:")
        
        layout.addLayout(boxesLayout, 0, 0)
        layout.addLayout(logLayout, 0, 1)
        layout.addLayout(varsLayout, 1, 0)
        layout.addLayout(buttonsLayout, 1, 1)
        buttonsLayout.addWidget(self.openFileButton)
        buttonsLayout.addWidget(self.saveLog)
        buttonsLayout.addWidget(self.analyzeButton)
        buttonsLayout.addWidget(self.suggestDteButton)
        minivarsLayout.addWidget(resultsNumLabel, 0, 0)
        minivarsLayout.addWidget(self.resultsNumCell, 0, 3)
        minivarsLayout.addWidget(mergedCharLenFromLabel, 1, 0)
        minivarsLayout.addWidget(self.mergedCharLenFromCell, 1, 1)
        minivarsLayout.addWidget(mergedCharLenToLabel, 1, 2)
        minivarsLayout.addWidget(self.mergedCharLenToCell, 1, 3)
        varsLayout.addLayout(minivarsLayout, 1, 0)
        varsLayout.addWidget(ignoredCharsLabel, 2, 0)
        varsLayout.addWidget(self.ignoredCharsCell, 3, 0)
        varsLayout.addWidget(ignoredDtesLabel, 4, 0)
        varsLayout.addWidget(self.ignoredDtesCell, 5, 0)
        boxesLayout.addWidget(enteredLabel)
        boxesLayout.addWidget(self.enteredBox)
        boxesLayout.addWidget(resultLabel)
        boxesLayout.addWidget(self.resultBox)
        logLayout.addWidget(logLabel)
        logLayout.addWidget(self.logBox)

TextAnalyzerWindow = TextAnalyzerMotherWindow()


#<-------------------------------------------[منشئ الخطوط موحدة حجم الحروف]------------------------------------------->
class FontsConverterMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        container = QWidget()
        layout = QGridLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.TtfSizeCell = QTextEdit()
        self.TtfSizeCell.setFixedSize(180, 26)
        self.TtfSizeCell.setText('28')
        TtfSizeLabel = QLabel()
        TtfSizeLabel.setText("حجم الخط:")
        self.WidthCell = QTextEdit()
        self.WidthCell.setFixedSize(180, 26)
        self.WidthCell.setText('32')
        WidthLabel = QLabel()
        WidthLabel.setText("عرض خلية الحرف:")
        self.HeightCell = QTextEdit()
        self.HeightCell.setFixedSize(180, 26)
        self.HeightCell.setText('32')
        HeightLabel = QLabel()
        HeightLabel.setText("طول خلية الحرف:")
        self.charsPerRowCell = QTextEdit()
        self.charsPerRowCell.setFixedSize(180, 26)
        self.charsPerRowCell.setText('8')
        charsPerRowLabel = QLabel()
        charsPerRowLabel.setText("عدد الحروف في السطر الواحد:")
        self.beforeFirstColCell = QTextEdit()
        self.beforeFirstColCell.setFixedSize(180, 26)
        self.beforeFirstColCell.setText('0')
        beforeFirstColLabel = QLabel()
        beforeFirstColLabel.setText("المسافة يسار العمود الاول:")
        self.beforeFirstRowCell = QTextEdit()
        self.beforeFirstRowCell.setFixedSize(180, 26)
        self.beforeFirstRowCell.setText('0')
        beforeFirstRowLabel = QLabel()
        beforeFirstRowLabel.setText("المسافة فوق السطر الاول:")
        self.BetweenCharsXCell = QTextEdit()
        self.BetweenCharsXCell.setFixedSize(180, 26)
        self.BetweenCharsXCell.setText('0')
        BetweenCharsXLabel = QLabel()
        BetweenCharsXLabel.setText("المسافة بين كل حرف أفقياً:")
        self.BetweenCharsYCell = QTextEdit()
        self.BetweenCharsYCell.setFixedSize(180, 26)
        self.BetweenCharsYCell.setText('0')
        BetweenCharsYLabel = QLabel()
        BetweenCharsYLabel.setText("المسافة بين كل حرف عمودياً:")
        self.charsCell = QTextEdit()
        self.charsCell.setFixedSize(180, 104)
        charsLabel = QLabel()
        charsLabel.setText("الحروف بالترتيب:")

        self.fromRightCheck = QCheckBox("إزاحة الحروف ليمين الخانة")
        self.smoothCheck = QCheckBox("تنعيم الخط (ttf)")
        self.monoSizedCheck = QCheckBox("توحيد حجم الحروف")

        self.saveButton = QPushButton()
        self.saveButton.setText("حفظ الجدول")
        self.TtfButton = QPushButton()
        self.TtfButton.setText("فتح خط")
        
        layout.addWidget(TtfSizeLabel, 0, 0)
        layout.addWidget(self.TtfSizeCell, 0, 1)
        layout.addWidget(WidthLabel, 1, 0)
        layout.addWidget(self.WidthCell, 1, 1)
        layout.addWidget(HeightLabel, 2, 0)
        layout.addWidget(self.HeightCell, 2, 1)
        layout.addWidget(charsPerRowLabel, 3, 0)
        layout.addWidget(self.charsPerRowCell, 3, 1)
        layout.addWidget(beforeFirstColLabel, 4, 0)
        layout.addWidget(self.beforeFirstColCell, 4, 1)
        layout.addWidget(beforeFirstRowLabel, 5, 0)
        layout.addWidget(self.beforeFirstRowCell, 5, 1)
        layout.addWidget(BetweenCharsXLabel, 6, 0)
        layout.addWidget(self.BetweenCharsXCell, 6, 1)
        layout.addWidget(BetweenCharsYLabel, 7, 0)
        layout.addWidget(self.BetweenCharsYCell, 7, 1)
        layout.addWidget(charsLabel, 8, 0)
        layout.addWidget(self.charsCell, 8, 1)
        layout.addWidget(self.smoothCheck, 9, 0)
        layout.addWidget(self.fromRightCheck, 9, 1)
        layout.addWidget(self.monoSizedCheck, 10, 0)
        layout.addWidget(self.TtfButton, 11, 0)
        layout.addWidget(self.saveButton, 11, 1)

FontsConverterWindow = FontsConverterMotherWindow()


#<-------------------------------------------[محوّل الجداول]------------------------------------------->
class TablesConverterMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        comboboxLayout = QHBoxLayout()
        fromComboBoxOptions = [
            "act",
            "fnt",
            "zts"
        ]
        toComboBoxOptions = [
            "act",
            "aft",
            "zts"
        ]
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(fromComboBoxOptions)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(toComboBoxOptions)

        fromLabel = QLabel()
        fromLabel.setText("حوّل:")
        toLabel = QLabel()
        toLabel.setText("إلى:")
        
        self.convertButton = QPushButton()
        self.convertButton.setText("اختر جدول وحوّله")
        
        comboboxLayout.addWidget(fromLabel)
        comboboxLayout.addWidget(self.fromComboBox)
        comboboxLayout.addWidget(toLabel)
        comboboxLayout.addWidget(self.toComboBox)
        
        layout.addLayout(comboboxLayout)
        layout.addWidget(self.convertButton)

TablesConverterWindow = TablesConverterMotherWindow()


#<-------------------------------------------[منشئ جداول الحروف]------------------------------------------->
class CharsTablesCreatorMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.bar = self.menuBar()
        file = self.bar.addMenu("ملف")

        file.addAction("فتح جدول حروف .tbl")
        file.addAction("فتح جدول حروف .act")
        file.addAction("فتح جدول حروف .csv")
        file.addAction("حفظ جدول الحروف كـ .tbl")
        file.addAction("حفظ جدول الحروف كـ .act")
        file.addAction("حفظ جدول الحروف كـ .csv")
        self.bar.addAction("مسح محتوى الجدول")
        
        container = QWidget()
        
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.Table = QTableWidget()
        self.Table.setColumnCount(16)
        self.Table.setRowCount(16)
        self.Table.setLayoutDirection(Qt.LeftToRight)
        
        charsLayout = QHBoxLayout()
        self.charsCell = QTextEdit()
        self.charsCell.setFixedSize(290, 66)
        charsLabel = QLabel()
        charsLabel.setText("الحروف المراد إدخالها:")
        
        self.nextChar = QLabel()
        self.nextChar.setFont(labelFont)
        self.nextChar.setText("الحرف التالي:")
        
        NUMS = '0123456789ABCDEF'
        self.Table.setHorizontalHeaderLabels(list(NUMS))
        self.Table.setVerticalHeaderLabels(list(NUMS))
        
        for i in range(16):
            self.Table.setRowHeight(i, 28)
            self.Table.setColumnWidth(i, 18)
        
        layout.addWidget(self.Table)
        layout.addLayout(charsLayout)
        charsLayout.addWidget(charsLabel)
        charsLayout.addWidget(self.charsCell)
        charsLayout.addWidget(self.nextChar)

CharsTablesCreatorWindow = CharsTablesCreatorMotherWindow()


#<-------------------------------------------[مجرب الخطوط]------------------------------------------->
class FontTesterMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        container = QWidget()

        layout = QGridLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.enteredTextBox = QTextEdit()
        self.resultTextBox = QTextEdit()
        self.enteredTextBox.setPlainText('تجربة الخط')
        self.enteredTextBox.setFont(textboxFont)
        self.resultTextBox.setFont(textboxFont)

        enteredTextLabel = QLabel()
        resultTextLabel = QLabel()
        enteredTextLabel.setText("   النص الداخل:")
        resultTextLabel.setText("   النص الناتج:")

        minilayout = QGridLayout()
        self.infoButton = QPushButton()
        self.openButton = QPushButton()
        self.fontButton = QPushButton()
        self.startButton = QPushButton()
        self.infoButton.setText("؟")
        self.openButton.setText("فتح ملف")
        self.fontButton.setText("فتح خط")
        self.startButton.setText("بدء")
        self.infoButton.setFixedSize(28, 28)
        
        layout.addWidget(enteredTextLabel, 0, 0)
        layout.addWidget(self.enteredTextBox, 1, 0)
        layout.addWidget(resultTextLabel, 2, 0)
        layout.addWidget(self.resultTextBox, 3, 0)
        layout.addLayout(minilayout, 4, 0)
        minilayout.addWidget(self.infoButton, 0, 0)
        minilayout.addWidget(self.openButton, 0, 1)
        minilayout.addWidget(self.fontButton, 0, 2)
        minilayout.addWidget(self.startButton, 0, 3)

FontTesterWindow = FontTesterMotherWindow()


#<-------------------------------------------[إعدادات مجرب الخطوط]------------------------------------------->
class FontTesterOptionsMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(480, 330)

        labelsWidth, labelsHeight = 145, 26

        self.fontSizeCell = QTextEdit(self)
        self.fontSizeCell.setGeometry(QRect(240, self.y(0), 70, 26))
        self.fontSizeCell.setText("16")
        fontSizeLabel = QLabel(self)
        fontSizeLabel.setGeometry(QRect(320, self.y(0), labelsWidth, labelsHeight))
        fontSizeLabel.setText("حجم الخط:")
        self.boxWidthCell = QTextEdit(self)
        self.boxWidthCell.setGeometry(QRect(240, self.y(1), 70, 26))
        self.boxWidthCell.setText("180")
        boxWidthLabel = QLabel(self)
        boxWidthLabel.setGeometry(QRect(320, self.y(1), labelsWidth, labelsHeight))
        boxWidthLabel.setText("عرض المربع:")
        self.boxHeightCell = QTextEdit(self)
        self.boxHeightCell.setGeometry(QRect(240, self.y(2), 70, 26))
        self.boxHeightCell.setText("60")
        boxHeightLabel = QLabel(self)
        boxHeightLabel.setGeometry(QRect(320, self.y(2), labelsWidth, labelsHeight))
        boxHeightLabel.setText("ارتفاع المربع:")
        self.pixelsPerCell = QTextEdit(self)
        self.pixelsPerCell.setGeometry(QRect(240, self.y(3), 70, 26))
        self.pixelsPerCell.setText("3")
        pixelsPerLabel = QLabel(self)
        pixelsPerLabel.setGeometry(QRect(320, self.y(3), labelsWidth, labelsHeight))
        pixelsPerLabel.setText("البيكسلات بين كل سطر:")
        self.newLineCell = QTextEdit(self)
        self.newLineCell.setGeometry(QRect(240, self.y(4), 70, 26))
        self.newLineCell.setText("<line>")
        newLineLabel = QLabel(self)
        newLineLabel.setGeometry(QRect(320, self.y(4), labelsWidth, labelsHeight))
        newLineLabel.setText("أمر سطر جديد:")
        self.newPageCell = QTextEdit(self)
        self.newPageCell.setGeometry(QRect(240, self.y(5), 70, 26))
        self.newPageCell.setText("<page>")
        newPageLabel = QLabel(self)
        newPageLabel.setGeometry(QRect(320, self.y(5), labelsWidth, labelsHeight))
        newPageLabel.setText("أمر صفحة جديدة:")
        self.beforeComCell = QTextEdit(self)
        self.beforeComCell.setGeometry(QRect(240, self.y(6), 70, 26))
        self.beforeComCell.setText("[")
        beforeComLabel = QLabel(self)
        beforeComLabel.setGeometry(QRect(320, self.y(6), labelsWidth, labelsHeight))
        beforeComLabel.setText("ما قبل الأوامر:")
        self.afterComCell = QTextEdit(self)
        self.afterComCell.setGeometry(QRect(240, self.y(7), 70, 26))
        self.afterComCell.setText("]")
        afterComLabel = QLabel(self)
        afterComLabel.setGeometry(QRect(320, self.y(7), labelsWidth, labelsHeight))
        afterComLabel.setText("ما بعدها:")
        self.offsetComCell = QTextEdit(self)
        self.offsetComCell.setGeometry(QRect(240, self.y(8), 70, 26))
        self.offsetComCell.setText("{(px)}")
        offsetComLabel = QLabel(self)
        offsetComLabel.setGeometry(QRect(320, self.y(8), labelsWidth, labelsHeight))
        offsetComLabel.setText("أمر الإزاحة:")

        offsetComboBoxOptions = [
            "اترك النص على حاله", "النص في البداية واملأ ما بعده", "النص في النهاية واملأ ما قبله",
            "النص في الوسط واملأ ما قبله", "النص في الوسط واملأ ما قبله وبعده"
            ]
        offsetWithComboBoxOptions = ["الفراغات", "الأوامر"]
        
        self.offsetComboBox = QComboBox(self)
        self.offsetComboBox.setGeometry(20, 35, 200, 30)
        self.offsetComboBox.addItems(offsetComboBoxOptions)
        self.offsetComboBox.setInsertPolicy(QComboBox.NoInsert)
        self.offsetWithComboBox = QComboBox(self)
        self.offsetWithComboBox.setGeometry(20, 105, 200, 30)
        self.offsetWithComboBox.addItems(offsetWithComboBoxOptions)
        self.offsetWithComboBox.setInsertPolicy(QComboBox.NoInsert)

        offsetComboBoxLabel = QLabel(self)
        offsetComboBoxLabel.setGeometry(QRect(130, 10, 80, 20))
        offsetComboBoxLabel.setText("إزاحة:")
        offsetWithComboBoxLabel = QLabel(self)
        offsetWithComboBoxLabel.setGeometry(QRect(130, 80, 80, 20))
        offsetWithComboBoxLabel.setText("باستعمال:")

        self.fromRightCheck = QCheckBox("تدفق النص من اليمين", self)
        self.fromRightCheck.setGeometry(QRect(75, 225, 145, 26))
        self.boxAnimationCheck = QCheckBox("أنميشن مربع الحوار", self)
        self.boxAnimationCheck.setGeometry(QRect(75, 250, 145, 26))
        self.lineBoxCheck = QCheckBox("صناديق السطور", self)
        self.lineBoxCheck.setGeometry(QRect(75, 275, 145, 26))
        self.charBoxCheck = QCheckBox("صناديق الحروف", self)
        self.charBoxCheck.setGeometry(QRect(75, 300, 145, 26))
        

    def y(self, num, height = 26, per = 10, first = 20):
        return first + (num * height) + ((num - 1) * per)

FontTesterOptionsWindow = FontTesterOptionsMotherWindow()


#<-------------------------------------------[محرر الملفات]------------------------------------------->
class FilesEditorMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        container = QWidget()
        layout = QGridLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.fileTypeComboBox = QComboBox()
        
        self.textBox = QTextEdit()
        self.textBox.setFont(textboxFont)
        self.translationBox = QTextEdit()
        self.translationBox.setFont(textboxFont)
        
        workLayout = QHBoxLayout()
        self.nextButton = QPushButton()
        self.nextButton.setText(">")
        self.backButton = QPushButton()
        self.backButton.setText("<")
        self.per = QLabel()
        self.per.setFont(perFont)
        
        buttonsLayout = QGridLayout()
        self.textButton = QPushButton()
        self.textButton.setText("فتح جدول ترجمة")
        self.openButton = QPushButton()
        self.openButton.setText("فتح ملف")
        self.saveButton = QPushButton()
        self.saveButton.setText("حفظ الملف")
        self.openTableButton = QPushButton()
        self.openTableButton.setText("نسخ لمحرر الجداول")
        
        convertLayout = QHBoxLayout()
        self.Convertbutton = QPushButton()
        self.Convertbutton.setText("تحويل الترجمة")
        self.ConvertAllbutton = QPushButton()
        self.ConvertAllbutton.setText("تحويل كل الترجمات")
        
        cellsLayout = QGridLayout()
        self.endCommandCell = QTextEdit()
        self.endCommandCell.setFixedSize(120, 26)
        self.endCommandCell.setText("<END>")
        endCommandLabel = QLabel()
        endCommandLabel.setText("أمر نهاية الجملة:")
        self.columnIndexCell = QTextEdit()
        self.columnIndexCell.setFixedSize(120, 26)
        self.columnIndexCell.setText("1")
        columnIndexLabel = QLabel()
        columnIndexLabel.setText("رقم عمود الجدول:")
        
        layout.addWidget(self.fileTypeComboBox, 0, 0)
        layout.addLayout(workLayout, 1, 0)
        layout.addWidget(self.textBox, 2, 0)
        layout.addWidget(self.translationBox, 3, 0)
        layout.addLayout(convertLayout, 4, 0)
        layout.addLayout(cellsLayout, 5, 0)
        layout.addLayout(buttonsLayout, 6, 0)
        buttonsLayout.addWidget(self.openButton, 0, 0)
        buttonsLayout.addWidget(self.textButton, 1, 0)
        buttonsLayout.addWidget(self.saveButton, 0, 1)
        buttonsLayout.addWidget(self.openTableButton, 1, 1)
        convertLayout.addWidget(self.Convertbutton)
        convertLayout.addWidget(self.ConvertAllbutton)
        workLayout.addWidget(self.backButton)
        workLayout.addWidget(self.per)
        workLayout.addWidget(self.nextButton)
        cellsLayout.addWidget(endCommandLabel, 0, 0)
        cellsLayout.addWidget(self.endCommandCell, 0, 1)
        cellsLayout.addWidget(columnIndexLabel, 1, 0)
        cellsLayout.addWidget(self.columnIndexCell, 1, 1)

FilesEditorWindow = FilesEditorMotherWindow()


#<-------------------------------------------[محول النصوص]------------------------------------------->
class TextConverterMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        container = QWidget()

        layout = QGridLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.enteredBox = QTextEdit()
        self.resultBox = QTextEdit()
        self.enteredBox.setPlainText('تجربةُ التّحويلِ')
        self.enteredBox.setFont(textboxFont)
        self.resultBox.setFont(textboxFont)

        enteredLabel = QLabel()
        resultLabel = QLabel()
        enteredLabel.setText("   النص الداخل:")
        resultLabel.setText("   النص الناتج:")

        buttonsLayout = QHBoxLayout()
        self.convertButton = QPushButton()
        self.openFileButton = QPushButton()
        self.ConvertFilesButton = QPushButton()
        self.convertButton.setText("تحويل\nالنص")
        self.openFileButton.setText("فتح ملف\nنص")
        self.ConvertFilesButton.setText("فتح مجلد\nوتحويل ملفاته")

        layout.addWidget(enteredLabel, 0, 0)
        layout.addWidget(self.enteredBox, 1, 0)
        layout.addWidget(resultLabel, 2, 0)
        layout.addWidget(self.resultBox, 3, 0)
        layout.addLayout(buttonsLayout, 4, 0)
        buttonsLayout.addWidget(self.convertButton)
        buttonsLayout.addWidget(self.openFileButton)
        buttonsLayout.addWidget(self.ConvertFilesButton)

TextConverterWindow = TextConverterMotherWindow()


#<-------------------------------------------[خيارات التحويل]------------------------------------------->

class TextConverterOptionsMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        tab1 = QWidget()
        tab2 = QWidget()
        container = QTabWidget()
        
        container.addTab(tab1, 'صفحة 1')
        container.addTab(tab2, 'صفحة 2')

        layout = QGridLayout()
        layout2 = QVBoxLayout()
        tab1.setLayout(layout)
        tab2.setLayout(layout2)
        self.setCentralWidget(container)
        
        OptionsWindow_Width = 400
        checkbox_size = [OptionsWindow_Width-5, 16]
        
        checksLayout = QVBoxLayout()
        self.RA_check = QCheckBox("تجميد النص العربي")
        self.UA_check = QCheckBox("إلغاء تجميد النص العربي")
        self.C_check = QCheckBox("تحويل النص")
        self.UC_check = QCheckBox("إلغاء تحويل النص")
        self.RT_check = QCheckBox("عكس النص كاملاً")
        self.RAO_check = QCheckBox("عكس العربية في النص (تجريبي)")
        self.CB_check = QCheckBox("تحويل البايتات")
        
        harakatLayout = QHBoxLayout()
        HarakatLabel = QLabel()
        HarakatLabel.setFixedSize(55, 26)
        HarakatLabel.setText("الحركات:")
        HarakatOptions = [
            "اتركها كما هي",
            "احذفها",
            "أبقي الأولى عند التتالي",
            "أعدها حرفاً للوراء",
            "قدمها حرفاً للأمام",
            "جمدها مع التطويلة",
            "ادمج الحركات"
        ]
        self.HarakatComboBox = QComboBox()
        self.HarakatComboBox.addItems(HarakatOptions)
        self.HarakatComboBox.setFixedSize(160, 27)
        
        customScriptLayout = QHBoxLayout()
        CustomScriptLabel = QLabel()
        CustomScriptLabel.setFixedSize(55, 26)
        CustomScriptLabel.setText("سكربتات:")
        self.CustomScriptComboBox = CheckableComboBox()
        self.CustomScriptComboBox.setFixedSize(160, 27)
        self.CustomScriptComboBox.AddItems(['تحديث القائمة', '...'])


        self.FixSlashes = QCheckBox(r"مراعاة (n, \r, \t, \0\)")
        self.AutoCopyCheck = QCheckBox("النسخ تلقائيا بعد التحويل")
        
        containerLayout = QVBoxLayout()
        cellsLayout = QGridLayout()
        startComLabel = QLabel()
        startComLabel.setText("قبل الأوامر:")
        self.startCommand = QTextEdit()
        self.startCommand.setFixedSize(90, 26)
        self.startCommand.setText("[")
        endComLabel = QLabel()
        endComLabel.setText("بعدها:")
        self.endCommand = QTextEdit()
        self.endCommand.setFixedSize(90, 26)
        self.endCommand.setText("]")
        pageComLabel = QLabel()
        pageComLabel.setText("أمر صفحة جديدة:")
        self.pageCommand = QTextEdit()
        self.pageCommand.setFixedSize(90, 26)
        self.pageCommand.setText("<page>")
        lineComLabel = QLabel()
        lineComLabel.setText("أمر سطر جديد:")
        self.lineCommand = QTextEdit()
        self.lineCommand.setFixedSize(90, 26)
        self.lineCommand.setText("<line>")
        convertedByteLabel = QLabel()
        convertedByteLabel.setText("صيغة البايت المحول:")
        self.convertedByte = QTextEdit()
        self.convertedByte.setFixedSize(90, 26)
        self.convertedByte.setText(r'\xXY')
        
        self.C_databaseButton = QPushButton()
        self.C_databaseButton.setText("فتح جدول تحويل")
        
        
        self.DDL_check = QCheckBox("حذف أسطر الصفحة المكررة")
        self.SSL_check = QCheckBox("ترتيب أسطر الصفحة تصاعديا")
        self.SLS_check = QCheckBox("ترتيب أسطر الصفحة تنازليا")
        self.RL_check = QCheckBox("عكس ترتيب أسطر الصفحات")
        self.RP_check = QCheckBox("عكس ترتيب الصفحات")
        

        cellsLayout.addWidget(startComLabel, 0, 0)
        cellsLayout.addWidget(self.startCommand, 0, 1)
        cellsLayout.addWidget(endComLabel, 1, 0)
        cellsLayout.addWidget(self.endCommand, 1, 1)
        cellsLayout.addWidget(pageComLabel, 2, 0)
        cellsLayout.addWidget(self.pageCommand, 2, 1)
        cellsLayout.addWidget(lineComLabel, 3, 0)
        cellsLayout.addWidget(self.lineCommand, 3, 1)
        cellsLayout.addWidget(convertedByteLabel, 4, 0)
        cellsLayout.addWidget(self.convertedByte, 4, 1)
        
        harakatLayout.addWidget(HarakatLabel)
        harakatLayout.addWidget(self.HarakatComboBox)
        customScriptLayout.addWidget(CustomScriptLabel)
        customScriptLayout.addWidget(self.CustomScriptComboBox)
        
        checksLayout.addWidget(self.RA_check)
        checksLayout.addWidget(self.UA_check)
        checksLayout.addWidget(self.C_check)
        checksLayout.addWidget(self.UC_check)
        checksLayout.addWidget(self.RT_check)
        checksLayout.addWidget(self.RAO_check)
        checksLayout.addWidget(self.CB_check)
        checksLayout.addLayout(harakatLayout)
        checksLayout.addLayout(customScriptLayout)
        checksLayout.addWidget(self.FixSlashes)
        checksLayout.addWidget(self.AutoCopyCheck)
        
        containerLayout.addLayout(cellsLayout)
        containerLayout.addWidget(self.DDL_check)
        containerLayout.addWidget(self.SSL_check)
        containerLayout.addWidget(self.SLS_check)
        containerLayout.addWidget(self.RL_check)
        containerLayout.addWidget(self.RP_check)
        containerLayout.addWidget(self.C_databaseButton)
        
        layout.addLayout(checksLayout, 0, 0)
        layout.addLayout(containerLayout, 0, 1)
        
        # layout2.addWidget()

TextConverterOptionsWindow = TextConverterOptionsMotherWindow()


#<-------------------------------------------[المدخل والمستخرج]------------------------------------------->
class EnteringMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        container = QWidget()
        
        layout = QGridLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        boxesLayout = QVBoxLayout()
        self.textBox = QTextEdit()
        self.translationBox = QTextEdit()
        self.translationBox.setPlainText('تجربة الإدخال')
        
        textLabel = QLabel()
        translationLabel = QLabel()
        textLabel.setText("   النص الأصلي:")
        translationLabel.setText("   الترجمة:")
        
        buttonsLayout = QHBoxLayout()
        self.enterButton = QPushButton()
        self.enterConvertButton = QPushButton()
        self.extractButton = QPushButton()
        self.enterButton.setText("إدخال")
        self.enterConvertButton.setText("تحويل وإدخال")
        self.extractButton.setText("استخراج")
        
        secondButtonsLayout = QHBoxLayout()
        self.fromFolder = QPushButton()
        self.toFolder = QPushButton()
        self.textTableButton = QPushButton()
        self.fromFolder.setText("مجلد الملفات")
        self.toFolder.setText("مجلد نواتج الإدخال")
        self.textTableButton.setText("فتح جدول نصوص")
        
        varsLayout = QGridLayout()
        self.beforeText = QTextEdit()
        self.beforeText.setFixedSize(80, 26)
        self.afterText = QTextEdit()
        self.afterText.setFixedSize(80, 26)
        self.minText = QTextEdit()
        self.minText.setFixedSize(80, 26)
        self.maxText = QTextEdit()
        self.maxText.setFixedSize(80, 26)
        beforeTextLabel = QLabel()
        beforeTextLabel.setText("ما يسبق النص في الملفات:")
        afterTextLabel = QLabel()
        afterTextLabel.setText("ما يلحقه:")
        minTextLabel = QLabel()
        minTextLabel.setText("أقصى حد لقصر النصوص المستخرجة:")
        maxTextLabel = QLabel()
        maxTextLabel.setText("أقصى حد لطولها:")
        
        OptinsLayout = QVBoxLayout()
        self.databaseCheck = QCheckBox("استخدام جدول النصوص للإدخال.")
        self.asciiCheck = QCheckBox("استخراج الآسكي فقط.")
        self.sortedCheck = QCheckBox("النصوص مرتبة حسب الاستخراج.")
        self.tooLongCheck = QCheckBox("عدم إدخال ترجمات أطول من النص الأصلي. (بقيم الهيكس)")
        self.translationOffsetCheck = QCheckBox("مكان الترجمة في حال كانت أقصر:")
        
        OffsetOptions = [
            "النص أول الجملة واملأ بعده فراغات",
            "النص آخر الجملة واملأ قبله فراغات",
            "النص وسط الجملة واملأ قبله فراغات",
            "النص وسط الجملة واملأ قبله وبعده فراغات"
        ]
        self.Offset = QComboBox()
        self.Offset.addItems(OffsetOptions)
        
        offsetTypeLabel = QLabel()
        offsetTypeLabel.setText("     وفق:")
        
        offsetTypeOptions = [
            "قيم الهيكس",
            "عدد الأحرف"
        ]
        self.OffsetType = QComboBox()
        self.OffsetType.addItems(offsetTypeOptions)
        
        
        layout.addLayout(boxesLayout, 0, 0)
        layout.addLayout(buttonsLayout, 1, 0)
        layout.addLayout(varsLayout, 2, 0)
        layout.addLayout(secondButtonsLayout, 3, 0)
        layout.addLayout(OptinsLayout, 4, 0)
        
        buttonsLayout.addWidget(self.enterButton)
        buttonsLayout.addWidget(self.enterConvertButton)
        buttonsLayout.addWidget(self.extractButton)
        secondButtonsLayout.addWidget(self.fromFolder)
        secondButtonsLayout.addWidget(self.toFolder)
        secondButtonsLayout.addWidget(self.textTableButton)
        varsLayout.addWidget(beforeTextLabel, 0, 0)
        varsLayout.addWidget(afterTextLabel, 1, 0)
        varsLayout.addWidget(minTextLabel, 2, 0)
        varsLayout.addWidget(maxTextLabel, 3, 0)
        varsLayout.addWidget(self.beforeText, 0, 1)
        varsLayout.addWidget(self.afterText, 1, 1)
        varsLayout.addWidget(self.minText, 2, 1)
        varsLayout.addWidget(self.maxText, 3, 1)
        boxesLayout.addWidget(textLabel)
        boxesLayout.addWidget(self.textBox)
        boxesLayout.addWidget(translationLabel)
        boxesLayout.addWidget(self.translationBox)
        OptinsLayout.addWidget(self.databaseCheck)
        OptinsLayout.addWidget(self.asciiCheck)
        OptinsLayout.addWidget(self.sortedCheck)
        OptinsLayout.addWidget(self.tooLongCheck)
        OptinsLayout.addWidget(self.translationOffsetCheck)
        OptinsLayout.addWidget(self.Offset)
        OptinsLayout.addWidget(offsetTypeLabel)
        OptinsLayout.addWidget(self.OffsetType)

EnteringWindow = EnteringMotherWindow()


#<-------------------------------------------[]------------------------------------------->
