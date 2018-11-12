#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 11:53
# @Author : maxu

# dict
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d ={'A':90,'B':55,'C':27}
print(d['B'])

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['D']=666
print(d['D'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['E'] = 888
print(d['E'])
d['E'] = 123
print(d['E'])

d = {
	'michael':95,
	'tom':90,
	'bruce':85,
}
print('d[\'michael\']=', d['michael'])
print('d[\'tom\']=', d['tom'])
print('d[\'bruce\']=',d['bruce'])
print('d.get(\'mark\',-1)=',d.get('mark',-1))

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# 和list比较，dict有以下几个特点： 查找和插入的速度极快，不会随着key的增加而变慢；需要占用大量的内存，内存浪费多。
# 而list相反：查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。所以，dict是用空间来换取时间的一种方法。

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key


# set: set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s = set([1,1,2,2,3,3,4,4,5])
print(s)
s.remove(4)
print(s)
s1 =set([1,3,5])
s2 =set([1,2,3])
print(s1 & s2)  #交集
print(s1 | s2)  #并集

a ='abc'
a.replace('a','A')
print(a)
b = a.replace('a','A')
print(b)
print(a)

