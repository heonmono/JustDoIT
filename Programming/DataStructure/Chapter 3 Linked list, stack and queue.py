# Chapter 3 Linked list, stack and queue
# Chapter 3-1 Abstract Data Types

'''
Weekly Objectives
This week, we learn the first set of data structures: linked list, stack, and queue.
Objectives are
Understanding the definition of abstract data types
Firmly understanding how references work
Understanding various linked list, stack, and queue structures
    Singly linked list, doubly linked list, circular linked list… / singly를 공부하면 stack and queue
    Able to implement a stack and a queue with a list
Understanding the procedures of linked list, stack, and queue management
    Insert, delete, search…
    Should be able to estimate the number of steps for inserts, deletes, and searches

'''

# Array for List - 구조화된 형태로 저장할 필요

'''
Abstract Data Types

An abstract data type (ADT) is an abstraction of a data structure # 데이터 구조 추상화
An ADT specifies:
    Data stored
    Operations on the data
    Error conditions associated with operations / 에러 조건을 미리 처리
Example: ADT modeling a simple stock trading system
    The data stored are buy/sell orders
    The operations supported are
        order buy(stock, shares, price)
        order sell(stock, shares, price)
        void cancel(order)
    Error conditions:
        Buy/sell a nonexistent stock
        Cancel a nonexistent order
'''

# Chapter 3-1 Array
'''
Creating a List by Array

Array - 동일한 data를 index를 활용하여 저장/access 할 수 있는 것
Array (in our Python example, List, yet we will use only its index function)
    Each element is accessible by index
    Index is typically zero or a positive integer
    Very simple creation  - That’s why people use it

Search procedure in array
    Let’s find ‘d’ and ‘c’ from the list in an array
       Of course, you can use ‘in’, but we commit ourselves to use indexes only
    Then, navigating from the first to the last until hit is the only way

Insert procedure in array
    Let’s insert ‘c’ between ‘b’ and ‘d’ in the list ( a = insert position index )
    First, make new list, or y, with six cells
    Second, copy the reference links of x[0:a-1] to y[0:a-1] (retrieval cnt.: a)
    Third, put a reference link to ‘c’ in y[a] (retrieval cnt.: 1)
    Fourth, copy the reference links of x[a:] to y[a+1:] (retrieval cnt.: n-a-1)
    Fifth, change x’s reference to y’s reference 
    Total count of retrievals = a + 1 + n – a – 1 = n
'''

x = ['a', 'b', 'd', 'e', 'f']

idxInsert = 2
valInsert = 'c'

y = list(range(6))  # 저장 공간 6
for itr in range(0, idxInsert):
    y[itr] = x[itr]
y[idxInsert] = valInsert
for itr in range(idxInsert, len(x)):
    y[itr + 1] = x[itr]
y
'''
Delete procedure in array

Let’s remove ‘d’ in the list ( a = delete position index )
First, make new list, or y, with five cells
Second, copy the reference links of x[0:a-1] to y[0:a-1] (retrieval cnt.: a)
Third, copy the reference links of x[a+1:] to y[a:] (retrieval cnt.: n-a-1)
Fifth, change x’s reference to y’s reference 
Total count of retrievals = a + n – a – 1 = n - 1
'''
x = y

y = list(range(5))
idxDelege = x.index('d')

for i in range(idxDelege):
    y[i] = x[i]

for i in range(idxDelege + 1, len(x)):
    y[i - 1] = x[i]

x = y

'''
Problems in Array

Whenever you put something in or get something out You have to perform line-wise retrievals
    Which is N retrievals (by assuming 100,000 – 1 ≒100,000)
This process is just like that
    There is a line of airline passengers / 모든 array가 다 이동해야해
    You want to put a passenger in the middle of the line because his flight is about to leave
    You are moving all the passengers one step back
    Then, you put the customer in the line
What-if we have a magic to create a space in the middle of the line?
    Array  you are bounded to the 1-dimension that you have
    Linked list  you are bounded no more!
'''

# Chapter 3-1 Linked List 1 / index값이 아닌 id기준  == : value, is : id

'''
Basic Structure: Singly linked list
    Construct a singly linked list with nodes and references
    A node consists of  # class 
        A variable to hold a reference to its next node # reference 구조
        A variable to hold a reference to its value object # reference 값
    Special nodes: Head and Tail  # 첫 노드, 마지막 노드
        You can construct the singly linked list without them
        But, using them makes search, insert and delete more convenient
    Generally, requires more coding than array 

Implementation of Node class
    Member variables
        Variable to reference the next node
        Variable to hold a value object
        (Optional) Variable to check whether it is a head or not
        (Optional) Variable to check whether it is a tail or not
    Member functions
        Various set/get methods
'''


