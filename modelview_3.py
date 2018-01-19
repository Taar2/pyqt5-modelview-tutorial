# -*- coding: utf-8 -*-
"""
@author: Taar
"""

#conversion of https://github.com/openwebos/qt/tree/master/examples/tutorials/modelview/3_changingmodel

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt as qt

class MyModel(QtCore.QAbstractTableModel):
    #notice that dataChanged is a class attribute from
    #the parent class; it's set at creation time
    #by inheritance
    def __init__(self,parent):
        super(MyModel,self).__init__(parent)
        timer = QtCore.QTimer(self)
        timer.setInterval(1000)
        timer.timeout.connect(self.timerHit)
        timer.start()

    def rowCount(self,n):
        return 2
    def columnCount(self,n):
        return 3
    def data(self,index,role):
        row = index.row()
        col = index.column()
        if role == qt.DisplayRole:
            if row == 0 and col == 0:
                return QtCore.QTime.currentTime().toString()
    def timerHit(self):
        changed_index = self.index(0,0)

        #notice that dataChanged has new
        #signature (QtCore.QModelIndex,QtCore.QModelIndex,QVector<int>)

        #and that QVector<int> are implemented as lists (of integers)

        #self.dataChanged.emit(changed_index,changed_index,[])
        #or better, indicated the changed roles :
        self.dataChanged.emit(changed_index,changed_index,[qt.DisplayRole])

if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app= QtWidgets.QApplication(sys.argv)
    tableView = QtWidgets.QTableView()
    myModel = MyModel(None)
    tableView.setModel(myModel)
    tableView.show()
    app.exec_()
    
