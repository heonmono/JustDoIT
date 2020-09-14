# 1402 : 거꾸로 출력하기 3

n = int(input())
lst = list(map(int, input().split(" ")))

for i in range(n) :
    print(lst.pop(), end= " ")


# 1714 : 숫자 거꾸로 출력하기

num = input()
len(num)
for i in range(len(num)-1,-1,-1):
    print(num[i], end="")

# 2016 : 천단위 구분기호

digit = int(input()) # 억지로 맞히는 답.. ㅎ
# n자리면 3의 나머지 부분 앞에 표시하고 그다음 세자리씩 출력
num = input()
lst = []
for i in range(digit) :
    lst.append(num[i])
lst2 = []
if digit >3 and digit%3 != 0 :
    for i in range(0,digit%3) :
        lst2.append(lst.pop(0))
    for i in range(digit%3, digit,3) :
        lst2.append(",")
        lst2.append(num[i:i+3])
elif digit > 3 and digit %3 == 0 :
    for i in range(0,digit-3,3) :
        lst2.append(num[i:i+3]) # 0:3
        lst2.append(",")
    lst2.append(num[digit-3:digit])
else :
    for i in range(0,digit) :
        lst2.append(lst.pop(0))
for i in lst2:
    print(i, end="")

# n자리일 경우 3의 나머지 앞부분 ,는 목의 수와 동일
if len(lst) >0 :
    i = 0
    while i < 3 :
        print(lst.pop(), end=" ")
        i +=1
    print()

print(num[0:digit%3], end=",") # 한자리면? 망한 코드
for i in range(digit%3,digit-3,3) :
    print(num[i:i+3], end=",")
print(num[digit-3:digit])


# 3021 : 큰 수 덧셈
a1 = input()
a2 = input()
lst1 = []
lst2 = []
for i in a1 :
    lst1.append(i)
for i in a2 :
    lst2.append(i)
if len(a1) < len(a2) :
    c = len(a1)
else:
    c = len(a2)
# pop해서 더해 더한게 10이 넘으면 그 다음 자릿수로
lst3 = []
b=0
for i in range(c) :
    a = int(lst1.pop()) + int(lst2.pop())+ b
    if a >= 10 :
        lst3.insert(0,a%10)
        b=1
    else :
        lst3.insert(0,a)
        b=0

if len(lst1) == 0 :
    d = lst2
else :
    d = lst1

for i in range(len(d)-1,-1,-1) :
    lst3.insert(0,d[i])

for i in range(len(lst3)) :
    print(lst3[i], end="")