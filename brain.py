#coding=utf-8
# 此脚本实现了利用pybrain模块预测接下来一天的pm25浓度
"""
---- author = "liang wu" ----
---- time = "20150705" ----
---- Email = "wl062345@gmail.com" ----
"""
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
import pandas as pd
import numpy as np
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
import random
import time

def normalize(mat):
    mean = mat.mean(axis=0)    # 每一列数据均值
    dif = mat - mean
    std = mat.std(axis=0)      # 每一列数据方差
    norMat = dif/std           # 计算归一化值
    return norMat

def getTrainData():
    df = pd.read_csv("dataSat.csv", sep=',', header=0)
    df = df.dropna()                                      # 去除NaN值
    df = df.reset_index(drop=True)
    df = df[df['est_time'] >= 20150101010000]
    df = df[df['est_time'] <= 20150128010000]
    len = df.shape[0]
    array = df.values
    X = array[:len-1, 2:13]
    X = normalize(X)
    y = array[1:,2]
    y = normalize(y)
    for i in range(X.shape[0]):
        ds.addSample(X[i], y[i])

def getTestData():
    df = pd.read_csv("dataSat.csv", sep=',', header=0)
    df = df.dropna()
    df = df.reset_index(drop=True)
    df = df[df['est_time'] >= 20150201010000]
    df = df[df['est_time'] <= 20150208010000]
    len = df.shape[0]
    array = df.values
    X = array[:len-1, 2:13]
    X = normalize(X)
    y = array[1:,2]
    y = normalize(y)
    for i in range(X.shape[0]):
        out.addSample(X[i], y[i])
    return X, y

start = time.clock()
net = buildNetwork(11, 6, 5, 1, bias=True, hiddenclass=TanhLayer)      # 构建神经网络
ds = SupervisedDataSet(11, 1)                                          # 创建11个特征1个标签的数据集
getTrainData()                                                         # 导入训练数据
trainer = BackpropTrainer(net, ds, momentum=0.1, verbose=True, weightdecay=0.01)     # 构建后向反馈神经网络
print "开始训练"
trainer.trainEpochs(epochs=20)                                         # 迭代训练，训练次数为20
print "训练完成"
out = SupervisedDataSet(11, 1)
test, label = getTestData()                                            # 导入测试数据
out = net.activateOnDataset(out)
print "预测完成"

c = random.randint(0, label.shape[0])
print('true number is: ' + str(label[c]),
    'prediction number is:' + str(out[c]),
      'error:' + str((out[c]-label[c])/label[c]))                      # 测试预测精度
np.savetxt("predict.txt",c)                                            # 保存预测结果
elapsed = (time.clock()-start)
print "time used:" + str(elapsed)