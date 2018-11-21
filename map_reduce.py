#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/15 11:11
# @Author : maxu

# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

L =[1,2,3,4,5,6,7,8,9]
def f(x):
	return x*x
r= map(f,L) # map()传入的第一个参数是f，即函数对象本身。
print(list(r))
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

# map()作为高阶函数，事实上它把运算规则抽象了

# 利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数

print(list(map(str,[1,3,5,4,5,6,7])))  #把列表1-7数字转换成列表1-7字符串


#reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)

from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
	return x*10+y
print(reduce(fn,[1,3,5,7,9]))

def fn(x,y):
	return x*10+y
def char2num(s):
	dights = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return dights[s]
print(reduce(fn,map(char2num,'13579')))


DIGITS ={'0',0,'1',1,'2',2,'3',3,'4',4,'5',5,'6',6,'7',7,'8',8,'9',9}
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return DIGITS
	return reduce(fn,map(char2num,s))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
	return  DIGITS

def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))

# reduce函数，本质上就是通过传入一个函数和初始值，不断的对集合中的每个元素进行迭代运算，每次运算的结果都作为第二次运算的参数。
# 和最后一个元素的运算结果作为reduce函数的返回值

# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']