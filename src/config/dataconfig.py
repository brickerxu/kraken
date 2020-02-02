# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/17
# @file dataconfig.py

from .config import Config
from common import directory

"""
需要爬取的动漫配置处理类
"""


class DataConfig(Config):
    def __init__(self):
        super(DataConfig, self).__init__(directory.data_config_path)
        self.SECTION = 'default'
