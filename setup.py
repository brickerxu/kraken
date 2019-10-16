# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/16
# @file setup.py

"""
爬虫工具打包脚本
"""

from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['./reptile/main.py', '-w', '-F', '--icon=favicon.ico']
    run(opts)