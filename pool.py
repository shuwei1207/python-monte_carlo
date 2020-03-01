# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:09:05 2019

@author: USER
"""

import matplotlib.pyplot as plt
import numpy.random as random
from multiprocessing import Pool
import numpy as np
import math
import time
#import cupy as cp


def do_plot(number):
    S = 100  #初始價格
    T = 252  #交易日
    mu = 0.2  #報酬率
    vol = 0.33  #波動度

    #蒙地卡羅模擬次數
    for i in range(10000):
        #報酬呈常態分佈
        daily_returns=np.random.normal(mu/T,vol/math.sqrt(T),T)+1
        price_list = [S]
    
        for x in daily_returns:
            price_list.append(price_list[-1]*x)
        #plt.plot(price_list)
    
    #plt.savefig("Monte Carlo")
    #plt.close()


if __name__ == '__main__':
    
    tStart = time.time()
    pool = Pool()
    pool.map(do_plot, range(1))
    tEnd = time.time()#計時結束
    #列印結果
    print ("耗時:" , (tEnd - tStart))#會自動做近位