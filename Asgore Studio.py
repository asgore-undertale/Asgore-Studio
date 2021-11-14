from PyQt5.QtWidgets import QApplication, QMdiSubWindow, QAction, QMessageBox
from PyQt5.QtCore import Qt, QEvent
from sys import argv
from os import path, chdir
from Parts.Scripts.UsefulLittleFunctions import ToModulePath, openFile

file_path = path.dirname(path.abspath(__file__))
chdir(file_path)

app = QApplication(argv)
QApplication.setLayoutDirection(Qt.RightToLeft)

clipboard = QApplication.clipboard()
event = QEvent(QEvent.Clipboard)
QApplication.sendEvent(clipboard, event)

from Parts.Windows import StudioWindow
from Parts.Tools.AsgoreTablesEditor import TableEditorWindow
from Parts.Tools.TextAnalyzer import TextAnalyzerWindow
from Parts.Tools.FontsConverter import FontsConverterWindow
from Parts.Tools.TablesConverter import TablesConverterWindow
from Parts.Tools.CharsTablesCreator import CharsTablesCreatorWindow
from Parts.Tools.FontTester import FontTesterWindow, FontTesterOptionsWindow
from Parts.Tools.AsgoreFilesEditor import FilesEditorWindow
from Parts.Tools.TextConverter import TextConverterWindow, TextConverterOptionsWindow
from Parts.Tools.ExtractorAndEnteror import EnteringWindow

TableEditorContainer = QMdiSubWindow()
TableEditorContainer.setWidget(TableEditorWindow)
TextAnalyzerContainer = QMdiSubWindow()
TextAnalyzerContainer.setWidget(TextAnalyzerWindow)
FontsConverterContainer = QMdiSubWindow()
FontsConverterContainer.setWidget(FontsConverterWindow)
TablesConverterContainer = QMdiSubWindow()
TablesConverterContainer.setWidget(TablesConverterWindow)
CharsTablesCreatorContainer = QMdiSubWindow()
CharsTablesCreatorContainer.setWidget(CharsTablesCreatorWindow)
FontTesterContainer = QMdiSubWindow()
FontTesterContainer.setWidget(FontTesterWindow)
FontTesterOptionsContainer = QMdiSubWindow()
FontTesterOptionsContainer.setWidget(FontTesterOptionsWindow)
FilesEditorContainer = QMdiSubWindow()
FilesEditorContainer.setWidget(FilesEditorWindow)
TextConverterContainer = QMdiSubWindow()
TextConverterContainer.setWidget(TextConverterWindow)
TextConverterOptionsContainer = QMdiSubWindow()
TextConverterOptionsContainer.setWidget(TextConverterOptionsWindow)
EnteringContainer = QMdiSubWindow()
EnteringContainer.setWidget(EnteringWindow)

def windowTrig(action):
    action = action.text()

    if   action == "عني": QMessageBox.about(StudioWindow, "عني", open('Parts/TextFiles/About me.txt', 'r', encoding='utf-8', errors='replace').read())
    elif action == "معلومات مهمة": QMessageBox.about(StudioWindow, "معلومات مهمة", StudioWindow.importantInfo)
    elif action == "تكبير النوافذ وصفها": StudioWindow.mdiArea.tileSubWindows()
    elif action == "تصغير النوافذ": StudioWindow.mdiArea.cascadeSubWindows()
    elif action == "إغلاق كافة النوافذ": StudioWindow.mdiArea.closeAllSubWindows()
    elif action == "جداول آسغور": StudioWindow.newChild(TableEditorWindow, TableEditorContainer, 'جداول آسغور')
    elif action == "مختزل النصوص": StudioWindow.newChild(TextAnalyzerWindow, TextAnalyzerContainer, 'مختزل النصوص')
    elif action == "محوّل الخطوط": StudioWindow.newChild(FontsConverterWindow, FontsConverterContainer, 'محوّل الخطوط')
    elif action == "محوّل الجداول": StudioWindow.newChild(TablesConverterWindow, TablesConverterContainer, 'محوّل الجداول')
    elif action == "منشئ جداول تحويل الآسكي": StudioWindow.newChild(CharsTablesCreatorWindow, CharsTablesCreatorContainer, 'منشئ جداول تحويل الآسكي')
    elif action == "مجرب الخطوط": StudioWindow.newChild(FontTesterWindow, FontTesterContainer, 'مجرب الخطوط')
    elif action == "إعدادات مجرب الخطوط": StudioWindow.newChild(FontTesterOptionsWindow, FontTesterOptionsContainer, 'إعدادات مجرب الخطوط')
    elif action == "محرّر الملفات": StudioWindow.newChild(FilesEditorWindow, FilesEditorContainer, 'محرّر الملفات')
    elif action == "محوّل النصوص": StudioWindow.newChild(TextConverterWindow, TextConverterContainer, 'محوّل النصوص')
    elif action == "خيارات محوّل النصوص": StudioWindow.newChild(TextConverterOptionsWindow, TextConverterOptionsContainer, 'خيارات محوّل النصوص')
    elif action == "المدخل والمستخرج": StudioWindow.newChild(EnteringWindow, EnteringContainer, 'المدخل والمستخرج')
    elif action == "تشغيل سكربت خارجي": runCustomScript()

def runCustomScript():
    try:
        scriptPath = filePath = openFile(['py'], text = 'ملف')
        scriptPath = scriptPath.replace(path.abspath('').replace('\\', '/')+'/', '', 1)
        exec(f"from {ToModulePath(scriptPath)} import Script", globals())
        Script()
    except Exception as e: print(e)

StudioWindow.bar.triggered[QAction].connect(windowTrig)

if __name__ == '__main__':
    StudioWindow.show()
    app.exec_()