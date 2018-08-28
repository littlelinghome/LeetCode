#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 下午8:45
# @Author  : littlelinghome
# @Site    : 
# @File    : ispalindrome.py
# @Software: PyCharm

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 :
输入: 121
输出: true

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""



def isPalindrome(x):
    l = len(str(x))
    c = str(x)
    if l == 1:
        b = 1
    else:
        for i in range(0,l - 1):
            if c[i] != c[l - i -1]:
                b = 0
                break
            else:
                b = 1
    if b == 1:
        return True
    else:
        return False

print(isPalindrome(1221))