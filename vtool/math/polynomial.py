#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/15 16:00
# @Author  : Vichayturen
# @email   : 1073931273@qq.com
# @Description
#          :

import numpy as np
import copy

class Polynomial:
    def __init__(self, factor:list):
        tmp_length = len(factor)
        for i in range(tmp_length):
            if factor[tmp_length-i-1] == 0:
                factor.pop(tmp_length-i-1)
            else:
                break
        self.factor = np.array(factor)
        self.degree = self.factor.size - 1

    def add(self, another):
        result_list = []
        operator1 = self.factor.tolist()
        operator2 = another.factor.tolist()
        result_degree = max([self.degree, another.degree])
        for i in range(result_degree - self.degree):
            operator1.append(0)
        for i in range(result_degree - another.degree):
            operator2.append(0)
        for i in range(result_degree+1):
            result_list.append(operator1[i]+operator2[i])
        return Polynomial(result_list)

    def sub(self, another):
        return self.add(another.mul_num(-1))

    def mul(self, another):
        result_list = []
        result_degree = self.degree + another.degree
        operator1 = self.factor.tolist()
        operator2 = another.factor.tolist()
        for i in range(result_degree - self.degree):
            operator1.append(0)
        for i in range(result_degree - another.degree):
            operator2.append(0)

        for i in range(result_degree+1):
            result_list_i = 0
            for j in range(i+1):
                result_list_i += operator1[j]*operator2[i-j]
            result_list.append(result_list_i)
        return Polynomial(result_list)

    def mul_num(self, x):
        operator = self.factor.tolist()
        for i in range(len(operator)):
            operator[i] *= x
        return Polynomial(operator)

    def pow(self, x):
        result = copy.deepcopy(self)
        for i in range(x-1):
            result = result.mul(self)
        return result

    def value(self, x):
        value = 0
        for i in range(self.factor.size):
            value += self.factor[i]*pow(x, i)
        return value

    def differentiate(self):
        result_list = []
        for i in range(1, self.factor.size):
            result_list.append(self.factor[i]*i)
        return Polynomial(result_list)

    def integrate(self):
        result_list = [0]
        for i in range(self.factor.size):
            result_list.append(self.factor[i]/(i+1))
        return Polynomial(result_list)

    def __str__(self):
        s = ""
        if self.factor.size == 0:
            return "0"
        for i in range(self.factor.size):
            s += str(self.factor[i])
            if i >= 1:
                s += "x"
            if i > 1:
                s += "^" + str(i)
            if i != self.factor.size - 1:
                s += "+"
        return s

