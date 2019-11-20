# PACKAGES LOADED
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import os
import warnings
warnings.filterwarnings("ignore")
print("PACKAGE IS LOADED")
# os
cwd = os.chdir(r"C:\Users\heon1\Desktop\big_contest_data\airplane_data")
cwd = os.getcwd()
print("Current folder is %s" %cwd)
# ROAD DATA
test_x = pd.read_csv(cwd + "\AFSNT_DLY.csv", encoding= 'euc-kr')
train_x = pd.read_csv(cwd+ "\AFSNT.csv", encoding = 'euc-kr')
SFSNT = pd.read_csv(cwd + "\SFSNT.csv", encoding='euc-kr')
#train_x = pd.read_csv(r'C:\Users\heon1\Desktop\big_contest_data\airplane_data\AFSNT.csv', encoding='euc-kr')

# DATA CHECK
train_x.columns
test_x.columns
SFSNT.columns
train_x.isna().sum() # reg 8200개
test_x.isna().sum()
train_x.shape
train_x.head(5)
# 전처리 전 dly수
dly_count = train_x[train_x['DLY'] == 'Y'].shape[0]

# -----------------------
# DATA CLEANING
# reg na는 cnl
reg_cnl_rate = (train_x[(train_x['REG'].isna() == True) & (train_x['CNL'] == 'Y')].shape[0]/
                train_x[train_x['REG'].isna() == True].shape[0])
print(reg_cnl_rate)

# Drop columns
del_columns =['CNR', 'CNL', 'DRR', 'FLT']
train_x.drop(del_columns, axis=1, inplace= True)

# reg na 99% IS CNL, SO DROPNA
train_x.dropna(inplace= True)
train_x.isna().sum()
train_x.shape


# IRR 부정기 삭제 (21296개 삭제, 이 중 3218개 DLY
irr_dly = train_x[(train_x['IRR'] == 'Y') & (train_x['DLY'] == 'Y')].shape[0] #부정기이면서 dly인 경우  15% 지연
irr_del = train_x.shape[0] - train_x[train_x.IRR != 'Y'].shape[0]
print("IRR = 'Y'로 삭제 되는 수 : %d\nIRR 삭제 중 DLY 비율 %f" %(irr_del, irr_dly/irr_del))
train_x = train_x[train_x.IRR != 'Y']
train_x.drop(['IRR'], axis=1 , inplace = True)
train_x.shape
# DATE 합치기, REG COUNT에서 사용
day = pd.DataFrame({'year' : train_x['SDT_YY'],
                    'month' : train_x['SDT_MM'],
                    'day' : train_x['SDT_DD']})
train_x['DATE'] = pd.to_datetime(day)
#---------------------------------------------
# STT의 시간 별, 시간+분 통해 REGCOUNT 계산
    # 1. str.split ':'
new2 = train_x['STT'].str.split(":", n=2, expand = True)
    # 2. change 'objects' to 'int'
new2 = new2.astype(int)
new2.dtypes
    # 3. 나눈 것 중 stt time , test에 없는 0,1,23 시 행 제거 # 27개 삭제
train_x['stt_h'] = new2[0]
train_x = train_x.drop(train_x[train_x['stt_h'] == 0].index, axis=0)
train_x = train_x.drop(train_x[train_x['stt_h'] == 1].index, axis=0)
train_x = train_x.drop(train_x[train_x['stt_h'] == 23].index, axis=0)
train_x.shape # 14개
    # 4. hour * 60 + minite으로 시간   # reg만드는데 사용
train_x['time_mh'] = new2[0]*60 + new2[1]
    # 5. stt_h 시간 별 딜레이률 계산
stt_hhh_ratio = (pd.get_dummies(train_x[train_x['DLY'] == 'Y']['stt_h']).sum()/
                 pd.get_dummies(train_x['stt_h']).sum())
print(stt_hhh_ratio)
train_x = pd.concat([train_x, pd.get_dummies(train_x['stt_h'])], axis=1) #17개추가
    # ATT, STT, DUMMY DELETE
train_x.drop(['ATT','STT', 6], axis=1, inplace=True) #0,1,23 test에 없어서 29개
train_x.shape
# 중간 저장
train_x2 = train_x


