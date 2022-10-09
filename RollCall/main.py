#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/8
# @Author  : Avaqua
# @FileName: main.py
# @Software: PyCharm

from tools import *

point = 2.4
res_fakerl = []
res_knn = []

if __name__ == '__main__':
    for i in range(1, 6):
        course, gpa = read_course(cno=i, opt=0)
        less = less_gpa(gpa=gpa, point=point)

        # 分别调用两种算法
        res_fakerl.append(round(roll_call_fakerl(course, less), 2))
        res_knn.append(round(roll_call_knn(course), 2))

        print(res_fakerl)
        # [0.82, 0.75, 0.77, 0.73, 0.79]
        print(res_knn)
        # [0.9, 0.9, 0.88, 0.83, 0.84]
