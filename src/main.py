# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/16
# @file main.py

import sys
from PyQt5.QtWidgets import QApplication

from windows import Index

'''
程序主入口
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    reptile = Index()
    reptile.show()
    sys.exit(app.exec_())