#-----------------ARP,ODP DUMMY화 카테고리화 및 원본칼럼 제거
arp_odp = train_x['ARP'] + train_x['ODP']
arp_odp.shape
ARP_ODP = pd.get_dummies(arp_odp) #40개
train_x = pd.concat([train_x, ARP_ODP], axis=1)
train_x.shape # 958150,69
train_x.drop(['ODP','ARP'],axis=1, inplace=True)

# ------------------------------------------------------------------------
# dly, flo, aod, dy  dummy, MAKING REG 후에 더미 FIRST DEL
# dummy화 하고 concat으로 넣고 그다음 하나씩 삭제해줘야해 dly빼고
flo = pd.get_dummies(train_x['FLO'])
aod = pd.get_dummies(train_x['AOD'])
dy = pd.get_dummies(train_x['SDT_DY'])
# A,D 구분 위해서 칼럼명 변경
aod2 = pd.DataFrame(aod)
train_x = pd.concat([train_x, aod2], axis= 1)
train_x = train_x.rename(columns = {'A' : 'ARRIVE',
                                    'D' : 'DEPARTURE'})

train_x = pd.concat([train_x, flo, dy], axis= 1)
train_x.shape # dummy 16개 증가 958123, 83 # 더미는 958123,14


# regcount
train_x_sort = train_x.sort_values(by=['REG', 'DATE', 'time_mh', 'ARRIVE'])
train_x_sort.reset_index(inplace=True)
train_x_A = train_x_sort[train_x_sort['ARRIVE'] == 1]
train_x_D = train_x_sort[train_x_sort['ARRIVE'] == 0]
train_x_A['reg_count'] = train_x_A.groupby(['REG', 'DATE'])['ARRIVE'].cumsum()
train_x_D['tmp'] = 1
train_x_D['reg_count'] = train_x_D.groupby(['REG', 'DATE'])['tmp'].cumsum()
tmp1 = pd.merge(left=train_x_sort, right=train_x_A['reg_count'], how='outer', right_index=True, left_index=True)
tmp2 = pd.merge(left=train_x_sort, right=train_x_D['reg_count'], how='outer', right_index=True, left_index=True)
train_x_sort['reg_count'] = tmp1['reg_count'].fillna(0) + tmp2['reg_count'].fillna(0)
train_x_sort['reg_count'] = train_x_sort['reg_count'].astype(int)
train_x = train_x_sort

# reg predict y
reg_train_y = train_x_sort['reg_count']
reg_train_y = {'reg_count' : reg_train_y}
reg_train_y = pd.DataFrame(reg_train_y)

# dummy 하나씩 삭제
del_columns2 = ['ARP11ARP1', 'ARRIVE', '월', 'A']
train_x.drop(del_columns2, axis = 1, inplace = True)

# dly to y
train_y = pd.get_dummies(train_x['DLY'])['Y']
train_y = {'DLY' : train_y}
train_y = pd.DataFrame(train_y)
train_y.sum() # 전처리 후 딜레이 115711


#reg 정규화
train_x['reg_count'] = (train_x['reg_count'] - train_x['reg_count'].mean())/ train_x['reg_count'].std()
pd.DataFrame.describe(train_x['reg_count'])
# 이미 사용 혹은 쓰지 않을 columns 삭제
del_columns3 = ['index', 'SDT_YY', 'SDT_MM', 'SDT_DD', 'SDT_DY', 'FLO', 'AOD', 'REG','DLY', 'DATE', 'stt_h', 'time_mh']
train_x.drop(del_columns3, axis = 1, inplace = True)
train_x.columns
train_x.dtypes
train_x.shape # 958150,69
# --------------------------------------------------
reg_train_x = train_x.drop(['reg_count'], axis=1)
reg_train_x.columns
reg_train_x.shape #68개



# --------------------------------------------------
# Reg PREDICT
# PACKAGE LOAD
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.externals import joblib
from sklearn.metrics import roc_auc_score
from sklearn.metrics import mean_squared_error
from math import sqrt

reg_train_x =pd.read_csv(cwd+r"\reg_train_x.csv", encoding= 'euc-kr')
reg_train_x
reg_train_y =pd.read_csv(cwd+r"\reg_train_y.csv", encoding= 'euc-kr')
reg_train_y
# TRAIN TEST 분리
reg_train_y =np.ravel(reg_train_y)
x_train_reg, x_test_reg, y_train_reg, y_test_reg = train_test_split(reg_train_x, reg_train_y, test_size=0.3, random_state=0)  #stratify=y 안됨

