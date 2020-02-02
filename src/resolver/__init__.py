# -*- coding:utf-8 -*-
# @author bricker
# @date 2020/2/2
# @file __init__.py

from .dmzj import Dmzj
from .tencent import Tencent


resolvers = []

resolvers.append(Dmzj())
resolvers.append(Tencent())
