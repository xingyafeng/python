#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import string

if __name__ == '__main__':
    pass
    # 常量
    print string.ascii_letters
    print string.ascii_lowercase
    print string.ascii_uppercase
    print string.digits
    print string.hexdigits
    print string.whitespace
    print '-'
    print string.letters
    print string.lowercase
    print string.uppercase

    # 方法
    str = 'tct'  # type: str
    print string.upper(str)
    print string.lower(str)
    print string.count(str, 't')
    print string.count(str, 'c')
    print string.count(str, 'a')
    print '--'
    print string.index(str, 't')
    print string.index(str, 'c')
    print string.split('t;c;t;1', ';', 2)
    print string.rsplit('t;c;t;2', ';', 2)
    print string.splitfields('t;c;t;3', ';', 3)
    print ' '.join('abcd')  # 每个后面添加
    print string.atof('123')  # 数字字符串转浮点数
    print string.lstrip(' s       t    r ')         # with leading whitespace removed. 移除前后的空格
    print string.rstrip('str')
    print string.swapcase('strDsssst')
    # print string.translate('123', 560)

