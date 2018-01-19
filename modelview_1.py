# -*- coding: utf-8 -*-
"""
@author: Taar
"""

#conversion of https://github.com/openwebos/qt/tree/master/examples/tutorials/modelview/1_readonly

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MyModel(QtCore.QAbstractTableModel):
    def __init__(self,parent):
        super(MyModel,self).__init__(parent)
    def rowCount(self,n):
        return 2
    def columnCount(self,n):
        return 3
    def data(self,index,role):
        if role == QtCore.Qt.DisplayRole:
            return 'Row{}, Column{}'.\
              format(index.row()+1,index.column()+1)

if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app= QtWidgets.QApplication(sys.argv)
    tableView = QtWidgets.QTableView()
    myModel = MyModel(None)
    tableView.setModel(myModel)
    tableView.show()
    app.exec_()
    
