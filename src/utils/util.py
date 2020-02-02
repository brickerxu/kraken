# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/7/4
# @file util.py

import re
from os import path

NUMBER_RE = re.compile(r'^[0-9]+$')


def is_null(string):
    return string is None or string == ''


def is_number(string):
    return not NUMBER_RE.match(string) is None


def get_parent_dir(file):
    if is_null(file):
        return None
    return path.abspath(path.dirname(file) + path.sep + ".")
