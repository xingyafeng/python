#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from com.tct.int.base.Num import test_num_features
from com.tct.int.base.String import test_string_features
from com.tct.int.base.List import test_list_features
from com.tct.int.base.TestPerso import test_perso_func
from com.tct.int.tools.utils import set_log_format, Log

if __name__ == '__main__':
    set_log_format()

    print 'main'

    # 数字
    # test_num_features()

    # 字符串
    # test_string_features()

    # 列表
    # test_list_features()

    test_perso_func()
