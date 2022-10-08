"""
生成测试数据
 @author ： Phoshowy
 update ： 2022/10/05
"""
import random

import matplotlib.pyplot as plt
import numpy as np


def getdata(course):
    """
    函数功能：根据值来获取下标
    score:该数组下标下的值
    返回值：二维数组的第二个下标值
    """

    def find_index(score):
        for i in range(90):
            if matrix[20][i] == score:
                return i

    """
    函数功能：创建频数列表
    num:绩点;pro:频数列表
    返回值：频数列表
    """

    def probility(num, pro):
        if (num >= 1.6 and num <= 2.0):
            po = 50
        elif (num > 2.0 and num <= 2.4):
            po = 30
        elif (num > 2.4 and num <= 2.8):
            po = 10
        elif (num > 2.8 and num <= 3.2):
            po = 3
        elif (num > 3.2 and num <= 3.6):
            po = 2
        else:
            po = 1
        for i in range(po):
            pro.append(num)
        return pro

    # 20次课
    class_num = []
    for i in range(20):
        class_num.append(i)
    # 90个人
    student_num = []
    for i in range(90):
        student_num.append(i)
    # print(class_num,student_num)

    # 数组初始化，默认为1，表示到位
    p = []
    normal = np.random.normal(2.8, 0.4, 90)  # 正态分布，假设均值2.8，由3-sigma原则算出标准差0.4
    matrix = [[0 for i in range(90)] for i in range(21)]
    for i in range(20):
        for j in range(90):
            matrix[i][j] = 1
            if normal[j] > 4.0:
                normal[j] = 4.0
            if normal[j] < 1.6:
                normal[j] = 1.6
            matrix[20][j] = round(normal[j], 2)
            # 构建抽样频次
            probility(matrix[20][j], p)
    random.shuffle(p)  # 打乱顺序
    # print(p)
    # print(min(matrix[20]))

    """
    #绩点分布可视化检查
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.distplot(normal, hist=False, label='normal')
    plt.show()
    """

    # 设置经常缺课的学生
    absent_student_num = random.randint(5, 8)
    absent_student_list = []
    absent_student_score = np.random.choice(p, absent_student_num)  # 选出经常缺课的学生的绩点
    for i in absent_student_score:
        absent_student_list.append(find_index(i))
    # print(absent_student_num)
    # print("缺课学生的绩点：",absent_student_score)
    # print("缺课学生的ID：",absent_student_list)

    # 绘制经常缺课学生的绩点分布情况图
    copy = absent_student_score
    copy.sort()
    for i in range(len(copy)):
        plt.plot(i, copy[i], '*', alpha=0.5, linewidth=1)
    plt.show()

    # 为每个缺课的学生选16-20节课缺课
    for i in absent_student_list:
        absent_class_num = random.randint(16, 20)  # 这学期缺了absent_class_num节课
        # 生成具体的缺课节数
        absent_class_list = random.sample(class_num, absent_class_num)
        # print(absent_class_list)
        for k in absent_class_list:
            matrix[k][i] = 0
    # print(matrix[10])

    # 设置每次课0-3缺课的人
    for i in range(20):
        small_absent_num = random.randint(0, 3)
        small_student_list = random.sample(student_num, small_absent_num)
        for j in small_student_list:
            matrix[i][j] = 0

    # 写入与导出
    with open(r'C:\Users\lenovo\Desktop\result' + str(course) + '.csv', 'w', encoding='utf-8') as f1:
        for j in range(21):
            f1.write(str(matrix[j]).strip('[').strip(']') + '\n')

    with open(r'C:\Users\lenovo\Desktop\explain' + str(course) + '.txt', 'w', encoding='utf-8') as f2:
        absent_student_score = str(absent_student_score)
        absent_student_list = str(absent_student_list)
        f2.write("缺课学生的绩点：" + absent_student_score + '\n' + "缺课学生的ID：" + absent_student_list)


# 运行
if __name__ == '__main__':
    course = eval(input("总共有几门课？"))
    for i in range(1, course + 1):
        getdata(i)
