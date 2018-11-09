#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 11:35
# @Author : maxu


# 定义函数
def my_abs(x):
	if x >=0:
		return x
	else:
		return -x

print(my_abs(-99))
print(my_abs(92))

def power(x):
	return x*x
print(power(5))
print(power(12))

def power(x,n):
	s=1
	while n > 0:
		n=n-1
		s=s*x
	return s
print(power(5,3))