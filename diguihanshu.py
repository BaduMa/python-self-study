#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 11:16
# @Author : maxu

# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。


def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)#表示n的阶乘
# print(fact(1))
print(fact(5))
# 递归函数的优点是定义简单，逻辑清晰。
# 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰

# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
#########print(fact(1000))
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，
# 所以，把循环看成是一种特殊的尾递归函数也是可以的
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出

def fact(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if num ==1:
		return product
	return fact_iter(num-1,num*product)
print(fact(5))
print(fact_iter(5,1))
print(fact_iter(10,1))
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。  即print(fact_iter(1000,1))还是会溢出