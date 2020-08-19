#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import sys

class Log:
    """
    format logging
    """

    def __init__(self, name, level, mode):
        logging.basicConfig(filename=name,
                            level=level,
                            filemode=mode,
                            format='[ %(levelname)s %(asctime)s fileName: %(filename)s lineNo: %(lineno)d funcName: '
                                   '%(funcName)s ] %(message)s')

    @staticmethod
    def setConsole(level=logging.WARNING):
        log = logging.getLogger()
        console = logging.StreamHandler()
        console.setLevel(level)
        log.addHandler(console)
        return log


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
