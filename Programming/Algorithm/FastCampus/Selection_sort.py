'''선택 정렬
1. 주어진 데이터중, 최소값을 찾음
2. 해당 최소값을 맨 앞의 데이터와 교체
3. 동일한 방법으로 반복'''

x = [3,1,7,6,2]
def Selection_sort(data) :
    for i in range(len(data)-1) :
        min, min_index = data[i],i # min을 그냥 i로 놓으면 1 줄이 줄고, 저장공간 하나가 줄 수 있음, 연산수는 n^2정도?

        for j in range(i+1,len(data)) :
            if min > data[j] :
                min, min_index = data[j], j
        data[min_index] = data[i]
        data[i] = min
    return data

Selection_sort(x)


# 알고리즘 복잡도
# 1.2.3.4.5.n-1까지의 합 n*n-1/2이므로 O(n^2)
