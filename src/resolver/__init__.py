# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/2
# @file __init__.py

from .dmzj import Dmzj
from .tencent import Tencent


class Resolver(object):
    def __init__(self):
        dmzj = Dmzj()
        tencent = Tencent()
        self.resolvers = {dmzj.key(): dmzj, tencent.key(): tencent}
