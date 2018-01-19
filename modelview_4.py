# -*- coding: utf-8 -*-
"""
@author: Taar
"""

#conversion of https://github.com/openwebos/qt/tree/master/examples/tutorials/modelview/4_headers

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
        if role == qt.DisplayRole:
            return 'Row{}, Column{}'.format(index.row()+1,index.column()+1)
    def headerData(self,section,orientation,role):
        if role == qt.DisplayRole:
            if orientation == qt.Horizontal:
                return ['first','second','third'][section]

if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app= QtWidgets.QApplication(sys.argv)
    tableView = QtWidgets.QTableView()
    myModel = MyModel(None)
    tableView.setModel(myModel)
    #one addition to the file, as shown in the tutorial
    #hide vertical header
    tableView.verticalHeader().hide()
    tableView.show()
    app.exec_()
    
