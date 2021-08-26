from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from sys import stdout

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
        
        # self.check_items()
    
    def item_checked(self, index):
        item = self.model().item(index, 0)
        return item.checkState() == Qt.Checked
    
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
    
    stdout.flush()