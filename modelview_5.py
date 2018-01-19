# -*- coding: utf-8 -*-
"""
@author: Taar
"""

#conversion of https://github.com/openwebos/qt/tree/master/examples/tutorials/modelview/5_edit

#I work with ints for values instead of strings (less cumbersome to add)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt as qt

ROWS = 2
COLS = 3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent):
        super(MainWindow,self).__init__(parent)
        tableView = QtWidgets.QTableView(self)
        self.setCentralWidget(tableView)
        myModel = MyModel(self)
        tableView.setModel(myModel)
        myModel.editCompleted.connect(self.showWindowTitle)
        self.setWindowTitle('Title pending...')
    @QtCore.pyqtSlot(int) #decorator has same signature as the signal
    def showWindowTitle(self,val):
        self.setWindowTitle(str(val))
    
class MyModel(QtCore.QAbstractTableModel):
    editCompleted = QtCore.pyqtSignal(int)
    def __init__(self,parent):
        super(MyModel,self).__init__(parent)
        self._m_gridData = [[0 for i in range(COLS)] for j in range(ROWS)]
    def rowCount(self,n):
        return ROWS
    def columnCount(self,n):
        return COLS
    def data(self,index,role):
        if role == qt.DisplayRole:
            return self._m_gridData[index.row()][index.column()]
    def setData(self,index,value,role):
        if role == qt.EditRole:
            try:
                self._m_gridData[index.row()][index.column()] = int(value)
            except:
                pass
            result = 0
            for row in range(ROWS):
                for col in range(COLS):
                    result += self._m_gridData[row][col]
            self.editCompleted.emit(result)
        return 1 #edit was done correctly
    def flags(self,index):
        #answer to requests for cell flags from QTableView
        return qt.ItemIsSelectable | qt.ItemIsEditable | qt.ItemIsEnabled

if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app= QtWidgets.QApplication(sys.argv)
    w = MainWindow(None)
    w.show()
    app.exec_()
    
