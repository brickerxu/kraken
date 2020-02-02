# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/2
# @file dmzj.py

"""
动漫之家
https://manhua.dmzj.com
"""

import requests
from .basics import Basics


class Dmzj(Basics):

    def __init__(self):
        super(Dmzj, self).__init__('动漫之家')
        self.__search__url__ = 'https://www.dmzj.com/dynamic/o_search/index'

    def search(self, keyword):
        if keyword is None:
            return None
        html = requests.post(self.__search__url__, data={'keywords': keyword})
        return html.content