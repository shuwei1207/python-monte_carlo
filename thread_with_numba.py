# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:40:09 2019

@author: USER
"""

#coding=utf-8
import threading
import time
import numpy as np
import math
import matplotlib.pyplot as plt
from queue import Queue
from numba import jit
import warnings
import sys
sys.setrecursionlimit(9000000) #這裡設定大一些
warnings.filterwarnings('ignore')

@jit
def thread_job(arr,q):
    daily_returns=np.random.normal(mu/T,vol/math.sqrt(T),T)+1
    arr = [S]
    for x in daily_returns:
        arr.append(arr[-1]*x)
    q.put(arr)
    #print(arr)
    
@jit
def multithreading():
    q = Queue()   # 宣告 Queue 物件
    threads = []  # 用來放 thread 的 array
    price_list=[[S] for i in range(times)]
    for i in range(times):
        t = threading.Thread(target=thread_job, args=(price_list[i],q)) 
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join() # 每個 thread 都要做 join
    
    results = [] # 用來接收與顯示結果的 array
    
    for _ in range(times):
        results.append(q.get())# 取出 queue 裡面的資料
        #plt.plot(results.pop())
    
if __name__=='__main__':
    
    times = 10000
    S = 100  #初始價格
    T = 252  #交易日
    mu = 0.2  #報酬率
    vol = 0.33  #波動度
    
    tStart = time.time()
    multithreading()
    tEnd = time.time()#計時結束
    #列印結果
    print ("耗時:" , (tEnd - tStart))#會自動做近位