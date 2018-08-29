#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 下午3:35
# @Author  : littlelinghome
# @Site    : 
# @File    : isvalid.py
# @Software: PyCharm


"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 :
输入: "()"
输出: true

输入: "()[]{}"
输出: true

输入: "(]"
输出: false

输入: "([)]"
输出: false

输入: "{[]}"
输出: true
"""


def isvalid(s):
    L = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            L.append(i)
        else:
            if len(L) == 0:
                return False
            else:
                ss = L.pop()
                if (ss == '(' and i == ')') or (ss == '[' and i == ']') or (ss == '{' and i == '}'):
                    continue
                else:
                    return False

    if len(L) != 0:
        return False

    return True

print(isvalid('{[]}'))




