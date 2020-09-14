#3016 : 1등한 학생의 성적

# input part
n = int(input())
lst1 = [[0 for i in range(4)] for j in range(n)]
lst1[0]
dic = dict()
dic
for i in range(n) :
    a,b,c,d = input().split(" ")
    b,c,d = int(b), int(c),int(d)
    dic['name'] = a
    dic['sub1'] = b
    dic['sub2'] = c
    dic['sub3'] = d
dic
data
data = list(data)
data

# 1920 : (재귀함수) 2진수 변환 # 0일때가 안돼..

# 8 4 2 10 :101 // 1 2 4 8 16 32
# 10 #
n = int(input())
def digit_2(n) :
    if n == 0 :
        return
    else :
        digit_2(n//2)
        print(n%2, end = "")

digit_2(10)
digit_2(0)
digit_2(n)
digit_2(11)

# 1953 : (재귀함수) 삼각형 출력하기 1

n = int(input())
a = 1
def triangle(n) :
    global a
    if n == 0 :
        return
    print("*" * a)
    a +=1
    return triangle(n-1)

triangle(n)

# 2625 : 삼각화단 만들기 (Small)
# c < a+b
# 11 :
# 6 3 2
# 9 : 4 , 41, 32
#     5 , 31, 22
# a+b > c
# b-a < c < a+b
# 빗변의 합이 나머지 변의 합보다 작아야함

# 그럼 가장큰 빗변에서 나머지 변의 합이 더 큰데 나머지 변보다는 크게 가야하나?
# b+c보다 작다는건 a가 50% 이상이 되어선 안된다. 다른 변보다는 길어야 한다.
# a< 50% 이하이면서 b나 c는 a보다 작아야한다.
# a는 50% 이하이면서 그 나머지의 50% 이하도 되어선 안된다.

# ex 세변의 총합 13
# 6 6,1 5,2 4,3
# 5 5,3 4,4
# 4 4,3
length = int(input())
length = 13
lim = length//2
lim
lim2 = lim//2+1
lim2

for a in range(lim2, lim+1) :
    length-a

