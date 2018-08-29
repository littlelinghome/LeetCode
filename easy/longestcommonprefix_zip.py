#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 下午2:26
# @Author  : littlelinghome
# @Site    : 
# @File    : longestcommonprefix_zip.py
# @Software: PyCharm

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例:

输入: ["flower","flow","flight"]
输出: "fl"

输入: ["dog","racecar","car"]
输出: ""
"""
###############################################################################

"""
python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素.
集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.

sets 支持 x in set, len(set),和 for x in set。
作为一个无序的集合，sets不记录元素位置或者插入点。
因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。

下面来点简单的小例子说明把。set 只接受一个参数（这个参数是可迭代对象：字符串，列表）
>>> x = set('spam')
>>> y = set(['h','a','m'])
>>> x
{'m', 'a', 'p', 's'}
>>> y
{'a', 'm', 'h'}
"""

###############################################################################

"""
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
zip()函数接受0个或多个序列作为参数，返回一个tuple列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
利用 * 号操作符，可以将元组解压为列表。

zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。



示例一（每个参数的长度一致）：
>>> x = [1,2,3]
>>> y = ['a','b','c']
>>> z = [4,5,6]
>>> zip_xyz = zip(x, y, z)
>>> print(zip_xyz)
<zip object at 0x7f7a92daaf48>
>>> print(list(zip_xyz))
[(1, 'a', 4), (2, 'b', 5), (3, 'c', 6)]


示例二（每个参数的长度不一致）：
>>> a = [1,2,3]
>>> b = [4,5,6,7]
>>> zip_ab = zip(a, b)
>>> print(zip_ab)
<zip object at 0x7f7a92daafc8>
>>> print(list(zip_ab))
[(1, 4), (2, 5), (3, 6)]


示例三（zip()对只有一个参数的处理）：
>>> c = ['a', 'b', 'c']
>>> zip_c = zip(c)
>>> print( zip_c)
<zip object at 0x7f7a92dbe088>
>>> print(list(zip_c))
[('a',), ('b',), ('c',)]


示例四 （zip(*list)也就是数组前面带个星号，是解压缩的操作）, * 只跟一个list参数
>>> zip(*[(1, 'a'), (2, 'b'), (3, 'c')])
<zip object at 0x7f7a92dbe248>
>>> a = zip(*[(1, 'a'), (2, 'b'), (3, 'c')])
>>> print(list(a))
[(1, 2, 3), ('a', 'b', 'c')]



示例四 （只对一个参数的解压）
>>> c
['a', 'b', 'c']
>>> zip_c = zip(*c)
>>> print(zip_c)
<zip object at 0x7f7a92dbe248>
>>> print(list(zip_c))
[('a', 'b', 'c')]

注：这个其实就是示例三的逆过程
"""




def longestcommonprefix(strs):
    if strs is None or len(strs) == 0:
        return ''
    for i in range(len(strs)):
        strs[i] = list(strs[i])
    tmp = zip(*strs)
    res = ''
    for i in tmp:
        if len(set(i)) == 1:
            res += i[0]
    return res



res = longestcommonprefix(["flower","flow","flight"])
print(res)