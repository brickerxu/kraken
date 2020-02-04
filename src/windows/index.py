# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/16
# @file index.py

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QTextCursor
from ui import Ui_index
from resolver import resolvers


class Index(QMainWindow, Ui_index):
    def __init__(self, parent=None):
        super(Index, self).__init__(parent)
        self.setupUi(self)
        self.__init_ui__()

    def __init_ui__(self):
        self.btn_search.clicked.connect(self.search_click)

    def search_click(self):
        keyword = self.edit_keyword.text()
        if not keyword or keyword is None:
            QMessageBox.information(self, "提示", "关键字为空！", QMessageBox.Ok)
            return
        self.search_result.setHidden(False)
        self.tree_search.clear()
        for r in resolvers:
            item = QTreeWidgetItem()
            item.setText(0, r.name())

            result = r.search(keyword)

            cartoons = result._res

            for c in cartoons:
                child = QTreeWidgetItem()
                child.setText(0, c._name)
                item.addChild(child)

            self.tree_search.insertTopLevelItem(0, item)
