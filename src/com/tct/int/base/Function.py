#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 4.7. 函数定义的更多形式

def test_func_features(n):
    """
    文档格式
    :rtype: result
    """
    a, b = 0, 1
    result = []

    while a < n:
        result.append(a)  # see below
        print a,
        # print b,
        print '--'

        a, b = b, a + b

    return result


# 4.7.1. 参数默认值
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)

        if ok in ('y', 'ye', 'yes'):
            print 'haha ok...'
            return True

        if ok in ('n', 'no', 'nop', 'nope'):
            print 'haha nonono ...'
            return False

        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')

        print complaint


# 4.7.1. 参数默认值
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# 4.7.2. 关键字参数,没定义使用默认值
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "if you put", voltage, "volts through it."

    print "-- This parrot wouldn't", action,
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"


def cheeseshop(kind, *arguments, **keywords):
    print '@' * 40
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]


# 4.7.3. 任意的参数列表
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# 4.7.4. 解包参数列表

def counter():
    c = [0]

    def inc():
        c[0] += 1
        return c[0]

    return inc


if __name__ == '__main__':

    c = counter()
    for i in range(len("dfdfdfdfdff")):
        print '---*',
        print c()

    for i in 'abdfdf'[:]:
        print '---&',
        print c()

    print '-----' * 20
    # f = test_func_features(100)
    # print f
    # ask_ok('Do you really want to quit?')
    print f(1)
    print f(2)
    print f(3)

    parrot(1000)  # 1 positional argument
    parrot(voltage=1000)  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

    print "#@" * 20
    d = {"voltage": "four million", "state": "bleedin' demised", "action": "ZZZZZ"}
    parrot(**d)
    print "#@" * 20

    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shopkeeper='Michael Palin',
               client="John Cleese",
               sketch="Cheese Shop Sketch")

    args = [3, 6]
    print range(*args)

    # ------------------------------------------------------------------------------------------------------------分割线

    # 为什么要使用lambda函数? 解决什么问题？
    # 1、用lambda函数首先减少了代码的冗余
    # 2、用lambda函数，不用费神地去命名一个函数的名字，可以快速的实现某项功能
    # 3、lambda函数使代码的可读性更强，程序看起来更加简洁

    # lambda函数的语法是唯一的，其形式如下：
    # lambda argument_list:expersion

    # 匿名函数通常用于高阶函数的参数，当此函数非常短小的时候，就适合使用匿名函数
    # 匿名函数中不能出现if或者for等一些条件判断，循环的语句
    # 匿名函数(lambda表达式)，只能写在一行上，所以也有人也叫他单行函数
    #
    # 匿名函数的特点
    # 1、使用lambda来定义的
    # 2、# 参数列表不需要用括号
    # 3、冒号不是用来开始新语句块的
    # 4、没有return，最后一个表达式的值即返回值

    print 'lambda----'
    print lambda x: x + 1

    func = lambda x: x + 1
    print func(100)

    # 匿名函数参数详解

    # 1.没有参数
    print (lambda: 0)()  # 0 默认值

    # 2.位置参数
    print (lambda x, y: x + y)(3, 5)

    # 3. 默认参数
    print (lambda x, y=3: x + y)(5)

    # 4.关键字参数
    print (lambda *args: args)(*range(5))

    # 5. 多个关键字参数

    # 疑虑： 没看明白？如何执行的呢？
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print pairs
