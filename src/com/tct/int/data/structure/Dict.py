#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test_dict():
    """
    另一个非常有用的 Python 內置数据类型是 字典 (参见 映射类型 — dict)。
    字典在其他语言里可能会被叫做 联合内存 或 联合数组。
    与以连续整数为索引的序列不同，字典是以 关键字 为索引的，
    关键字可以是任意不可变类型，通常是字符串或数字。
    如果一个元组只包含字符串、数字或元组，那么这个元组也可以用作关键字。
    但如果元组直接或间接地包含了可变对象，那么它就不能用作关键字。
    列表不能用作关键字，因为列表可以通过索引、切片或 append() 和 extend() 之类的方法来改变。

    字典主要的操作是使用关键字存储和解析值。也可以用 del 来删除一个键值对。
    如果你使用了一个已经存在的关键字来存储值，那么之前与这个关键字关联的值就会被遗忘。
    用一个不存在的键来取值则会报错。
    """
    tel = dict(jack=4098, sape=4139)
    tel['guido'] = 4127
    print tel['jack']
    print tel

    del tel['sape']
    print tel

    tel['irv'] = 4127
    print tel

    print tel.keys()
    print 'guido' in tel

    # 推导式
    print {x: x ** 2 for x in (2, 4, 6)}


if __name__ == '__main__':
    test_dict()
