# 1172 : 세 수 정렬하기

a = map(int, input().split(" "))

a = list(a)

a.sort()
for i in range(len(a)) :
    print(a[i], end= " ")


# 1451 : 데이터 정렬 (small)
n = int(input())

a = list()
for i in range(n) :
    b = int(input())
    a.append(b)

a.sort()

for i in range(n) :
    print(a[i])

# 3004 : 데이터 재정렬
n = int(input())

list1 = list(map(int, input().split(" ")))
list2 = list1[:]
list2.sort()
dic = dict()
for i in range(n) :
    for j in range(n) :
        if list1[i] == list2[j] :
           dic[j] = list1[i]
for key, value in dic.items() :
    print(key, end = " ")


# 3011 : 거품 정렬(Bubble Sort) .. .왜 안될까?
n = int(input())

list1 = list(map(int, input().split(" ")))
def bubble_sort(x) :
    for i in range(len(x) -1) :
        bef_list = x[:]
        for j in range(len(x) -i -1) :
            if x[j] > x[j+1] :
                x[j], x[j+1] = x[j+1], x[j]

        aft_list = x[:]
        if bef_list == aft_list :
            print(i+1)
            break

bubble_sort(list1)

# 1526 : [기초-함수작성] 함수로 hello 문자열 출력하기

def hello() :
    print("hello")

hello

# 1535 : [기초-함수작성] 함수로 가장 큰 값 위치 리턴하기

def max_index() :
    n = int(input())
    a = 0
    list1 = list(map(int, input().split(" ")))
    for i in range(1,n) :
        if list1[a] < list1[i] :
            a = i
    return a + 1


''' 퀵 정렬은 알고리즘은 중앙 값 정렬 방식을 확장해서 개발한 방식 
1. 임의로 선정된 데이터를 중심으로 데이터를 2등분
각 분리된 부분의 첫 번째 원소 기준으로 데이터를 분리
이작업 반복'''

def Quick_Sort(x) : # 내가 해서망한거
    if len(x) > 2:
        hal = 0
        l_list, r_list = list()
        # 중앙값 기준으로 좌우로 나눠야지
        for i in range(len(x)) :
            if x[i] < x[hal] :
                l_list.append(x[i])
            else :
                r_list.append(x[i])
        Quick_Sort(l_list)
        Quick_Sort(r_list) #

def change(x, i, j) : # 두 값 교환
    x[i], x[j] = x[j], x[i]

def Select(x,l, r) :
    select_val = x[l] # pivot값 설정
    select_idx = l # pivot index
    while l <= r : # 중간값을 찾아가는 의미
        while l <= r and x[l] <= select_val : # pivot값보다 작음을 의미
            l += 1  # 한칸씩 증가
        while l <= r and x[r] >= select_val : # pivot값도다 오른쪽이 클때
            r -= 1 # 오른쪽 한칸씩 아래로
        if l <= r : # l과 r이 차이가 많은것은 l에 큰것이 많다는 의미?
            change(x, l, r)
            l =+ 1
            r -= 1
    change(x, select_idx, r) # 이 과정을 거치고 나서는 r이 중간값이므로 변경
    return r

def quickSort(x, pivotMethod = Select) :
    def Qsort(x ,first, last) :
        if first < last :
            splitP = pivotMethod(x, first, last) # 정렬
            Qsort(x, first, splitP-1)
            Qsort(x, splitP+1, last)
    Qsort(x,0,len(x)-1)

x = [5 ,2 ,8,6,1,9,3,7]
quickSort(x)
print(x)
# 내가 했던 문제는 list를 나누는 것이다. list가 나누어질수록 메모리 소비가 너무크낟
# 두번째로  index첫번째를 이용하기때문에 중앙을 더 잘 찾는것이 효율적이다.