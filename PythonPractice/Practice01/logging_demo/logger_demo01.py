# -*- coding: utf-8 -*-


# @Time    : 2020/3/16 23:16
# @Author  : Administrator
# @Comment : Logging 模块

from log_init import logger

logger = logger()


def hypotenuse(a, b):
    """
    勾股定理
    :param a:
    :param b:
    :return:
    """
    return (a**2+b**2)**0.5

logger.info("{a}, {b}的斜边是{c}".format(a=3, b=4, c=hypotenuse(a=3, b=4)))
logger.error("a={a}, b={b}, a不能为负数".format(a=-3, b=4, c=hypotenuse(a=3, b=4)))
logger.warning("a={a}, b={b}, a不能为负数".format(a=-3, b=4, c=hypotenuse(a=3, b=4)))
