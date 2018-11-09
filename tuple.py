#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 11:55
# @Author : maxu


#tuple:tuple一旦初始化就不能修改
tuple1 = ()
print(tuple1)
tuple2 = (1)
print(tuple2)
tuple3 = (1,)
print(tuple3)
tuple4 = ('a','b',['A','B'])
tuple4[2][0] = 'X'
tuple4[2][1] = 'Y'
print(tuple4)
# tuple练习题
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# # 打印Apple:
print(L[0][0])
# # 打印Python:
print(L[1][1])
# # 打印Lisa:
print(L[2][2])