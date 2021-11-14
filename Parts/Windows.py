from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Parts.Classes.UI import *

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
        # version ([rewrite studio].[updates].[fixes])
        self.setWindowTitle("Asgore Studio 2.07.79")
 
        self.mdiArea = QMdiArea()
        self.setCentralWidget(self.mdiArea)
        
        self.createBars()
        self.createMenus()
        self.createActions()
        
        self.importantInfo = open('Parts/TextFiles/Important Info.txt', 'r', encoding='utf-8', errors='replace').read()
    
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
        self.tools.addAction("تشغيل سكربت خارجي")

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
        file.addAction("فتح جدول .tbl")
        file.addAction("حفظ الجدول كـ .ate")
        file.addAction("حفظ الجدول كـ .csv")
        file.addAction("حفظ الجدول كـ .tbl")
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
        logLabel = QLabel("   الإحصاءات:")

        boxesLayout = QVBoxLayout()
        self.enteredBox = QTextEdit()
        self.resultBox = QTextEdit()
        self.enteredBox.setPlainText('تجربة الاختزال')

        enteredLabel = QLabel("   النص الداخل:")
        resultLabel = QLabel("   النص الناتج:")
        
        buttonsLayout = QVBoxLayout()
        self.saveLog = QPushButton("حفظ الإحصاءات في ملف")
        self.analyzeButton = QPushButton("اختزال النص")
        self.openFileButton = QPushButton("فتح ملف نص")
        self.suggestDteButton = QPushButton("اقتراح حروف مدمجة")

        varsLayout = QGridLayout()
        minivarsLayout = QGridLayout()
        self.resultsNumCell = AdvancedCell(40, 26, 25)
        resultsNumLabel = QLabel("عدد النتائج:")
        self.mergedCharLenFromCell = AdvancedCell(40, 26, 2)
        mergedCharLenFromLabel = QLabel("طول الاختزال المقترح من:")
        self.mergedCharLenToCell = AdvancedCell(40, 26, 2)
        mergedCharLenToLabel = QLabel("لـ:")
        self.ignoredCharsCell = AdvancedCell(255, 30, "")
        ignoredCharsLabel = QLabel("الحروف المتجاهلة في الاقتراح:")
        self.ignoredDtesCell = AdvancedCell(255, 30, "")
        ignoredDtesLabel = QLabel("الاختزالات المتجاهلة:")
        
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
        
        self.TtfSizeCell = AdvancedCell(180, 26, 28)
        TtfSizeLabel = QLabel("حجم الخط:")
        self.WidthCell = AdvancedCell(180, 26, 32)
        WidthLabel = QLabel("عرض خلية الحرف:")
        self.HeightCell = AdvancedCell(180, 26, 32)
        HeightLabel = QLabel("طول خلية الحرف:")
        self.charsPerRowCell = AdvancedCell(180, 26, 8)
        charsPerRowLabel = QLabel("عدد الحروف في السطر الواحد:")
        self.beforeFirstColCell = AdvancedCell(180, 26)
        beforeFirstColLabel = QLabel("المسافة يسار العمود الاول:")
        self.beforeFirstRowCell = AdvancedCell(180, 26)
        beforeFirstRowLabel = QLabel("المسافة فوق السطر الاول:")
        self.BetweenCharsXCell = AdvancedCell(180, 26)
        BetweenCharsXLabel = QLabel("المسافة بين كل حرف أفقياً:")
        self.BetweenCharsYCell = AdvancedCell(180, 26)
        BetweenCharsYLabel = QLabel("المسافة بين كل حرف عمودياً:")
        self.charsCell = AdvancedCell(180, 104, "")
        charsLabel = QLabel("الحروف بالترتيب:")

        self.fromRightCheck = QCheckBox("إزاحة الحروف ليمين الخانة")
        self.smoothCheck = QCheckBox("تنعيم الخط (ttf)")
        self.monoSizedCheck = QCheckBox("توحيد حجم الحروف")

        self.saveButton = QPushButton("حفظ الجدول")
        self.TtfButton = QPushButton("فتح خط")
        
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

        fromLabel = QLabel("حوّل:")
        toLabel = QLabel("إلى:")
        
        self.convertButton = QPushButton("اختر جدول وحوّله")
        
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
        self.charsCell = AdvancedCell(290, 66, "")
        charsLabel = QLabel("الحروف المراد إدخالها:")
        
        self.nextChar = QLabel("الحرف التالي:")
        self.nextChar.setFont(labelFont)
        
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

        enteredTextLabel = QLabel("   النص الداخل:")
        resultTextLabel = QLabel("   النص الناتج:")

        minilayout = QGridLayout()
        self.infoButton = QPushButton("؟")
        self.openButton = QPushButton("فتح ملف")
        self.fontButton = QPushButton("فتح خط")
        self.startButton = QPushButton("بدء")
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
        
        container = QWidget()

        layout = QVHBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        cellsLayout = QGridLayout()
        self.fontSizeCell = AdvancedCell(80, 26, 24)
        fontSizeLabel = QLabel("حجم الخط:")
        self.boxWidthCell = AdvancedCell(80, 26, 360)
        boxWidthLabel = QLabel("عرض المربع:")
        self.boxHeightCell = AdvancedCell(80, 26, 120)
        boxHeightLabel = QLabel("ارتفاع المربع:")
        self.pixelsPerCell = AdvancedCell(80, 26, 3)
        pixelsPerLabel = QLabel("البيكسلات بين السطور:")
        self.newLineCell = AdvancedCell(80, 26, "<line>")
        newLineLabel = QLabel("أمر السطر:")
        self.newPageCell = AdvancedCell(80, 26, "<page>")
        newPageLabel = QLabel("أمر الصفحة:")
        self.beforeComCell = AdvancedCell(80, 26, "[")
        beforeComLabel = QLabel("قبل الأوامر:")
        self.afterComCell = AdvancedCell(80, 26, "]")
        afterComLabel = QLabel("بعدها:")
        self.offsetComCell = AdvancedCell(80, 26, "{(px)}")
        offsetComLabel = QLabel("أمر الإزاحة:")
        
        optionsLayout = QVBoxLayout()
        offsetComboBoxOptions = [
            "اترك النص على حاله", "النص في البداية واملأ ما بعده", "النص في النهاية واملأ ما قبله",
            "النص في الوسط واملأ ما قبله", "النص في الوسط واملأ ما قبله وبعده"
            ]
        offsetWithComboBoxOptions = ["الفراغات", "الأوامر"]
        
        offsetComboBoxLabel = QLabel("إزاحة:")
        self.offsetComboBox = QComboBox()
        self.offsetComboBox.setFixedSize(240, 30)
        self.offsetComboBox.addItems(offsetComboBoxOptions)
        self.offsetComboBox.setInsertPolicy(QComboBox.NoInsert)
        offsetWithComboBoxLabel = QLabel("باستعمال:")
        self.offsetWithComboBox = QComboBox()
        self.offsetWithComboBox.setFixedSize(240, 30)
        self.offsetWithComboBox.addItems(offsetWithComboBoxOptions)
        self.offsetWithComboBox.setInsertPolicy(QComboBox.NoInsert)
        
        self.fromRightCheck = QCheckBox("تدفق النص من اليمين")
        self.BoxesCheck = QCheckBox("صناديق الحدود")
        
        
        layoutItemsGrid = [
            [fontSizeLabel, self.fontSizeCell],
            [pixelsPerLabel, self.pixelsPerCell],
            [boxWidthLabel, self.boxWidthCell, boxHeightLabel, self.boxHeightCell],
            [newLineLabel, self.newLineCell, newPageLabel, self.newPageCell],
            [beforeComLabel, self.beforeComCell, afterComLabel, self.afterComCell],
            [offsetComboBoxLabel, self.offsetComboBox],
            [offsetWithComboBoxLabel, self.offsetWithComboBox],
            [self.fromRightCheck, self.BoxesCheck]
            ]
        
        layout.addwidgetsGrid(layoutItemsGrid)

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
        self.nextButton = QPushButton(">")
        self.backButton = QPushButton("<")
        self.per = QLabel()
        self.per.setFont(perFont)
        
        buttonsLayout = QGridLayout()
        self.textButton = QPushButton("فتح جدول ترجمة")
        self.openButton = QPushButton("فتح ملف")
        self.saveButton = QPushButton("حفظ الملف")
        self.openTableButton = QPushButton("نسخ لمحرر الجداول")
        
        convertLayout = QHBoxLayout()
        self.Convertbutton = QPushButton("تحويل الترجمة")
        self.ConvertAllbutton = QPushButton("تحويل كل الترجمات")
        
        cellsLayout = QGridLayout()
        self.endCommandCell = AdvancedCell(120, 26, "<END>")
        endCommandLabel = QLabel("أمر نهاية الجملة:")
        self.columnIndexCell = AdvancedCell(120, 26, 1)
        columnIndexLabel = QLabel("رقم عمود الجدول:")
        
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

        enteredLabel = QLabel("   النص الداخل:")
        resultLabel = QLabel("   النص الناتج:")

        buttonsLayout = QHBoxLayout()
        self.convertButton = QPushButton("تحويل\nالنص")
        self.openFileButton = QPushButton("فتح ملف\nنص")
        self.ConvertFilesButton = QPushButton("فتح مجلد\nوتحويل ملفاته")

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
        
        container = QTabWidget()
        charsConverter = QWidget()
        hexConverter = QWidget()
        pagesAndLines = QWidget()
        advancedOptions = QWidget()
        
        container.addTab(charsConverter, 'تحويل الحروف')
        container.addTab(hexConverter, 'يونيكود')
        container.addTab(pagesAndLines, 'الأسطر والصفحات')
        container.addTab(advancedOptions, 'آخر')

        charsConverterLayout = QVHBoxLayout()
        hexConverterLayout = QVHBoxLayout()
        pagesAndLinesLayout = QVHBoxLayout()
        advancedOptionsLayout = QVBoxLayout()
        
        self.setCentralWidget(container)
        charsConverter.setLayout(charsConverterLayout)
        hexConverter.setLayout(hexConverterLayout)
        pagesAndLines.setLayout(pagesAndLinesLayout)
        advancedOptions.setLayout(advancedOptionsLayout)
        
        # -->
        
        OptionsWindow_Width = 400
        checkbox_size = [OptionsWindow_Width-5, 16]
        
        self.RA_check = QCheckBox("تجميد النص العربي")
        self.UA_check = QCheckBox("إلغاء تجميد النص العربي")
        self.C_check = QCheckBox("تحويل النص")
        self.UC_check = QCheckBox("إلغاء تحويل النص")
        self.RT_check = QCheckBox("عكس النص كاملاً")
        self.RAO_check = QCheckBox("عكس العربية في النص")
        
        HarakatLabel = QLabel("الحركات:")
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
        self.HarakatComboBox.setFixedSize(240, 27)
        
        CustomScriptLabel = QLabel("سكربتات:")
        self.CustomScriptComboBox = CheckableComboBox()
        self.CustomScriptComboBox.setFixedSize(240, 27)
        self.CustomScriptComboBox.AddItems(['تحديث القائمة', '...'])
        
        startComLabel = QLabel("تجاهل ما بعد:")
        self.startCommand = AdvancedCell(90, 26, "[")
        endComLabel = QLabel("و قبل:")
        self.endCommand = AdvancedCell(90, 26, "]")
        
        self.C_databaseButton = QPushButton("فتح جدول تحويل")
        
        # -->
        
        pageComLabel = QLabel("أمر الصفحة قبل التحويل:")
        self.pageCommand = AdvancedCell(90, 26, "<page>")
        lineComLabel = QLabel("أمر السطر قبل التحويل:")
        self.lineCommand = AdvancedCell(90, 26, "<line>")
        newpageComLabel = QLabel("أمر الصفحة بعد التحويل:")
        self.newpageCommand = AdvancedCell(90, 26, self.pageCommand.getValue())
        newlineComLabel = QLabel("أمر السطر بعد التحويل:")
        self.newlineCommand = AdvancedCell(90, 26, self.lineCommand.getValue())
        
        self.DDL_check = QCheckBox("حذف أسطر الصفحة المكررة")
        self.RL_check = QCheckBox("عكس ترتيب الأسطر")
        self.RP_check = QCheckBox("عكس ترتيب الصفحات")
        
        sortLabel = QLabel("ترتيب السطور:")
        sortOptions = [
            "اتركها على حالها",
            "من الأقصر للأطول",
            "من الأطول للأقصر",
            "أبجدياً"
        ]
        self.sortComboBox = QComboBox()
        self.sortComboBox.addItems(sortOptions)
        self.sortComboBox.setFixedSize(240, 27)
        
        # -->
        
        self.FixSlashes = QCheckBox("تغيير (n, \\r, \\t, \\0\\)\nلأشكالهاغير الطباعية")
        self.UseTable = QCheckBox("استعمال تيبل المستخدم")
        # self.UseTable.setCheckState(Qt.Checked)
        
        byte_1_Label = QLabel("تعبير البايت -1-:")
        self.byte_1 = AdvancedCell(90, 26, '\\xX')
        byte_2_Label = QLabel(":-2-")
        self.byte_2 = AdvancedCell(90, 26, '{$X}')
        readByteLengthLabel = QLabel("طول البايت المقروء:")
        self.readByteLength = AdvancedCell(42, 26, 1, 1, 1)
        self.readByteLength2 = AdvancedCell(41, 26, 2, 1, 2)
        resultByteLengthLabel = QLabel("طول البايت المستخرج:")
        self.resultByteLength = AdvancedCell(90, 26, 1)
        placeHolderLabel = QLabel("الرمز الافتراضي: (لما ينقص من التيبل)")
        self.placeHolder = AdvancedCell(90, 26, '?')
        
        unicodeLabel = QLabel("تحويل البايت:")
        unicodeOptions = [
            "عدم التحويل",
            "تحويل من التعبير 1 لـ 2",
            "تحويل من التعبير 1 للأشكال الطباعية",
            "تحويل من الأشكال الطباعية للتعبير 2",
            "تحويل من يونيكود للأشكال الطباعية",
            "تحويل من الأشكال الطباعية ليونيكود"
        ]
        self.unicodeComboBox = QComboBox()
        self.unicodeComboBox.addItems(unicodeOptions)
        self.unicodeComboBox.setFixedSize(240, 27)
        
        self.bytesTableButton = QPushButton("فتح تيبل هيكس")
        
        # -->
        
        self.AutoCopyCheck = QCheckBox("النسخ تلقائياً بعد التحويل")
        self.AutoConvertCheck = QCheckBox("التحويل تلقائياً عند الكتابة")
        
        # -----------------------------------
        
        ConvertItemsGrid = [
            [self.RA_check, self.UA_check],
            [self.C_check, self.UC_check],
            [self.RT_check, self.RAO_check],
            [HarakatLabel, self.HarakatComboBox],
            [CustomScriptLabel, self.CustomScriptComboBox],
            [startComLabel, self.startCommand, endComLabel, self.endCommand],
            [self.C_databaseButton]
            ]
        
        charsConverterLayout.addwidgetsGrid(ConvertItemsGrid)
        
        # -->
        
        pagesAndLinesItemsGrid = [
            [pageComLabel, self.pageCommand],
            [lineComLabel, self.lineCommand],
            [newpageComLabel, self.newpageCommand],
            [newlineComLabel, self.newlineCommand],
            [sortLabel, self.sortComboBox],
            [self.DDL_check],
            [self.RL_check, self.RP_check]
            ]
        
        pagesAndLinesLayout.addwidgetsGrid(pagesAndLinesItemsGrid)
        
        # -->
        
        hexCellsGrid = [
            [self.FixSlashes, self.UseTable],
            [readByteLengthLabel, self.readByteLength, self.readByteLength2],
            [resultByteLengthLabel, self.resultByteLength],
            [placeHolderLabel, self.placeHolder],
            [byte_1_Label, self.byte_1, byte_2_Label, self.byte_2],
            [unicodeLabel, self.unicodeComboBox],
            [self.bytesTableButton]
            ]
        
        hexConverterLayout.addwidgetsGrid(hexCellsGrid)
        
        # -->
        
        advancedOptionsLayout.addWidget(self.AutoCopyCheck)
        advancedOptionsLayout.addWidget(self.AutoConvertCheck)

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
        
        textLabel = QLabel("   النص الأصلي:")
        translationLabel = QLabel("   الترجمة:")
        
        buttonsLayout = QHBoxLayout()
        self.enterButton = QPushButton("إدخال")
        self.enterConvertButton = QPushButton("تحويل وإدخال")
        self.extractButton = QPushButton("استخراج")
        
        secondButtonsLayout = QHBoxLayout()
        self.fromFolder = QPushButton("مجلد الملفات")
        self.toFolder = QPushButton("مجلد نواتج الإدخال")
        self.textTableButton = QPushButton("فتح جدول نصوص")
        
        varsLayout = QGridLayout()
        self.beforeText = AdvancedCell(80, 26, "")
        self.afterText = AdvancedCell(80, 26, "")
        self.minText = AdvancedCell(80, 26, 0)
        self.maxText = AdvancedCell(80, 26, 1000)
        beforeTextLabel = QLabel("ما يسبق النص في الملفات:")
        afterTextLabel = QLabel("ما يلحقه:")
        minTextLabel = QLabel("أقصى حد لقصر النصوص المستخرجة:")
        maxTextLabel = QLabel("أقصى حد لطولها:")
        
        OptinsLayout = QVBoxLayout()
        self.databaseCheck = QCheckBox("استخدام جدول النصوص للإدخال.")
        self.asciiCheck = QCheckBox("استخراج الآسكي فقط.")
        self.filesEditorCheck = QCheckBox("استخراج باستخدام محرر الملفات.")
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
        
        offsetTypeLabel = QLabel("     وفق:")
        
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
        OptinsLayout.addWidget(self.filesEditorCheck)
        OptinsLayout.addWidget(self.sortedCheck)
        OptinsLayout.addWidget(self.tooLongCheck)
        OptinsLayout.addWidget(self.translationOffsetCheck)
        OptinsLayout.addWidget(self.Offset)
        OptinsLayout.addWidget(offsetTypeLabel)
        OptinsLayout.addWidget(self.OffsetType)

EnteringWindow = EnteringMotherWindow()


#<-------------------------------------------[]------------------------------------------->
