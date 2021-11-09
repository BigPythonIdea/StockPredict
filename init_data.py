import pandas as pd
import numpy as np
import xgboost

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Ridge
from sklearn import linear_model

from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, mean_absolute_percentage_error

df = pd.read_csv('talibsIII.csv', index_col=0)

scaler = MinMaxScaler()
for i in df:
    df[[str(i)]] = scaler.fit_transform(df[[str(i)]])
    
X = df.drop(['Price'], axis = 1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, shuffle=False)

##############################以下設計參數############################

# 參數範例
param_grid = {
    'max_depth' : [20],
    'n_estimators' : [140], 
    'gamma' : [0.5],
    'subsample' : [0.8, 1.0],
    'colsample_bytree' : [0.8, 1.0],
    'reg_alpha': [0, 0.2] ,
    'reg_lambda' : [0, 0.2]
}

##############################以下設計模型############################

#模型範例
clf = xgboost.XGBRegressor()
clf.fit(X_train, y_train)

############################驗證模型################################

# 回歸方法 X_test, y_test, X_train, y_train
# 範例
def validation(*args):
    predict = args[1].predict(args[2])
    accuracy = explained_variance_score(args[3], predict, multioutput='uniform_average')
    R2 = args[1].score(args[4], args[5])
    mse =  mean_squared_error(args[3], predict)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(args[3], predict)
    mape = mean_absolute_percentage_error(args[3], predict)
    print("{}_validation :\n Acc : {}\n MSE: {}\n RMSE : {}\n Mae : {}\n MAPE : {}" .format(args[0], accuracy, mse, rmse, mae, mape))

print(validation("Xgboost", clf, X_test ,y_test ,X_train ,y_train))