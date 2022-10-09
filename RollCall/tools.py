#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/7
# @Author  : Avaqua
# @FileName: tools.py
# @Software: PyCharm

import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def read_course(cno: int, opt: int):
    """
    :param cno: 需要读取的课程id
    :param opt: 若为0,读取课程信息;若为1,读取测试集信息
    :return: 出勤课程情况和绩点信息
    """
    if opt == 0:
        path = "../course_data/course" + str(cno) + "/result" + str(cno) + ".csv"
    else:
        path = "../new_course/" + str(cno) + "/" + str(cno) + ".csv"
    course = np.genfromtxt(path, delimiter=',', skip_header=True).tolist()
    gpa = course.pop(-1)
    return course, gpa


def less_gpa(gpa: list, point: float):
    """
    :param gpa: 绩点信息
    :param point: 特定绩点值
    :return: 低于特定绩点值的学生编号
    """
    less = []
    for index, value in enumerate(gpa):
        if value < point:
            less.append(index)
    return less


def roll_call_fakerl(course: list, gpa: list):
    """
    :param course: 课程信息
    :param gpa: 需要抽取的学生学号
    :return: 有效点名次数和总次数
    """
    total_times = 0
    eff_times = 0
    absent = []
    for i in range(len(course)):
        # 第一次对绩点较低全点
        if i == 0:
            for j in gpa:
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
    """
    :param course: 课程信息
    :return: 有效点名次数和总次数
    """
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
    """
    :param res: 点名次数和总次数组成的列表
    :return: 评价指标E
    """
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
