#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 16:09
# @Author  : Vichayturen
# @email   : 1073931273@qq.com
# @Description
#          :

def saveDataToTxt(data, toPath):
    with open(toPath, "w", encoding="utf-8") as f:
        f.write(data)
    print("向\033[0;36;40m{}\033[0m文件中写出文本已完成".format(toPath))

def loadDataFromTxt(fromPath):
    with open(fromPath, "r", encoding="utf-8") as f:
        data = f.read()
    print("从\033[0;36;40m{}\033[0m文件中读入文本已完成".format(fromPath))
    return data