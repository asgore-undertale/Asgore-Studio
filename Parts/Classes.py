from PyQt5.QtWidgets import QComboBox, QTextEdit
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QStandardItemModel

from Parts.Scripts.UsefulLittleFunctions import tryTakeNum

class CheckableComboBox(QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handle_item_pressed)
        self.setModel(QStandardItemModel(self))
        
        self.checkboxes = []
  
    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        if item not in self.checkboxes: return
        
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
    
    def item_checked(self, index):
        item = self.model().item(index, 0)
        return item.checkState() == Qt.Checked
    
    def check_items(self):
        checkedItems = []
        for i in range(self.count()):
            if self.item_checked(i):
                checkedItems.append(i)
        return checkedItems
    
    def AddItems(self, items):
        self.addItems(items)
    
    def AddCheckBoxItems(self, items):
        startIndex = self.count()
        for i in range(len(items)):
            self.addItem(items[i])
            item = self.model().item(i+startIndex, 0)
            item.setCheckState(Qt.Unchecked)
            
            self.checkboxes.append(item)
    
    # def reloadItems(self, Items, index = 0): بسبب وجود عناصر مربع تحقق وأخرى لا
        # self.blockSignals(True)
        # self.clear()
        # self.blockSignals(False)

class AdvancedCell(QTextEdit):
    def __init__(self, Width, Height, DefaultValue = 0):
        super(AdvancedCell, self).__init__()
        
        self.setFixedSize(Width, Height)
        self.Value = DefaultValue
        self.Type = str(type(DefaultValue))[8:-2]
        
        self.updateCell()
    
    def focusOutEvent(self, event):
        self.updateCell()
        super(AdvancedCell, self).focusInEvent(event)
    
    def updateValue(self):
        if self.Type == 'str':
            self.Value = self.toPlainText()
        elif self.Type == 'int':
            self.Value = tryTakeNum(self.toPlainText(), self.Value)
        elif self.Type == 'float':
            self.Value = tryTakeNum(self.toPlainText(), self.Value, False)
    
    def updateCell(self):
        self.updateValue()
        self.setPlainText(str(self.Value))
    
    def getValue(self):
        return self.Value
