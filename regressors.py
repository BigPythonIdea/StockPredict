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


clf = xgboost.XGBRegressor()
rig = Ridge(alpha=2.0)
bay = linear_model.BayesianRidge()

clf.fit(X_train, y_train, eval_set=[(X_train, y_train)], callbacks=[es])
rig.fit(X, y)
bay.fit(X, y)

# 回歸方法 X_test y_test X_train y_train
def validation(*args):
    predict = args[1].predict(args[2])
    accuracy = explained_variance_score(args[3], predict, multioutput='uniform_average')
    R2 = rig.score(args[4], args[5])
    mse = metrics.mean_squared_error(args[3], predict)
    print("{}_validation : Acc : {:.2f}, R2 : {:.5f}, Mse: {:.2f}".format(args[0], accuracy, R2, mse))

print(validation("Xgboost", clf, X_test ,y_test ,X_train ,y_train))
print(validation("Ridge", rig, X_test ,y_test ,X_train ,y_train))
print(validation("Bayesian", bay, X_test ,y_test ,X_train ,y_train))