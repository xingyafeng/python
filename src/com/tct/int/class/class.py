#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class MyClass:
    id = '1001'

    def __init__(self, name):
        self.name = name
        self.tricks = list()

    @staticmethod
    def f():
        return 'hello python'

    def add_trick(self, trick):
        self.tricks.append(trick)


def __print():
    print "x.id = " + x.id
    print "y.id = " + y.id
    print "id   = " + MyClass.id
    print '--------- end '


if __name__ == '__main__':
    x = MyClass('x')
    y = MyClass('y')

    x.add_trick('a')
    y.add_trick('b')

    print x.tricks
    print y.tricks
    print x.name
    print y.name

    x.id = '5'
    __print()
    y.id = '10'
    __print()

