from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
        self.setWindowTitle("Asgore Studio 2.014v")
 
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
        self.tools.addAction("منشئ الخطوط الموحدة حجم الحروف")
        self.tools.addAction("محوّل الجداول")
        self.tools.addAction("منشئ جداول الحروف")
        self.tools.addAction("مجرب الخطوط")
        self.tools.addAction("إعدادات مجرب الخطوط")
        self.tools.addAction("محرّر الملفات")
        self.tools.addAction("محوّل النصوص")
        self.tools.addAction("خيارات محوّل النصوص")
        self.tools.addAction("المدخل والمستخرج")

    def newChild(self, widget, container, title):
        if container not in self.mdiArea.subWindowList():
            container.setWindowTitle(title)
            self.mdiArea.addSubWindow(container)
        widget.show()

    def AddReportWindow(self, title, reportText):
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
        
        self.ROWS, self.COLS = 100, 40
        
        TableContainer = QWidget()
        layout = QVBoxLayout()

        # self.TableContainer.setWindowTitle(f"Asgore Tables {_ATE_VERSION_}v")
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
        self.resultsNumCell = QTextEdit()
        self.resultsNumCell.setFixedSize(90, 26)
        self.resultsNumCell.setText("25")
        resultsNumLabel = QLabel()
        resultsNumLabel.setText("عدد النتائج:")
        self.mergedCharLenCell = QTextEdit()
        self.mergedCharLenCell.setFixedSize(90, 26)
        self.mergedCharLenCell.setText("2")
        mergedCharLenLabel = QLabel()
        mergedCharLenLabel.setText("طول الحرف المدمج المقترح:")
        self.ignoredCharsCell = QTextEdit()
        self.ignoredCharsCell.setFixedSize(90, 26)
        ignoredCharsLabel = QLabel()
        ignoredCharsLabel.setText("الحروف المراد تجاهلها في الاقتراح:")
        
        self.ignoreDefault = QCheckBox(r'تجاهل: (n, \r\)')
        
        layout.addLayout(boxesLayout, 0, 0)
        layout.addLayout(logLayout, 0, 1)
        layout.addLayout(varsLayout, 1, 0)
        layout.addLayout(buttonsLayout, 1, 1)
        buttonsLayout.addWidget(self.openFileButton)
        buttonsLayout.addWidget(self.saveLog)
        buttonsLayout.addWidget(self.analyzeButton)
        buttonsLayout.addWidget(self.suggestDteButton)
        varsLayout.addWidget(resultsNumLabel, 0, 0)
        varsLayout.addWidget(self.resultsNumCell, 0, 1)
        varsLayout.addWidget(mergedCharLenLabel, 1, 0)
        varsLayout.addWidget(self.mergedCharLenCell, 1, 1)
        varsLayout.addWidget(ignoredCharsLabel, 2, 0)
        varsLayout.addWidget(self.ignoredCharsCell, 2, 1)
        varsLayout.addWidget(self.ignoreDefault, 3, 0)
        boxesLayout.addWidget(enteredLabel)
        boxesLayout.addWidget(self.enteredBox)
        boxesLayout.addWidget(resultLabel)
        boxesLayout.addWidget(self.resultBox)
        logLayout.addWidget(logLabel)
        logLayout.addWidget(self.logBox)

TextAnalyzerWindow = TextAnalyzerMotherWindow()


