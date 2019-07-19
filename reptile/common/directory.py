# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/7/19
# @file directory.py

"""
目录结构管理文件
"""

import os
from os import path


class Directory(object):
    def __init__(self):
        # 获取默认输出目录
        self.user_home = path.expanduser('~')
        self.reptile_dir = path.join(self.user_home, 'reptile')
        self.log_dir = path.join(self.reptile_dir, 'logs')
        if not path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.temp_dir = path.join(self.reptile_dir, 'temp')
        if not path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        self.out_dir = path.join(self.reptile_dir, 'out')
        if not path.exists(self.out_dir):
            os.makedirs(self.out_dir)


directory = Directory()
