#!/usr/bin/env python
import sys

import pexpect

PROMPT = '[$#>]'  # ['#', '>>>', '>', '\$']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = "Are you sure you want to continue connecting"
    connStr = 'ssh ' + user + '@' + host

    print("ss = " + connStr)
    child = pexpect.spawn(connStr)
    # child.logfile = sys.stdout

    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        print('111')
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
        if ret == 0:
            print('[-] Error Connecting')
            return

    child.sendline(password)
    child.expect(PROMPT)

    return child


def main():
    host = "10.129.46.47"
    user = "yafeng.xing"
    password = "llf436502"

    child = connect(user, host, password)
    # send_command(child, 'touch ttt')

    child.sendline("ls -l")
    child.expect(PROMPT)
    print(child.before)


if __name__ == '__main__':
    main()
