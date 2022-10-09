#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/7
# @Author  : Avaqua
# @FileName: tools.py
# @Software: PyCharm

import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def read_course(cno: int, opt: int):
    if opt == 0:
        path = "../course_data/course" + str(cno) + "/result" + str(cno) + ".csv"
    else:
        path = "../new_course/" + str(cno) + "/" + str(cno) + ".csv"
    course = np.genfromtxt(path, delimiter=',', skip_header=True).tolist()
    gpa = course.pop(-1)
    return course, gpa


def less_gpa(gpa: list, point: float):
    less = []
    for index, value in enumerate(gpa):
        if value < point:
            less.append(index)
    return less


def roll_call_fakerl(course: list, less: list):
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
    return eff_times, total_times


def roll_call_knn(course: list):
    stuno = np.array(list(range(90)))
    total_times = 0
    eff_times = 0
    for i in range(1, len(course)):
        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(np.tile(stuno, i).reshape(-1, 1), np.array(course[0:i]).reshape(-1, 1))
        pre = knn.predict(stuno.reshape(-1, 1)).astype(int).tolist()
        for j, value in enumerate(pre):
            if value == 0:
                total_times += 1
                if course[i][j] == 0:
                    eff_times += 1
    return eff_times, total_times


def calculate_e(res: list):
    eff = 0
    total = 0
    for r in res:
        if isinstance(r, tuple):
            eff += r[0]
            total += r[1]
        else:
            eff = res[0]
            total = res[1]
            break
    return eff / total
