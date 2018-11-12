#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/12 16:22
# @Author : maxu

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 在Python中，迭代是通过for ... in来完成的

from collections import Iterable

d={'a':1,'b':2,'c':3}
for key in d:
 print(key)

# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

# 由于字符串也是可迭代对象，因此，也可以作用于for循环
for ch in 'ABCDE':
	print(ch)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

print(isinstance('abc',Iterable))
print(isinstance([1,2,3,4,5],Iterable))
print(isinstance([1234],Iterable))

# 对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['a','b','c']):
	print(i,value)