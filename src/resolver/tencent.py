# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/2
# @file tencent.py

"""
腾讯动漫
https://ac.qq.com/
"""

import requests
from .basics import Basics


class Tencent(Basics):

    def __init__(self):
        super(Tencent, self).__init__('腾讯动漫')
        self.__search__url__ = 'https://ac.qq.com/Comic/searchList'

    def search(self, keyword):
        if keyword is None:
            return None
        html = requests.get(self.__search__url__, params={'search': keyword})
        return html.content
