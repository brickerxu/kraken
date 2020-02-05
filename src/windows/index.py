# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/16
# @file index.py

import requests
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QTextCursor, QImage, QPixmap
from ui import Ui_index
from resolver import resolvers


class Index(QMainWindow, Ui_index):
    def __init__(self, parent=None):
        super(Index, self).__init__(parent)
        self.setupUi(self)
        self.__init_ui__()

    def __init_ui__(self):
        self.btn_download.setHidden(True)
        self.btn_search.clicked.connect(self.click_search)
        self.btn_download.clicked.connect(self.click_download)
        self.tree_search.clicked.connect(self.click_tree_search)

    def click_search(self):
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
            cartoons = result.res()
            for c in cartoons:
                child = QTreeWidgetItem()
                child.setText(0, c.name())
                child.setToolTip(0, c.name())
                child.setText(1, c.url())
                child.setText(2, c.image_url())
                item.addChild(child)

            self.tree_search.insertTopLevelItem(0, item)

    def click_tree_search(self):
        self.btn_download.setHidden(False)
        header = {'Referer': 'https://www.dmzj.com/dynamic/o_search/index', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        item = self.tree_search.currentItem()
        if item.text(2):
            image_url = item.text(2)
            res = requests.get(image_url, headers=header)
            img = QImage.fromData(res.content)
            self.label_image.setScaledContents(True)
            self.label_image.setPixmap(QPixmap.fromImage(img))

    def click_download(self):
        item = self.tree_search.currentItem()
        print('0->%s, 1->%s, 2->%s'%(item.text(0), item.text(1), item.text(2)))