param_grid = {
'bootstrap': [True],
'max_depth': [40, 50],
'max_features': [5],
'min_samples_leaf': [3],
'n_estimators': [50, 100]}

rf = RandomForestClassifier()
grid_reg = GridSearchCV(estimator = rf, n_jobs=-1, param_grid= param_grid,cv=3)
grid_reg.fit(x_train_reg ,y_train_reg)

# if want output directly
#grid_reg =joblib.load(r'C:\Users\heon1\Desktop\big_contest_data\airplane_data\grid_reg.pkl')


grid_reg.best_score_
grid_reg.best_params_
grid_reg.predict(x_test_reg)
#rf = RandomForestClassifier(bootstrap=True, max_depth=40, max_features=5, min_samples_leaf=3, n_estimators=100)

# 정확도 확인
accuracy_score(y_train_reg, grid_reg.predict(x_train_reg))
accuracy_score(y_test_reg , grid_reg.predict(x_test_reg))



#------------------------------
# test STT 전처리
test_x.columns # stt, arpodp, aod, flo dy reg
    # STT ":" 제거
new_test = test_x['STT'].str.split(":", n=2, expand= True)
    # TPYE INT로 변경
new_test = new_test.astype(int)
    # STT_H 더미화
test_x['stt_h'] = new_test[0]
test_x = pd.concat([test_x, pd.get_dummies(test_x['stt_h'])], axis=1) # 17개추가 , not first drop

test_x.drop(['STT'], axis=1, inplace=True)
test_x.shape #29개
print(test_x.head(1))


#test ARPODP 만들어주기
arp_odp_test = test_x['ARP'] + test_x['ODP']
ARP_ODP_test = pd.get_dummies(arp_odp_test)
    #ARP ODP TRAIN셋과 비교
list(set(ARP_ODP_test.columns) - set(ARP_ODP.columns)) # TEST가 4개 더 많으므로 TRAIN있는 칼럼으로 변환
ARP_ODP_test.shape                                     # 2가 포함된 1-2, 1-3으로 변환
ARP_ODP_test['ARP1ARP2'] = ARP_ODP_test['ARP10ARP2'] + ARP_ODP_test['ARP1ARP2']
ARP_ODP_test['ARP2ARP1'] = ARP_ODP_test['ARP2ARP10'] + ARP_ODP_test['ARP2ARP1']
ARP_ODP_test['ARP1ARP3'] = ARP_ODP_test['ARP10ARP3'] + ARP_ODP_test['ARP10ARP3']
ARP_ODP_test['ARP3ARP1'] = ARP_ODP_test['ARP3ARP10'] + ARP_ODP_test['ARP3ARP10']
ARP_ODP_test.drop(['ARP10ARP2','ARP2ARP10','ARP10ARP3','ARP3ARP10'], axis=1, inplace=True)
ARP_ODP_test.shape #40개
test_x = pd.concat([test_x, ARP_ODP_test], axis=1)
test_x.shape #69개
# FLO 더미화
flo_test = pd.get_dummies(test_x['FLO'])
flo_test.columns
    # M은 TRAIN에 없기 때문에, J로 변환
flo_test['J'] = flo_test['M'] + flo_test['J']
flo_test.drop(['M'], axis=1, inplace=True)
# AOD 더미화
aod_test = pd.get_dummies(test_x['AOD'])
# DY 더미화
dy_test = pd.get_dummies(test_x['SDT_DY'])
# AOD 추가 후 ARRIVE, DEPARTURE로 변환
aod22 = pd.DataFrame(aod_test)
test_x = pd.concat([test_x, aod22], axis=1)
test_x.shape
test_x = test_x.rename(columns = {'A' : 'ARRIVE',
                                  'D' : 'DEPARTURE'})
# FLO, DY 추가
test_x = pd.concat([test_x,flo_test, dy_test], axis=1)
test_x.shape #85개 칼럼

