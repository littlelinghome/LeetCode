#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 下午2:53
# @Author  : littlelinghome
# @Site    : 
# @File    : longestcommonprefix_两两比较.py
# @Software: PyCharm


def longestcommonprefix(strs):
    if strs is None or len(strs) == 0:
        return ''
    res = strs[0]
    for i in range(1,len(strs)):
        tmp = res   #每一次比较之后，这个临时变量都会随之改变
        res = ''
        for j in range(min(len(strs[i]),len(tmp))):
            #第一轮比较：strs第一个元素和第二个元素比较；第二轮：strs第二个元素和tmp比较（tmp是第一轮比较的结果）；第三列;strs第三个元素和tmp比较（tmp是第二轮比较的结果）
            if tmp[j] == strs[i][j]:
                res += tmp[j]
            else:
                break
    return res


res = longestcommonprefix(["flower","flow","flight"])
print(res)