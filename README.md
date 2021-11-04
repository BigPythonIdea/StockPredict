# StockPredict

###### tags: `Solana dissertation`

# 實驗記錄

## XGBoost
### 參考論文
> An optimized XGBoost method for predicting reservoir porosity using petrophysical logs!

參數:
```
param_grid = {
    'max_depth' : [20],
    'in_child_weight' : [8],
    'n_estimators' : [140], 
    'gamma' : [0.5],
    'subsample' : [0.8, 1.0],
    'colsample_bytree' : [0.8, 1.0],
    'reg_alpha': [0, 0.2] ,
    'reg_lambda' : [0, 0.2]
}
```

對比結果:

![](https://i.imgur.com/lPimwTN.png)

### My Lab1(XGB):
#### 參數無調整 資料有做正規化
#### Acc : 0.8792487960523886
#### R2 : 0.9999884663098598
#### MSE: 0.0002832283728993998
#### RMSE : 0.016829390152331716
#### Mae : 0.009619678587472098
#### MAPE : 0.08804848964164483



### My Lab2(GS-XGB):
#### 參數依照論文 資料有做正規化
#### Xgboost_validation : 
#### Acc : 0.758098731704439
#### R2 : 0.9781578700670892
#### MSE: 0.0005583792071208798
#### RMSE : 0.02363004881757293
#### Mae : 0.016411225029281145
#### MAPE : 0.16482942970471648


