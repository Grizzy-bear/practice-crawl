# encoding: utf-8
"""
@version:3.6
@author:lamplight
@file:03.py
@time:2018/1/2415:10
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/23/18 1:37 AM
# @Author  : Grizzly
# @Site    :
# @File    : 统计字段.py
# @Software: PyCharm
import pymongo
from bson import json_util as jsonb
import pandas as pd
from pandas.core.frame import DataFrame

clients = pymongo.MongoClient('localhost')
db = clients["ximalaya"]
# col2 = db["detaile2"].find({"album_title":"单田芳经典—封神演义"})
# -------------------------------------
# print(col2.find({"Key":"play_path"}))
# print(jsonb.dumps(list(col2.find({"Key":"play_path"}))))
# for cil in list(col2).:
#     print(cil)
# print(col2)
# print(type(dict(col2)))
# print(list(col2)[])
# --------------------------------------
# result=[]
# for x in col2:
#     result.append(x)
# data = DataFrame(result)
# print(data['play_path'][0])
# print(result)
# print(col2.count())
# col1 = db["detaile2"].aggregate([{$group:{"_id":{"title":"$title","count":{$sum:1}}}}])
col1 = db["detaile2"]
expa = [{"$group":{"_id":"$title", "num_tutor":{"$sum":1}}}]
data = col1.aggregate(expa)
# print(data)
for i in data:
    print(i)