# 재귀 호출
''' 고급 정렬에서 사용하므로, 미리 익히기
1. 재귀 용법 - 함소 안에서 동일 함수 호출, 익해져야함
2. 재귀 용법 이해'''

# 예제 1. factorial

a = 5
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)

def factorial(num) :
    if num > 1 :
        return num * factorial(num-1)
    else :
        return num

factorial(0)

# 시간 복잡도와 공간복잡도는 O(n)
# 파이썬은 깊이가 1000회 이하

def multiple(n) :
    start = 1
    for i in range(1,n+1) :
        start = start * i
    return start

multiple(5)

def multiple(n) :
    if n <= 1 :
        return n
    return n * multiple(n-1)
multiple(5)

# 누적함

def sum_list(data) :
    if len(data) == 1 :
        return data[0]
    return data[0] + sum_list(data[1:])

data = [1,2,3,4,5]

sum_list(data)

# 회문 판단
data = [1]
data[-1]
def check(data) :
    if data[0] == data[-1] :
        if len(data) == 1:
            return True
        return check(data[1:-1])
    else :
        return False
data = 'abc'
check(data)
data = 'lev;el'


# n이 홀짝이면 1이될때까지
# 홀수면 *3 +1 짝수면 /2

def make(n) :
    if n > 1 :
        if n % 2 == 1:
            n = 3*n +1
            print(int(n))
            return make(n)
        else :
            n = n/2
            print(int(n))
            return make(n)

make(3)


# 정수 4를 1,2,3의 조합으로 나타내는 방법
# f(n) = f(n-1) + f(n-2) + f(n-3)
def make(n) :
    if n ==1 :
        return 1
    if n == 2 :
        return 2
    if n == 3:
        return 4
    if n >= 3:
        return make(n-1) + make(n-2) +make(n-3)

make(5)


