# 1901 : (재귀 함수) 1부터 n까지 출력하기 for while x

a = int(input())
x = 1
def recursion_add() :
    global x
    print(x)
    x+= 1
    if x <= a :
        recursion_add()

recursion_add()
# 전역변수를 함수내에서 수정하는 것은 사실 그렇게 긍정적인 방식은 아닌 것 같다.
# 그런데 x를 안에 놓으면 x가 1로 픽싱된다. 아마 함수안에 다시 함수를 만들어서 나눈다면
#괜찮지 않았을까 싶다.

# 1902 : (재귀 함수) 1부터 n까지 역순으로 출력하기

a = int(input())
def recursion_minus(x) :
    print(x)
    x -= 1
    if x > 0 :
        recursion_minus(x)

recursion_minus(a)


# 1904 : (재귀함수) 두 수 사이의 홀수 출력하기

a, b = map(int, input().split(" "))

def recursion_odd(x, y) :
    if x <= y:
        if x % 2 == 1 :
            print(x)
            x+=1
        else :
            x+=1
        recursion_odd(x,y)

recursion_odd(a, b)

# 1905 : (재귀함수) 1부터 n까지 합 구하기
# 기존 값은 12345처럼 큰 수를 감당하지 못해서 가우스 공식을 이용해야한다.
# n(n-1)*2 1 100 2 99 3 98
# gaus가 홀수일땐 gaus -1은 짝수라서 상관 없음 101을 100/2인 50번 더하면 상관없음
# gaus가 짝수일때 gaus -1은 홀수이기 때문에 목 + gaus/2 더하기
# 근데 1일때 동작을 안한다. 사실 for문이나 그냥 gauss도 있는데
# 왜이렇게 복잡하게 해야할까.. 내가 코딩을 못해서 그렇겠지 뭐 ㅎㅎ
n = int(input())
a = 1
gaus = n + 1
sum = 0
def integrated_sum(gaus,a) :
    global sum
    if gaus % 2 == 1 :
        if a <= gaus/2 :
            sum += gaus
            a +=1
            integrated_sum(gaus,a)
        return sum
    else :
        if a <= gaus/2 :
            sum += gaus
            a +=1
            integrated_sum(gaus,a)
        return sum + gaus/2

result = integrated_sum(gaus,a)
print(result)

n = int(input())
def inte_sum(x) :
    if x > 1 :
        return x*(x+1)/2
    else :
        return 1
result = inte_sum(n)
print(int(result))


'''
순차 검색 알고리즘(sequential search)
순차검색은 주어진 데이터를 처음부터 검색 
'''

def sequential_search(x,a) :
    for i in range(len(x)) :
        if x[i] == a :
            return i
    return False

x = [1, 2, 3, 4 ,5]
sequential_search(x,6)

