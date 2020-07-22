#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from com.tct.int.base.Num import test_num_features
from com.tct.int.base.String import test_string_features
from com.tct.int.base.List import test_list_features
from com.tct.int.tools.utils import set_log_format

if __name__ == '__main__':
    set_log_format()

    print 'main'

    test_string_features()
    test_num_features()
    test_list_features()
