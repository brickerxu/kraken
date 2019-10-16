# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/7/19
# @file directory.py

import os
import sys
from os import path

"""
目录结构管理文件
"""


class Directory(object):
    def __init__(self):
        # 获取默认输出目录
        self.__getRootDir__()
        self.reptile_dir = path.join(self.base_dir, 'reptile')
        self.log_dir = path.join(self.base_dir, 'logs')
        if not path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.config_dir = path.join(self.base_dir, 'config')
        if not path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        self.reptile_config_path = path.join(self.config_dir, 'reptile.ini')
        if not path.exists(self.reptile_config_path):
            file = open(self.reptile_config_path, 'w')
            file.close()
        self.data_config_path = path.join(self.config_dir, 'data.ini')
        if not path.exists(self.data_config_path):
            file = open(self.data_config_path, 'w')
            file.close()
        self.temp_dir = path.join(self.base_dir, 'temp')
        if not path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    '''
    获取根目录
    '''
    def __getRootDir__(self):
        setup_path = path.abspath("../setup.py")
        if path.exists(setup_path):
            self.base_dir = path.dirname(setup_path)
        else:
            self.base_dir = path.dirname(sys.argv[0])

directory = Directory()
