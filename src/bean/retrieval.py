# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/3
# @file retrieval.py

"""
检索结果信息
"""


class Retrieval(object):

    def __init__(self, code=-1, msg='', res=[]):
        self._code = code
        self._msg = msg
        self._res = res

    def code(self):
        return self._code

    def set_code(self, new_code):
        self._code = new_code

    def msg(self):
        return self._msg

    def set_msg(self, new_msg):
        self._msg = new_msg

    def res(self):
        return self._res

    def set_res(self, new_res):
        self._res = new_res