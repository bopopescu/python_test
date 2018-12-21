# -*- coding: utf-8 -*-

# @Time    : 2018/10/12 16:08
# @Author  : songq001
# @Comment :

import types
import json
import re
import string
import random
import time
from datetime import date, timedelta


# eval()方法二次封装
def eval_str(str_data):
    # eval()对特殊值处理
    null = ""
    true = True
    false = False
    return eval(str_data)


def is_numeric(s):
    if str(s).startswith("-") or str(s).startswith("+") or "." in s:
        return all(c in "0123456789.+-" for c in s)
    else:
        return all(c in "0123456789" for c in s)


# 获取复杂嵌套list，json对应的下标（key）值, 可以去到任意值
# 格式：keytag： "2.a"      dict_data：[{"a": "111", "b": 222}, "bbbb", {"a": "555", "b": 222}]
def get_nestdict_value(keytag, dict_data):
    """
    :param keytag: 目标key，嵌套则用key1.key2  或者 key1.0.key2
    :param dict_data: 要查询的字典
    :return: 
    """
    if type(dict_data) not in [types.ListType, types.DictType]:
        # dict_data = json.loads(dict_data)
        dict_data = eval_str(dict_data)  # 效果同上
    sname = keytag.strip()
    obj = scmd = realval = ""
    for i in sname.split("."):
        if is_numeric(i):
            obj = "%s[%s]" % (obj, i)
        else:
            obj = "%s['%s']" % (obj, i)
    scmd = "%s%s" % ("dict_data", obj)
    try:
        realval = eval(scmd)
    except Exception, e:
        print e.message
        return "[Failed]:cmd change error,eval(%s)" % scmd
    return realval


def my_t_01():
    json_t = [{"is_deleted": 0, "subnet_id": None,
               "vpc_info": {"zone_id": "1", "tenant_id": "a7ee782a867c4447b5628a597b165436", "public": True,
                            "project": {"updated_date": "2018-09-14 15:32:34", "status": "active", "is_deleted": 0,
                                        "name": "auto_test", "update_openstack_flag": None,
                                        "tenant_id": "a7ee782a867c4447b5628a597b165436", "enabled": True,
                                        "create_security_group_flag": True, "created_date": "2018-09-14 15:32:31",
                                        "deleted_date": None, "create_openstack_flag": True,
                                        "id": "7c6e89dac1964d79ada8665c5b915c52", "desc": "Auto_自动化测试数据，勿动"},
                            "state": "up", "created_date": "2018-09-14 16:03:01", "cidr": "100.69.4.0/24",
                            "project_id": "7c6e89dac1964d79ada8665c5b915c52", "id": "7cd61f81167f4af4867adca0cfcee0bd",
                            "tenant": {"updated_date": "2018-09-14 15:31:03", "is_deleted": 0, "name": "test",
                                       "enabled": True, "created_date": "2018-09-14 15:30:47",
                                       "desc": "Auto_云管自动化脚本数据，勿动", "id": "a7ee782a867c4447b5628a597b165436",
                                       "cmdb_tenant_id": "ch"}, "name": "auto_test_slave"},
               "service_ip": "100.69.4.106", "service_id": "832adc597b1b4051812501edbc7ee6f1",
               "vpc_id": "7cd61f81167f4af4867adca0cfcee0bd", "id": "0ffb8963c3114ec18ab4794ffb485eda"}]
    json_t = eval(str(json_t).strip())
    print type(json_t) in [types.ListType, types.DictType]
    print json_t
    print get_nestdict_value("0.id", json_t)
    print json_t[0]["id"]