class Node:
    nodeNext = None
    nodePrev = ''
    objValue = ''
    binHead = False
    binTail = False

    def __init__(self, objValue='', nodeNext=None, binHead=False, binTail=False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.binHead = binHead
        self.binTail = binTail

    def getValue(self):
        return self.objValue

    def setValue(self, objValue):
        self.objValue = objValue

    def getNext(self):
        return self.nodeNext

    def setNext(self, nodeNext):
        self.nodeNext = nodeNext

    def isHead(self):
        return self.binHead

    def isTail(self):
        return self.binTail


node1 = Node(objValue='a')
nodeTail = Node(binTail=True)
nodeHead = Node(binHead=True, nodeNext=node1)

# Chapter 3-4 Linked List 2
'''
Head and Tail
    Specialized node
        Head : Always at the first of the list / not object
        Tail : Always at the last of the list / no object, next node
        These are the two corner stone showing the start and the end of the list
    These are optional nodes. 
        Linked list works okay without these
        However, having these makes implementation very convenient

Search procedure in singly linked list
    Again, let’s find ‘d’ and ‘c’ from the list
    Just like an array, navigating from the first to the last until hit is the only way
    No difference in the search pattern, though you cannot use index any further!
    Your list implementation may include the index function, but it is not required in the linked list
1. find head from list 2. next node if next == tail break else next.object=='b'/ 찾을때까지 반복 / n번검사해야함

Insert procedure in singly linked list
    This is the moment that you see the power of a linked list
    Last time, you need N retrievals to insert a value in the array list / 기존 array는 n번 해야한다
    This time, you need only three operations / node prev의 next를 node new로 변경
        With an assumption that you have a reference to the node, Nodeprev that you want to put your new node next
        First, you store a Node, or a Nodenext, pointed by a reference from Nodeprev’s nodeNext member variable
        Second, you change a reference from Nodeprev’s nodeNext to Nodenew
        Third, you change a reference from Nodenew’s nodeNext to Nodenext

Delete procedure in singly linked list / linked list의 장점
    This is the another moment that you see the power of a linked list
    Last time, you need N retrievals to delete a value in the array list / 기존에는 n번
    This time, you need only three operations
        With an assumption that you have a reference to the node, Nodeprev that you want to remove the node next
        First, you retrieve Nodenext that is two steps next from Nodeprev
        Second, you change a reference from Nodeprev’s nodeNext to Nodenext
    The node will be removed because there is no reference to Noderemove
    garbage collector가 안쓰는 메모리 삭제
'''


class SinglyLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0

    def __init__(self):
        self.nodeHead = Node(binHead=True, nodeNext=self.nodeTail)
        self.nodeTail = Node(binTail=True)

    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue=objInsert)
        nodePrev = self.get(idxInsert - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1

    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()

    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end="")
        print("")

    def getSize(self):
        return self.size


list1 = SinglyLinkedList()
list1.insertAt('a', 0)
list1.insertAt('b', 1)
list1.insertAt('c', 2)
list1.insertAt('d', 3)

# Chapter 3-4 Stack and Queue

'''
Scenario for Stack
    Back seat of a taxi One way in and out
    We are traveling from the source to our destinations
    Who should seat first and last?
    A scenario for a taxi= A scenario for SCM
    A cargo plane with one way in and out
    How to organize thecargo loading to theplane?

Structure of Stack
    Stacks are linear like linked lists - A variation of a singly linked list
    Difference
    Voluntarily giving up
        Access to the middle in the linked list
        Only accesses to the first instance in the list
        The first instance in the list    = The top instance in the stack
    An item is inserted or removed from the stack from one end called the “top” of the stack.
    This mechanism is called Last-In-First-Out (LIFO). /
    
Operation of Stack
    Stack operation / search insert delete는 안돼, only top control
    Push
        = Insert an instance at the first in the linked list
        = Put an instance at the top in the stack
    Pop
        = Remove and return an instance at the first in the linked list
        = Remove and return an instance at the top in the stack

Implementation of Stack
    Python code of a stack -Utilizing a singly linked list
    To pop an instance
        1 retrieval count
    To push an instance
        1 retrieval count
'''


class Stack(object):
    lstInstance = SinglyLinkedList()

    def pop(self):
        return self.lstInstance.removeAt(0)

    def push(self, value):
        return self.lstInstance.insertAt(value, 0)

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
print(stack.pop())

'''
Example: Balancing Symbols
Balancing symbols?
    [2+(1+2)]-3  Symbols are balanced
    [2+(1+2]-3  Symbols are not balanced
    Then, just counting opening and closing symbols?
    What if? [2+(1]+2)-3
Algorithm for the balanced symbol checking
    Make an empty stack
    read symbols until end of formula
        if the symbol is an opening symbol push it onto the stack
        if it is a closing symbol do the following
            If the stack is empty report an error
            Otherwise pop the stack. 
            If the symbol popped does not match the closing symbol report an error
At the end of the of formula if the stack is not empty report an error

'''

# Chapter 3-4 Stack and Queue

''' 
Senario for Queue # 맨처음 들어간게 맨 처음 나와
    Line at an airport- A way for going in At the end of the line
    Another way for going out -At the first of the line
    No one gets in the middle of the line
    A scenario of a line at the airport= A scenario of a production line at a factory
    The first product out is the first product in
    How to track the production line?

Structure of Queue
    Queues are linear like linked lists -    A variation of a singly linked list
    Difference
    Voluntarily giving up
        Access to the middle in the linked list == Same to the stacks
        Only accesses to the first and the last instances in the list
        The first instance in the list
        = The front instance in the queue
        The last instance in the list
        = The rear instance in the queue
    An item is inserted at the last
    An item is removed at the front
    This mechanism is called First-In-First-Out (FIFO)

Operation of Queue
Enqueue # insert역할로 마지막으로
    = Insert an instance at the last in the linked list
    = Put an instance at the rear in the queue
Dequeue # remove를 첫번째부터
    = Remove and return an instance at the first in the linked list
    = Remove and return an instance at the front in the queue

'''

class Queue(object) :
    lstInstance = SinglyLinkedList()
    def Dequeue(self):
        return self.lstInstance.removeAt(0)
    def Enqueue(self, value):
        self.lstInstance.insertAt(value,self.lstInstance.getSize())
    def isEmpty(self):
        if queue.lstInstance.getSize() == 0 :
            return True
        else :
            return False



queue = Queue()
queue.Enqueue(2)
queue.Enqueue(3)
queue.Enqueue(4)
queue.Dequeue()
queue.isEmpty()
queue.lstInstance.getSize()