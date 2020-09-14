#4011 : 생년월일 출력

birth = input()

if birth[-7] == '1' or birth[-7] == '2' :
    a = '19' + birth[:2]
else :
    a = '20' + birth[:2]

if birth[-7] == '1' or birth[-7] == '3' :
    c = 'M'
else :
    c = "F"

print(a +"/" + birth[2:4] + "/" + birth[4:6] + " " + c)

# 4013 : 진법 변환

n = int(input())
print("2 " + bin(n)[2:])
print("8 " + oct(n)[2:])
print("16 " + hex(n)[2:].upper())



# 패스트캠퍼스 링크드리스트

'''장점  미리 데이터 공간을 하지 않아도 됨(배열의 단점)
단점 : 데이터 저장공간이 따로 있으니까 저장 효율이 안좋고 접근 속도가 느림 중간에 유실될경우 어려움'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next : # node.next가 있으면
        node = node.next# 마지막 노드로 가는것
    node.next = Node(data)

node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

node = head
while node.next :
    print(node.data)
    node = node.next
print(node.data)

search = True
while search :
    if node.data == 1:
        search = False
    else : node = node.next

node3 = Node(1.5)
node_next = node.next
node.next = node3
node3.next = node_next

class Node :
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class NodeMgmt :
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == "" :
            self.head = Node(data)
        else :
            node = self.head
            while node.next :
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next


linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1,10) :
    linkedlist1.add(data)

linkedlist1.desc()
