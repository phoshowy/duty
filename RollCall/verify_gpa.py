#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/9
# @Author  : Avaqua
# @FileName: verify_gpa.py
# @Software: PyCharm

from tools import *

point = 2.4
rate = []

for i in range(1, 11):
    course, gpa = read_course(i, 1)
    less = less_gpa(gpa, point)
    rate.append(calculate_e(roll_call_fakerl(course, less)))

print("平均值为：%f" % np.mean(rate))
print("方差为：%f" % np.var(rate))
# 平均值为：0.762120
# 方差为：0.002653
