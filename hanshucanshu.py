#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 11:31
# @Author : maxu

# 默认参数
# 新的power(x, n)函数定义没有问题，
# 但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用

def power(x,n=2):
	s= 1
	while n>0:
		n=n-1
		s=s*x
	return s
print(power(3))

def enroll(name,gender):
	print('name:',name)
	print('gender:',gender)
print(enroll('JACK','F'))

def enroll(name,gender,age=6,city='Dalian'):
	print('name:',name)
	print('gender:',gender)
	print('age:', age)
	print('city:', city)
print(enroll('Bruce','G'))
print(enroll('Snow','K',9))
print(enroll('George','B',city='Bayuquan'))# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上
#
def add_end(L=[]):
	L.append('END')
	return L
print(add_end([1,2,3]))
print(add_end(['A','B','C']))
print(add_end())
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
print(add_end())
print(add_end())

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
print(add_end())
print(add_end())
print(add_end())

def calc(numbers):
	sum =0
	for n in numbers:
		sum = sum + n*n
	return sum
print(calc([1, 2, 3]))
print(calc([1, 3, 5, 7]))

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc(*numbers):
	sum =0
	for n in numbers:
		sum = sum + n*n
	return sum
print(calc(1,2,5))
print(calc())
#
# # 已经有一个list或者tuple，要调用一个可变参数
nums =[1,2,3,4,5,6]
print(calc(nums[1],nums[3],nums[5]))
# # Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*nums))

# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name,age,**kw):
	print('name:', name,'age:', age,'other:',kw)
print(person('MAXU',28))
print(person('Jingjing',25,city='Dalian'))
extra ={'city':'Sanya','job':'Teacher'}
print(person('Tom',10,city=extra['city'],job=extra['job']))
# # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# # ，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
# # 对kw的改动不会影响到函数外的extra
print(person('Yiwei',18,**extra))

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内部通过kw检查。

def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)
print(person('JAY',32,city='Shanghai',add='Jinganqu'))
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# *args：可以理解为只有一列的表格，长度不固定。
# **kwargs：可以理解为字典，长度也不固定。
# 注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict

def person(name,age,*,city,job):
	print(name,age,city,job)
print(person('MAXU', 28, city='DALIAN', job='QA'))

def person(name,age,*,city,job='teacher'):
	print(name,age,city,job)
print(person('Xiaoma',28,city='Sanya'))

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
def f1(a, b, c=0, *args, **kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a, b, c=0, *,d, **kw):
	print('a=',a,'b=',b,'c=',c,d,'kw=',kw)

# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
print(f1(1,2))
print(f1(1,2,c=3))
# print(f1(1,2,3,'a','b'))
# print(f1(1,2,3,'a','b',x=99))
# print(f2(1,2,d=99,ext=None))
args=(1,2,3,4)
kw={'d':88,'x':'#'}
print(f1(*args,**kw))
args=(3,6,9)
kw={'d':55,'x':'$$'}
print(f2(*args,**kw))

# 敲黑板，划重点
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。