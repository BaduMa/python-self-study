#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/12 16:51
# @Author : maxu

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print(list(range(1,11)))
# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
L =[]
for x in range(1,11):
	L.append(x*x)
print(L)

print([x*x for x in range(1,11)])  #列表生成式则可以用一行语句代替循环生成上面的list

# 表达式：写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用

print([x*x for x in range(1,11)if x%2==0])   #print里面整体作为一个列表

# 两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])  #n for m in 'ABC' 一层循环；  一层循环的值再次与XYZ循环

import os
print([d for d in os.listdir('.')])   #列出当前目录下的所有文件和目录名

d ={'X':1,'y':2,'z':3}  #for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
for k,v in d.items():
	print(k,'=',v)

d ={'X':'XXX','Y':'YYY','Z':'ZZZ'}   #列表生成式也可以使用两个变量来生成list
print([k+'='+v for k,v in d.items()])

L =['Hello','World','Jack']
print([s.lower() for s in L])  #把一个list中所有的字符串变成小写