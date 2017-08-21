#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;  # 引入time模块
import calendar

ticks = time.time()
print(time.localtime())
print("当前时间戳为:", ticks)


cal = calendar.month(2016,1)
print("以下输出2016年1月份的日历:")
print(cal)