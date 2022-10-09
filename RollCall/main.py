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
        res_fakerl.append(roll_call_fakerl(course, less))
        res_knn.append(roll_call_knn(course))

        # 分别计算两种算法的E值
        print(calculate_e(res_fakerl))
        # 0.7806788511749347

        print(calculate_e(res_knn))
        # 0.8747591522157996
