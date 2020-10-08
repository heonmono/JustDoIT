# 삽입정렬
'''
1. 앞부분과 비교
2. 비교 시 자기보다 크면 뒤로 미루기
3. 자기보다 작을 시 그 자리에 삽입
'''

def Insertion_sort(data) : # 스왑하기 싫어서 한번에 하려고 했는데 실패했네.
    for i in range(1,len(data)) : # 1부터 끝까지
        val = data[i]

        for j in range(i-1,-1,-1) : # i에서 역순으로
            # 1. 앞의 숫자와 비교하여 어디까지 가는지 파악한다.
            # 2. 앞의 숫자까지 다 비교하였는데 끝까지 같다면 다 미뤄버린다.
            # 3. 앞의 숫자가 더 크면
            if data[i] < data[j] : # i보다 j가 큰 경우 j를 하나씩 미뤄야해
                if j == 0 : # 0까지 가서도 i가 더 작은 경우
                    data[j + 1: i + 1] = data[j: i]
                    data[j] = val
                    break
                else :
                    pass
            else :
                if i == j :
                    pass
                else :
                    data[j+1 : i+1] = data[j:i]
                    data[j] = val
                    break
    return data


a = [3,1,4,2,5,0]
Insertion_sort(a)


def Insertion_sort(data) : # 스왑하기 싫어서 한번에 하려고 했는데 실패했네.
    for i in range(0,len(data)-1) : # 몇번 반복할 것인가
        for j in range(i+1,0,-1) : # i에서 역순으로
            if data[j] < data[j-1] : # i보다 j가 큰 경우 j를 하나씩 미뤄야해
                data[j],data[j-1] = data[j-1] , data[j]
            else :
                break
    return data

a = [3,1,4,2,5,0]
Insertion_sort(a)

# 알고리즘 분석 반복문이 두개 o(n^2)