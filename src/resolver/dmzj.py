# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/2
# @file dmzj.py

"""
动漫之家
https://manhua.dmzj.com
"""

import requests
from lxml import etree
from .basics import Basics
from bean import Cartoon


class Dmzj(Basics):

    def __init__(self):
        super(Dmzj, self).__init__('动漫之家')
        self._url = 'https://manhua.dmzj.com'
        self._search_url = 'https://www.dmzj.com/dynamic/o_search/index'

    def search_request(self, keyword):
        return requests.post(self._search_url, data={'keywords': keyword})

    def search_parser(self, content):
        cartoons = []
        select = etree.HTML(content)
        chapters = select.xpath('//div[contains(@class, "wrap_search")]/*/*/*/ul[contains(@class, "update_con")]/li')
        for chapter in chapters:
            name = chapter.xpath('a[1]/@title')[0].strip()
            url = 'https:' + chapter.xpath('a[1]/@href')[0].strip()
            image_url = chapter.xpath('a[1]/img[1]/@src')[0].strip()
            cartoon = Cartoon(name, url, image_url)
            cartoons.append(cartoon)
        return cartoons
