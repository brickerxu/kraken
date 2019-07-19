# -*- coding:utf-8 -*-
# @author bricker
# @date 2019/7/19
# @file httputils.py

import os
import traceback
from urllib import request
from common import directory
from utils.util import *
from logger import logger


TAG = 'httputils'


'''
下载函数
@:param url 下载路径
@:param dist_path 下载目标路径
'''


def download(url, dist_path=None):
    if is_null(url):
        logger.debug(TAG, u'url is null')
        return None
    if is_null(dist_path):
        dist_path = directory.temp_dir
    if path.isfile(dist_path):
        dist_path = get_parent_dir(dist_path)
    if not path.exists(dist_path):
        os.makedirs(dist_path)

    file_name = url[url.rfind(r'/') + 1:len(url)]
    file_path = path.join(dist_path, file_name)
    if path.exists(file_path):
        os.remove(file_path)
    try:
        request.urlretrieve(url, file_path)
        logger.debug(TAG, u'文件下载完成[%s][%s]' % (url, file_path))
        return file_path
    except:
        exc = traceback.format_exc()
        logger.error(TAG, u'文件下载失败,url:%s' % url, exc)
    return None
