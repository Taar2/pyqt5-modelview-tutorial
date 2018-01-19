# -*- coding: utf-8 -*-
"""
@author: Taar
"""

#conversion of https://github.com/openwebos/qt/tree/master/examples/tutorials/modelview/2_formatting

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt as qt

class MyModel(QtCore.QAbstractTableModel):
    def __init__(self,parent):
        super(MyModel,self).__init__(parent)
    def rowCount(self,n):
        return 2
    def columnCount(self,n):
        return 3
    def data(self,index,role):
        row = index.row()
        col = index.column()
        print('row {}, col {}, role {}'.format(row,col,role))
        if role == qt.DisplayRole:
            if row == 0 and col == 1:
                return '<--left'
            if row == 1 and col == 1:
                return 'right-->'
            return 'Row{}, Column{}'.format(row+1,col+1)
        elif role == qt.FontRole:
            if row == 0 and col == 0: #change font only for cell(0,0)
                boldFont = QtGui.QFont()
                boldFont.setBold(True)
                return boldFont
        elif role == qt.BackgroundRole:
            if row == 1 and col == 2: #change background only for cell(1,2)
                redBackground = QtGui.QBrush(qt.red)
                return redBackground
        elif role == qt.TextAlignmentRole:
            if row == 1 and col == 1: #change text alignment only for cell(1,1)
                return qt.AlignRight + qt.AlignVCenter
        elif role == qt.CheckStateRole:
            if row == 1 and col == 0: #add a checkbox to cell(1,0)
                return qt.Checked

if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app= QtWidgets.QApplication(sys.argv)
    tableView = QtWidgets.QTableView()
    myModel = MyModel(None)
    tableView.setModel(myModel)
    tableView.show()
    app.exec_()
    
