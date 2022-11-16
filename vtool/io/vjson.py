#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 11:01
# @Author  : Vichayturen
# @email   : 1073931273@qq.com
# @Description
#          :

import json

def saveDataToJson(data, toPath):
    with open(toPath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("向\033[0;36;40m{}\033[0m文件中导入数据已完成".format(toPath))

def loadDataFromJson(fromPath):
    with open(fromPath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("从\033[0;36;40m{}\033[0m文件中导出数据已完成".format(fromPath))
    return data
