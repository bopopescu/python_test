# -*- coding: utf-8 -*-

# @Time    : 2018/10/23 14:48
# @Author  : songq001
# @Comment : 


"""
python2:
1.open  f = open('your_file.txt','r')
1、未指定文件编码格式，如果文件编码格式与当前默认的编码格式不一致，那么文件内容的读写将出现错误。 
2、如果读写文件有错误，会导致文件无法正确关闭。因为哪怕在后面有
python3:
f = open('your_file.txt', 'r', encoding='utf-8')

面的两种方式在python2和python3下都可以使用，因此如果想要让你的代码在2和3下都兼容的话可以尝试下面的两种方法：
python2 & python3
import codecs
f1 = codecs.open('your_file1.txt', 'r', 'utf-8') #使用codecs包
f1.close()
import io
f2 = io.open('your_file2.txt', 'r', encoding='utf-8') #使用io包
f2.close(

"""

file01 = open('demo01.txt', 'r+')
file_contant = file01.read()
print file_contant

import io
file_02 = io.open('demo01.txt', 'r', encoding='utf-8')
file_contant02 = file_02.read()
print file_contant02


import codecs
file_03 = codecs.open('demo01.txt', 'r', encoding='utf-8')
file_contant03 = file_03.read()
print file_contant03

