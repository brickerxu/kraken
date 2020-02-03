# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/2
# @file tencent.py

"""
腾讯动漫
https://ac.qq.com/
"""

import requests
from lxml import etree
from .basics import Basics
from bean import Cartoon


class Tencent(Basics):

    def __init__(self):
        super(Tencent, self).__init__('腾讯动漫')
        self._url = 'https://ac.qq.com'
        self._search_url = 'https://ac.qq.com/Comic/searchList'

    def search_request(self, keyword):
        return requests.get(self._search_url, params={'search': keyword})

    def search_parser(self, content):
        cartoons = []
        select = etree.HTML(content)
        chapters = select.xpath('//ul[contains(@class, "mod_book_list")]/li')
        for chapter in chapters:
            name = chapter.xpath('a[1]/@title')[0].strip()
            url = self._url + chapter.xpath('a[1]/@href')[0].strip()
            image_url = chapter.xpath('a[1]/img[1]/@data-original')[0].strip()
            cartoon = Cartoon(name, url, image_url)
            cartoons.append(cartoon)
        return cartoons
