# LET'S GO BOSTON HOUSE PRICE PREDICT

# PACKAGES LOAD
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
import seaborn as sns
from seaborn import heatmap
import matplotlib.pyplot as plt
import sklearn
from  sklearn import  preprocessing
from  sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from  sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score, mean_squared_error, mean_absolute_error, r2_score
from sklearn.svm import SVR
import statsmodels.api as sm
from sklearn.linear_model import Ridge
from scipy import stats

# DATA LOAD
boston = load_boston()
print(boston.DESCR)
train_x = pd.DataFrame(boston.data, columns= boston.feature_names)
train_y = pd.DataFrame(boston.target, columns= ['MEDV'])
df = pd.concat([train_x, train_y], axis=1)


#DATA CHECK
train_x.columns
train_x.isna().sum()
train_x.head(5)
train_x.shape
print(df[df.columns[0:6]].describe())
print(df[df.columns[6:12]].describe())
print(df[df.columns[12:]].describe())
# boxflot으로 이상치보기
fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in df.items():
    sns.boxplot(y=k, data=df, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0) # medv outlier


sns.distplot(train_y)
df = df[df['MEDV'] < 50]
df.shape
# -----------------------
# EDA
fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in df.items(): # 왜도가 심한 것들이 많음
    sns.distplot(v, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
# PLOT # HEON : OUTLIER 제거 필요 # 데이터가 적으니까 log
cols = ["MEDV", "RM", "AGE", "RAD"]
sns.pairplot(df[cols])
plt.show()

# CORR HEATMAP # HEON : 다중공선성 제거
plt.figure(figsize=(20,20))
sns.heatmap(data = df.corr(), annot=True,
            fmt = '.2f',  cmap='Blues')
sel_columns = ['INDUS', 'LSTAT', 'NOX', 'PTRATIO', 'RM', 'TAX', 'DIS', 'AGE']
x = df.loc[:, sel_columns]
from sklearn.preprocessing import RobustScaler
minmax = MinMaxScaler()
minmax.fit(x)
x = minmax.transform(x)
#robustScaler = RobustScaler()
#print(robustScaler.fit(x))
#x = robustScaler.transform(x)
y = df['MEDV']
x = pd.DataFrame(data = x, columns= sel_columns)
x.isna().sum()
x.shape
y.shape
fig, axs = plt.subplots(ncols = 4, nrows =2, figsize= (20,10))
index= 0
axs = axs.flatten()
for i, k in enumerate(sel_columns):
    sns.regplot(y=y, x=x[k], ax=axs[i])
plt.tight_layout(pad=0.4, w_pad =0.5, h_pad=5.0)

# LOG를 안했을 때 결과는 어떨까??
x_notlog = x
y_notlog = y
x_notlog
# 왜도 줄이기 위한 LOG 근데 y는 왜 로그하냐?
np.abs(x.skew())  # 이렇게 하면 안되겠지? left skew 에 대해서 오히려 증폭? 그림상으론 문제없는듯
y = np.log1p(y)


for col in x.columns:
    if np.abs(x[col].skew()) > 0.3:
        x[col] = np.log1p(x[col]) # warning 안돌아간다는 소리 왜일까? robust라서그래~
x_notlog.head(5)
x.head(5)
x.isna().sum()
x_notlog.isna().sum()
x.columns
# -----------------
# CLEANING
# DUMMY # 다시해야해 이부분
#train_x2 = pd.concat([x,pd.get_dummies(train_x['CHAS'],drop_first= True)], axis=1)
#train_x2
#train_x2.columns[:-1]

# -------------------------------
# PREDICT

# split인데 그냥 안함
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2)

# LinearRegression # HEON : MSE가 너무 높음
reg = LinearRegression()
reg.fit(x,y)
y_pred =reg.predict(x)
mean1 =mean_squared_error(y, y_pred).
3266666666666666666666555555555555555555555
mean1
pow(10, mean1)
r2_score(y, y_pred)
reg.coef_
reg.intercept_


# Lidge
a = (0.1, 0.01, 1, 10 ,100)
b = []
c = []
for i in a :
    rid = Ridge(alpha= i)
    rid.fit(x,y)
    b = b+ [r2_score(y, rid.predict(x))]
    c = c+ [mean_squared_error(y, rid.predict(x))]
b
len(c)
for i in range(len(c)):
    print(pow(10, c[i]))

for i, z in enumerate(c):
    print(pow(10, c[i]))


# SVM
svm = SVR()
svm.fit(train_x, train_y)
svm.score(svm.predict(train_x), train_y)
pred2 = svm.predict(train_x)
train_y
r2_score(train_y, pred2)
mean_squared_error(train_y , pred2)

'''
# statsmodels
tmp=  sm.OLS(train_y, train_x).fit()
predict = tmp.predict(train_x)
tmp.summary()
model = sm.OLS(train_x, train_y).fit()
prdic = model.predict(train_x)

prdic.mean()
train_y
print(model.summary())
'''
