import numpy as np
import pandas as pd

data = pd.read_excel(r"D:\Crrc_Point\制动点.xlsx")
data_array = data.values

data_array_copy = data_array.copy()
# print(data_array_copy.shape[0], data_array_copy.shape[1])
# 用来接收 数据的排列组合
# data_list 里面全是 前4个是原数据，后4个是要被预测的，组成的列表
# data_tem  用来在循环中临时变量
data_list = np.array((((data_array.shape[0] * 4) ** 2 - data_array.shape[0] * 4) / 2, 8), dtype='float32')
print(data_list)
# print(data_list.shape[1])