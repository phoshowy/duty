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


def less_gpa(gpa: list, point: int):
    less = []
    for index, value in gpa:
        if value < point:
            less.append(index)
    return less



