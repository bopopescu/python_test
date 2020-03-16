# -*- coding: utf-8 -*-

# @Time    : 2020/3/16 23:46
# @Author  : Administrator
# @Comment : 

from properties import parse
import logging
from functools import wraps
# from logger.log import get_logger
import traceback
import time
import os

file_path = 'log.properties'
props = parse(file_path)  # 读取文件


def logger():
    level = props.get("level")
    log_format = props.get("format")
    # log_datefmt = props.get("datefmt")
    log_file = props.get("filename")
    log_filemode = props.get("filemode")

    if level == "DEBUG":
        log_level = logging.DEBUG
    elif level == "WARNING":
        log_level = logging.WARNING
    elif level == "ERROR":
        log_level = logging.ERROR
    elif level == "CRITICAL":
        log_level = logging.CRITICAL
    else:
        log_level = logging.INFO

    # 第一步，创建一个logger
    loggerL = logging.getLogger()
    loggerL.setLevel(log_level)      # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    # log_name = log_path + rq + '.log'
    # logfile = log_name
    fh = logging.FileHandler(log_file, mode=log_filemode)
    fh.setLevel(logging.DEBUG)      # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    loggerL.addHandler(fh)
    return loggerL


# 使用装饰器并记录log
# def decoratore(func):
#     @wraps(func)
#     def log(*args,**kwargs):
#         try:
#             print("当前运行方法",func.__name__)
#             return func(*args,**kwargs)
#         except Exception as e:
#             get_logger().error(f"{func.__name__} is error,here are details:{traceback.format_exc()}")
#     return log
#
# @decoratore
# def start():
#    print("666")


if __name__ == '__main__':
    logger = logger()
