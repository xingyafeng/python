#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import sys

def set_log_format():
    """
     logging.basicConfig函数对日志的输出格式及方式做相关配置logger = logging.getLogger(__name__)
    """
    logging.basicConfig(level=logging.NOTSET,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %('
                               'message)s'
                        )

def get_cur_info():
    print sys._getframe(0).f_code.co_name  #
    print sys._getframe().f_lineno  # 当前行号