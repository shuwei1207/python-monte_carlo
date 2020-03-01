# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:10:44 2019

@author: warrantnew.brk
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import time

S = 100  #初始價格
T = 252  #交易日
mu = 0.2  #報酬率
vol = 0.33  #波動度
    
price = np.zeros(T)
tStart = time.time()
price[0] = S
#蒙地卡羅模擬次數
for i in range(1000000):
    #報酬呈常態分佈
    x= np.random.normal(mu/T,vol/math.sqrt(T),T)+1
    for i in range(1,T):
        price[i] = price[i-1]*x[i]
        
    price=list(price)
    #plt.plot(price)
#plt.show()

tEnd = time.time()#計時結束
#列印結果
print ("耗時:" , (tEnd - tStart))#會自動做近位