def my_t_02():
    """
    关于python2中的unicode和str以及python3中的str和bytes
    https://www.cnblogs.com/yangmingxianshen/p/7990102.html
    :return: 
    """
    my_bytes = 'byte类型'
    print type(my_bytes)
    # str to bytes
    # my_bytes_02 = my_bytes.encode('utf-8')      # 通过encode()把str转成byte  注：python3中的方法， python2报错
    # my_bytes_02 = bytes(my_bytes, encoding='utf8')  # 效果同上    注：python3中的方法， python2报错
    # print type(my_bytes_02)

    # bytes to str
    # my_bytes_03 = my_bytes_02.decode('utf-8')
    # my_bytes_03 = str(my_bytes_02, encoding="utf-8")

    my_bytes_00 = unicode(my_bytes, encoding='utf-8')
    my_bytes_001 = my_bytes.decode('utf-8')  # 效果同上
    print type(my_bytes_00)
    print type(my_bytes_001)
    print type(u'byte类型')
    print my_bytes
    print u'byte类型'


def dcit_te_02():
    dict01 = {"a": 11, "b": 2222}
    print "a" in dict01  # True
    print 2222 in dict01  # False


def dict_handle(dict_data):
    """
    该方法处理json嵌套中，嵌套的json和list是str类型。则需要eval处理。 eg: {"a": "[]"}  --> {"a": []}
    :param dict_data: 
    :return: 
    """
    if type(dict_data) in [types.DictType]:
        for k, v in dict_data.items():
            if type(v) in [types.StringType, types.UnicodeType] and (str(v).startswith("[") or str(v).startswith("{")):
                v1 = eval_str(v)
                dict_data[k] = v1
            else:
                pass
    elif type(dict_data) in [types.ListType]:
        for l in dict_data:
            dict_handle(l)
    return dict_data


def sometest_do_here():
    """
    需要做一些验证的测试，可以写在此方法
    :return:
    """
    contant = {"flag": "Y",
               "applyBarInfo": "[{\"applicantNo\":\"440301199401010636\",\"applyBarCode\":\"1186020001394827\",\"insuredType\":null,\"firstPremium\":\"5170000\",\"applicantName\":\"晓玲\",\"checkReason\":null,\"productName\":\"招商仁和招享人生年金保险（2018）\",\"productCode\":\"2008\",\"applicantType\":\"01\",\"totalNUM\":\"4\",\"insuredNo\":null,\"insuredName\":\"晓玲\",\"relationship\":\"01\"},{\"applicantNo\":\"440301199401010636\",\"applyBarCode\":\"1186020001394928\",\"insuredType\":null,\"firstPremium\":\"5700000\",\"applicantName\":\"晓玲\",\"checkReason\":null,\"productName\":\"招商仁和招享人生年金保险\",\"productCode\":\"2002\",\"applicantType\":\"01\",\"totalNUM\":\"4\",\"insuredNo\":null,\"insuredName\":\"晓玲\",\"relationship\":\"01\"},{\"applicantNo\":\"110101198001010037\",\"applyBarCode\":\"1194040227849439\",\"insuredType\":\"01\",\"firstPremium\":\"2700000\",\"applicantName\":\"皮银一\",\"checkReason\":null,\"productName\":\"招商仁和招享人生年金保险\",\"productCode\":\"2002\",\"applicantType\":\"01\",\"totalNUM\":\"4\",\"insuredNo\":\"110100200301010016\",\"insuredName\":\"银保皮二\",\"relationship\":\"03\"},{\"applicantNo\":\"110101199401010313\",\"applyBarCode\":\"1194040227959340\",\"insuredType\":\"01\",\"firstPremium\":\"3080000\",\"applicantName\":\"杨希\",\"checkReason\":null,\"productName\":\"招商仁和招享人生年金保险\",\"productCode\":\"2002\",\"applicantType\":\"01\",\"totalNUM\":\"4\",\"insuredNo\":\"110101199401011367\",\"insuredName\":\"馁李\",\"relationship\":\"02\"}]"}
    contant00 = "[{\"a\": \"bbbb\"}]"
    print contant00.startswith("[")
    print type(json.loads(contant00))
    print json.loads(json.dumps(contant))  # json.loads() 会把str转成Unicode
    print type(json.loads(json.dumps(contant)))
    print type(contant)
    contant01 = dict_handle(contant)
    print contant01
    print type(contant01)
    print get_nestdict_value("applyBarInfo.0.applyBarCode", contant01)


