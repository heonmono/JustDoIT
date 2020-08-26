# string - 문자열
strTest = "Hello World!"
print(strTest)
strTestComp = "Hello World!"
print(strTest == strTestComp)

# str slicing
print(strTest[0])
print(strTest[-1])
print(strTest[:-1])

# length
print(len(strTest))
print(strTest + " " + "Dept")
print(strTest + "Dept")

print(strTest*2)
print( "hello" in strTest)
print( "hello" not in strTest)

## List Tuple Dictionary

# index in sequence
print(strTest[1:9:2]) # x:y:z -> form x to y with z steps
print(strTest[1: len(strTest)])
print(strTest[5::-1]) # negative step 5 4 3 2 1 0

# List
lstTest = [1, 2, 3, 4] # list is another type of sequence variables
print(lstTest)
print(lstTest[0])
print(lstTest+lstTest)
print(lstTest*3)

lstTest = range(1,20,3) # range(x,y,z)_ == x:y:z you will this function many, many times
lstTest2 = list(range(1,20))
print(lstTest2)

print( 4 in lstTest, 100 in lstTest)

lstTest2.append('hey') # list 요소에 추가
lstTest2 # list에 data type은 중요하지 않음
del lstTest2[0]
lstTest2.reverse()
print(lstTest2)
lstTest2.remove(4) # del은 index이고 remove는 요소값이다
lstTest2.sort() # 음 강의에서는 문자 숫자 상관없다고 하는데 실행시 상관이 있음
print(lstTest2)

# Tuple - 튜플은 리스트와 비슷하지만 튜플은 데이터 변화를 받아들이지 않는다.
tplTest = (1, 2, 3)
print(tplTest)
print(tplTest[0], tplTest[2])
print(tplTest[1:3])
print(tplTest+tplTest)
print(tplTest*3)
# tplTest[0] = 100 # tuple can't change instances
# why it is need?  constant

# Dictionary - it is not sequential , it works by av pair of keys and values
#   a set of keys and values

dicTest = { 1: 'one', 2:'two', 3:'three'}
print(dicTest[1])
dicTest[4] = 'four'
print(dicTest)
dicTest[1] = 'hana'
print(dicTest.keys()) # list & tuple slice by index but dictionary is called by key
print(dicTest.values())
print(dicTest.items()) # list with tuple?

# Condition and Loop Statement

# if = condition statement
# python doesnt have a switch-case statement
# watch out indentations carefully beacuse that is your block statements
numScore = 75
if numScore > 90 :
    print('A')
else :
    print('lower grade')

# for = loop statement
''' for variable in sequence
        statements for loop
    else :
        when for-loop is finished wuthout a break'''
for itr in range(10) :
    print(itr)

sum = 0
for itr in range(1,11) :
    sum += itr
print(sum)

for itr in range(1, 100, 10) :
    if itr ==51 :
        continue # 아무 실행하지 않고 다시 for문으로
    else :
        print(itr, end="")

for itr in range(5) :
    print( itr)
else :
    print('!')

for itr in range(5) :
    if itr == 3 : # for문을 중지
        break
    print(itr)
else :
    print("!")
print("done")

# function statement
'''
def name(params) :
    statements
    return val1, val2... # python can return multiple variables
                         # dont have to specify return types
                         # one line function is called lambda
'''

numA = 1
numB = 2

def add(numparam1, numparam2) :
    return numparam1 + numparam2

def multiply(numparam1, numparam2) :
    return  numparam1*2, numparam2 * 3

def increase(numparam1, step =1) :
    return numparam1+step

numC = add(numA,numB)
numD, numE = multiply(numA,numB)
numF = increase(numA, 5)

lambdaAdd = lambda numparam1, numparam2 : numparam1 + numparam2
numH = lambdaAdd(numA,numB)
print(numA,numB,numC,numD,numE,numH)

# Finding Prime Numbers

def isPrimeNumber(numparam1) :
    for itr in range(2, numparam1) :
        if numparam1 % itr == 0 :
            break
        else:
            return True
    return False

def findPrimes(numparam1, numparam2) :
    numcount = 1
    for itr in range(numparam1, numparam2) :
        if isPrimeNumber(itr) == True :
            print(numcount, " th prime", itr)
            numcount = numcount +1

findPrimes(1,10)

# Assignment and Equivalence
x = [1, 2, 3]
y = [100, x, 120]
z = [x, 'a', 'b']

print(x)
print(y)
print(z)

x[1] = 1717

print('\nx : ', x)
print('y : ', y) # x가 변하면 값이 같이 변해, x의 값을 저장하는게 아니라 x가 가지고 있는 값을 새롭게 가져감, reference 포인터의 개념
print('z : ', z)