#<-------------------------------------------[منشئ الخطوط موحدة حجم الحروف]------------------------------------------->
class FontsCreatorMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(360, 460)

        labelsWidth, labelsHeight = 180, 26

        self.TtfSizeCell = QTextEdit(self)
        self.TtfSizeCell.setGeometry(QRect(10, self.y(0), 180, 26))
        self.TtfSizeCell.setText('28')
        TtfSizeLabel = QLabel(self)
        TtfSizeLabel.setGeometry(QRect(170, self.y(0), labelsWidth, labelsHeight))
        TtfSizeLabel.setText("حجم خط ttf:")
        self.WidthCell = QTextEdit(self)
        self.WidthCell.setGeometry(QRect(10, self.y(1), 180, 26))
        self.WidthCell.setText('32')
        WidthLabel = QLabel(self)
        WidthLabel.setGeometry(QRect(170, self.y(1), labelsWidth, labelsHeight))
        WidthLabel.setText("عرض الحروف الموحد:")
        self.HeightCell = QTextEdit(self)
        self.HeightCell.setGeometry(QRect(10, self.y(2), 180, 26))
        self.HeightCell.setText('32')
        HeightLabel = QLabel(self)
        HeightLabel.setGeometry(QRect(170, self.y(2), labelsWidth, labelsHeight))
        HeightLabel.setText("طول الحروف الموحد:")
        self.charsPerRowCell = QTextEdit(self)
        self.charsPerRowCell.setGeometry(QRect(10, self.y(3), 180, 26))
        self.charsPerRowCell.setText('8')
        charsPerRowLabel = QLabel(self)
        charsPerRowLabel.setGeometry(QRect(170, self.y(3), labelsWidth, labelsHeight))
        charsPerRowLabel.setText("عدد الحروف في السطر الواحد:")
        self.beforeFirstColCell = QTextEdit(self)
        self.beforeFirstColCell.setGeometry(QRect(10, self.y(4), 180, 26))
        self.beforeFirstColCell.setText('0')
        beforeFirstColLabel = QLabel(self)
        beforeFirstColLabel.setGeometry(QRect(170, self.y(4), labelsWidth, labelsHeight))
        beforeFirstColLabel.setText("المسافة يسار العمود الاول:")
        self.beforeFirstRowCell = QTextEdit(self)
        self.beforeFirstRowCell.setGeometry(QRect(10, self.y(5), 180, 26))
        self.beforeFirstRowCell.setText('0')
        beforeFirstRowLabel = QLabel(self)
        beforeFirstRowLabel.setGeometry(QRect(170, self.y(5), labelsWidth, labelsHeight))
        beforeFirstRowLabel.setText("المسافة فوق السطر الاول:")
        self.BetweenCharsXCell = QTextEdit(self)
        self.BetweenCharsXCell.setGeometry(QRect(10, self.y(6), 180, 26))
        self.BetweenCharsXCell.setText('0')
        BetweenCharsXLabel = QLabel(self)
        BetweenCharsXLabel.setGeometry(QRect(170, self.y(6), labelsWidth, labelsHeight))
        BetweenCharsXLabel.setText("المسافة بين كل حرف أفقياً:")
        self.BetweenCharsYCell = QTextEdit(self)
        self.BetweenCharsYCell.setGeometry(QRect(10, self.y(7), 180, 26))
        self.BetweenCharsYCell.setText('0')
        BetweenCharsYLabel = QLabel(self)
        BetweenCharsYLabel.setGeometry(QRect(170, self.y(7), labelsWidth, labelsHeight))
        BetweenCharsYLabel.setText("المسافة بين كل حرف عمودياً:")
        self.charsCell = QTextEdit(self)
        self.charsCell.setGeometry(QRect(10, self.y(8), 180, 80))
        charsLabel = QLabel(self)
        charsLabel.setGeometry(QRect(170, self.y(8), labelsWidth, labelsHeight))
        charsLabel.setText("الحروف بالترتيب:")

        self.fromRightCheck = QCheckBox("إزاحة الحروف ليمين الخانة", self)
        self.fromRightCheck.setGeometry(QRect(30, self.y(10.5), 150, 26))
        self.smoothCheck = QCheckBox("نعومة الخط", self)
        self.smoothCheck.setGeometry(QRect(190, self.y(10.5), 150, 26))

        self.saveButton = QPushButton(self)
        self.saveButton.setGeometry(QRect(180, self.y(11.5), 170, 30))
        self.saveButton.setText("حفظ الجدول")
        self.TtfButton = QPushButton(self)
        self.TtfButton.setGeometry(QRect(10, self.y(11.5), 170, 30))
        self.TtfButton.setText("فتح خط ttf")

    def y(self, num, height = 26, per = 10, first = 20):
        return first + (num * height) + ((num - 1) * per)

