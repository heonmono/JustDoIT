# 그리디 어려워.. 하기싫어.. 다 틀려

# 3321 : 최고의 피자 # 실패.. 음... 토핑 가장 큰수부터 해야하는게 맞을듯
''' 1달러당 열랑이 최대
같은 토핑은 1개만
no topping 가능
도우가격 a 토핑가격 b
피자 가격 a + b* k'''


n_topping = int(input())
dow_price, topping_price = map(int, input().split(" "))
dow_calories = int(input())
topping_calories = list()

for i in range(n_topping) :
    tmp = int(input())
    topping_calories.append(tmp)

# 달러당 최고 칼로리
# 기본적으로 도우는 들어가기 때문에, 토핑을 추가했을때 오르는 방식으로 해야겠지?

# 분모 상승률이 분자 상승률보다 클때 cut하는 것으로
# 처음 분자 200에서 하나씩 상승
# 분모는 12에서 2씩 증가
# price ratio = 가격변화율 = 변화된 가격/ 기존가격
# cal ratio = 칼로리 변화율
# parent ratio < child ratio일때 변화
base_price = dow_price # 변화하면 2씩
base_cal = dow_calories # 변화하면 토핑칼로리[0]

for i in range(n_topping) :
    price_ratio = (base_price + 2) / base_price
    cal_ratio = (base_cal + topping_calories[i]) / base_cal
    if price_ratio < cal_ratio :
        base_price += 2
        base_cal += topping_calories[i]
print(int(base_cal/base_price))
# 4040 : 펜션

n,m = map(int, input().split(" "))
ox_list = []
ox_list = [[0 for i in range(m)] for j in range(n)]

for i in range(n) :
    tmp = input()
    for j in range(m) :
        ox_list[i][j] = tmp[j]

# 연속된 날끼리 그냥 숫자로 되어있으면 편하지 않을까?

s,y = map(int,input().split(" "))
# 2일부터 봐야하고 y가 n보다 크면 안돼
# s일부터 y일까지 방이 있나?



# 2651 : 극장 좌석 배치 1 # 조건부확률인듯 # 실패
n, k = map(int, input().split(" "))

# nCk n(n-1)...(n-k)
# n! / n-k!* r!

def factorial(n) :
    if n == 0 :
        return 1
    return n * factorial(n-1)

print(int(factorial(n)/(factorial(n-k)*factorial(k))))

# 2653 : 규칙에 맞는 이진수 만들기 (Small) #실패
a = int(input()) # n-1의 누적합을빼줘

def integrated_sum(n) :
    if n == 1 :
        return 1
    if n == 0 :
        return 0
    return n + integrated_sum(n-1)
two_digit = 2**a
print(two_digit - integrated_sum(a-1))
2**4 - 3 -2 -1