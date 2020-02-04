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
        index.resize(800, 600)
        index.setMinimumSize(QtCore.QSize(800, 600))
        index.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(index)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-2, -1, 811, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_search = QtWidgets.QWidget()
        self.tab_search.setObjectName("tab_search")
        self.edit_keyword = QtWidgets.QLineEdit(self.tab_search)
        self.edit_keyword.setGeometry(QtCore.QRect(130, 110, 421, 35))
        self.edit_keyword.setObjectName("edit_keyword")
        self.btn_search = QtWidgets.QPushButton(self.tab_search)
        self.btn_search.setGeometry(QtCore.QRect(589, 110, 80, 35))
        self.btn_search.setObjectName("btn_search")
        self.search_result = QtWidgets.QGroupBox(self.tab_search)
        self.search_result.setGeometry(QtCore.QRect(20, 190, 761, 311))
        self.search_result.setProperty("hidden", True)
        self.search_result.setObjectName("search_result")
        self.search_result_layout = QtWidgets.QHBoxLayout(self.search_result)
        self.search_result_layout.setObjectName("search_result_layout")
        self.tree_search = QtWidgets.QTreeWidget(self.search_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_search.sizePolicy().hasHeightForWidth())
        self.tree_search.setSizePolicy(sizePolicy)
        self.tree_search.setObjectName("tree_search")
        self.search_result_layout.addWidget(self.tree_search)
        self.label_image = QtWidgets.QLabel(self.search_result)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.search_result_layout.addWidget(self.label_image)
        self.tabWidget.addTab(self.tab_search, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        index.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(index)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        index.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(index)
        self.statusbar.setObjectName("statusbar")
        index.setStatusBar(self.statusbar)
        self.action_setting = QtWidgets.QAction(index)
        self.action_setting.setObjectName("action_setting")
        self.action_logout = QtWidgets.QAction(index)
        self.action_logout.setObjectName("action_logout")
        self.menu.addAction(self.action_setting)
        self.menu.addSeparator()
        self.menu.addAction(self.action_logout)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(index)
        QtCore.QMetaObject.connectSlotsByName(index)

    def retranslateUi(self, index):
        _translate = QtCore.QCoreApplication.translate
        index.setWindowTitle(_translate("index", "漫画嗅探器"))
        self.btn_search.setText(_translate("index", "搜索"))
        self.search_result_layout.setProperty("hidden", _translate("index", "true"))
        self.tree_search.headerItem().setText(0, _translate("index", "搜索列表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_search), _translate("index", "搜索"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("index", "传输列表"))
        self.menu.setTitle(_translate("index", "文件"))
        self.action_setting.setText(_translate("index", "设置"))
        self.action_logout.setText(_translate("index", "退出"))
