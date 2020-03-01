# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:44:50 2019

@author: SeasonTaiInOTA
"""

from numba import jit
import numpy as np
import time
import math
import matplotlib.pyplot as plt

S = 100  #初始價格
T = 252  #交易日
mu = 0.2  #報酬率
vol = 0.33  #波動度

@jit
def plot(a):
    #報酬呈常態分佈
    daily_returns=np.random.normal(mu/T,vol/math.sqrt(T),T)+1
    price_list = [S]
    
    for x in daily_returns:
        price_list.append(price_list[-1]*x)
    return price_list

start = time.time()
for i in range(1000000):
    plot(T)
    #plt.plot(plot(T))
#plt.show()
end = time.time()
print("Elapsed time = %s" % (end - start))