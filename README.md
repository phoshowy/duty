# duty

福州带学 软件工程第Ⅱ次结对作业
（👑⭐）
## 结果
| 算法               | E    |
|------------------|------|
| roll_call_fakerl | 0.78 |
| roll_call_knn    | 0.87 |

## 实验环境
在进行前,请确保你的电脑上安装了python 3.9,并具有如下的第三方库
- numpy 1.23.1
- matplotlib 3.5.2
- scikit-learn 1.1.1

## 程序运行
### 生成数据集
文件：**data_maker.py<br>**
使用：使用Python编译器打开后，在文件末尾位置的写入模块改变输出文件的路径，随后运行。 运行时输入课程数n（为一个自然数），程序结束后会在指定路径下生成两个文件：
1. result(n).csv :内含一个21x90的矩阵，前20行，90列表示20次课程90位学生的到位情况，其中1表示到位，0表示缺席。第21行为90位学生的绩点。
2. explain(n).txt :内含两行内容，分别是经常缺课学生的绩点与ID

### 结果测试
文件：**RollCall/main.py**<br>
使用：直接执行main.py，得到
- 第一行为roll_call_fakerl算法结果
- 第二行为roll_call_knn算法结果

## 算法
对于评价指标**E**
$$E = \frac{五门课程的有效点名次数}{总请求次数}$$
为使**E**最大化,最合理的点名方法即为：在前几次的点名中找出缺课率为80%的5-8名同学，接着在每次课程中都对其做点名，这样可使**E**保持在一个较高的水准<br>
本次设计的两种算法均基于这种思想实现<br>
<font color='grey'>~~注：因为该题的特殊性，相关算法针对数据集和目标具有相关优化~~</font>

## 其他
具体部分详见相关代码