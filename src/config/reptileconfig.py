# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/10/17
# @file reptileconfig.py

from .config import Config
from common import directory

"""
项目全局配置处理类
"""


class ReptileConfig(Config):
    def __init__(self):
        super(ReptileConfig, self).__init__(directory.reptile_config_path)
        self.SECTION = 'default'

    def get_output(self):
        if self.__has_option__(self.SECTION, 'output'):
            return self.config.get(self.SECTION, 'output')
        return None


reptileConfig = ReptileConfig()
