# -*- coding: utf-8 -*-

# @Time    : 2018/12/20 0020 22:58
# @Author  : Administrator
# @Comment : jsonpath, jsonpath_rw 对嵌套json取值处理  https://mp.weixin.qq.com/s/xn2P2a7ixdfZFPq7UTWq0Q



import urllib2
import requests
import json
import jsonpath as jsonpath01
from jsonpath_rw import jsonpath, parse
import chardet
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# 移除SSL认证，控制台输出InsecureRequestWarning。
urllib3.disable_warnings(InsecureRequestWarning)
session = requests.session()

base_url = "https://jsonview.com"
url = "/example.json"

# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# html = response.read()

response = requests.get(base_url+url, verify=False)
html = response.text
# print html

null = ""
true = True
false = False
# print response.text
# jsonobj = response.json


# 把json格式字符串转换成python对象
# jsonobj = json.loads(html)

jsonobj = {"a": 1, "b": {"kk": {"nn": 111, "pp": "ppoii"}, "yy": "123aa", "uu": "777aa"},
              "c": [{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": ["ppp", 3, 4, True]}]}

# 从根节点开始，匹配name节点
# citylist = jsonpath01.jsonpath(jsonobj, '$..pp')            # '$..pp' 等同于 $.b.kk.pp
# citylist = jsonpath01.jsonpath(jsonobj, '$..b')
citylist = jsonpath01.jsonpath(jsonobj, '$..c[?(@.a>2)]')       # 取c中a>2的所有信息
# citylist = jsonpath01.jsonpath(jsonobj, '$.c[2].b[3]')

# 使用jsonpath_rw处理
citylist_rw = parse('$.c[2].b[3]')
citylist_tx = citylist_rw.find(jsonobj)
print citylist_tx
print type(citylist_tx)
print [match.value for match in citylist_tx]


print citylist
print(type(citylist))

fp = open('city.json', 'w')

content = json.dumps(citylist, ensure_ascii=False)
print content
fp.write(content.encode('utf-8'))

fp.close()


