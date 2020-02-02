# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/2
# @file basics.py

import abc


class Basics(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.__name__ = name

    def name(self):
        return self.__name__

    '''
    搜索关键字
    返回固定格式结果
    '''
    @abc.abstractmethod
    def search(self, keyword):
        pass
