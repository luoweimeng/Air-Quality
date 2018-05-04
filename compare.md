
## RMSE计算结果

Model|  lag=4, predict=1 | lag=8, predict=1|lag=8, predict=3
-----|-------------------|-----------------|--
LR   |        34.8       | 37.1 |37.1, 46.9, 53.7
LSTM |        33.1       | 29.8 |29.7, 35.9, 40.1

LR feature selection 作用不大 21* 8=168 features -> 20% features

LR: linear regression

### Increase training set: training: 4930, test:548

Model|  lag=4, predict=1 | lag=8, predict=1|lag=8, predict=3
-----|-------------------|-----------------|--
LR   |               |   |33.8, 43.0, 48.9
LSTM |               |   |26.8, 34.8, 40.6