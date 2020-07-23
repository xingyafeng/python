#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
from collections import deque

# 列表是一个序列，用于顺序的存储数据的，也可以说是顺序存储数据的一个容器。
def test_list_features():
    # type: () -> test_list_features()
    """
    :rtype: object
    """
    logging.debug("test list ...")

    a = [1, 2, 3, 4, 5, 5, 5, ]
    print a

    a.reverse()
    print a
    a.sort()
    print a

    a.append('dd')
    print a
    a.pop()
    print a
    print a + [0, 0, 0, 0, 0]

    quene = deque(["a", "b", "c"])
    quene.append("d")
    quene.append("e")
    print quene.popleft()
    print quene
    del quene[2]
    print quene

    for i, v in enumerate(['a', 'b', 'c']):
        print i, v
