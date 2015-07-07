#coding=utf-8
# 此脚本实现了提取特定时间特定空间的pm25数据
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

def getAverage(pollution, cwriter):

    csvName = "urban-country/beijing_" + pollution + '.csv'
    df = pd.read_csv(csvName, sep=',',)
    dfLength = df.shape[0]
    df['averageUrban'] = Series(np.random.randn(dfLength), index=df.index)
    df['averageCountry'] = Series(np.random.randn(dfLength), index=df.index)
    df['averageUrban'] = df[["东四","天坛","官园","万寿西宫","奥体中心","农展馆","万柳",
                   "北部新区","植物园","丰台花园","云岗","古城","前门","永定门内","西直门北","南三环","东四环"]].mean(axis=1)

    df['averageCountry'] = df[["房山","大兴","亦庄","通州","顺义","昌平","门头沟","平谷",
                          "怀柔","密云","延庆","定陵","八达岭","密云水库","东高村","永乐店","榆垡","琉璃河"]].mean(axis=1)
    df = df.ix[:,["date","hour","type",'averageUrban', 'averageCountry']]

    df_01 = df[df['date']>=20140321]
    df_01 = df_01[df_01['date']<20140621]
    urban_01_avr = df_01['averageUrban'].mean(axis=0)
    urban_01_max = df_01['averageUrban'].max(axis=0)
    urban_01_min = df_01['averageUrban'].min(axis=0)
    country_01_avr = df_01['averageCountry'].mean(axis=0)
    country_01_max = df_01['averageCountry'].max(axis=0)
    country_01_min = df_01['averageCountry'].min(axis=0)

    df_02 = df[df['date']>=20140621]
    df_02 = df_02[df_02['date']<20140923]
    urban_02_avr = df_02['averageUrban'].mean(axis=0)
    urban_02_max = df_02['averageUrban'].max(axis=0)
    urban_02_min = df_02['averageUrban'].min(axis=0)
    country_02_avr = df_02['averageCountry'].mean(axis=0)
    country_02_max = df_02['averageCountry'].max(axis=0)
    country_02_min = df_02['averageCountry'].min(axis=0)

    df_03 = df[df['date']>=20140923]
    df_03 = df_03[df_03['date']<20141222]
    urban_03_avr = df_03['averageUrban'].mean(axis=0)
    urban_03_max = df_03['averageUrban'].max(axis=0)
    urban_03_min = df_03['averageUrban'].min(axis=0)
    country_03_avr = df_03['averageCountry'].mean(axis=0)
    country_03_max = df_03['averageCountry'].max(axis=0)
    country_03_min = df_03['averageCountry'].min(axis=0)

    df_04 = df[df['date']>=20141222]
    df_04 = df_04[df_04['date']<20150321]
    urban_04_avr = df_04['averageUrban'].mean(axis=0)
    urban_04_max = df_04['averageUrban'].max(axis=0)
    urban_04_min = df_04['averageUrban'].min(axis=0)
    country_04_avr = df_04['averageCountry'].mean(axis=0)
    country_04_max = df_04['averageCountry'].max(axis=0)
    country_04_min = df_04['averageCountry'].min(axis=0)

    '''
    item = [pollution, urban_01_avr, urban_01_max, urban_01_min, country_01_avr, country_01_max, country_01_min,
                urban_02_avr, urban_02_max, urban_02_min, country_02_avr, country_02_max, country_02_min,
                urban_03_avr, urban_03_max, urban_03_min, country_03_avr, country_03_max, country_03_min,
                urban_04_avr, urban_04_max, urban_04_min, country_04_avr, country_04_max, country_04_min]
    '''
    item = [pollution, urban_01_avr, urban_02_avr, urban_03_avr, urban_04_avr,
            country_01_avr, country_02_avr, country_03_avr, country_04_avr]
    cwriter.writerow(item)

def dayAvrage(pollution, cwriter):
    csvName = "average" + pollution + '.csv'
    df = pd.read_csv(csvName, sep=',',)
    for day, same_day_rows in df.groupby('date'):
        urbanAvr = same_day_rows['averageUrban'].mean(axis=0)
        countryAvr = same_day_rows['averageCountry'].mean(axis=0)
        item = [day, urbanAvr, countryAvr]
        cwriter.writerow(item)

def cuDayAvr(pollution):
    pollution = ['pm25', 'pm10', 'so2', 'no2', 'co', 'o3']
    for i in range(len(pollution)):
        csv_file = open("day_average" + pollution[i] + '.csv', 'a+')
        cwriter = csv.writer(csv_file, delimiter=',')
        #getAverage(pollution[i], cwriter)
        #dayAvrage(pollution[i], cwriter)

def plot():
    fig = plt.figure(figsize=(18,5))
    rect = fig.patch
    rect.set_facecolor('white')
    df = pd.read_csv("urban-country/day_averageco.csv", sep=',', header=0)
    df = df[df['date']>=20150201]
    df = df[df['date']<=20150315]
    df['date'] = df['date'].astype(str)
    dateAndTime = pd.to_datetime(df['date'], "%Y%m%d")
    urbanAvrDay = df['urbanAvrDay'].tolist()
    countryAvrDay = df['countryAvrDay'].tolist()

    ts_urban = Series(urbanAvrDay, index=dateAndTime)
    plot1 = ts_urban.plot(linestyle='-', color='black', marker='8', markersize=10, markerfacecolor='None', label='urban')
    ts_country = Series(countryAvrDay, index=dateAndTime)
    plot2 = ts_country.plot(linestyle='-', color='black', marker='8', markersize=10, label='country')

    ##fig.legend([plot1, plot2], ['urban', 'country'], loc=2)
    plt.legend( loc='upper left', numpoints = 1 )

    plt.show()

def aoti(pollution):
    csvName = "urban-country/beijing_" + pollution + '.csv'
    print csvName
    df = pd.read_csv(csvName, sep=',',)
    df = df.ix[:, ["date","hour","type","奥体中心"]]
    df.to_csv('aoti_' + pollution + '.csv', sep=',', encoding='utf-8', index=False)

def aoti_avr_day(pollution, cwriter):
    csvName = "aoti_" + pollution + '.csv'
    df = pd.read_csv(csvName, sep=',',)
    for day, same_day_rows in df.groupby('date'):
        aotiAvr = same_day_rows['奥体中心'].mean(axis=0)
        item = [day, aotiAvr]
        cwriter.writerow(item)

def getAOTI():

    pollution = ['pm25', 'pm10', 'so2', 'no2', 'co', 'o3']
    for i in range(len(pollution)):
        aoti(pollution[i])
    for i in range(len(pollution)):
        csv_file = open("aotiAvr" + pollution[i] + '.csv', 'a+')
        cwriter = csv.writer(csv_file, delimiter=',')
        aoti_avr_day(pollution[i], cwriter)

if __name__=="__main__":
    print ""