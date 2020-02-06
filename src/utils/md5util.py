# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/6
# @file md5util.py

import hashlib


def md5(text):
    if not text:
        return None
    return hashlib.md5(text.encode('utf8')).hexdigest()
