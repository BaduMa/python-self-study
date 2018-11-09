#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 11:13
# @Author : maxu

#1.切片：取一个list或者tuple的部分元素
L = ['Mike','Jack','Bob','Tony']
#取前三个元素  即取0-（N-1）的元素
print(L[0:3])  #0-2元素
print(L[:3])   #0-2元素
print(L[1:3])  #从1开始取2个元素
print(L[-1])   #倒数第一个
print(L[-2:])  #倒数2个
print(L[-2:-1]) #倒数第2个

L1 = list(range(1,101))
print(L1)
print(L1[:10])
print(L1[-10:])
print(L1[-10])
print(L1[10:20])
print(L1[:10:2])  #前10个数，每两个取一个
print(L1[::5])    #所有数，每5个取一个
print(L1[:])      #原样复制一个list

T =(1,3,5,7,9)  #tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print(T[:3])

st ='ABCDEFG'    #L[]   tuple()   str''
print(st[-2:])
