#coding=utf-8
# 不同参数二元线性回归
"""
---- author = "liang wu" ----
---- time = "20150705" ----
---- Email = "wl062345@gmail.com" ----
"""
from scipy import stats
import numpy as np
import pylab
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


def regression(a, b):

    df = pd.read_csv("dataSat.csv", sep=',', header=0)
    df = df.dropna()
    df = df.reset_index(drop=True)
    df = df[df['est_time'] >= 20140701010000]
    df = df[df['est_time'] <= 20140801010000]
    array = df.values
    x = np.array(array[:, a])
    y = np.array(array[:, b])

    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
    predict_y = intercept + slope * x
    pred_error = y - predict_y
    degrees_of_freedom = x.shape[0] - 2
    residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
    X = sm.add_constant(x) # intercept
    model = sm.OLS(y, X)
    fit = model.fit()
    print "回归方程参数: %s"%fit.params
    print "回归方程确定性系数: %s"%fit.rsquared
    print "回归方程残差: %s"%np.sqrt(fit.mse_resid)
    function = "y = " + "%s + "%intercept + "%s * x"%slope
    print "回归方程为:     "
    print "y = " + "%s + "%intercept + "%s * x"%slope
    fig = plt.figure(figsize=(10,6))
    rect = fig.patch
    rect.set_facecolor('white')
    plt.plot(x, y, 'o', markersize = 3, color='blue')
    plt.plot(x, predict_y, 'k-', label="$"+function+"$")
    plt.legend()
    plt.show()

pm25 = 2
pm10 = 3
o3 = 4
no2 = 5
so2 = 6
co = 7

regression(pm10, pm25)