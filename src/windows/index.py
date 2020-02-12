# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/16
# @file index.py

import requests
import service
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTreeWidgetItem
from PyQt5.QtGui import QImage, QPixmap
from ui import Ui_index
from resolver import resolverManager


class Index(QMainWindow, Ui_index):
    def __init__(self, parent=None):
        super(Index, self).__init__(parent)
        self.setupUi(self)
        self.__init_ui__()
        self.resolverManager = resolverManager

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
        resolvers = self.resolverManager.resolvers
        for key in resolvers:
            r = resolvers[key]
            item = QTreeWidgetItem()
            item.setText(0, r.name())
            item.setText(1, key)

            result = r.search(keyword)
            cartoons = result.res()
            for c in cartoons:
                child = QTreeWidgetItem()
                child.setText(0, c.name())
                child.setToolTip(0, c.name())
                child.setText(1, c.key())
                child.setText(2, c.url())
                child.setText(3, c.image_url())
                item.addChild(child)

            self.tree_search.insertTopLevelItem(0, item)

    def click_tree_search(self):
        self.btn_download.setHidden(False)
        header = {'Referer': 'https://www.dmzj.com/dynamic/o_search/index', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        item = self.tree_search.currentItem()
        if item.text(3):
            image_url = item.text(3)
            res = requests.get(image_url, headers=header)
            img = QImage.fromData(res.content)
            self.label_image.setScaledContents(True)
            self.label_image.setPixmap(QPixmap.fromImage(img))

    def click_download(self):
        item = self.tree_search.currentItem()
        parent = item.parent()
        if parent is None:
            return
        service.download(parent.text(1), item.text(2))
