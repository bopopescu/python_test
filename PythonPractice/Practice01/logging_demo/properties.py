# -*- coding: utf-8 -*-

# @Time    : 2020/3/16 23:55
# @Author  : Administrator
# @Comment : https://www.cnblogs.com/EWWE/p/6979787.html

import re
import os
import tempfile


class Properties(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            fopen = open(self.file_name, 'r')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception, e:
            raise e
        else:
            fopen.close()

    def has_key(self, key):
        return key in self.properties

    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
        return default_value

    def put(self, key, value):
        self.properties[key] = value
        replace_property(self.file_name, key + '=.*', key + '=' + value, True)


def parse(file_name):
    return Properties(file_name)


def replace_property(file_name, from_regex, to_str, append_on_not_exists=True):
    tmpfile = tempfile.TemporaryFile()      # 创建一个临时文件对象

    if os.path.exists(file_name):
        r_open = open(file_name, 'r')
        pattern = re.compile(r'' + from_regex)
        found = None
        for line in r_open:
            if pattern.search(line) and not line.strip().startswith('#'):
                found = True
                line = re.sub(from_regex, to_str, line)
            tmpfile.write(line)
        if not found and append_on_not_exists:
            tmpfile.write('\n' + to_str)
        r_open.close()
        tmpfile.seek(0)                     # 将文件指针移到文件开始

        content = tmpfile.read()

        if os.path.exists(file_name):
            os.remove(file_name)

        w_open = open(file_name, 'w')
        w_open.write(content)
        w_open.close()

        tmpfile.close()
    else:
        print "file %s not found" % file_name


if __name__ == '__main__':
    file_path = 'log.properties'
    props = parse(file_path)  # 读取文件
    # props.put('key_a', 'value_a')  # 修改/添加key=value
    print props.get('level')  # 根据key读取value
    print "props.has_key('key_a')=" + str(props.has_key('key_a'))  # 判断是否包含该key

