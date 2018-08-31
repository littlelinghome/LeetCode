#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 下午2:33
# @Author  : littlelinghome
# @Site    : 
# @File    : removeduplicates_2.py
# @Software: PyCharm


# 已排序列表，直接此次循环结束，然后将num[i+1]之后的数据进行比较


nums = [0,0,1,1,1,2,2,3,3,4]

def removeduplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i])
        else:
            i = i + 1
    return nums

print(removeduplicates(nums))