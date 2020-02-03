# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/16
# @file reptile.py

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QTextCursor
from ui import Ui_index


class Reptile(QMainWindow, Ui_index):
    def __init__(self, parent=None):
        super(Reptile, self).__init__(parent)
        self.setupUi(self)
