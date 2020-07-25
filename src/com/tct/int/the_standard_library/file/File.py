#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import glob
import os
import sys
import time

import pexpect

from com.tct.int.tools.Utils import docmd, chdir

if __name__ == '__main__':

    t=''
    test_path = '/data/nishome/td/yafeng.xing/workspace/project/android'

    os.chdir(test_path)

    for oneDir in glob.glob("*"):
        if os.path.isdir(oneDir):
            print '----| start'

            print '---dir : ' + oneDir
            # print os.stat(oneDir).st_mtime
            # print time.time()
            # print time.time() - os.stat(oneDir).st_mtime
            mtime = time.time()
            print 'it is %s %s.%d' % (oneDir, oneDir, mtime)
            docmd('mv %s %s.%d' % (oneDir, oneDir, mtime))
            # docmd('sleep 1000s')
            docmd('rm -vrf %s.%d' % (oneDir, mtime))
            print '----| end'

    print chdir('/home')
