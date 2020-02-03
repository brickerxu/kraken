# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/3
# @file cartoon.py

"""
漫画信息类
"""


class Cartoon(object):

    def __init__(self, name='', url='', image_url=''):
        self._name = name
        self._url = url
        self._image_url = image_url

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, new_url):
        self._url = new_url

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, new_image_url):
        self._image_url = new_image_url
