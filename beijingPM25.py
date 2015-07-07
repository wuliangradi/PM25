#coding=utf-8
# 此脚本实现了提取特定时间特定空间的pm25数据并可视化
"""
---- author = "liang wu" ----
---- time = "20150705" ----
---- Email = "wl062345@gmail.com" ----
"""
import csv
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from pandas import Series, DataFrame, Panel
from datetime import datetime
import datetime as dt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import matplotlib.dates as mdates

def plotAotiDay():

    fig = plt.figure(figsize=(18,5))
    rect = fig.patch
    rect.set_facecolor('white')
    df = pd.read_csv("urban-country/aotiAvrpm25.csv", sep=',', header=0)
    df = df[df['date']>=20140301]
    df = df[df['date']<=20140810]
    df['date'] = df['date'].astype(str)
    dateAndTime = pd.to_datetime(df['date'], "%Y%m%d")
    aoti = df['PM25'].tolist()
    ts_aoti = Series(aoti, index=dateAndTime)
    plot = ts_aoti.plot(linestyle='-', color='black', marker='8', markersize=6, label='奥体中心')

    time = dt.datetime(2014, 04, 14)
    value = df[df['date']=='20140414'].iloc[0,1]
    plt.annotate(u'星期一', xy=(mdates.date2num(time), value), xytext=(30, -20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))

    time = dt.datetime(2014, 05, 31)
    value = df[df['date']=='20140531'].iloc[0,1]
    plt.annotate(u'星期六', xy=(mdates.date2num(time), value), xytext=(30, -20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))

    time = dt.datetime(2014, 07, 06)
    value = df[df['date']=='20140706'].iloc[0,1]
    plt.annotate(u'星期日', xy=(mdates.date2num(time), value), xytext=(30, 20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))

    time = dt.datetime(2014, 06, 16)
    value = df[df['date']=='20140616'].iloc[0,1]
    plt.annotate(u'星期一', xy=(mdates.date2num(time), value), xytext=(30, 20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))

    time = dt.datetime(2014, 03, 24)
    value = df[df['date']=='20140324'].iloc[0,1]
    plt.annotate(u'星期一', xy=(mdates.date2num(time), value), xytext=(-30, 20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))

    time = dt.datetime(2014, 04, 8)
    value = df[df['date']=='20140408'].iloc[0,1]
    plt.annotate(u'星期二', xy=(mdates.date2num(time), value), xytext=(-10, 20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))

    time = dt.datetime(2014, 04, 8)
    value = df[df['date']=='20140408'].iloc[0,1]
    plt.annotate(u'星期一', xy=(mdates.date2num(time), value), xytext=(-10, 20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))

    time = dt.datetime(2014, 04, 18)
    value = df[df['date']=='20140418'].iloc[0,1]
    plt.annotate(u'星期五', xy=(mdates.date2num(time), value), xytext=(-10, 20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))
    plt.show()

def plotAotiHour():

    fig = plt.figure(figsize=(18,5))
    rect = fig.patch
    rect.set_facecolor('white')
    df = pd.read_csv("urban-country/aoti_pm25.csv", sep=',', header=0)
    df = df[df['date']>=20140514]
    df = df[df['date']<=20140527]
    df['date'] = df['date'].astype(str)
    df['hour'] = df['hour'].astype(str)
    dateAndTime = pd.to_datetime(df['date'] + df['hour'], format="%Y%m%d%H")
    aoti = df['奥体中心'].tolist()
    ts_aoti = Series(aoti, index=dateAndTime)
    plot = ts_aoti.plot(linestyle='-', color='black', marker='8', markersize=4, label=u'奥体中心')
    time = dt.datetime(2014, 05, 17, 10)
    df = df[df['date']=='20140517']
    df = df[df['hour']=='10']
    value = df.iloc[0,3]
    print mdates.date2num(time), value
    plt.annotate(u'aoti24', xy=(mdates.date2num(time), value), xytext=(30, 20),
                 textcoords='offset points',arrowprops=dict(arrowstyle='-|>'))
    plt.show()

if __name__=='__main__':
    # plotAotiDay()    # 画图：奥体中心站PM25逐日变化图
    # plotAotiHour()   # 画图：奥体中心站PM25逐时变化图
    print "bingo!"