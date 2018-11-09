#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/9 13:10
# @Author : maxu

#转义字符\可以转义很多字符，比如\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m Ok')
print('I\'m learning \nPython') #\n表示换行
print(r'\\\t\\') #Python还允许用r''表示''内部的字符串默认不转义
print('''line1
line2
line3''') #Python允许用'''...'''的格式表示多行内容