# 기본 사칙 4 -1

input_Data = input().split(" ")
A = int(input_Data[0])
B = int(input_Data[1])
print(A+B)

# 주민번호 입력받기

UserCode = input().split("-")
a = UserCode[0]
b = UserCode[1]
print(a+b)

# [기초-산술연산] 정수 1개 입력받아 1 더해 출력하기(설명)
a = int(input())
print(a+1)

# [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
input_Data = input().split(" ")
A = int(input_Data[0])
B = int(input_Data[1])
C = int(input_Data[2])
print(A+B+C)
print("%.1f" % ((A+B+C)/3))

# 1049 : [기초-비교연산] 두 정수 입력받아 비교하기1(설명)
input_Data = input().split(" ")
a = int(input_Data[0])
b = int(input_Data[1])
if a > b :
    print(1)
else :
    print(0)

# 1054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)

input_Data = input().split(" ")
a = int(input_Data[0])
b = int(input_Data[1])
if a == 1 and b == 1 :
    print(1)
else :
    print(0)

# 1058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
input_Data = input().split(" ")
a = int(input_Data[0])
b = int(input_Data[1])
if a == 0 and b == 0 :
    print(1)
else :
    print(0)


# 1064 : [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기(설명)
input_Data = input().split(" ")
A = int(input_Data[0])
B = int(input_Data[1])
C = int(input_Data[2])

if A < B :
    if A < C :
        print(A)
    else:
        print(C)
else :
    if B < C :
        print(B)
    else :
        print(C)

# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)
input_Data = input().split(" ")
A = int(input_Data[0])
B = int(input_Data[1])
C = int(input_Data[2])

if A % 2 == 0 :
    print(A)
if B % 2 == 0 :
    print(B)
if C % 2 == 0 :
    print(C)

# 1071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1(설명)
a = input().split(" ")
for i in range(len(a)) :
    if int(a[i]) == 0 :
        break
    else :
        print(a[i])



# 1076 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)
ord('a')
chr(97)

a = input()
for i in range(97, ord(a)+1) :
    print(chr(i), end = " ")

# 1078 : [기초-종합] 짝수 합 구하기(설명)

a = int(input())
sum = 0

for i in range(0, a + 1) :
    if i % 2 == 0 :
        sum+= i
    else :
        continue
print(sum)

# 1079 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
a = input().split(" ")

for i in range(len(a)) :
    print(a[i])
    if a[i] == 'q' :
        break


# 1080 : [기초-종합] 언제까지 더해야 할까?
a = int(input())
i = 0
sum = 0
while True :
    i = i+1
    sum+= i
    if sum >= a :
        print(i)
        break

# 1083 : [기초-종합] 3 6 9 게임의 왕이 되자!(설명)
a = int(input())

for i in range(1, a+1) :
    if i % 3 == 0 :
        print("X", end = " ")
    else :
        print(i, end = " ")

# 1084 : [기초-종합] 빛 섞어 색 만들기(설명)

input_data = input().split(" ")
r = int(input_data[0])
g = int(input_data[1])
b = int(input_data[2])

for i in range(r) :
    for j in range(g) :
        for z in range(b) :
            print("%d %d %d" %(i, j, z))
print(r*g*b)
