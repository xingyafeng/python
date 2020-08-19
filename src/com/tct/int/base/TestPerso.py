#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import commands
import datetime
import logging
import os
import re
import sys
from time import sleep

from com.tct.int.tools.utils import Log


def test_perso_func():
    """

    """
    starttime = datetime.datetime.now()
    sleep(1)
    endtime = datetime.datetime.now()
    print endtime - starttime

    print os.path.basename(sys.argv[0]).split('.')[0] + '.log'

    LOG = Log(os.path.basename(sys.argv[0]).split('.')[0] + '.log', logging.DEBUG, 'a')
    log = LOG.setConsole(level=logging.WARNING)
    log.info("test log info time consuming = %s  ", endtime - starttime)

    print os.path.abspath('')
    print os.getcwd()
    # cmd = 'ls * | egrep .py$'
    cmd = 'ls * | grep  perso'
    wimdata_path = commands.getoutput(cmd)
    st = commands.getstatusoutput(cmd)
    # 命令执行的结果 零 or 非零
    print st[0]

    # return text
    print wimdata_path.strip()

    # re.search()
