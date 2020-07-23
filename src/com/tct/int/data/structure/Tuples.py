#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test_tuples():
    """
    我们看到列表和字符串有很多共同特性，例如索引和切片操作。他们是 序列 数据类型
    （参见 Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange）中的两种。
    随着 Python 语言的发展，其他的序列类型也会被加入其中。这里介绍另一种标准序列类型: 元组。
    """
    tt = 12345, 54321, 'hello!'  # 元组自动打包的过程
    t = (12345, 54321, 'hello!')
    print t[0]
    u = t, (1, 2, 3, 4, 5)
    print u
    print u[0]
    v = ([1, 2, 3], [3, 2, 1])
    print v

    empty = ()
    singleton = 'hello',  # <-- note trailing comma
    print len(empty)
    print len(singleton)
    print singleton
    print singleton[0]


if __name__ == '__main__':
    test_tuples()
