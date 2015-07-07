#coding=utf-8
# 处理原始数据
"""
---- author = "liang wu" ----
---- time = "20150705" ----
---- Email = "wl062345@gmail.com" ----
"""
import csv
import numpy as np
import os

def mergeCsv(csvName):
    with open(csvName) as fp:
        for line in fp.readlines()[1:]:
            li = line.strip().split(",")
            if (len(li)>=3 and li[2] == "CO"):
                cwriter.writerow(li)

def folder():
    folder = '/Users/wuliang/Documents/数据/地面监测数据/北京aqi/北京空气质量/all'
    for root, dirs, files in os.walk(folder):
        for name in files:
            if len(name)>=20:
                csv_file = root+os.sep+name
                mergeCsv(csv_file)

if __name__=="__main__":
    csv_file = open("beijing_co.csv", 'a+')
    cwriter = csv.writer(csv_file, delimiter=',')
    #folder()