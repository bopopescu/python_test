# -*- coding: utf-8 -*-


# @Time    : 2020/3/16 23:16
# @Author  : Administrator
# @Comment : Logging 模块

"""
Python 中的 logging 模块可以让你跟踪代码运行时的事件，当程序崩溃时可以查看日志并且发现是什么引发了错误。
Log 信息有内置的层级——调试（debugging）、信息（informational）、警告（warnings）、错误（error）和严重错误（critical）

logging有 5 个不同层次的日志级别，可以将给定的 logger 配置为这些级别：
DEBUG：详细信息，用于诊断问题。Value=10。
INFO：确认代码运行正常。Value=20。
WARNING：意想不到的事情发生了，或预示着某个问题。但软件仍按预期运行。Value=30。
ERROR：出现更严重的问题，软件无法执行某些功能。Value=40。
CRITICAL：严重错误，程序本身可能无法继续运行。Value=50。

默认 logger 是root，其默认的 basicConfig 级别是WARNING。也就是说，只有来自logging.warning或者更高级别的信息才会被记录下来。
因此，logging.info()中的信息不会被打印出来。这也是为什么 basicConfig 被设为INFO

"""

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log_demo01.txt',
                    filemode='a')


def hypotenuse(a, b):
    """
    勾股定理
    :param a:
    :param b:
    :return:
    """
    return (a**2+b**2)**0.5

logging.info("{a}, {b}的斜边是{c}".format(a=3, b=4, c=hypotenuse(a=3, b=4)))
logging.error("a={a}, b={b}, a不能为负数".format(a=-3, b=4, c=hypotenuse(a=3, b=4)))
logging.warning("a={a}, b={b}, a不能为负数".format(a=-3, b=4, c=hypotenuse(a=3, b=4)))
