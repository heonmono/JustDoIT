# 정렬 알고리즘 종률 : 버킷, 기수, 선택, 교환, 삽입, 셀, 병합, 퀵, 힙 정렬

'''
그림으로 정리한 자료구조와 알고리즘 책을 정리하는 것을 목표로 한다.
자료구조 부분은 edwith강의로 대체하였기에, 책을 정리하지는 않는다.
'''

# 1. Bucket Sort
'''
자료의 버킷이라는 단위 기억 장소에 정렬, 버킷별 키값에 따라 다시 정렬
1. 정렬 데이터 확보, 정렬 데이터 이상의 공간 확보 후 숫자를 해당하는 공간에 차례로 할당
2. 데이터 각자 위치 할당 후 처음부터 읽어서 값 출력'''

# 2. 기수 정렬 알고리즘
'''
버킷 정렬의 경우, 데이터가 1, 1000이면 1000개의 공간이라는 문제
각 자릿수별로 버킷 정렬을 반복 수행
1. 각 자릿수는 0~ 9
2. 1의 자릿수 기준 버킷 정렬
3. 10의 자릿수 기준 버킷 정렬
3. 100의 자릿수 기준 버킷 정렬'''

# RadixSort
def radix(order) :
    is_sorted = False # 정렬 여부
    position = 1 # 1의 자리부터

    while not is_sorted : # 정렬 x 라면
        is_sorted = True
        queue_list = [list() for _ in range(10)] # 10자리를 만들어줌

        for num in order :
            digit_number = (int) (num/position) % 10 # 몇번째 자리인지 선정
            queue_list[digit_number].append(num)
            if is_sorted and digit_number > 0 :
                is_sorted = False
        index = 0

        for numbers in queue_list :
            for num in numbers : # queue list에 있는 number를 통해 order index 변화
                order[index] = num
                index += 1
        position *= 10 # 10의 자리로 다시 시작


# 선택 정렬 알고리즘 (Selection Sort)
'''
선택 정렬 알고리즘 - 가장 작은 데이터를 찾아 가장 앞 데이터와 교환하는 알고리즘
데이터 중 가장 작은 것을 찾아서 처음에 있는 것과 위치를 교환
두 번째부터 마지막까지의 데이터 중 가장 작은 것을 찾아서 두번째와 위치 교환'''

def change(x, i, j) : # i , j의 위치를 변경
    x[i], x[j] = x[j], x[i]

def SelectionSort(x) :
    for size in range(len(x)-1,-1, -1) :
        max_i = 0
        for i in range(1, 1+size) :
            if x[i] > x[max_i] :
                max_i = i
        change(x, max_i, size)

x = [5, 2, 8, 9, 1, 3]
SelectionSort(x)


# 교환 정렬 알고리즘(exchange sort)
''' 
작은 것부터 큰 순서로 정렬할때, 작은 키를 갖는 데이터를 찾아 앞 데이터와 교환하는 알고리즘
1. 앞에서부터 인접 두개의 크기 비교
2. 끝까지 수행 후 다시 처음부터 동일 반복'''
'''
def ExchangeSort(x) :
    for i in range(len(x)) :
        for j in range(i, len(x)) :
            if x[i] > x[j] :
                change(x, i, j)
    return x
'''

def mergeSort(x) :
    if len(x) > 1 :
        mid = len(x) // 2 # 반으로 나눠준다
        left_mid = x[:mid] # 왼쪽
        right_mid = x[mid :] # 오른쪽
        mergeSort(left_mid)
        mergeSort(right_mid)

        lefti, righti, i = 0,0,0
        while lefti < len(left_mid) and righti < len(right_mid) : # 반으로 나눈 것들이 lefti보다 큰동안
            if left_mid[lefti] < right_mid[righti] : # right가 더 크면 x[i]에 left
                x[i] = left_mid[lefti]
                lefti += 1
            else :
                x[i] = right_mid[righti]
                righti += 1
            i+=1
        x[i:] = left_mid[lefti:] if lefti != len(left_mid) else right_mid[righti:] # left i 의 숫자가 left의 숫자와 다르면 x[i:]는 left[lefti:]와 동일 아니면 right[righti:]와 동일.

