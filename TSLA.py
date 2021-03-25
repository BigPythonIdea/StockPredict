# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:47:14 2021

@author: Mooncat

以AAPL Model 預測 TSLA
"""

import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout, LSTM



df = pd.read_csv('TSLA.csv')

#重組資料Date Low
data = pd.DataFrame(df, columns=["Date", "Low"])

#分割train test
test = data[data.Date>'2020-01-01']
train = data[:len(data)-len(test)]

#取出Low作為縮放代表
train_set = train['Low']
test_set = test['Low']


#縮放資料0~1之間 規一化
sc = MinMaxScaler(feature_range = (0, 1))
train_set= train_set.values.reshape(-1,1)
training_set_scaled = sc.fit_transform(train_set)

#切割每10個一組
x_train=[]
y_train=[]
for i in range(10,len(train_set)):
    x_train.append(training_set_scaled[i-10:i-1, 0])
    y_train.append(training_set_scaled[i, 0])

#目前有1000組 每組資料有9個數據 因此要reshape -> (1000,9,1)
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

model = Sequential()
model.add(LSTM(units = 100,return_sequences=True, input_shape = (x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units = 100,activation='tanh'))
model.add(Dense(1))
model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.summary()

history = model.fit(x_train, y_train, epochs = 500, batch_size = 16)

predict_data = df['Low']

#輸入TSLA的資料當作預測樣本 
inputs = np.array(predict_data)

# #轉化成1行 259列
inputs = inputs.reshape(-1,1)

# #歸一化
inputs = sc.transform(inputs)

# #每10個為一組進行預測
X_test = []
for i in range(10, len(inputs)):
    X_test.append(inputs[i-10:i-1, 0])


# #轉成nparray reshape成 249,9,1
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# #預測結果
predicted_stock_price = model.predict(X_test)

# #使用sc的 inverse_transform將股價轉為歸一化前
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

plt.plot(df['Low'].values, color = 'black', label = 'Real TSLA Stock Price')
plt.plot(predicted_stock_price, color = 'green', label = 'Predicted TSLA Stock Price')
plt.title('TATA Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()








