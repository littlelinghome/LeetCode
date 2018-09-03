#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 下午5:30
# @Author  : littlelinghome
# @Site    : 
# @File    : removeduplicates.py
# @Software: PyCharm

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

说明:
请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
"""

#已排序列表，将nums[i]与之后的数据进行比较删除，遍历完成后，再将num[i+1]与之后的数据进行比较

nums = [0,0,0,0,0,0,0,1,1,1,2,2,3,3,5]
print(nums[7:])



def removeduplicates(nums):
    for i in range(len(nums)):
        for j in nums[i+1:]:
            if nums[i] == j:
                nums.remove(nums[i])
            else:
                break
    return nums

print(removeduplicates(nums))



"""
for 循环 不能修改迭代变量
如果想要修改循环变量的取值，可以换while循环
"""

