#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class MyClass:
    id = '1001'
    __Name = 'ttt'

    def __init__(self, name):
        print self.__Name
        self.name = name
        self.tricks = list()

    @staticmethod
    def f():
        print MyClass.__Name
        return 'hello python'

    def add_trick(self, trick):
        print self.__Name
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
    x.f()
    y.f()

    x.age = 100
    print x.age
    # del x.age
    # print MyClass.__Name

    print hasattr(x, 'age')
    print getattr(x, 'age')
    print setattr(x, 'age', 200)
    print delattr(x, 'age')
