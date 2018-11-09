#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 11:38
# @Author : maxu

# 条件判断---1注意不要少写了冒号:
# 2if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，
# 把该判断对应的语句执行后，就忽略掉剩下的elif和else
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
age1 = 20
if age1 >= 18:
	print('u r adult')

age2 = 5
if age2 <18:
	print('u r child')
else:
	print('u r teenager')

age3 = 3
if age3 >= 18:
	print('成年')
elif age3 >= 6:
	print('少年')
else:
	print('小屁孩')

#if判断条件还可以简写，比如写：
if x:  print('True') #只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if 1:
	print('True')

#str需要转换成int
s = input('birthday:')
birthday = int(s)   #birthday = int(input('birthday:'))

if birthday < 2000:
	print('蛋蛋前')
else:
	print('蛋蛋后')

#练习题 计算BMI，肥胖指数的判断
height = 1.75
weight = 80.5

bmi = weight/(height ** height)

if bmi < 18.5:
	print("过轻")
elif 18.5 <= bmi < 25:
	print('正常')
elif 25 <= bmi < 28:
	print('过重')
elif 28 <= bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')