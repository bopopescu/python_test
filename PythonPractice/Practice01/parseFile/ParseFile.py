# -*- coding: utf-8 -*-

# @Time    : 2018/11/29 17:18
# @Author  : songq001
# @Comment : 

import os
import re


def parse_txtfile(in_file):
    """
    旧模板txt文件转成新模板txt文件处理： 处理data_source为新模板格式存入list
    :param in_file:
    :return:new_list[data_source]
    """
    vfile = open(in_file, "r")
    new_list = []
    list_api = []  # 换行时要上下拼装，故list_api需作为方法中全局变量
    list02 = []
    num = 0
    try:
        read_content_list = vfile.readlines()
        for line in read_content_list:
            # 公共处理
            length_oneline_api = line_parse(line)[1]
            line_list = line_parse(line)[0]

            if "Resource" in line:
                line = line.replace("html_model", "html_model_new")
                new_list.append(line)
            elif line.find("    ") != -1 and line.find("[Tags]") == -1 and line.find("[Template]") == -1 and line.find("[Documentation]") == -1 and "..." not in line:
                # 先清除list_api, list02原有的元素，确保只保留当前处理的接口数据
                del list_api[:]
                del list02[:]
                list02 = get_list_api(line_list)[0]
                list_api = get_list_api(line_list)[1]

                db_num = len(re.findall("\.db", "".join(list02[:length_oneline_api+1])))         # 尽可能处理接口之间有db处理的情况
                dmldb_num = len(re.findall("\.dmldb", "".join(list02[:length_oneline_api+1])))
                num = length_oneline_api + db_num + dmldb_num       # 存储num记录第一行处理到的接口节点。
                # 拼成新模板用例 存入list_end
                list_end = list_end_parse(db_num, dmldb_num, list_api, length_oneline_api, line_list, num=0)

                # 把新模板list_end转成ride规范格式后存入new_list
                new_list.append(list_end_to_ride("    ", list_end))

            elif "..." in line:
                db_num = len(re.findall("\.db", "".join(list02[num+1:num+length_oneline_api+1])))         # 尽可能处理接口之间有db处理的情况
                dmldb_num = len(re.findall("\.dmldb", "".join(list02[num+1:num+length_oneline_api+1])))

                # 拼成新模板用例 存入list_end
                list_end = list_end_parse(db_num, dmldb_num, list_api, length_oneline_api, line_list, num)

                num = num + length_oneline_api + db_num + dmldb_num
                # 把新模板list_end转成ride规范格式后存入new_list
                new_list.append(list_end_to_ride("    ...    ", list_end))

            else:
                new_list.append(line)
    finally:
        vfile.close()
    return new_list


def line_parse(line):
    """
    封装
    把处理每一行为用"    "分隔成list的方法，抽取出来方便直接调用
    :param line:
    :return:
    """
    line = line.strip()
    line_list = line.split("    ")
    # print line_list
    length_oneline_api = (len(line_list) - 1) / 2
    return line_list, length_oneline_api


def list_end_parse(db_num, dmldb_num, list_api, length_oneline_api, line_list, num=0):
    """
    封装
    重复方法抽取出来，处理返回最终需要的list
    :param num:
    :param db_num:
    :param dmldb_num:
    :param list_api:
    :param length_oneline_api:
    :param line_list:
    :return:list_end
    """
    list_end = []
    for i in range(length_oneline_api + db_num + dmldb_num):
        list_end.append(list_api[num + i])

        # 兼容处理num引用问题
        if num == 0:
            num01 = length_oneline_api + db_num + dmldb_num
        else:
            num01 = num

        # 先确定处理的行是否为单个接口最后一行：通过 --> num == len(list_api) - length_oneline_api - 1
        # 若为最后一行且.db 或者 .dmldb为最后一个接口，则不用做减     PS：最后两个接口若为： .db;.dmldb 或者.dmldb;.db的情况暂不考虑
        if num01 == len(list_api) - length_oneline_api - 1 and ".db" in list_api[-1]:
            db_num = db_num - 1
        elif num01 == len(list_api) - length_oneline_api - 1 and ".dmldb" in list_api[-1]:
            dmldb_num = dmldb_num - 1
        # 处理拼接
        if ".db" not in list_api[num + i] and ".dmldb" not in list_api[num + i]:
            list_end.append(line_list[2 * (i - db_num - dmldb_num) + 1])
            list_end.append(line_list[2 * (i - db_num - dmldb_num) + 2])
    return list_end


def get_list_api(line_list):
    """
    封装
    获取data_source第一列组装后的list    即： ["uw:interfaceName01", "uw:interfaceName02"]
    :param line_list:
    :return:
    """
    list_api = []
    list01 = line_list[0].split(":")[0].split(";")
    list02 = line_list[0].split(":")[1].split(";")
    # 拆分旧案例第一列
    for i in range(len(list02)):
        if len(list01) == 1:
            list_api.append(list01[0] + ":" + list02[i])
        else:
            list_api.append(list01[i] + ":" + list02[i])
    return list02, list_api


def list_end_to_ride(str_prefix, list_end):
    """
    封装
    把处理完成的新模板格式的list_end转成ride规范格式
    :return:
    """
    line_new = "" + str_prefix
    for j in list_end:
        line_new = line_new + j + "    "
        # print line_new.rstrip()
    return line_new.rstrip()                # 去除末尾的   "    "


def trip_list(vlist):
    """
    list中的str去掉尾部空格
    :param vlist:
    :return:
    """
    txt_list = []
    for li in vlist:
        li = li.rstrip()  # 去掉尾部空格
        txt_list.append(li)
    return txt_list


def write_new_txt(txt_list, new_file):
    """
    把list内容逐行写入txt
    :param txt_list:
    :param new_file:
    :return:
    """
    with open(new_file, "a+") as f:  # 以追加的方式
        f.truncate()                 # 写入前清空文件
        for li in txt_list:
            if li.find("    ") != -1 and li.find("[Tags]") == -1 and li.find("[Template]") == -1 and li.find("[Documentation]") == -1:  # 一个案例处理完后加一行回车
                f.write(li + "\n")
            else:
                f.write(li)


def batch_handle(in_param, out_path):
    """
    获取目录下文件，批量转换，若传单个txt，则转换单个
    :param vpath:
    :return:
    """
    if ".txt" in in_param:
        write_new_txt(parse_txtfile(in_param), out_path + "/" + os.path.splitext(os.path.split(in_param)[1])[0] + "_new.txt")
    else:
        list_dir = os.listdir(in_param)
        for vfile in list_dir:
            file_path = os.path.join(in_param, vfile)
            # print os.path.splitext(file_path)[0].decode("GBK")
            write_new_txt(parse_txtfile(file_path), out_path + "/" + os.path.splitext(os.path.split(file_path)[1])[0] + "_new.txt")


# file_path = os.getcwd() + r"/" + u"01案例样例01.txt"
# file_path = os.getcwd() + r"/" + u"01新单录入.txt"
# file_path = os.getcwd() + r"/" + u"14承保流程.txt"
# file_path = os.getcwd() + r"/" + u"01查询机构考勤.txt"

# print parse_txtfile(file_path)

# new_file = "new_file.txt"u
# write_new_txt(parse_txtfile(file_path), new_file)


# in_param = os.path.join(os.getcwd(), "file", u"01新单录入.txt")
in_param = os.path.join(os.getcwd(), "file")
out_param = os.path.join(os.getcwd(), "newfile")
batch_handle(in_param, out_param)

