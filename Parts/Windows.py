from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Parts.Classes import *

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
        self.setWindowTitle("Asgore Studio 2.0.4.67")
 
        self.mdiArea = QMdiArea()
        self.setCentralWidget(self.mdiArea)
        
        self.createBars()
        self.createMenus()
        self.createActions()
        
        self.importantInfo = ('- للكتابة بالبايتات في الحقول الصغيرة اكتب [b] وبعدها البايتات.\n'
            '(هذا في المدخل وخيارات التحويل فقط) (ولا تضع فراغات)\n'
            '- اضغط F3 في محرّر الملفات لإضافة <c>.\n'
            '- اضغط lctrl+B لتحويل النص المحدد.\n'
            '- اضغط lctrl+P لكتابة أمر الصفحة الجديد من إعدادات محول النصوص.\n'
            '- اضغط lctrl+L لكتابة أمر السطر الجديد من إعدادات محول النصوص.\n'
            '- في منشئ جداول الحروف اضغط F3 لكتابة الحرف التالي وF4 للعودة حرفاً للوراء وF5 للعودة لأول حرف.\n'
            '- اضغط ctrl+S لالتقاط صورة لمربع الحوار في مجرب الخطوط')
    
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

        layout = QHBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        cellsLayout = QGridLayout()
        self.fontSizeCell = AdvancedCell(80, 26, 16)
        fontSizeLabel = QLabel("حجم الخط:")
        self.boxWidthCell = AdvancedCell(80, 26, 180)
        boxWidthLabel = QLabel("عرض المربع:")
        self.boxHeightCell = AdvancedCell(80, 26, 60)
        boxHeightLabel = QLabel("ارتفاع المربع:")
        self.pixelsPerCell = AdvancedCell(80, 26, 3)
        pixelsPerLabel = QLabel("البيكسلات بين السطور:")
        self.newLineCell = AdvancedCell(80, 26, "<line>")
        newLineLabel = QLabel("أمر السطر:")
        self.newPageCell = AdvancedCell(80, 26, "<page>")
        newPageLabel = QLabel("أمر الصفحة:")
        self.beforeComCell = AdvancedCell(80, 26, "[")
        beforeComLabel = QLabel("ما قبل الأوامر:")
        self.afterComCell = AdvancedCell(80, 26, "]")
        afterComLabel = QLabel("ما بعدها:")
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
        self.offsetComboBox.setFixedSize(220, 30)
        self.offsetComboBox.addItems(offsetComboBoxOptions)
        self.offsetComboBox.setInsertPolicy(QComboBox.NoInsert)
        offsetWithComboBoxLabel = QLabel("باستعمال:")
        self.offsetWithComboBox = QComboBox()
        self.offsetWithComboBox.setFixedSize(220, 30)
        self.offsetWithComboBox.addItems(offsetWithComboBoxOptions)
        self.offsetWithComboBox.setInsertPolicy(QComboBox.NoInsert)
        
        self.fromRightCheck = QCheckBox("تدفق النص من اليمين")
        self.boxAnimationCheck = QCheckBox("أنميشن مربع الحوار")
        self.lineBoxCheck = QCheckBox("صناديق السطور")
        self.charBoxCheck = QCheckBox("صناديق الحروف")
        
        
        layout.addLayout(cellsLayout)
        layout.addLayout(optionsLayout)
        cellsLayout.addWidget(fontSizeLabel, 0, 0)
        cellsLayout.addWidget(self.fontSizeCell, 0, 1)
        cellsLayout.addWidget(boxWidthLabel, 1, 0)
        cellsLayout.addWidget(self.boxWidthCell, 1, 1)
        cellsLayout.addWidget(boxHeightLabel, 2, 0)
        cellsLayout.addWidget(self.boxHeightCell, 2, 1)
        cellsLayout.addWidget(pixelsPerLabel, 3, 0)
        cellsLayout.addWidget(self.pixelsPerCell, 3, 1)
        cellsLayout.addWidget(newLineLabel, 4, 0)
        cellsLayout.addWidget(self.newLineCell, 4, 1)
        cellsLayout.addWidget(newPageLabel, 5, 0)
        cellsLayout.addWidget(self.newPageCell, 5, 1)
        cellsLayout.addWidget(beforeComLabel, 6, 0)
        cellsLayout.addWidget(self.beforeComCell, 6, 1)
        cellsLayout.addWidget(afterComLabel, 7, 0)
        cellsLayout.addWidget(self.afterComCell, 7, 1)
        cellsLayout.addWidget(offsetComLabel, 8, 0)
        cellsLayout.addWidget(self.offsetComCell, 8, 1)
        optionsLayout.addWidget(offsetComboBoxLabel)
        optionsLayout.addWidget(self.offsetComboBox)
        optionsLayout.addWidget(offsetWithComboBoxLabel)
        optionsLayout.addWidget(self.offsetWithComboBox)
        optionsLayout.addWidget(self.fromRightCheck)
        optionsLayout.addWidget(self.boxAnimationCheck)
        optionsLayout.addWidget(self.lineBoxCheck)
        optionsLayout.addWidget(self.charBoxCheck)

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
        
        tab1 = QWidget()
        tab2 = QWidget()
        container = QTabWidget()
        
        container.addTab(tab1, 'صفحة 1')
        container.addTab(tab2, 'صفحة 2')

        layout = QGridLayout()
        layout2 = QGridLayout()
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
        self.HarakatComboBox.setFixedSize(160, 27)
        
        customScriptLayout = QHBoxLayout()
        CustomScriptLabel = QLabel("سكربتات:")
        self.CustomScriptComboBox = CheckableComboBox()
        self.CustomScriptComboBox.setFixedSize(160, 27)
        self.CustomScriptComboBox.AddItems(['تحديث القائمة', '...'])


        self.FixSlashes = QCheckBox(r"مراعاة (n, \r, \t, \0\)")
        self.AutoCopyCheck = QCheckBox("النسخ تلقائياً بعد التحويل")
        self.AutoConvertCheck = QCheckBox("التحويل تلقائياً عند الكتابة")
        
        containerLayout = QVBoxLayout()
        cellsLayout = QGridLayout()
        startComLabel = QLabel("قبل الأوامر:")
        self.startCommand = AdvancedCell(90, 26, "[")
        endComLabel = QLabel("بعدها:")
        self.endCommand = AdvancedCell(90, 26, "]")
        pageComLabel = QLabel("أمر الصفحة:")
        self.pageCommand = AdvancedCell(90, 26, "<page>")
        lineComLabel = QLabel("أمر السطر:")
        self.lineCommand = AdvancedCell(90, 26, "<line>")
        convertedByteLabel = QLabel("صيغة البايت المحول:")
        self.convertedByte = AdvancedCell(90, 26, r'\xXY')
        
        self.C_databaseButton = QPushButton("فتح جدول تحويل")
        
        self.DDL_check = QCheckBox("حذف أسطر الصفحة المكررة")
        self.SSL_check = QCheckBox("ترتيب أسطر الصفحة تصاعديا")
        self.SLS_check = QCheckBox("ترتيب أسطر الصفحة تنازليا")
        self.RL_check = QCheckBox("عكس ترتيب أسطر الصفحات")
        self.RP_check = QCheckBox("عكس ترتيب الصفحات")
        
        
        newpageComLabel = QLabel("أمر الصفحة الجديد:")
        self.newpageCommand = AdvancedCell(90, 26, "{page}")
        newlineComLabel = QLabel("أمر السطر جديد:")
        self.newlineCommand = AdvancedCell(90, 26, "{line}")
        
        
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
        checksLayout.addWidget(self.AutoConvertCheck)
        
        containerLayout.addLayout(cellsLayout)
        containerLayout.addWidget(self.DDL_check)
        containerLayout.addWidget(self.SSL_check)
        containerLayout.addWidget(self.SLS_check)
        containerLayout.addWidget(self.RL_check)
        containerLayout.addWidget(self.RP_check)
        containerLayout.addWidget(self.C_databaseButton)
        
        layout.addLayout(checksLayout, 0, 0)
        layout.addLayout(containerLayout, 0, 1)
        
        layout2.addWidget(newpageComLabel, 0, 0)
        layout2.addWidget(self.newpageCommand, 0, 1)
        layout2.addWidget(newlineComLabel, 1, 0)
        layout2.addWidget(self.newlineCommand, 1, 1)
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
