# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/10
# @file download.py

from resolver import resolverManager


def download(key, url):
    resolver = resolverManager.resolvers[key]
    resolver.crawl(url)