def sometest_do_here02():
    """
    random测试
    :return:
    """
    print(random.randint(1, 10))        # 产生 1 到 10 的一个整数型随机数
    print(random.random())              # 产生 0 到 1 之间的随机浮点数
    print(random.uniform(1.1, 5.4))     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
    print(random.choice('tomorrow'))    # 从序列中随机选取一个元素
    print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数

    a = [1, 3, 5, 6, 7]
    random.shuffle(a)                   # 将序列a中的元素顺序打乱
    print(a)

    print string.ascii_letters, string.digits, type(string.digits)
    print random.choice(string.digits)+random.choice(string.ascii_letters)


def list_removal(v_list):
    """
    list去重
    :param v_list: 
    :return: 
    """
    v_list02 = []
    for v in v_list:
        if v not in v_list02:
            v_list02.append(v)
    return v_list02


if __name__ == '__main__':
    pass
    # my_t_02()
    # dict_01 = {"pageIndex": "0", "agentNo": "", "pageSize": "10", "posType": "P", "serviceItems": "23", "pip23": {"idNo": "", "policyNo": "", "clientName": "彭"}}
    # print get_nestdict_value("pip23.clientName", dict_01)

    sometest_do_here02()

    print "$g_idcard*2$*".find("*")

    a = +100
    b = -100
    c = '100'
    # print is_numeric(a), is_numeric(b), is_numeric(c)
    i = 'str(3006)'
    print i[i.find('(')+1:-1]

    print type(time.strftime("%Y-%m-%d", time.localtime()))
    print type(date.today())
    print (date.today() + timedelta(days=int(7))).strftime('%Y-%m-%d')

    list0001 = ["运营支持平台建设项目","银保通平台优化项目","研发支持平台","渠道管理平台优化项目","监管平台优化项目","营销支持平台建设项目","研发支持平台","仁和财务平台优化项目","招商金融办公平台","招商金融人力资源管理平台","招商金融财务操作中心平台建设项目","仁和风险管理系统建设项目","招商金融审计数据分析系统项目","云门户","云管平台","云自动化引擎","云存储","云主机","研发支持","研发支持平台","金控监管管理系统","研发支持","客户服务平台建设项目","金科其它研发工作","招融通达项目","金科研发过程改进咨询项目","第三方开放平台","移保通收银台","仁和财务平台优化项目","云主机","金控监管管理系统","研发支持平台","招商金融风险管理平台","招商金融财务操作中心平台建设项目","招商金融人力资源管理平台","仁和财务平台优化项目","仁和财务平台优化项目","仁和财务平台优化项目","运营支持平台建设项目","运营支持平台建设项目","运营支持平台建设项目","运营支持平台建设项目","运营支持平台建设项目","云自动化引擎","仁和风险管理系统建设项目","云管平台","云存储","云备份","云监控","云门户项目","用户接触平台","营销支持平台建设项目","营销支持平台建设项目","营销支持平台建设项目","营销支持平台建设项目","银保通平台优化项目","银保通平台优化项目","渠道管理平台优化项目","渠道管理平台优化项目","监管平台优化项目","招融通达项目","大数据平台建设项目","客户服务平台建设项目","客户服务平台建设项目","在线投保","金科招聘管理系统","仁和在线服务","和宝宝项目","仁和在线服务","法人业务大平台建设项目","法人业务大平台建设项目","法人业务大平台建设项目","海达优智保PC版项目","增值服务管理系统建设项目","集成协作平台","快乐招融","招商金融办公平台","招融通达项目","用户接触平台","集团影像平台","金科招聘管理系统","金科其它研发工作","招商平安资产核心系统建设项目","招商金融人力资源管理平台","招商金融风险管理平台","研发支持平台","快乐招融","招商平安资产核心系统建设项目","招融通达项目","研发支持平台","集成协作平台","集成协作平台","招融通达项目","招融通达项目","营销支持平台建设项目","招商金融办公平台","法人业务大平台建设项目","运营支持平台建设项目"]
    list0002 = list_removal(list0001)

    for k in list0002:
        print k



