# 동적 계획법 & 분할 정복(Divide and Conquer)
'''
동적 계획법(Dynamic Programming
작은 문제 해결 후 , 큰 부분을 해결하여 알고리즘만드는 것
최하위 해답 구한 후 저장하여 상위 문제 해결
Memoizaition 기법 - 이전 계산 값 저장하여 다시 계산하지 않아 빠르게됨

분할 정복(Divide and Conquer)
문제를 나누어 합병하여 문제의 답을 얻는 방식
하양식 접근법으로, 아래로 내려가면서 하위 해답 구현 - 재귀함수 사용
문제를 잘게 쪼갤때 부분 문제는 서로 중복되지 않음 ex) 병합정렬 퀵정렬

공통점 - 작은 문제로 쪼갬
동적 계획법 - 메모이제이션, 반복
분할 정복 - 중복x, 메모이제이션x
'''


# 동적 계획법 알고리즘 이해

# 피보나치 수열

# recursive call
def Fibonacci(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

# dynamic programming
def Fibonacci(n) :
    cashe = [0 for i in range(n+1)]
    cashe[0] = 0
    cashe[1] = 1
    for i in range(2, n+1) :
        cashe[i] = cashe[i-1] + cashe[i-2]
    return cashe[n]

Fibonacci(10)

