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

### 實驗結果1
| XGB |      ACC      |  
|----------|:-------------:|
| Acc |  0.87 |  |
| R2 |    0.99   | 
| MSE | 0.000283 | 
| RMSE | 0.016829 | 
| MAE | 0.009619 |  
| MAPE | 0.088048 |

<br/>

### 實驗結果2                                                      
| GS-XGB |      ACC      |                    
|----------|:-------------:|
| Acc |  0.75 |  |
| R2 |    0.97   | 
| MSE | 0.000558 | 
| RMSE | 0.023630 | 
| MAE | 0.016411 |  
| MAPE | 0.164829 |


