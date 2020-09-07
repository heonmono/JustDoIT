# 2001 : 최소 대금 해결
a = list()
for i in range(5) :
    b = int(input())
    a.append(b)

# 파스타 최소값과 음료최소값 찾기
min_pasta = a[0]
for i in range(3) :
    if min_pasta > a[i] :
        min_pasta = a[i]

min_juice = a[3]
for i in range(3,5) :
    if min_juice > a[i] :
        min_juice = a[i]

min_price = (min_juice+min_pasta)*1.1
print("%.1f" % min_price)

# 3120 : 리모컨 ''' 재귀함수 안에서 어떻게 counting을하는지 왜 모르겠지..
a,b = map(int, input().split(" "))
# 10 초 이상이면 무조건 10씩
# 8~9도면 10이동 -1 -2
# 5~7도면 5이동 0 +1 +2
# 3~4도면 5이동 -2 -1
# 1,2 도면 +1 +2
def change(a,b) :
    if a > b :
        a,b= b,a
a = 5
b = 37
def main() :
    c= 1
    temper_conditioner(a,b,c)

def temper_conditioner(a,b,c) :
    while b-a > 0 :
        if b- a >= 10 : # 10보다 큰 경우
            temper_conditioner(a,b-10,c+1)
        elif 10 > b -a > 7  : # 10보다 작지만 10 이동
            temper_conditioner(b - 10, a,c+1)
        elif 8> b-a >= 5 : # 5보다 큰 경우
            temper_conditioner(a, b-5,c+1)
        elif 5> b-a > 2 : # 5보다 작지만 5이동 #################
            temper_conditioner(b-5, a,c+1) #################3 여기서 에러
        else : # 1씩이동
            temper_conditioner(a, b-1,c+1)
    return c
main()
print(temper_conditioner(5,37,0))
# 37 -10 =27 5 c = 2
# 27 -10 =17 5 c = 3
# 17 -10 =7 5 c = 4
# 7 -5 = 2 5 c =5
#

# 37 27 17 7 2


# 3301 : 거스름돈

money = int(input())
# 50000 => 10 * 5000
# 자릿수로 변환해볼까? 만의자리 천의자리 백의자리 10의자리 이러면 쉬울듯?
#digit = list(map(int,str(money)))
a = money//50000
b = money%50000
digit = [int(i) for i in str(b)]
c= 0
for i in digit :
    if i >= 5 :
        c = c+1+ i-5
    else :
        c = c +i
print(a + c)
a
def count_remainder(n, c= 0) :
    while n > 0 :
        if n > 50000 :
            c = c + n//50000
            n = n%50000
        elif n > 10000 :
            c = c + n//10000
            n = n%10000
        elif n > 5000 :
            c = c + n//5000
            n = n%5000
        elif n > 1000 :
            c = c+ n//1000
            n = n%1000
        elif n > 500 :
            c = c+ n//500
            n = n%500
        elif n > 100 :
            c = c+n//100
            n = n%100
        elif n > 50 :
            c = c + n//50
            n = n%50
        elif n > 10 :
            c = c + n//10
            n = n%10
    return c
print(count_remainder(money))

100//5
100%5