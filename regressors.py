import pandas as pd
import numpy as np
import xgboost
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import explained_variance_score
from sklearn.linear_model import Ridge
from sklearn import linear_model
from sklearn import metrics

df = pd.read_csv('talibsII.csv', index_col=0)

X = df.drop(['Price'], axis = 1)
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, shuffle=False)

#XGB parameter
es = xgboost.callback.EarlyStopping(
    rounds=100,
    save_best=True,
    maximize=False,
    data_name="validation_0",
)

