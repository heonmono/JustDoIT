# 1912 : (재귀함수) 팩토리얼 계산

n = int(input())

def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)

result = factorial(n)
print(result)


# 1915 : (재귀함수) 피보나치 수열
n = int(input())
# 1 1 2 3 5
def fibonacci(n) :
    if n == 1 or n == 2 :
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
result = fibonacci(n)
print(result)


# 2650 : 디지털 도어 락
''' 3개의 자연수의 최대공약수를 추출하는 것을 목표로한다.'''
a,b,c = map(int,input().split(" "))
def gcd(x,y) :
    while y :
        x, y = y, x%y
    return x

result = gcd(a,b)
result2 = gcd(c, result)
print(result2)

# 2628 : 케익 자르기
'''a,b가 c,d보다 다 크거나 작은 경우에는 교차점이 생기지 않는다.
ex) 1, 5 / 10, 90
 1, 100 / 10 60 잘못된 가정이다.
 1~50/ 51~100을 기준으로 생각해보아야한다. 원은 동그랗다.
 
 '''

a,b = map(int, input().split(" "))
c,d = map(int, input().split(" "))
# 1~ 50은 정상/ 51~ 100은 역순으로 1

def order(a,b) :
    if a > b :
        a,b = b,a
    return a,b
a,b = order(a,b)
c,d = order(c,d)
def check_cross(a,b,c,d) :
    if a < c < b :
        if d < a or d > b :
            return "cross"
        else :
            return "not cross"
    else :
        if a < d < b :
            return "cross"
        else :
            return "not cross"
result = check_cross(a,b,c,d)
print(result)

# 2631 : 보물 찾기 # 실행 안됨..
'''n개 중 몇개..? '''
n, k = map(int, input().split(" "))
data = list(map(int, input().split(" ")))

def integrated_sum(data, i , j) : #i는 시작값 j는 끝나는값
    sum = 0
    for i in range(i,j+1) :
        sum = sum + data[i] # i부터 j-1까지의 sum
    return sum
def find_some(data, k) :
    a= 0 # 찾을때마다 하나씩 증가
    for i in range(len(data)) :
        j = i
        while j < len(data) :
            if integrated_sum(data, i, j) < k :
                j += 1
            elif integrated_sum(data,i,j) == k :
                a = a+1
                break
            else :
                break
    return a
result =find_some(data, 15)
print(result)