FontsCreatorWindow = FontsCreatorMotherWindow()


#<-------------------------------------------[محوّل الجداول]------------------------------------------->
class TablesConverterMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(170, 75)
        
        self.convertButton = QPushButton(self)
        self.convertButton.setGeometry(QRect(10, 45, 150, 25))
        self.convertButton.setText("اختر جدول وحوّله")

        comboLineWidth = 120
        y = 10

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
        self.fromComboBox = QComboBox(self)
        self.fromComboBox.addItems(fromComboBoxOptions)
        self.fromComboBox.setGeometry(QRect(comboLineWidth-35, y, 40, 25))
        self.toComboBox = QComboBox(self)
        self.toComboBox.addItems(toComboBoxOptions)
        self.toComboBox.setGeometry(QRect(comboLineWidth-110, y, 40, 25))

        fromLabel = QLabel(self)
        fromLabel.setGeometry(QRect(comboLineWidth, y, 40, 25))
        fromLabel.setText("تحويل:")
        toLabel = QLabel(self)
        toLabel.setGeometry(QRect(comboLineWidth-75, y, 30, 25))
        toLabel.setText("إلى:")

TablesConverterWindow = TablesConverterMotherWindow()


#<-------------------------------------------[منشئ جداول الحروف]------------------------------------------->
class CharsTablesCreatorMotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(517, 570)
        self.setWindowTitle("CharsTablesCreator")

        self.Table = QTableWidget(self)
        self.Table.setColumnCount(16)
        self.Table.setRowCount(16)
        self.Table.setGeometry(QRect(0, 20, 516, 475))

        self.bar = self.menuBar()
        file = self.bar.addMenu("ملف")

        file.addAction("فتح جدول حروف .tbl")
        file.addAction("فتح جدول حروف .act")
        file.addAction("فتح جدول حروف .csv")
        file.addAction("حفظ جدول الحروف كـ .tbl")
        file.addAction("حفظ جدول الحروف كـ .act")
        file.addAction("حفظ جدول الحروف كـ .csv")
        self.bar.addAction("مسح محتوى الجدول")

        self.nextChar = QLabel(self)
        self.nextChar.setGeometry(QRect(5, 490, 90, 40))
        self.nextChar.setFont(labelFont)

        self.charsCell = QTextEdit(self)
        self.charsCell.setGeometry(QRect(110, 500, 290, 66))
        charsLabel = QLabel(self)
        charsLabel.setGeometry(QRect(380, 500, 130, 26))
        charsLabel.setText("الحروف المراد إدخالها:")

        NUMS = '0123456789ABCDEF'
        self.Table.setHorizontalHeaderLabels(list(NUMS))
        self.Table.setVerticalHeaderLabels(list(NUMS))
        
        for i in range(16):
            self.Table.setRowHeight(i, 28)
            self.Table.setColumnWidth(i, 20)
        
        self.nextChar.setText("الحرف التالي:")

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
        self.startButton = QPushButton()
        self.fontButton = QPushButton()
        self.openButton = QPushButton()
        self.startButton.setText("بدء")
        self.fontButton.setText("فتح خط")
        self.openButton.setText("فتح ملف")

        layout.addWidget(enteredTextLabel, 0, 0)
        layout.addWidget(self.enteredTextBox, 1, 0)
        layout.addWidget(resultTextLabel, 2, 0)
        layout.addWidget(self.resultTextBox, 3, 0)
        layout.addLayout(minilayout, 4, 0)
        minilayout.addWidget(self.startButton, 0, 2)
        minilayout.addWidget(self.fontButton, 0, 1)
        minilayout.addWidget(self.openButton, 0, 0)

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
        self.fromRightCheck.setGeometry(QRect(75, 250, 145, 26))
        self.boxAnimationCheck = QCheckBox("أنميشن مربع الحوار", self)
        self.boxAnimationCheck.setGeometry(QRect(75, 275, 145, 26))
        self.lineBoxCheck = QCheckBox("صناديق الأسطر", self)
        self.lineBoxCheck.setGeometry(QRect(75, 300, 145, 26))
        

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
        
        fileTypeComboBoxOptions = [
            "ملف زيلدا نفس البرية msyt.",
            "ملف نص مستخرج من الكروبتار"
        ]
        self.fileTypeComboBox = QComboBox()
        self.fileTypeComboBox.addItems(fileTypeComboBoxOptions)
        
        self.textBox = QTextEdit()
        self.textBox.setFont(textboxFont)
        self.translationBox = QTextEdit()
        self.translationBox.setFont(textboxFont)
        
        buttonsLayout = QHBoxLayout()
        self.textButton = QPushButton()
        self.textButton.setText("جدول نصوص")
        self.openButton = QPushButton()
        self.openButton.setText("فتح ملف")
        self.saveButton = QPushButton()
        self.saveButton.setText("حفظ الملف")
        
        workLayout = QHBoxLayout()
        self.nextButton = QPushButton()
        self.nextButton.setText(">")
        self.backButton = QPushButton()
        self.backButton.setText("<")
        self.per = QLabel()
        self.per.setFont(perFont)
        
        self.Convertbutton = QPushButton()
        self.Convertbutton.setText("تحويل الترجمة")
        self.ConvertAllbutton = QPushButton()
        self.ConvertAllbutton.setText("تحويل كل الترجمات")
        
        cellsLayout = QHBoxLayout()
        self.endCommandCell = QTextEdit()
        self.endCommandCell.setFixedSize(120, 26)
        self.endCommandCell.setText("<END>")
        endCommandLabel = QLabel()
        endCommandLabel.setText("أمر نهاية الجملة:")
        
        layout.addWidget(self.fileTypeComboBox, 0, 0)
        layout.addLayout(workLayout, 1, 0)
        layout.addWidget(self.textBox, 2, 0)
        layout.addWidget(self.translationBox, 3, 0)
        layout.addLayout(buttonsLayout, 4, 0)
        layout.addWidget(self.Convertbutton, 5, 0)
        layout.addWidget(self.ConvertAllbutton, 6, 0)
        layout.addLayout(cellsLayout, 7, 0)
        buttonsLayout.addWidget(self.openButton)
        buttonsLayout.addWidget(self.saveButton)
        buttonsLayout.addWidget(self.textButton)
        workLayout.addWidget(self.backButton)
        workLayout.addWidget(self.per)
        workLayout.addWidget(self.nextButton)
        cellsLayout.addWidget(endCommandLabel)
        cellsLayout.addWidget(self.endCommandCell)

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
        
        container.addTab(tab1, 'التحويل')
        container.addTab(tab2, 'الأسطر والصفحات')

        layout = QGridLayout()
        layout2 = QVBoxLayout()
        tab1.setLayout(layout)
        tab2.setLayout(layout2)
        self.setCentralWidget(container)
        
        OptionsWindow_Width = 400
        checkbox_size = [OptionsWindow_Width-5, 16]
        
        self.DDL_check = QCheckBox("حذف أسطر الصفحة المكررة")
        self.SSL_check = QCheckBox("ترتيب أسطر الصفحة من الأقصر للأطول")
        self.SLS_check = QCheckBox("ترتيب أسطر الصفحة من الأطول للأقصر")
        self.RP_check = QCheckBox("عكس ترتيب الصفحات")
        self.RL_check = QCheckBox("عكس ترتيب أسطر الصفحات")
        
        checksLayout = QVBoxLayout()
        self.RA_check = QCheckBox("تجميد النص العربي")
        self.UA_check = QCheckBox("إلغاء تجميد النص العربي")
        self.C_check = QCheckBox("تحويل النص")
        self.UC_check = QCheckBox("إلغاء تحويل النص")
        self.RT_check = QCheckBox("عكس النص كاملاً")
        self.RAO_check = QCheckBox("عكس العربية في النص")
        self.Ext_check = QCheckBox("استخرج من النص")
        self.CB_check = QCheckBox("تحويل البايتات")
        
        comboBoxLayout = QHBoxLayout()
        HarakatLabel = QLabel(self)
        HarakatLabel.setGeometry(QRect(240, 350, 150, 26))
        HarakatLabel.setText("الحركات:")
        HarakatOptions = [
            "اتركها كما هي",
            "احذفها",
            "أبقي الأولى في حالة التتالي",
            "أعدها حرفاً للوراء",
            "قدمها حرفاً للأمام",
            "حولها لشكلها مع التطويلة"
        ]
        self.HarakatComboBox = QComboBox(self)
        self.HarakatComboBox.setGeometry(QRect(195, 350, 145, 26))
        self.HarakatComboBox.addItems(HarakatOptions)
        self.HarakatComboBox.setFixedSize(160, 27)

        self.EnglishOnlyCheck = QCheckBox("استخراج الانكليزية فقط")
        self.FixSlashes = QCheckBox(r"مراعاة (n, \r, \t, \0\)")
        self.AutoCopyCheck = QCheckBox("النسخ تلقائية بعد التحويل")
        
        
        containerLayout = QVBoxLayout()
        cellsLayout = QGridLayout()
        startComLabel = QLabel(self)
        startComLabel.setText("قبل الأوامر:")
        self.startCommand = QTextEdit(self)
        self.startCommand.setFixedSize(90, 26)
        self.startCommand.setText("[")
        endComLabel = QLabel(self)
        endComLabel.setText("بعدها:")
        self.endCommand = QTextEdit(self)
        self.endCommand.setFixedSize(90, 26)
        self.endCommand.setText("]")
        pageComLabel = QLabel(self)
        pageComLabel.setText("أمر صفحة جديدة:")
        self.pageCommand = QTextEdit(self)
        self.pageCommand.setFixedSize(90, 26)
        self.pageCommand.setText("<page>")
        lineComLabel = QLabel(self)
        lineComLabel.setText("أمر سطر جديد:")
        self.lineCommand = QTextEdit(self)
        self.lineCommand.setFixedSize(90, 26)
        self.lineCommand.setText("<line>")
        beforeTextLabel = QLabel(self)
        beforeTextLabel.setText("ما قبل النصوص:")
        self.beforeText = QTextEdit(self)
        self.beforeText.setFixedSize(90, 26)
        afterTextLabel = QLabel(self)
        afterTextLabel.setText("ما بعدها:")
        self.afterText = QTextEdit(self)
        self.afterText.setFixedSize(90, 26)
        miniTextLabel = QLabel(self)
        miniTextLabel.setText("أقصى حد لقصرها:")
        self.miniText = QTextEdit(self)
        self.miniText.setFixedSize(90, 26)
        maxTextLabel = QLabel(self)
        maxTextLabel.setText("أقصى حد لطولها:")
        self.maxText = QTextEdit(self)
        self.maxText.setFixedSize(90, 26)
        convertedByteLabel = QLabel(self)
        convertedByteLabel.setText("صيغة البايت المحول:")
        self.convertedByte = QTextEdit(self)
        self.convertedByte.setFixedSize(90, 26)
        self.convertedByte.setText(r'\xXY')

        self.C_databaseButton = QPushButton(self)
        self.C_databaseButton.setText("فتح جدول تحويل")
        
        
        cellsLayout.addWidget(startComLabel, 0, 0)
        cellsLayout.addWidget(self.startCommand, 0, 1)
        cellsLayout.addWidget(endComLabel, 1, 0)
        cellsLayout.addWidget(self.endCommand, 1, 1)
        cellsLayout.addWidget(pageComLabel, 2, 0)
        cellsLayout.addWidget(self.pageCommand, 2, 1)
        cellsLayout.addWidget(lineComLabel, 3, 0)
        cellsLayout.addWidget(self.lineCommand, 3, 1)
        cellsLayout.addWidget(beforeTextLabel, 4, 0)
        cellsLayout.addWidget(self.beforeText, 4, 1)
        cellsLayout.addWidget(afterTextLabel, 5, 0)
        cellsLayout.addWidget(self.afterText, 5, 1)
        cellsLayout.addWidget(miniTextLabel, 6, 0)
        cellsLayout.addWidget(self.miniText, 6, 1)
        cellsLayout.addWidget(maxTextLabel, 7, 0)
        cellsLayout.addWidget(self.maxText, 7, 1)
        cellsLayout.addWidget(convertedByteLabel, 8, 0)
        cellsLayout.addWidget(self.convertedByte, 8, 1)
        comboBoxLayout.addWidget(HarakatLabel)
        comboBoxLayout.addWidget(self.HarakatComboBox)
        checksLayout.addWidget(self.RA_check)
        checksLayout.addWidget(self.UA_check)
        checksLayout.addWidget(self.C_check)
        checksLayout.addWidget(self.UC_check)
        checksLayout.addWidget(self.RT_check)
        checksLayout.addWidget(self.RAO_check)
        checksLayout.addWidget(self.Ext_check)
        checksLayout.addWidget(self.CB_check)
        checksLayout.addLayout(comboBoxLayout)
        checksLayout.addWidget(self.EnglishOnlyCheck)
        checksLayout.addWidget(self.FixSlashes)
        checksLayout.addWidget(self.AutoCopyCheck)
        containerLayout.addLayout(cellsLayout)
        containerLayout.addWidget(self.C_databaseButton)
        layout.addLayout(checksLayout, 0, 0)
        layout.addLayout(containerLayout, 0, 1)
        
        layout2.addWidget(self.DDL_check)
        layout2.addWidget(self.SSL_check)
        layout2.addWidget(self.SLS_check)
        layout2.addWidget(self.RP_check)
        layout2.addWidget(self.RL_check)

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
        
        secondButtonsLayout = QGridLayout()
        self.fromFolder = QPushButton()
        self.toFolder = QPushButton()
        self.textTableButton = QPushButton()
        self.extractTableButton = QPushButton()
        self.fromFolder.setText("المجلد الحاوي للملفات")
        self.toFolder.setText("مجلد الملفات بعد الإدخال")
        self.textTableButton.setText("فتح جدول النصوص")
        self.extractTableButton.setText("فتح جدول الاستخراج")
        
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
        maxTextLabel.setText("وطولها:")
        
        OptinsLayout = QVBoxLayout()
        self.databaseCheck = QCheckBox("استخدام قاعدة بيانات النصوص للإدخال.")
        self.tooLongCheck = QCheckBox("عدم إدخال ترجمات أطول من النص الأصلي. (بقيم الهيكس)")
        self.translationOffsetCheck = QCheckBox("مكان الترجمة في حال كانت أقصر: (بقيم الهيكس)")
        
        OffsetOptions = [
            "النص أول الجملة واملأ بعده فراغات",
            "النص آخر الجملة واملأ قبله فراغات",
            "النص وسط الجملة واملأ قبله وبعده فراغات"
        ]
        self.Offset = QComboBox()
        self.Offset.addItems(OffsetOptions)
        
        
        layout.addLayout(boxesLayout, 0, 0)
        layout.addLayout(buttonsLayout, 1, 0)
        layout.addLayout(varsLayout, 2, 0)
        layout.addLayout(secondButtonsLayout, 3, 0)
        layout.addLayout(OptinsLayout, 4, 0)
        
        buttonsLayout.addWidget(self.enterButton)
        buttonsLayout.addWidget(self.enterConvertButton)
        buttonsLayout.addWidget(self.extractButton)
        secondButtonsLayout.addWidget(self.fromFolder, 0, 0)
        secondButtonsLayout.addWidget(self.toFolder, 0, 1)
        secondButtonsLayout.addWidget(self.textTableButton, 1, 0)
        secondButtonsLayout.addWidget(self.extractTableButton, 1, 1)
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
        OptinsLayout.addWidget(self.tooLongCheck)
        OptinsLayout.addWidget(self.translationOffsetCheck)
        OptinsLayout.addWidget(self.Offset)

EnteringWindow = EnteringMotherWindow()


#<-------------------------------------------[]------------------------------------------->