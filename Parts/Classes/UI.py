from PyQt5.QtWidgets import QComboBox, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QStandardItemModel

from Parts.Scripts.UsefulLittleFunctions import tryTakeNum, hexToString, minimax, getType

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
    def __init__(self, Width, Height, DefaultValue = 0, min = False, max = False):
        super(AdvancedCell, self).__init__()
        
        self.bytesign = '[b]'
        self.min = min
        self.max = max
        
        self.setFixedSize(Width, Height)
        self.setValue(DefaultValue)
    
    def focusOutEvent(self, event):
        self.updateCell()
        super(AdvancedCell, self).focusInEvent(event)
    
    def updateValue(self):
        if self.Type == 'str':
            value = self.toPlainText()
            if minimax(len(value), self.min, self.max):
                self.Value = value
            
        elif self.Type == 'int':
            value = tryTakeNum(self.toPlainText(), self.Value)
            if minimax(value, self.min, self.max):
                self.Value = value
            
        elif self.Type == 'float':
            value = tryTakeNum(self.toPlainText(), self.Value, False)
            if minimax(value, self.min, self.max):
                self.Value = value
    
    def updateCell(self):
        self.updateValue()
        self.setPlainText(str(self.Value))
    
    def byteToText(self, value):
        if self.Type != 'str': return value
        if self.bytesign not in self.Value: return value
        return hexToString(self.Value.replace(self.bytesign, '').replace(' ', ''))
    
    def setValue(self, value):
        self.Value = value
        self.Type = getType(value)
        self.setPlainText(str(self.Value))
    
    def getValue(self):
        return self.byteToText(self.Value)


class QVHBoxLayout(QVBoxLayout):
    def __init__(self):
        super(QVHBoxLayout, self).__init__()
    
    def addwidget(self, item):
        self.addWidget(item)
    
    def addwidgetsRow(self, itemsList):
        H = QHBoxLayout()
        for item in itemsList:
            H.addWidget(item)
        self.addLayout(H)
    
    def addwidgetsGrid(self, itemsGrid):
        for row in itemsGrid:
            self.addwidgetsRow(row)