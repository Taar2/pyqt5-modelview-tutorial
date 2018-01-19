# -*- coding: utf-8 -*-
"""
@author: Taar
"""

#conversion of https://github.com/openwebos/qt/tree/master/examples/tutorials/modelview/6_treeview

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt as qt

ROWS = 2
COLS = 3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        treeView = QtWidgets.QTreeView(self)
        self.setCentralWidget(treeView)
        standardModel = QtGui.QStandardItemModel()
        rootNode = standardModel.invisibleRootItem()
        
        #defining a couple of items
        americaItem = QtGui.QStandardItem("America")
        mexicoItem =  QtGui.QStandardItem("Canada")
        usaItem =     QtGui.QStandardItem("USA")
        bostonItem =  QtGui.QStandardItem("Boston")
        europeItem =  QtGui.QStandardItem("Europe")
        italyItem =   QtGui.QStandardItem("Italy")
        romeItem =    QtGui.QStandardItem("Rome")
        veronaItem =  QtGui.QStandardItem("Verona")
        
        #building up the hierarchy
        rootNode.appendRow(americaItem)
        rootNode.appendRow(europeItem)
        americaItem.appendRow(mexicoItem)
        americaItem.appendRow(usaItem)
        usaItem.appendRow(bostonItem)
        europeItem.appendRow(italyItem)
        italyItem.appendRow(romeItem)
        italyItem.appendRow(veronaItem)
        
        #register the model
        treeView.setModel(standardModel)
        treeView.expandAll()
        
        #selection changes shall trigger a slot
        selectionModel= treeView.selectionModel()
        selectionModel.selectionChanged.connect(self.selectionChangedSlot)
        
        self.treeView = treeView
        
    @QtCore.pyqtSlot(QtCore.QItemSelection,QtCore.QItemSelection) #decorator has same signature as the signal
    def selectionChangedSlot(self,newSelection,oldSelection):
        #get the text of the selected item
        index = self.treeView.selectionModel().currentIndex()
        selectedText = index.data(qt.DisplayRole)
        
        #find out the hierarchy level of the selected item
        hierarchyLevel=1
        seekRoot = index
        invalid = QtCore.QModelIndex()
        while seekRoot.parent() != invalid:
            seekRoot = seekRoot.parent()
            hierarchyLevel += 1
        showString = '{}, Level {}'.format(selectedText,hierarchyLevel)
        self.setWindowTitle(showString)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app= QtWidgets.QApplication(sys.argv)
    w = MainWindow(None)
    w.show()
    app.exec_()
    
