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

    def name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def url(self):
        return self._url

    def set_url(self, new_url):
        self._url = new_url

    def image_url(self):
        return self._image_url

    def set_image_url(self, new_image_url):
        self._image_url = new_image_url
