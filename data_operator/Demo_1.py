import torch
import os
import pandas as pd


def write():
    os.makedirs(os.path.join('..', 'data'), exist_ok=True)
    data_file = os.path.join('..', 'data', 'house_tiny.csv')
    with open(data_file, 'w') as f:
        f.write('NumRooms,Alley,Price\n')  # 列名
        f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
        f.write('2,NA,106000\n')
        f.write('4,NA,178100\n')
        f.write('NA,NA,140000\n')

def read():
    data_file = os.path.join('..', 'data', 'house_tiny.csv')
    data = pd.read_csv(data_file)
    print(data)

    inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
    print(inputs)
    print("==========>")
    print(outputs)
    inputs = inputs.fillna(inputs.mean())
    print(inputs)

    inputs = pd.get_dummies(inputs, dummy_na=True)
    print(inputs)

if __name__ == '__main__':
    read()