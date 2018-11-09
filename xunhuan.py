#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 13:13
# @Author : maxu


#循环 for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
numbers = ['1','2','3','4']
for number in numbers:
	print(number)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum +x
print(sum)

#直接使用range(n)就可以产生0~（n-1）的序组
print(list(range(5)))

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)  #在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出

# break
# 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')


# 上面的代码可以打印出1~100。
# 如果要提前结束循环，可以用break语句：
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
# 执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。
# 可见break的作用是提前结束循环。

# continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

n = 0
while n < 10:
    n = n + 1
    print(n)

# 上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
# 执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9。 可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。