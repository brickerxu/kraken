# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/7/19
# @file exceptions.py


"""
通用异常类
"""


class ReptileException(Exception):
    def __init__(self, message='', error_labels=None):
        super(ReptileException, self).__init__(message)
        self._error_labels = set(error_labels or [])

# from common import ReptileException
# '''
# 集合不存在异常
# '''
# class CollectionNotFoundError(ReptileException):
#     def __init__(self, message='Collection Not Found', error_labels=None):
#         if error_labels is None:
#             error_labels = ("CollectionNotFoundError",)
#         super(CollectionNotFoundError, self).__init__(message, error_labels=error_labels)
