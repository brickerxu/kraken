# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/16
# @file config.py

"""
配置管理工具文件
包含配置的读取与修改
"""

import configparser

from common import constants
from utils import *

"""
配置服务基础父类
关于配置的读取与写入
"""


class Config(object):
    def __init__(self, config_path):
        self.SECTION = 'default'
        # 初始化配置文件
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path, constants.DEFAULT_CHARSET)

    def add_config(self, section, key, value):
        pass

    def remove_config(self, section, key):
        pass

    def update_config(self, section, key, value):
        pass

    def get_config(self, section, key):
        if section in self.config.sections() and key in self.config.options(section):
            return self.config.get(section, key)
        return None

    def __has_option__(self, section, option):
        if section is None:
            section = self.SECTION
        if option is None:
            return False
        return self.config.has_section(section) and self.config.has_option(section, option)




"""
Mongo数据库配置管理类
"""
class MongoConfig(Config):
    def __init__(self):
        super(MongoConfig, self).__init__(directory.mongo_config_path)
        self.SECTION = 'default'
    def get_host(self):
        if self.__has_option__(self.SECTION, 'host'):
            return self.config.get(self.SECTION, 'host')
        return None
    def get_port(self):
        if self.__has_option__(self.SECTION, 'port'):
            port = self.config.get(self.SECTION, 'port')
            if is_number(port):
                return int(port)
        return None
    def get_name(self):
        if self.__has_option__(self.SECTION, 'name'):
            return self.config.get(self.SECTION, 'name')
        return None

    def __has_option__(self, section, option):
        if section is None:
            section = self.SECTION
        if option is None:
            return False
        return self.config.has_section(section) and self.config.has_option(section, option)
