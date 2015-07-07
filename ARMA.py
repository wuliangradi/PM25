#coding=utf-8
# 此脚本实现了利用ARMA模型预测pm25浓度时间序列趋势
"""
---- author = "liang wu" ----
---- time = "20150705" ----
---- Email = "wl062345@gmail.com" ----
"""
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from pandas import Series
from scipy import interpolate
from statsmodels.graphics.api import qqplot
from pandas.tools.plotting import autocorrelation_plot

def arma():
    df = pd.read_csv("urban-country/beijing_pm25.csv", sep=',', header=0)      # pandas模块打开数据
    df = df.ix[:,["date", "hour", "东四"]]                                      # 取出特定的column
    df = df[df['date']>=20140325]
    df = df[df['date']<=20140417]                                              # 获取特定时间段的数据
    df = df.replace(r'\s+', np.nan, regex=True)                                # 将空值代替为NaN
    df['东四'] = df['东四'].interpolate()
    df['date'] = df['date'].astype(str)
    df['hour'] = df['hour'].astype(str)
    dateAndTime = pd.to_datetime(df['date'] + df['hour'], format="%Y%m%d%H")   # 创建时间标签
    dongSi = df['东四'].tolist()
    ts_dongSi = Series(dongSi, index=dateAndTime)                              # 创建时间序列

    arma_mod20 = sm.tsa.ARMA(ts_dongSi, (3, 0)).fit()                          # 建立ARMA模型
    resid = arma_mod20.resid
    predict = arma_mod20.predict('20140410', '20140417', dynamic=True)         # 预测

    fig, ax = plt.subplots(figsize=(12, 8))
    ax = ts_dongSi.plot(ax=ax)
    predict.plot(ax=ax)
    plt.show()

if __name__=='__main__':
    arma()













