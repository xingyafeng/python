#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from collections import deque
from math import pi


def test_list():
    """
    5.1. 列表的更多特性
    列表数据类型还有很多的方法
    这里是列表对象方法的清单
    """
    lst = list(range(0, 10))  # type: List[int]

    # 添加一个元素到列表的末尾
    lst.append(200)
    print lst

    # 在给定的位置插入一个元素。第一个参数是要插入的元素的索引，所以 a.insert(0, x) 插入列表头部， a.insert(len(a), x) 等同于 a.append(x) 。
    # 在某个位置插入元素
    lst.insert(2, -100)
    print lst

    # 计算某个元素在那个位置
    print lst.index(-100, 0, len(lst))

    # 移除某个元素
    lst.remove(1)
    print lst

    # 返回元素 x 在列表中出现的次数。
    print lst.count(-100)

    # 删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素。
    #  方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法)。
    print lst.pop()

    # 对列表中的元素进行排序
    lst.sort()
    print lst

    # Reverse the elements of the list, in place. 对列表中的元素进行反向排序，逆序排列
    lst.reverse()
    print lst


def stack():
    """
    5.1.1. 列表作为栈使用
    列表方法使得列表作为堆栈非常容易，最后一个插入，最先取出（“后进先出”）。
    要添加一个元素到堆栈的顶端，使用 append() 。要从堆栈顶部取出一个元素，使用 pop() ，不用指定索引。
    """
    lst = list(range(1, 8))

    lst.append(8)
    lst.append(9)

    print lst
    print lst.pop()
    print lst
    print lst.pop()
    print lst


def queue():
    """
    5.1.2. 列表作为队列使用
    列表也可以用作队列，其中先添加的元素被最先取出 (“先进先出”)；然而列表用作这个目的相当低效。
    因为在列表的末尾添加和弹出元素非常快，但是在列表的开头插入或弹出元素却很慢 (因为所有的其他元素都必须移动一位)。

    若要实现一个队列，可使用 collections.deque，它被设计成可以快速地从两端添加或弹出元素。
    """
    lst = deque(["Eric", "John", "Michael"])
    lst.append("zhangsan")
    lst.append("lisi")

    print lst
    print lst.popleft()
    print lst.popleft()
    print lst


def f(x): return x % 3 == 0 or x % 5 == 0


def cube(x): return x * x * x


def add(x, y): return x + y


def programming_tools():
    """
    5.1.3. Functional Programming Tools
    """
    print filter(f, range(2, 25))
    print map(cube, range(1, 11))

    seq = range(8)
    print seq
    print map(add, seq, seq)
    print reduce(add, range(1, 11))  # 同下，使用lambda替换add()
    print reduce(lambda x, y: x + y, range(1, 11))


def comprehension():
    """
    5.1.4. 列表推导式, 迭代器
    列表推导式提供了一个更简单的创建列表的方法。常见的用法是把某种操作应用于序列或可迭代对象的每个元素上，
    然后使用其结果来创建列表，或者通过满足某些特定条件元素来创建子序列。
    """
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # 创建一个平方列表
    squares = [x ** 2 for x in range(10)]
    print squares
    squares = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print squares

    vec = [-4, -2, 0, 2, 4]
    print [x * 2 for x in vec]
    print [x for x in vec if x > 0]
    print [abs(x) for x in vec]

    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print [weapon.strip() for weapon in freshfruit]

    print [(x, x ** 2) for x in range(8)]

    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print [num for elem in vec for num in elem]

    print [str(round(pi, i)) for i in range(1, 6)]

    print zip(*matrix)

    # 5.2. The del statement
    print 'del @@@'
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    print a
    del a[0]
    print a

    del a[2:4]
    print a

    del a[:]
    print a


if __name__ == '__main__':
    # test_list()
    stack()
    # queue()
    # programming_tools()
    # comprehension()stack
