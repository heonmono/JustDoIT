
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

    def delete(self, data):
        if self.head == "" :
            print("해당 값을 가진 노드가 없습니다.")
            return
        if self.head.data == data : # 헤드를 삭제
            temp = self.head
            self.head = self.head.next
            del temp
        else :
            node = self.head
            while node.next :
                if node.next.data == data :
                    temp = node.next
                    node.next = node.next.next # 맨 마지막이든 중간이든 가능
                    del temp
                else :
                    node = node.next
    def find(self, data):
        if self.head == "" :
            print("해당 값을 가진 노드가 없습니다.")
            return
        node = self.head
        while node.next :
            if node.data == data :
                return node.data
            else :
                node = node.next



# head삭제해보기
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
linkedlist1.head
linkedlist1.delete(0)
linkedlist1.head


# 여러개중 삭제
linkedlist1 = NodeMgmt(0)
for data in range(1,10) :
    linkedlist1.add(data)
linkedlist1.find(1)
linkedlist1.desc()

linkedlist1.delete(9)

''' double linked list - 앞에 노드주소도 기억 '''

class Node :
    def __init__(self, data, prev=None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head # 맨 끝의 위치도 기억하자.

    def insert(self, data):
        if self.head == None :
            self.head = Node(data)
            self.tail = self.head
        else :
            node = self.head
            while node.next :
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new # 마지막 위치를 update

    def desc(self):
        node =self.head
        while node :
            print(node.data)
            node = node.next

double_linked = NodeMgmt(0)
for data in range(1,10) :
    double_linked.insert(data)

double_linked.desc()

# 위의 코드에서 노드데이터가 특정 숫자인 노드앞에 데이터를 추가하는 함수를 만들고 테스트

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head # 맨 끝의 위치도 기억하자.

    def insert(self, data):
        if self.head == None :
            self.head = Node(data)
            self.tail = self.head
        else :
            node = self.head
            while node.next :
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new # 마지막 위치를 update


    def search_from_head(self,data):
        node = self.head
        while node :
            if node.data == data :
                return node
            else :
                node = node.next
        return False

    def search_from_tail(self,data):
        node = self.tail
        while node :
            if node.data == data :
                return node
            else :
                node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head == None :
            self.head = Node(data)
            return True
        else :
            node = self.tail
            while node.data != before_data :
                node = node.prev
                if node == None :
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

    def desc(self):
        node =self.head
        while node :
            print(node.data)
            node = node.next

 ''' def insert_prev(self, location, data): # 특정데이터를 찾아서 그 앞에 추가
        if self.head == None :
            print("해당하는 데이터가 없습니다.")
        node = self.head
        while node :
            if node.data == location :
                prev = node.prev
                next = node
                new = Node(data, prev = prev, next= next)
                # 문제점 - 기존 노드들의 prev랑 next를 new로 설정하지 않은 문제점
            else :
                node = node.next'''

double_linked = NodeMgmt(0)
for data in range(1,10) :
    double_linked.insert(data)
double_linked.insert_before(1.5,2)
double_linked.insert_prev(3,10)
double_linked.desc()
node3 = double_linked.search_from_head(3)
node3 = double_linked.search_from_tail(3)
node3.data