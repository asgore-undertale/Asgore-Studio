from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from sys import stdout

class CheckableComboBox(QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handle_item_pressed)
        self.setModel(QStandardItemModel(self))
  
    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        
        self.check_items()
    
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
        boxItemNum = self.count()
        for i in range(len(items)):
            self.addItem(items[i])
            item = self.model().item(i+boxItemNum, 0)
            item.setCheckState(Qt.Unchecked)
    
    # def clearItems(self, items):
        # pass
    
    stdout.flush()