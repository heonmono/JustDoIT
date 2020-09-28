# bubble 정렬
'''인접한 두 데이터를 비교하여, 앞이 뒤보다 크면 변경'''

''' 가장 높은 값은 맨 뒤로 가는것을 판단 할 수 있음'''
a = [5,2,3,1]
a[0]
def Bubble_Sort(data) :
    for j in range(len(data)-1):
        swap = False
       for i in range(len(data)-j-1) :
           if data[i] > data[i+1] :
               data[i], data[i+1] = data[i+1],data[i]
               swap = True
           else :
               pass

        if swap == False :
            break
    return data

import random
data_list = random.sample(range(100),50)
Bubble_Sort(data_list)
Bubble_Sort(a) # (n-1)*n/2/  O(n^2)

