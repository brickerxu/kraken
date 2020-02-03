# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_index(object):
    def setupUi(self, index):
        index.setObjectName("index")
        index.setWindowModality(QtCore.Qt.WindowModal)
        index.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(index)
        self.centralwidget.setObjectName("centralwidget")
        index.setCentralWidget(self.centralwidget)
        self.action_tuichu = QtWidgets.QAction(index)
        self.action_tuichu.setObjectName("action_tuichu")
        self.action_shezhi = QtWidgets.QAction(index)
        self.action_shezhi.setObjectName("action_shezhi")

        self.retranslateUi(index)
        QtCore.QMetaObject.connectSlotsByName(index)

    def retranslateUi(self, index):
        _translate = QtCore.QCoreApplication.translate
        index.setWindowTitle(_translate("index", "漫画嗅探器"))
        self.action_tuichu.setText(_translate("index", "退出"))
        self.action_shezhi.setText(_translate("index", "设置"))
