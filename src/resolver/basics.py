# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/2
# @file basics.py

import abc
import requests
import utils
from bean import Retrieval


class Basics(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.__name__ = name

    def key(self):
        return utils.md5(self.__name__)

    def name(self):
        return self.__name__

    def search(self, keyword):
        if keyword is None:
            return Retrieval(msg='关键字为空！！！')
        html = self.search_request(keyword)
        if html is None:
            return Retrieval(msg='请求失败！')
        if html.status_code == 200:
            cartoons = self.search_parser(html.content)
            return Retrieval(200, res=cartoons)
        else:
            return Retrieval(html.status_code, msg='请求失败！')

    '''
    搜索关键字
    返回requests请求结果
    '''
    @abc.abstractmethod
    def search_request(self, keyword):
        pass

    '''
    解析搜索结果
    返回固定格式列表
    '''
    @abc.abstractmethod
    def search_parser(self, content):
        pass

    def crawl(self, url):
        if not url:
            return None
        html = requests.get(url)
        if html is None:
            return None
        if html.status_code == 200:
            xmls = self.crawl_parser(html.content)

    @abc.abstractmethod
    def crawl_parser(self, content):
        pass
