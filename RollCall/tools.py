#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/7
# @Author  : Avaqua
# @FileName: tools.py
# @Software: PyCharm

import numpy as np


def read_course(cno: int):
    path = "../course_data/course" + str(cno) + "/result" + str(cno) + ".csv"
    course = np.genfromtxt(path, delimiter=',', skip_header=True).tolist()
    gpa = course.pop(-1)
    return course, gpa


def less_gpa(gpa: list, point: float):
    less = []
    for index, value in enumerate(gpa):
        if value < point:
            less.append(index)
    return less


def roll_call_rate(course: list, less: list):
    total_times = 0
    eff_times = 0
    absent = []
    for i in range(len(course)):
        # 第一次对绩点较低全点
        if i == 0:
            for j in less:
                total_times += 1
                if course[i][j] == 0:
                    absent.append(j)
                    eff_times += 1
        # 第二次排除只有第一次未到的学生
        elif i == 1:
            for j in absent:
                total_times += 1
                if course[i][j] == 1:
                    absent.remove(j)
                else:
                    eff_times += 1
        else:
            for j in absent:
                total_times += 1
                if course[i][j] == 0:
                    eff_times += 1
    return eff_times / total_times
