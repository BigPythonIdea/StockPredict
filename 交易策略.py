# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:09:47 2020

@author: Mooncat
"""

import pandas as pd
import numpy as np
from talib.abstract import *
import matplotlib.pyplot as plt

df = pd.read_csv('AAPL.csv')

data = df.sort_index(ascending=True, axis=0)

lst = []
for i in range(0,1259):
    try:
        pre = df.Close[i]
        suf = df.Close[i+10]
        lst.append(pre-suf)
    except:
        pass


Money = 2000000
Profit = 0
unit = 1000
date = 0
new_date = []
Money = Money-df.Close[0]*unit*10 #初始10張
unit2 = 10 #張數

for i in lst:
    date = date+1
    if unit2 <= 0:
        print("你已經輸光了")
        break
    elif i>5:
        unit2 = unit2-5
        print("交易成功")
    elif i<-5:
        unit2 = unit+5
    else:
        pass
    

print(unit2)
        
        

    
    


















# =============================================================================
# def Rsi(close,v=None):
#     read = RSI(df['Close'],timper=14)
#     if v is None:
#         lst = []
#     for i in read:
#         if i < 45:
#             lst.append("1")
#         else:
#             lst.append("0")
#     return lst
# 
# df['RSI'] = pd.DataFrame(Rsi(df.Close))
# =============================================================================


        

    
            