# 사용하지 않는 칼럼 삭제
del_columns4 = ['SDT_YY', 'SDT_MM', 'SDT_DD', 'SDT_DY', 'DLY', 'DLY_RATE',
                'FLT', 'ARP', 'ODP', 'stt_h', 'FLO', 'AOD', 'stt_h']
test_x.drop(del_columns4, axis=1, inplace =True)
# 더미화한 칼럼 삭제
del_columns5 = ['ARP11ARP1', 6, 'ARRIVE', 'A', '월']
test_x.drop(del_columns5, axis=1, inplace= True) # shape(16076, 68)

# TEST REG 예측
test_x['reg_count'] = grid_reg.predict(test_x)
# TEST REG 정규화
test_x['reg_count'] = (test_x['reg_count'] - test_x['reg_count'].mean())/ test_x['reg_count'].std()
pd.DataFrame.describe(test_x['reg_count'])

# SIZE CHECK
print("train_x shape is : %s \ntrain_y shape is : %s" %(train_x.shape, train_y.shape ))
print("test_x shape is : {0}".format(test_x.shape))
print("train, test columns check : %s" %(train_x.columns == test_x.columns).sum()) # print문으로
print("train na is : %s\ntest na is : %s)" %(test_x.isna().sum().sum() , train_x.isna().sum().sum()))



# -----------------------------
# PREDICT
train_x =pd.read_csv(cwd + r"\train_x.csv", encoding='euc-kr')
train_y =pd.read_csv(cwd + r"\train_y.csv", encoding= 'euc-kr')
test_x = pd.read_csv(cwd + r"\test_x.csv", encoding='euc-kr')

train_x.columns
train_y.columns
test_x.columns
train_y.shape
train_x.shape
test_x.shape

train_y =np.ravel(train_y)
# TRAIN TEST SPLIT
x_train, x_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.3)  #stratify=y 안됨
print("x_train, y_train shape is %s, %s: \nx_test, y_test shape is %s, %s"
        %(x_train.shape, y_train.shape,x_test.shape, y_test.shape))

# Random Forest

param_grid = {
   'bootstrap': [True],
   'max_depth': [40, 50],
   'max_features': [40, 50],
   'min_samples_leaf': [3, 5],
   'n_estimators': [150, 100],
   'class_weight' : ['balanced']
}
rf =RandomForestClassifier()
grid_search = GridSearchCV(estimator = rf, param_grid= param_grid, scoring='roc_auc', cv=3, n_jobs=-1)
grid_search.fit(x_train,y_train)
# IF YOU WANT DIRECTLY OUTPUT
#grid_search =joblib.load(r'C:\Users\heon1\Desktop\big_contest_data\airplane_data\grid.pkl')

grid_search.best_params_
grid_search.best_score_
grid_search.cv_results_
#rf = RandomForestClassifier(bootstrap=True, class_weight='balanced', max_depth=40, max_features=40, min_samples_leaf=5, n_estimators=150)
# -------------------------------------
# 결과평가
#train
accuracy_score(y_train , grid_search.predict(x_train))
confusion_matrix(y_train , grid_search.predict(x_train))
print(classification_report(y_train , grid_search.predict(x_train)))
roc_auc_score(y_train , grid_search.predict(x_train))
sqrt(mean_squared_error(y_train, grid_search.predict_proba(x_train)[:, 1]))

#test
accuracy_score(y_test , grid_search.predict(x_test))
confusion_matrix(y_test , grid_search.predict(x_test))
print(classification_report(y_test , grid_search.predict(x_test)))
roc_auc_score(y_test , grid_search.predict(x_test))
sqrt(mean_squared_error(y_test, grid_search.predict_proba(x_test)[:, 1]))

# ----------------------------------
# 예측
DLY = grid_search.predict(test_x)
DLY_RATE = grid_search.predict_proba(test_x)[:, 1]
DLY
DLY_RATE
OUTPUT = {'DLY' : DLY,
          'DLY_RATE' : DLY_RATE}
OUTPUT=  pd.DataFrame(OUTPUT)
#OUTPUT.to_csv(r'C:\Users\heon1\Desktop\big_contest_data\airplane_data\OUTPUT.csv',
#              columns= OUTPUT.columns, encoding='euc-kr', index=False)
tmp = pd.read_csv(cwd+ r"\OUTPUT.csv", encoding = 'euc-kr')
tmp
