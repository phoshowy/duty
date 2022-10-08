#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/8
# @Author  : Avaqua
# @FileName: draw_gpa.py
# @Software: PyCharm

from tools import *
import matplotlib.pyplot as plt

points = [point / 10 for point in range(20, 30)]

for i in range(1, 6):
    course, gpa = read_course(i)
    rate = []
    for point in points:
        less = less_gpa(gpa, point)
        rate.append(roll_call_fakerl(course, less))
    plt.plot(points, rate)

plt.savefig("../course_data/gpa.png")
plt.show()
