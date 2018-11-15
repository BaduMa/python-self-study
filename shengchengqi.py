#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/13 10:58
# @Author : maxu

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
# 在Python中，这种一边循环一边计算的机制，称为生成器  generator
L = [x*x for x in range(10)]
print(L)
g =(x*x for x in range(10))
print(g)
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator


# 我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

g =(x*x for x in range(10))
for n in g:
	print(n)
# 我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象

# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
# 斐波拉契数列---这个数列从第3项开始，每一项都等于前两项之和（用列表生成式写不出来，但是，用函数把它打印出来却很容易）

def fib(max):
	n,a,b = 0, 0, 1
	while n < max:   # 注意，赋值语句：# a, b = b, a + b相当于：# t = (b, a + b) # t是一个tuple  a = t[0]  b = t[1]
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
print(fib(10))


# fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了

def fib(max):   #这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
	n,a,b=0,0,1
	while n < max:
		yield b
		a, b =b,a+b
		n=n+1
	return 'done'
print(fib(8))

# 最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
	print('step1')
	yield 1
	print('step2')
	yield (3)
	print('step3')
	yield (5)
o = odd()
print(next(o))
print(next(o))
print(next(o))
# 可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
# 执行3次yield后，已经没有yield可以执行了，所以，如果第4次调用next(o)就会报错

# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。    当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
# 同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
for n in fib(6):
	print(n)  #1 1 2 3 5 8

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g =fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break


# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束


# 生成器---1 可迭代   2 只能读取一次   3 实时生成数据，不全存在内存中


# 请注意区分普通函数和generator函数，
# 普通函数调用直接返回结果：
# >>> r = abs(6)
# >>> r
# 6

# generator函数的“调用”实际返回一个generator对象：
# >>> g = fib(6)
# >>> g
# <generator object fib at 0x1022ef948>


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
# 我直接解释代码运行顺序，相当于代码单步调试：
# 1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)
# 2.直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环
# 3.程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)语句执行完成，
# 所以输出的前两行（第一个是while上面的print的结果,第二个是return出的结果）是执行print(next(g))的结果，
# 4.程序执行print("*"*20)，输出20个*
# 5.又开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，
# 这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），所以这个时候res赋值是None,所以接着下面的输出就是res:None,
# 6.程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止，print函数输出的4就是这次return出的4