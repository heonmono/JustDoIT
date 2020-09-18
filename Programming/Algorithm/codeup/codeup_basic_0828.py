''' 1,2,3번 문제 다 정상 작동하는데 2,3번이 왜 에러로 뜨는지 잘 모르겠다.
마지막은 거의 다 완성했고 입력순서를 기준으로 하는것이 잘 안된다. 사실 item만 내림차순으로 했는데
왜 입력순서가 변하는지 잘 모르겠어서 내일 다시 생각해볼 것이다.'''

# 1805 : 입체기동장치 생산공장
n = int(input())
dic = dict()
for i in range(n) :
    a, b = map(int, input().split(" "))
    dic[a] = b
key = sorted(dic.keys())
for i in range(n) :
    print("%d %d" %(key[i], dic[key[i]]))

# 3004 : 데이터 재정렬

n = int(input())
dic = dict()
list_a = list(map(int,input().split(" ")))
list_a2 = sorted(list_a)
for i in range(n) :
    for j in range(n) :
        if list_a[i] == list_a2[j] :
            dic[list_a[i]] = j

for value in dic.values() :
    print(value, end = " ")

# 3005 : 최소공배수
def gcd(x,y) : # 왜 안되지...
    if x % y != 0 :
        gcd(y, (x%y))
    else :
        return x
'''최대 공약수로 나누고 서로소를 곱한다. 
3개가 넘을 경우, 여러개의 공약수로라도 '''
''' 2~ 7까지로 계속 나눠서 목과 나머지를 합쳐줘
나머지의 합이 최소가 되는거로 하면 되나...?'''
''' 아니면 소인수 분해로 할까...? 다 같이 하기엔 안좋을거 같기도 한데'''

n = int(input()) # 아......... 결과는 나오는데 왜 코드업에선 틀렸다고 하지?
a = list(map(int,input().split(" ")))

def gcd(x,y) :
    while y :
        x, y = y , x % y
    return x

def lcm(x,y) :
    return x * y // gcd(x,y)

def solution(arr) :
    while True :
        arr.append(lcm(arr.pop(),arr.pop()))
        if len(arr) == 1:
            return arr[0]

print(solution(a))

# 3015 : 성적표 출력
n, m = map(int,input().split(" "))
dic = {}
for i in range(n) :
    a, b = input().split(" ")
    dic[a] = int(b)

sorted_dic = sorted(dic.items(), key= lambda items : -items[1])
sorted_dic
val = list()
for key, value in sorted_dic :
    val.append(key)


for i in range(m) :
    print(val[i])
