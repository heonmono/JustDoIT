# 해쉬 테이블(Hash Table)
'''
해쉬 구조 - 키에 데이터를 저장하는 데이터 구조 키를 통해 해쉬 함수?(python은 딕셔너리)
            배열처럼 전체 데이터를 볼 필요가 없음
해쉬 : 임의 값을 고정 길이로 변환하는 것
해쉬 테이블 : 키 값의 연산에 직접 접근이 가능한 데이터 구조
해싱 함수 : key에 대한 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
해쉬 값 : key를 해싱함수로 연산해서, 해쉬값을 알아내고, 이를 기반으로 해당 key에 대한 데이터 위치
슬롯 : 한개의 데이터를 저장할 수 있는 공간
저장할 데이터에 대해 key를 추출할 수 있는 별도 함수도 존재할 수 있음
'''


# 간단한 해쉬 예
hash_table = list([0 for i in range(10)]) #list comprehenshion
hash_table

# 해쉬 함수 division법
def hash_func(key) :
    return key%5

# 해쉬 테이블에 저장
data1 = 'andy'
data2 = 'dave'
data3 = 'trump'
print(ord(data1[0]),ord(data1[1]), ord(data1[2]))# ord(): 문자의 ASCII코드 리턴
print(hash_func(ord(data1[0])),hash_func(ord(data1[1])), hash_func(ord(data1[2])))# ord(): 문자의 ASCII코드 리턴

# 해쉬테이블에 갑 저장 예
def storage_data(data, value) :
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('andy', '010555232')
storage_data('dave', '0105432332')
storage_data('trump', '010553212')

def get_data(data) :
    key =ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

get_data('andy')


'''
장점 - 저장읽기 빠름, 중벅 확인 편리
단점 - 저장공이 좀 크다, 저장 주소가 동일시 충돌로 새로운 저장공간 필요
사용용도 - 검색, 저장, 삭제, 읽기가 빈번한 경우/ 캐쉬 구현시
'''

# 리스트 변수를 이용하여 해쉬테이블 구현해 보기,
hash_table = list([0 for i in range(8)])

def get_key(data) :
    return hash(data)
def hash_func(key) :
    return key % 8

def save_data(data, value) :
    hash_address = hash_func(get_key(data))
    hash_table[hash_address] = value

def read_data(data) :
    hash_address = hash_func(get_key(data))
    return hash_table[hash_address]
save_data('DAVE','02030232')
save_data('DAVE22','0203023222')
hash_table


# 충돌(collision) 해결 알고리즘

# 6.1 chaining 기법 - 충돌이 일어나면, 링크드 리스트 자료구조로 뒤에 연결

hash_table = list([0 for i in range(8)])

def get_key(data) :
    return hash(data)
def hash_func(key) :
    return key % 8

def save_data(data, value) :
    index_key = get_key(data) # 인덱스키를 추가하여 링크의 주소로

    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0 : # 초기값 0으로 했기 때문에
        for index in range(len(hash_table[hash_address])) : # 링크드 리스트대신 리스트로 했음
            if hash_table[hash_address][index][0] == index_key :
                hash_table[hash_address][1] = value
                return
            hash_table[hash_address].append([index_key, value])
    else :
        hash_table[hash_address] = list([index_key,value])


def read_data(data) :
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0 :
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key :
                return hash_table[hash_address][index][1]
        return None
    else :
        return None



save_data('DAVE','02030232')
save_data('DAVE22','0203023222')
save_data('Dd','0203023222')
save_data('Data','0203023222')
hash_table

# 6.2 linear probing - 빈공간에 넣기 - 폐쇄 해슁, 저장공간 활용도 좋음


hash_table = list([0 for i in range(8)])

def get_key(data) :
    return hash(data)
def hash_func(key) :
    return key % 8

def save_data(data, value) :
    index_key = get_key(data) # 인덱스키를 추가하여 링크의 주소로
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0 : # 초기값 0으로 했기 때문에
        for index in range(hash_address, len(hash_table)) :
            if hash_table[index] == 0 :
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key : # 키가 동일시 업데이트
                hash_table[index][1] == value
                return
    else :
        hash_table[hash_address] = [index_key,value]


def read_data(data) :
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0 :
        for index in range(hash_address, len(hash_table)) :
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else :
        return None

print(hash('dk')%8)
print(hash('dz')%8)

save_data('dk','0203023222')
save_data('dz','0203023222')
hash_table
read_data('dk')


#6.3 빈번한 충돌을 개선하는 기법
#6.3.1 저장공간을 확대(2배정도)



#시간복잡도 - O(0), 최악의 경우 O(n)







