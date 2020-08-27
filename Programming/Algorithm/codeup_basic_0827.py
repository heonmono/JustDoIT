# 1089 : [기초-종합] 수 나열하기1

''' 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
n번째 수를 출력하는 프로그램을 만들어보자.
'''

x, y, z = map(int, input().split(" "))

def add_equal(x,y,z) : # x =2 , y = 3
    for i in range(z) :
        if i == 0 :
            continue
        if i != 0 :
            x = x+y
    print(x)
add_equal(x,y,z)
add_equal(1,3,5)


# 1090 : [기초-종합] 수 나열하기2
'''
예를 들어
2 6 18 54 162 486 ... 은
2부터 시작해 이전에 만든 수에 3을 곱해 다음 수를 만든 수열이다.'''

x, y, z = map(int, input().split(" "))

def multiple_equal(x,y,z) : # x =2 , y = 3
    for i in range(z) :
        if i == 0 :
            continue
        if i != 0 :
            x = x*y
    print(x)

multiple_equal(x,y,z)


# 1092 : [기초-종합] 함께 문제 푸는 날(설명)

x, y, z = map(int, input().split(" "))
a = 1
while True :
    if a % x == 0 and a % y == 0 and a % z == 0 :
        print(a)
        break
    else :
        a+= 1


# 1093 : [기초-1차원배열] 이상한 출석 번호 부르기1(설명)

init = int(input())
input_data = map(int, input().split(" "))
input_data2 = list(input_data)
'''for i in range(23):
    a.append(0)'''
a = [0 for i in range(23)]

for i in range(len(input_data2)) :
    a[input_data2[i]-1] = a[input_data2[i]-1] + 1

for i in range(len(a)):
    print(a[i], end= " ")
'''
num = int(input())
ranMap = map(int, input().split())

ranList = list(ranMap)
numArr = [0 for i in range(23)]

for i in range(num):
    numArr[ranList[i]-1] += 1

for i in range(len(numArr)):
    print(numArr[i], end=" ")'''

# 1094 : [기초-1차원배열] 이상한 출석 번호 부르기2(설명)

num = int(input())
ranMap = map(int, input().split())
ranList = list(ranMap)

for i in range(len(ranList)-1, -1, -1) :
    print(ranList[i], end= ' ')


# 1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기(설명)
num = int(input())
dot = [[0 for i in range(19)] for j in range(19)]
for i in range(num) :
    a,b = map(int, input().split(" "))
    dot[a-1][b-1] = 1
for i in range(19) :
    for j in range(19) :
        print(dot[i][j], end = " ")
    print(end="\n")







# 1099 : [기초-2차원배열] 성실한 개미
path = [[0 for i in range(10)] for j in range(10)]
for i in range(10) :
#    path.append(map(int, input().split()))
    a = map(int, input().split(" "))
    b = list(a)
    for j in range(10) :
        path[i][j] = b[j]
# 2,2에서 시작
# 오른쪽 0이면 오른쪽 이동하고 9로 변경 , 2면 멈춤
# 오른쪽이 1이면 아래쪽이 0인지 확인하고 아래로 이동
# 마지막으로 9,9에 도착하면 멈춤

x = 1
y = 1
while True:
    if path[x][y] == 0 :
        path[x][y] = 9
    elif path[x][y] == 2 :
        path[x][y] = 9
        break
    else :
        break
    if path[x][y+1] == 0 : # 오른쪽이 0이면
        y += 1 # 오른쪽 한칸이동
    elif path[x][y + 1] == 2:  # 오른쪽이 2 이면
        path[x][y + 1] = 9 # 오른쪽 9 표시
        break
    elif path[x][y+1] == 1: # 오른쪽이 1 이면
        if path[x+1][y] == 0 : # 아래쪽이 0인지 확인
            x += 1 # 아래쪽 이동
        elif path[x+1][y] == 2:  # 아래쪽이 2면
            path[x+1][y] = 9  # 아래쪽 9 표시
            break
        else:
            break

for i in path:
    for j in i:
        print(j, end=" ")
    print()

for i in range(10) :
    for j in range(10) :
        print(path[i][j], end = " ")
    print()