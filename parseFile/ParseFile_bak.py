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
    num = 0
    list01 = []
    list02 = []
    try:
        read_content_list = vfile.readlines()
        for line in read_content_list:
            if "Resource" in line:
                line = line.replace("html_model", "html_model_new")
                new_list.append(line)
            elif line.startswith("    ") and line.find("[Tags]") == -1 and line.find("[Template]") == -1 and line.find("[Documentation]") == -1 and "..." not in line:
                del list01[:]
                del list02[:]
                list_end = []
                line = line.strip()
                line_list = line.split("    ")
                list01 = line_list[0].split(":")[0].split(";")
                list02 = line_list[0].split(":")[1].split(";")
                # 先清除list_api原有的元素，确保只保留当前处理的接口数据
                del list_api[:]
                # 拆分旧案例第一列
                for i in range(len(list02)):
                    if len(list01) == 1:
                        list_api.append(list01[0] + ":" + list02[i])
                    else:
                        list_api.append(list01[i] + ":" + list02[i])

                length_oneline_api = (len(line_list) - 1) / 2
                db_num = len(re.findall("\.db", "".join(list02[:length_oneline_api+1])))         # 尽可能处理接口之间有db处理的情况
                dmldb_num = len(re.findall("\.dmldb", "".join(list02[:length_oneline_api+1])))
                num = length_oneline_api + db_num + dmldb_num
                # 拼成新模板用例 存入list_end
                for k in range(num):
                    list_end.append(list_api[k])
                    # 若.db 或者 .dmldb在最后，则不用做减
                    if num == len(list_api) - length_oneline_api - 1 and ".db" in list_api[-1]:
                        db_num = db_num - 1
                    elif num == len(list_api) - length_oneline_api - 1 and ".dmldb" in list_api[-1]:
                        dmldb_num = dmldb_num - 1
                    # 处理拼接
                    if ".db" not in list_api[k] and ".dmldb" not in list_api[k]:
                        list_end.append(line_list[2 * (k - db_num - dmldb_num) + 1])
                        list_end.append(line_list[2 * (k - db_num - dmldb_num) + 2])
                # 把新模板list_end转成ride规范格式
                line_new = "    "
                for j in list_end:
                    line_new = line_new + j + "    "
                # print line_new.rstrip()
                new_list.append(line_new.rstrip())
            elif "..." in line:
                list_end = []
                line = line.strip()
                line_list = line.split("    ")
                # print line_list
                length_oneline_api = (len(line_list) - 1) / 2
                db_num = len(re.findall("\.db", "".join(list02[num+1:num+length_oneline_api+1])))         # 尽可能处理接口之间有db处理的情况
                dmldb_num = len(re.findall("\.dmldb", "".join(list02[num+1:num+length_oneline_api+1])))
                for i in range(length_oneline_api + db_num + dmldb_num):
                    list_end.append(list_api[num + i])
                    # 若.db 或者 .dmldb在最后，则不用做减
                    if num == len(list_api) - length_oneline_api - 1 and ".db" in list_api[-1]:
                        db_num = db_num - 1
                    elif num == len(list_api) - length_oneline_api - 1 and ".dmldb" in list_api[-1]:
                        dmldb_num = dmldb_num - 1
                    # 处理拼接
                    if ".db" not in list_api[num + i] and ".dmldb" not in list_api[num + i]:
                        list_end.append(line_list[2 * (i-db_num-dmldb_num) + 1])
                        list_end.append(line_list[2 * (i-db_num-dmldb_num) + 2])
                num = num + length_oneline_api + db_num + dmldb_num
                # 把新模板list_end转成ride规范格式
                line_new = "    ...    "
                for j in list_end:
                    line_new = line_new + j + "    "
                # print line_new.rstrip()
                new_list.append(line_new.rstrip())
            else:
                new_list.append(line)
    finally:
        vfile.close()
    return new_list


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
        f.truncate()  # 写入前清空文件
        for li in txt_list:
            if li.startswith("    ") and li.find("[Tags]") == -1 and li.find("[Template]") == -1 and li.find("[Documentation]") == -1:  # 一个案例处理完后加一行回车
                f.write(li + "\n")
            else:
                f.write(li)


file_path = os.getcwd() + r"/" + u"01案例样例01.txt"
# file_path = os.getcwd() + r"/" + u"01新单录入.txt"
# file_path = os.getcwd() + r"/" + u"14承保流程.txt"

print parse_txtfile(file_path)

new_file = "new_file.txt"
write_new_txt(parse_txtfile(file_path), new_file)


