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

### My Lab(XGB):
#### 參數無調整 資料有做正規化
#### Xgboost_validation : 
#### Acc : 0.8792487960523886, 
#### R2 : 0.9999884663098598, 
#### Mse: 0.0002832283728993998