x = [3 , 5 ,9 ,2 ,6 ,10]
mergeSort(x)
x

# 삽입 정렬 알고리즘(insert sort)
'''위치 교환이 발생한 것을 대상으로 주변의 것과 비교하여 위치를 교환'''

def insertSort(x) :
    i = 0
    while i < len(x) :
        if x[i] < x[i+1] : # 다음 것이 더 크면 변환 x
            pass
        else :
            x[i], x[i+1] = x[i+1], x[i] # 다음 것이 더 크면 변환
            i = i -1 # 문제점은 무한루프로 빠진다는 것. i가 증가되었다 작아지기를 반복
        i = i+1

def insertSort(x) :
    for size in range(1, len(x)) :
        val = x[size] # val로 따로 빼줌으로써, 이전것과 지속적인 변화 확인 가능
        i = size # size

        while i > 0 and x[i-1] > val : # 이전것이 1번째보다 크면
            x[i] = x[i-1]
            i -= 1
        x[i] = val

x = [3 , 5 ,9 ,2 ,6 ,10]
insertSort(x)
print(x)


# 쉘 정렬 알고리즘(shell sort)
'''삽입 정렬의 느린 속도를 보완하기 위해 만들어짐, 그룹을 나누어 쉘정렬 수행하고 마지막에 삽입정렬
1. 2개의 무리로 분할하고 각 무리의 처음값을 비교하여 작은 것이 앞으로
2. 3개의 무리로 나누어 동일 작업 수행, 1개로 구성될떄까지 진행
3. 삽입 정렬을 수행'''
'''
잘못된 이해였다. 삽입정렬은 뒤에서부터 앞에부분까지 하나씩 순차적으로 간다. 이것을 대신하여
한칸씩이 아니라 여러칸씩 이동하여 이동시간을 줄이는 것을 목표로 한다.'''


def Between(x, start, ranges) :
    for target in range(start+ ranges, len(x), ranges) : # range start에서 끝까지 ranges간격으로 이동
        val = x[target] # 이것은 삽입정렬과 유사
        i = target
        while i > start :
            if x[i - ranges] > val : # 이 전것과 비교
                x[i] = x[i - ranges] # 현재 x[i]에 이전것으로 넣기
            else:
                break
            i -= ranges
        x[i] = val # 줄어든 x[i]에 삽입

def shellSort(x) :
    ranges = len(x)//2 # gap의 크기를 반씩 줄이는것과 유사하다.
    while ranges >0 :
        for start in range(ranges) :
            Between(x, start, ranges)
        ranges = ranges//2 # gap의 크기를 점점 줄이는 것이다.


def shellSort(x) :
    # 무리를 점점 나누기
    i = 2
    y = 0
    while cut == 0  :
        cut = len(x) // i
        for z in range(i) :
        x1, x2 = x[:cut], x[cut:]
        j = 0
        for j in range(cut) :
            if x1[j] < x2[j] :
                x1[j] , x2[j] = x2[j], x1[j] # 데이터가 한개까지

    insertSort(x)

x = [5, 2, 8, 6, 1, 3]
shellSort(x)
print(x)

# 병합 정렬 알고리즘(Merge Sort)
'''병합 정렬 알고리즘은 데이터를 분할한 다음 각자 계산하고 나중에 합쳐서 정렬하는 알고리즘
작은 수에서 큰 수로 정렬한다고 가정
정렬 데이터 단위 최소 한개 될 때까지 분할 작업 반복
분할된 데이터를 대상으로 2, 4, 8개씩 병합하면서 정렬을 수행
최종적 2무리가 만들어진 후, 2차 병합 알고리즘을 적용'''


# 퀵 정렬 알고리즘(Quick sort)
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


# 힙정렬 알고리즘
'''힙정렬은 힙의 개념을 이용하여 정렬하는 알고리즘
1. 주어진 자료를 기반으로 힙을 구성, 큰수에서 작은수로 정렬하고자 한다면 
최상위 데이터를 가장 큰 수로 설정하도록
2. 최상위 데이터를 빼고 나면 나머지 데이터로 다시 힙을 구성 가장 큰 수가 최상위
데이터'''

