#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 11:44
# @Author : maxu


# list是一种有序的集合，可以随时添加和删除其中的元素;list里面的元素的数据类型也可以不同
classmates = ['1', '2', '3']
classmates.append('4') #列表最后位置添加4
classmates.insert(3,'Ture') #列表第4个位置添加布尔True
classmates[1]='22222' #列表第2的位置换成22222字符串
print(len(classmates)) #执行完以上命令后输出列表长度
classmates.pop() #列表最后位置的元素删除
print(classmates)
print(classmates[2]) #第3个
print(classmates[-1]) #倒数第1个
list1 = ['a',True,123,['A','B','C']] #list元素也可以是另一个list
print(list1)
list2 =[] #如果一个list中一个元素也没有，就是一个空的list，它的长度为0
print(len(list2))