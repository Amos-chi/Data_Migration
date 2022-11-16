import csv

import pandas as pd

f = open('aaaa.csv', 'r', encoding= 'utf-8')

#print(data).

def fun1read(): # 一个字一行
    data = f.read()
    print(type(data))
    for l in data:
        print(l)

def fun2read(): # 每一行是一个字符串 组成一个集合
    data = f.read()
    print(type(data))
    list = data.split('\n')
    print(list)

def csvread():
    cr = csv.reader(f)
    #print(cr) # <_csv.reader object at 0x0000021F3FF8BAC0>
    for row in cr:     # 每一行的字符串是一个集合
        print(row)

def pdread():
    reader = pd.read_csv(f)   # 读取成表格
    print(reader)
    # 接下来的操作


if __name__ == '__main__':
    #fun2read()
    #csvread()
    pdread()