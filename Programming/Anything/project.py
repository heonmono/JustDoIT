# 학교에서 진행하는 m&a

# 1.데이터 복사되는거 어떻게 할지

'''
1. ;이 있는 걸 걸러서 중복이 있는걸 먼저 탐구

2. ; 수만큼 행을 행을 더 만들기
3. 거기에 대해서 ; split한걸 넣어줘야하는거 같은데?
4. ; 수만큼 split해서 다른 데이터프레임에 넣고 추가
'''

# package& data
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\heon1\Desktop\프로젝트\data_dematel\data_split.csv")

# 따로 df를 새로 만들어서 데이터를 축소시키는 장점이 있다. 나중에 다시 늘려준다.
# 인덱스를 추가하여서 다시 재검색하기도 편안할 수 있게 만든다.
df2 = df[df.columns[-2]]
df3 = pd.DataFrame(columns=[df.columns[-2]])
for i in range(df.shape[0]) :
    if ';' in df.iloc[i, -2]:
        df3.loc[i] = [df.iloc[i,11]]

df_dupl = df.loc[df3.index] # 나눠주어야 할것들
df_dupl.to_csv(r"C:\Users\heon1\Desktop\프로젝트\data_dematel\splited_data_0921.csv")
df_dupl = pd.read_csv(r"C:\Users\heon1\Desktop\프로젝트\data_dematel\splited_data_0921.csv")

# buyers로 몇개있는지 확인 후 행 중복으로 만들기
df_dupl.columns[5]
df_dupl.columns
df_dupl.shape
df_dupl.reset_index(drop=True, inplace = True)
# 1. 공란 삭제
df_dupl.isna().sum()
df_dupl.loc[2]
df_buyer = df_dupl[df_dupl.columns[7]] #
df_buyer.loc[1].split(";")
len(df_buyer.loc[1].split(";")) # 이 숫자로 추가하면 될듯 #그냥 outer join하면 해결되려나??

''''#data_a = {"buyer" : [df_buyer.loc[1]], "buyers" : df_buyer.loc[1].split(";")}
#data_a
#data_a = pd.DataFrame(data_a, columns= ['buyer', 'buyers'])
index = 0
tmp_df = pd.DataFrame(columns=[df_dupl.columns[6]])
for i in range(df_buyer.shape[0]) :
    len(df_buyer.loc[i].split(";"))
'''


# 어떻게 추가하지?

# 인덱스만큼 행추가
a = 0
df_dupl.columns
df_new = pd.DataFrame(columns = df_dupl.columns)
#df_new.loc[1] = df_dupl.loc[0]
df_new
for i in range(df_dupl.shape[0]) : # 각 행에 대해서
    for j in range(len(df_buyer.loc[i].split(";"))) : # 듀플 수만큼
        df_new.loc[a] = df_dupl.loc[i] # i를 df_new에 추가
        a+=1
df_new.to_csv(r"C:\Users\heon1\Desktop\프로젝트\data_dematel\splited_data_0923.csv")
df_new.shape
# 중복을 칼럼화
df_split
df_split = df[df_dupl.columns[-2:]]
df_split.columns[1]

#new_col = pd.DataFrame(columns=[df_split.columns[0]])
#new_col2 = pd.DataFrame(columns=[df_split.columns[1]])
new_list = list()
#new_list.append(df_split.iloc[0,0].split(";")[1])
#new_list
#new_list.append(3)
#len(df_split.iloc[0,0].split(";"))
#for j in df_split.iloc[0, 0].split(";"):
#    print(j)
#df_split.iloc[0,df_split.shape[0]-1].split(";")
for i in range(df_split.shape[0]):
    for j in df_split.iloc[i,0].split(";") :
        new_list.append(j)
len(new_list)
df_new.shape

# 둘이 길이가 달라 -> 어떤 buyer의 경우 secter가 없음
# 이에 따라서, 기업이름을 비교하여 만들어야함




new_col=new_col.append(df_buyer.loc[3].split(";"))
new_col.append()
new_col
new_col.append()
df_split.iloc[1,1].split(";")[]
df_buyer.loc[1].split(";")
len(df_buyer.loc[1].split(";")) # 이 숫자로 추가하면 될듯 #그냥 outer join하면 해결되려나??


df5 = df.append(pd.Series(row), ignore_index=True)
df_new

# index를 중복만큼 추가하기 인덱스만큼 늘어나야겠지?

# 나눈 것을 칼럼화 하기



# 2. 데이터 특징 탐색 - 이건 주피터가 나을 듯

