#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging


def test_string_features():
    """
    test_string_features
    :rtype: null
    """
    string = 'abc'
    logging.debug('test string features ...')
    print "@" * 60

    path1 = r'C:\some\name'
    path2 = 'C:\some\name'
    print path1
    print path2

    print '#' * 20

    print """\
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """

    print "ac" "bd"

    text = 'Put several strings within parentheses ' \
           'to have them joined together.'

    print text

    print text + " Connect on."

    for s in string:
        print s

    print '&' * 60
    print string[0]
    print string[-1]
    print string[len(string) - 1]
    print string[:2] + string[2:]
    # ??????????????:
    print string[1:100]
    print string[100:]

    # 7. https://docs.python.org/zh-cn/2.7/library/stdtypes.html#typesseq
    # 5.6.2. String Formatting Operations

    print '   spacious   '.strip()

    print '%(language)s has %(number)03d quote types.' % \
          {"language": "Python", "number": 2}

    # 8 Unicode Strings
    print u'Hello World !'
    print u'Hello\u0020World !'
    print ur'Hello\u0020World !'
    print ur'Hello\\u0020World !'

    print u"abc"
    # print string(u"abc")

    print '---' * 20

    # 一、字符串的定义
    s = 'hello python'
    s = "hello python"
    s = '''hello python'''
    s = """hello python"""

    print s

    # 二、字符串的操作
    string = '123456789'
    print string[0:3]  # 截取第一位到第三位的字符
    print string[:]  # 截取字符串的全部字符
    print string[6:]  # 截取第七个字符到结尾
    print string[:-3]  # 截取从头开始到倒数第三个字符之前
    print string[2]  # 截取第三个字符
    print string[-1]  # 截取倒数第一个字符
    print string[::-1]  # 创造一个与原字符串顺序相反的字符串
    print string[-3:-1]  # 截取倒数第三位与倒数第一位之前的字符
    print string[-3:]  # 截取倒数第三位到结尾
    print string[:-5:-3]  # 逆序截取，具体啥意思没搞明白？

    # string[0] = 10  # 会报出TypeError的错误，由此我们可以看出字符串是不可变的

    for i in string:
        print i

    # 字符串常用方法详解

    # 1. join 将可迭代对象转换成字符串，参数是可迭代对象，接收者是分隔符
    lst = ['lan', 'yu', 'lei']
    print ';'.join(lst)  # 以逗号为分隔符来将列表中的所有元素连接成字符串

    # 2. 分割操作

    # ** split **
    # split 将字符串转换成一个可迭代对象，默认是根据空格来分割的，若是有多个连续的空格会当做一个空格来识别，可传递参数指定分隔符是什么。
    strings = 'lan       yu lei'

    # split 从左往右分割字符串，maxsplit参数表示分割多少次，默认值为-1，表示分割所有分割符, 注意2.x版本
    # print strings.split(" ", 1)

    # ** rsplit **
    print strings.rsplit(" ", -1)

    # 3. 字符串的书写规范
    s = 'test'
    print 's.upper() = ' + s.upper()  # 转换成大写
    print 's.lower() =  ' + s.lower()  # 转换成小写
    print 's.title() =  ' + s.title()  # 将每个单词的首字母转换成大写
    print 's.capitalize() =  ' + s.capitalize()  # 只将这一组字符串的首字母转换成大写
    # print 's.casefold() =  ' + s.casefold()  # 不同的平台有不同的表现形式，但是同一平台下，变现形式相同
    print 's.swapcase() =  ' + s.swapcase()  # 大小写互相转换，将这组数据中的大写变成小写，小写变成大写
    # print '\\t.expandtabs() = '  '\t'.expandtabs(4)  # 将table转换成空格，在这里的含义是：将table转换成 4 个空格

    # 4. 字符串的修改
    # 5. 字符串的查找
    # 6. 字符串的判断

    # 三、字符串与bytes

    # 四、字符串格式