x[1] =2
x2 = [ 1, 2, 3]

if x == x2 :
    print("values are equivalence")
else :
    print("value is not equivaence")


if x is x2 :
    print("values are stored at the same place")
else :
    print("values are not stored at the same place")

if x[1] is y[1][1] :
    print("values are stored at the same place")
else:
    print("values are not stored at the same place")
# int나 string같은 것들은 값이 저장되고 리스트나 듀플은 레퍼런스 형식
# 값이 같은지 참조가 같은지 파악할 필요가 존제

'''
one variable's value is changed, but you see three changes
why this happened? beacause of references, x has two references from y and z
the valuse of y and z are determined by x , and x is changed 

* == checks   the equivalence of two referenced values
* is checks   the equivalence of two referenced objects' ids
'''

# Class and Instance

class MyHome : # class definition
    colorRoof = 'red'
    stateDoor = 'closed'
    def paintRoof(self, color) :
        self.colorRoof = color # myhome의 statedoor을 변수로 변환
    def openDoor(self) :
        self.stateDoor = 'open'
    def closeDoor(self) :
        self.stateDoor = 'close'
    def printStatus(self) :
        print("roof color is", self.colorRoof, end="")
        print(", and door is", self.stateDoor)

home1 = MyHome() # instance
home1.paintRoof('blue')
home1.printStatus() # see how to instantiate a class / var = classname(param)
#if home1 is home2, instance는 따로니까 false


# Important Methods in Class - Constructor, Desturctor

''' 
some basic methods, or member functions in classes
constuctor - called when instanitiated
destructor - called when the instance is removed from the value table'''

from time import ctime

class MyHome : # class definition
    colorRoof = 'red'
    stateDoor = 'closed'
    def paintRoof(self, color) :
        self.colorRoof = color # myhome의 statedoor을 변수로 변환
    def openDoor(self) :
        self.stateDoor = 'open'
    def closeDoor(self) :
        self.stateDoor = 'close'
    def printStatus(self) :
        print("roof color is", self.colorRoof, end="")
        print(", and door is", self.stateDoor)
    def __init__(self, strAddress): # __init__ : constuctor
        print("built on", strAddress)
        print("built at", ctime())
    def __del__(self): # __del__ : deconstructor, del을 통해 생성된 instance 삭제
        print("destroyed at", ctime())

homeAtdeajeon = MyHome("Deajeon Kaist")
homeAtdeajeon.printStatus()

del homeAtdeajeon

## Module and Import
'''
see how to separate the source code files
just put your code in another file , filename.py
use from to specify the directory , or the folder, path

import home call home.py
ctime class를 불러오고 MyHome class가 실행된다. 
'''

from time import ctime # time is packages and ctime is class

class MyHome : # class definition
    colorRoof = 'red'
    stateDoor = 'closed'
    def paintRoof(self, color) :  # def는 각각 member
        self.colorRoof = color # myhome의 statedoor을 변수로 변환
    def openDoor(self) :
        self.stateDoor = 'open'
    def closeDoor(self) :
        self.stateDoor = 'close'
    def printStatus(self) :
        print("roof color is", self.colorRoof, end="")
        print(", and door is", self.stateDoor)
    def __init__(self, strAddress): # __init__ : constuctor
        print("built on", strAddress)
        print("built at", ctime())
    def __del__(self): # __del__ : deconstructor, del을 통해 생성된 instance 삭제
        print("destroyed at", ctime())

# Organizing Modules by Packages
'''
from edu.Kaist,sealab.week1 import home / we can load packages by path 
같은 directory 라면 from이 필요없지만 그런 경우는 적을 듯.

__init__.py mean this is python packages
'''

'''
* directory or folder
    clusters modules / modules -> filename.py
    we call these directories as package
    hence, the precious infromation is exactly from package import module
* packages has __init__.py in the directory
this is how to differentiate between the ordinary and the packages directories
'''

# sample program : Interaction wuth Your Program
class CashierLine :
    lstLine = [] # member variable, and list
    def addCustomer(self, strName): # def is member function or method
        self.lstLine.append(strName)
    def processCustomer(self):
        strReturnName = self.lstLine[0]
        self.lstLine.remove(strReturnName)
    def printStatus(self):
        strReturn = ""
        for itr in range(len(self.lstLine)) :
            strReturn += self.lstLine[itr] + " "
            return strReturn

binLoop = True
line = CashierLine() # constructor, 하나의 istance create
while binLoop :
    strName = input("enter customer name :")
    if strName == "." :
        break
    elif strName == "->" :
        print("processed :", line.processCustomer())
        print("line", line.printStatus())
    else :
        line.addCustomer(strName)
        print("line :", line.printStatus())

print("number of remaining customers :", len(line.lstLine))




