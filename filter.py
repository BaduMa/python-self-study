#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/12/4 16:35
# @Author : maxu

# Python内建的filter()函数用于过滤序列。

# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
	return n % 2 ==1
L1 =[1,2,4,5,6,9,10,15]
print(list(filter(is_odd,L1)))

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
def main(): #1000以内   （质数）
	for n in primes():
		if n<1000:
			print(n)
		else:
			break

def _odd_iter(): #用Python来实现这个算法，可以先构造一个从3开始的奇数序列
	n=1
	while True:
		n= n + 2
		yield n

def _not_divisible(n): #然后定义一个筛选函数
	return lambda x:x*n>0

def primes(): #最后，定义一个生成器，不断返回下一个素数
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it =filter(_not_divisible(n),it)

if __name__ == '__main__':
	main()