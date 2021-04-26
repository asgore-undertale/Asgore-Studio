from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QMessageBox
from PyQt5.QtCore import Qt

class MotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        QApplication.setLayoutDirection(Qt.RightToLeft)
 
        self.mdiArea = QMdiArea()
        self.setCentralWidget(self.mdiArea)
        self.setWindowTitle("Asgore Studio 1.0v")
        
        self.createBars()
        self.createMenus()
        self.createActions()
 
    def windowTrig(self, action):
        def check(text): return action.text() == text

        if check("عني"): QMessageBox.about(self, "عني", "صفحتي: https://github.com/asgore-undertale\nلك كامل الحرية في التعديل والنشر بشرط ذكري وصفحتي.")
        elif check("معلومات مهمة"): QMessageBox.about(self, "معلومات مهمة", "- للكتابة بالبايتات في الحقول الصغيرة اكتب [b] وبعدها البايتات.\n  (هذا في المدخل وخيارات التحويل فقط)\n  (ولا تضع فراغات)\n- لا تفتح ملفات الاكسل أثناء تشغيل الأداة.")
        elif check("تكبير النوافذ وصفها"): self.mdiArea.tileSubWindows()
        elif check("تصغير النوافذ"): self.mdiArea.cascadeSubWindows()
        elif check("إغلاق كافة النوافذ"): self.mdiArea.closeAllSubWindows()
        elif check("جداول آسغور"): self.newChild(TableEditorWindow, TableEditorContainer, 'جداول آسغور')
        elif check("محوّل النصوص"): self.newChild(CMainWindow, CMainContainer, 'محوّل النصوص')
        elif check("المدخل والمستخرج"): self.newChild(EnteringWindow, EnteringContainer, 'المدخل والمستخرج')
        elif check("خيارات التحويل"): self.newChild(OptionsWindow, OptionsContainer, 'خيارات التحويل')
        elif check("محرّر msyt."): self.newChild(MsytWindow, MsytContainer, 'محرّر msyt.')
        elif check("مربع الحوار"): self.newChild(FitAdvancedWindow, FitAdvancedContainer, 'مربع الحوار')
        elif check("منشئ جداول الخطوط"): self.newChild(FontsTablesCreatorWindow, FontsTablesCreatorContainer, 'منشئ جداول الخطوط')
        elif check("محوّل الجداول"): self.newChild(TablesConverterWindow, TablesConverterContainer, 'محوّل الجداول')
    
    def createBars(self):
        self.bar = self.menuBar()
        self.bar.triggered[QAction].connect(self.windowTrig)
    
    def createMenus(self):
        self.tools = self.bar.addMenu("الأدوات")
        self.windows = self.bar.addMenu("النوافذ")
    
    def createActions(self):
        self.windows.addAction("تكبير النوافذ وصفها")
        self.windows.addAction("تصغير النوافذ")
        self.windows.addAction("إغلاق كافة النوافذ")
        self.bar.addAction("معلومات مهمة")
        self.bar.addAction("عني")
        self.tools.addAction("جداول آسغور")
        self.tools.addAction("محوّل النصوص")
        self.tools.addAction("المدخل والمستخرج")
        self.tools.addAction("خيارات التحويل")
        self.tools.addAction("محرّر msyt.")
        self.tools.addAction("مربع الحوار")
        self.tools.addAction("منشئ جداول الخطوط")
        self.tools.addAction("محوّل الجداول")

    def newChild(self, widget, container, name):
        if container not in self.mdiArea.subWindowList():
            container.setWindowTitle(name)
            self.mdiArea.addSubWindow(container)
        widget.show()

if __name__ == '__main__':
    from Parts.AsgoreTablesEditor import TableEditorWindow
    from Parts.ATCEE import OptionsWindow, CMainWindow, EnteringWindow
    from Parts.AsgoreMsytTool import MsytWindow
    from Parts.FitInBoxAdvanced import FitAdvancedWindow
    from Parts.FontsTablesCreator import FontsTablesCreatorWindow
    from Parts.TablesConverter import TablesConverterWindow
    from sys import argv

    app = QApplication(argv)

    TableEditorContainer = QMdiSubWindow()
    TableEditorContainer.setWidget(TableEditorWindow)
    OptionsContainer = QMdiSubWindow()
    OptionsContainer.setWidget(OptionsWindow)
    CMainContainer = QMdiSubWindow()
    CMainContainer.setWidget(CMainWindow)
    EnteringContainer = QMdiSubWindow()
    EnteringContainer.setWidget(EnteringWindow)
    MsytContainer = QMdiSubWindow()
    MsytContainer.setWidget(MsytWindow)
    FitAdvancedContainer = QMdiSubWindow()
    FitAdvancedContainer.setWidget(FitAdvancedWindow)
    FontsTablesCreatorContainer = QMdiSubWindow()
    FontsTablesCreatorContainer.setWidget(FontsTablesCreatorWindow)
    TablesConverterContainer = QMdiSubWindow()
    TablesConverterContainer.setWidget(TablesConverterWindow)

    main = MotherWindow()
    main.show()
    app.exec_()