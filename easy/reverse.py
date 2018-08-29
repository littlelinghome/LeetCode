#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 下午8:04
# @Author  : littlelinghome
# @File    : reverse.py
# @Software: PyCharm

"""
给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 :
输入: 123
输出: 321

输入: -123
输出: -321

输入: 120
输出: 21
"""


# 传统算法
def reverse1(x):
    if x > 0:
        new_x = 0
        while x > 0:
            value = x % 10  #模10，取个位数
            x = int(x / 10)  #除以10，取整数
            new_x = new_x * 10 + value
        if new_x >= -2 ** 31 and new_x <= 2 ** 31 -1:  #判断溢出
            return new_x
        else:
            return 0

    elif x < 0:
        x = -x
        new_x = 0
        while x > 0:
            value = x % 10
            x = int(x / 10)
            new_x = new_x * 10 + value
        if new_x >= -2 ** 31 and new_x <= 2 ** 31 -1:
            return -new_x
        else:
            return 0

    else:
        return 0



# python 切片算法
def reverse2(x):
    x = str(x)  #转换成字符串
    if x[0] == '-':   #为负数
        x = x[1:]   #从第一个数字开始取
        new_x = '-' + x[::-1]
    else:
        new_x = x[::-1]
    new_x = int(new_x)
    if new_x >= -2 ** 31 and new_x <= 2**31 - 1:
        return new_x
    else:
        return 0

