#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test_set():
    """
    Python也包含有 集合 类型。集合是由不重复元素组成的无序的集。它的基本用法包括成员检测和消除重复元素。
    集合对象也支持像 联合，交集，差集，对称差分等数学运算。

    花括号或 set() 函数可以用来创建集合。注意：要创建一个空集合你只能用 set() 而不能用 {}，
    因为后者是创建一个空字典，这种数据结构我们会在下一节进行讨论。
    """
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    fruit = set(basket)
    print fruit
    print 'orange' in fruit
    print 'crabgrass' in fruit

    a = set('abracadabra')
    b = set('alacazam')
    print a
    print b
    print a - b
    print a | b
    print a & b
    print a ^ b

    a = {x for x in 'abracadabra' if x not in 'abc'}
    print a


if __name__ == '__main__':
    test_set()
