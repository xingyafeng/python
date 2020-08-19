#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse

if __name__ == '__main__':
    """
    https://docs.python.org/zh-cn/2.7/library/argparse.html 参考实例
    """

    # (1) 声明一个parser
    parser = argparse.ArgumentParser()

    # (2) 添加参数
    parser.add_argument("parg")  # 位置参数，这里表示第一个出现的参数赋值给parg
    parser.add_argument('-d', "--digit", type=int, help="输入数字")  # 通过 --echo xxx声明的参数，为int类型
    parser.add_argument('-n', "--name", nargs=argparse.REMAINDER, required=False, help="名字",
                        default="cjf")  # 同上，default 表示默认值

    # (3) 读取命令行参数
    args = parser.parse_args()

    # (4) 调用这些参数
    print(args.parg)
    print("echo = {0}".format(args.digit))
    print("name = {0}".format(args.name))
