# 데이터 구조7 : 트리
'''
노드와 브런치를 이용하여, 사이클을 이루지 않는 자료구조
이진트리와 이진 탐색 트리(binary search tree)
- 이진 트리 : 노드의 최대 branch가 2개
- 이진 탐색트리(BTS) : 추가적인 조건으로 왼쪽은 작은 오른쪽은 큰값

주요 용도 : 데이터 검색(탐색)
'''

# 5.1 노드 클래스 만들기
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt :
    def __init__(self, head): # root node
        self.head = head

    def insert(self,value):
        self.current_node = self.head
        while True :
            if value < self.current_node.value :
                if self.current_node.left != None :
                    self.current_node = self.current_node.left
                else :
                    self.current_node.left = Node(value)
                    break
            else :
                if self.current_node.right != None :
                    self.current_node = self.current_node.right
                else :
                    self.current_node.right = Node(value)
                    break

    def search(self,value):
        self.current_node = self.head
        while self.current_node : # 현 노드가 있는지
            if self.current_node.value == value :
                return True
            elif value < self.current_node.value :
                self.current_node = self.current_node.left
            else :
                self.current_node = self.current_node.right
        return False # true가 아니면 false겠지

    def delete(self, value):
        # 삭제할 노드 탐색
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

            # case1
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # case2
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

                # case 3
        elif self.current_node.left != None and self.current_node.right != None:
            # case3-1
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            # case 3-2
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

        return True
'''    
    def delete(self,value): # 삭제시 오른쪽 자식중 가장 작은 값, 삭제시 왼쪽 자식중 가작 큰값으로 대체
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node :
            if self.current_node.value == value :
                searched = True
                break
            elif value < self.current_node.value :
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else :
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False :
            return False # 이후부터 케이스별로

        if self.current_node.left == None and self.current_node.right == None : # leafnode
            if value < self.parent.value :
                self.parent.left = None
            if value > self.parent.value :
                self.parent.right = None
            del self.current_node

        if self.current_node.left != None and self.current_node.right == None : # child node가 하나일때
            if value < self.parent.value :
                self.parent.left = self.current_node.left
            else :
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None : # child node가 하나일때
            if value < self.parent.value :
                self.parent.left = self.current_node.right
            else :
                self.parent.right = self.current_node.right

        if self.current_node.left != None and self.current_node.right != None : # child가 2개일때
            if value < self.parent.value : #
                self.change_node = self.current_node.right # 오른쪽에서 가장 작은값
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None :
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None : # right가 있으면
                    self.change_node_parent.left = self.change_node.right
                else :
                    self.change_node_parent.left = None
                self.parent.left = self.change_node # 연결을 다시해주기
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else : # 오른쪽에 있을때
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None :
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None :
                    self.change_node_parent.left = self.change_node.right
                else :
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
'''

'''
1. 삭제할 node의 오른쪽 자식 선택
2. 오른쪽 자식의 가장 왼쪽에 있는 node를 선택
3. 해당 node를 삭제할 node의 parent node의 왼쪽 branch가 가리케가함
4. 해당 node의 왼쪽 branch가 삭제할 node의 왼쪽 childnode를 가리키게함
5. 해당 node의 오른쪽 branch가 삭제할 node의 오른쪽 childnode를 가리키게함
6. 만약 해당 노드가 오른쪽 childnode를 가지고 있었을 경우, 해당 node의 본래 parent node의 왼쪽 branch가 해당 오른쪽
child node를 가리키게함'''


#1~1000 숫자중 임의의 100개로 추출하여, 이진 탐색 트리에 입력, 검색,
import random
bst_nums = set() # 집합 중복없애려고
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0,999))
#print(bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의 로트 노드 500
head= Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums :
    binary_tree.insert(num)

# 입력한 100개 숫자 검색
for num in bst_nums :
    if binary_tree.search(num) == False :
        print('search falied', num)

# 입력 숫자중 10개를 random 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10 :
    delete_nums.add(bst_nums[random.randint(0,99)])

for num in delete_nums :
    if binary_tree.delete(num) == False :
        print("delete failed", num)

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
BST.search(6)

'''
트리의 시간 복잡도 O(logn) -> O(h) depth와 동일
최악의 경우 가장 작은값이 root이며 순차적으로 큰값이 들어올경우 링크드리스트와 동일해짐'''