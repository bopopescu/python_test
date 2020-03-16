# -*- coding: utf-8 -*-

# @Time    : 2019/6/9 19:45
# @Author  : Administrator
# @Comment : 清楚pyc文件        https://www.cnblogs.com/love9527/p/8036867.html


import os

path = 'E:\work_2\github0102\python_test\PythonPractice\Practice01'        # project-path
print(os.walk(path))

for prefix, dirs, files in os.walk(path):     # os.walk:os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下
    for name in files:
        if name.endswith('.pyc'):
            filename = os.path.join(prefix, name)
            os.remove(filename)


# for prefix, dirs, files in os.walk(path):
#     print prefix, dirs, files
