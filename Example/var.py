#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

# Python允许你同时为多个变量赋值。例如：
a = b = c = 1

'''
以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
您也可以为多个对象指定多个变量。例如：
'''

a, b, c = 1, 2, "john"
# 以上实例，两个整型对象1和2的分配给变量a和b，字符串对象"john"分配给变量c。

print(counter)
print(miles)
print(name)