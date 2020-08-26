# Chapter 4 Recursion and dynamic programming
# Chapter 4 -1 Recursions

'''
Weekly Objectives

This week, we learn how to program recursive routines and dynamic programming concepts
    Recursion
    Dynamic programming
Objectives are
    Understanding the concept of recursions # 재귀 호출
    Repeating problems
    Divide and conquer
    Recursion function call
    Recursion escape
    Recursion depth
Able to implement recursive programs
Understanding the concept of dynamic programming # 재귀의 결과를 사용하는 것
    Reusing previous function call result
    Memoization for time saving
'''

'''
Recursion
Repeating Problems andDivide and Conquer 
    Calculating a budget of a company?
        Departments consist of the company
        Departments within departments
    Can’t avoid the below structures
    class Department
    dept = [sales, manu, randd]
    def calculateBudget(self)
        Sum = 0
        For itr in range(0, numDepartments)
        Sum = sum + dept[itr].calculateBudget() # 동일함수 재귀. 분할된 작은 문제에 대해서
        Return sum

More examples…
    Factorial
        𝐹𝑎𝑐𝑡𝑜𝑟𝑖𝑎𝑙(𝑛)={█(1 𝑖𝑓 𝑛=0@𝑛×(𝑛−1)×…×2×1 𝑖𝑓 𝑛>0)┤
        Repeating problems?
        𝐹𝑎𝑐𝑡𝑜𝑟𝑖𝑎𝑙(𝑛)={█(1 𝑖𝑓 𝑛=0@𝑛×𝐹𝑎𝑐𝑡𝑜𝑟𝑖𝑎𝑙(𝑛−1) 𝑖𝑓 𝑛>0)┤
    Great Common Divisor ( 최대 공약수)
    GCD(32,24) = 8
    Euclid’s algorithm
        GCD(A, B)=GCD(B, A mod B)
        GCD(A, 0)=A
    Commonality
        Repeating function calls
        Reducing parameters
        Just like the mathematical induction # 점화식..? 수학적 귀납법

Recursion
A programming method to handle the repeating items in a self-similar way
    Often in a form of
    Calling a function within the function # function 속에서 다시 불러/ pseudo code
        def functionA(target)
        ….
        functionA(target’) # size가 줄어들어 있어야 한다.
        ….
        if (escapeCondition) # escape route가 필요
        Return A; 
'''

def Fibonacci(n) :
    if n  == 0 :
        return 0
    if n == 1 :
        return 1
    intRet = Fibonacci(n-1) + Fibonacci(n-2)
    return intRet

for itr in range(0, 10) :
    print(Fibonacci(itr), end=" ")

'''
Recursions and Stackframe
Recursion of functions
    Increase the items in the stackframe
    Stackframe is a stack storing your function call history
        Push: When a function is invoked
        Pop: When a function hits return or ends # return 시에 
        What to store? # within function variable
        Local variables and function call parameters
'''


# Chapter 4 - 2 Merge Sort and Problems in Recursions

'''
Merge Sort
    Merge sort: One example of recursive programming - 재귀 솔팅의 한 방법
    Decompose into two smaller lists - 점점 작은 것으로 나눈다.
    Aggregate to one larger and sorted list
'''

import random

def perfromMergeSort(lstElementToSort) :
    if len(lstElementToSort) == 1 : # escape code
        return lstElementToSort

    lstElementToSortSub1 = []
    lstElementToSortSub2 = []

    for itr in range(len(lstElementToSort)) : # decomposite
        if len(lstElementToSort)/2 > itr :
            lstElementToSortSub1.append(lstElementToSort[itr])
        else :
            lstElementToSortSub2.append(lstElementToSort[itr])

    lstElementToSortSub1 = perfromMergeSort(lstElementToSortSub1) # recursion
    lstElementToSortSub2 = perfromMergeSort(lstElementToSortSub2)

    idxCount1 = 0
    idxCount2 = 0

    for itr in range(len(lstElementToSort)) :
        if idxCount1 == len(lstElementToSortSub1) :
            lstElementToSort[itr] = lstElementToSortSub2
            idxCount2 = idxCount2 + 1
        elif idxCount2 == len(lstElementToSortSub2) :
            lstElementToSort[itr] = lstElementToSortSub1[idxCount1]
            idxCount1 = idxCount1 + 1
        elif lstElementToSortSub1[idxCount1] > lstElementToSortSub2[idxCount2] :
            lstElementToSort[itr] = lstElementToSortSub2[idxCount2]
            idxCount2 = idxCount2 + 1
        else :
            lstElementToSort[itr] = lstElementToSortSub1[idxCount1]
            idxCount1 = idxCount1 + 1
    return lstElementToSort

lstRandom = []
for itr in range(100) :
    lstRandom.append(random.randrange(0,100))
print(lstRandom)
lstRandom = perfromMergeSort(lstRandom)
print(lstRandom)

'''
Problems in Recursions of Fibonacci Sequence

Problems in recursions
    Excessive function calls
    Calling functions again and again
    Even though the function is executed before with the same parameters # 같은 파라미터를 너무 많이 불러..
For instance, Fibonacci(4)
Has two repeated calls of F(0)
Has three repeated calls of F(1)
Has two repeated calls of F(2)
These are unnecessarily taking timeand space
How to solve this problem?  -> dynamic programming
'''


# Chapter 4 - 2 Dynamic Programming 1 (Memoization)
'''
Dynamic programming: recursion이 사용하는 불필요한 콜들을 저장함으로써 해결
    A general algorithm design technique for solving problems defined by or formulated as recurrences with overlapping sub-instances
    In this context, Programming == Planning

Main storyline
    Setting up a recurrence
    Relating a solution of a larger instance to solutions of some smaller instances
    Solve small instances once
    Record solutions in a table
    Extract a solution of a larger instance from the table


Memoization - 미모아이제이션
Key technique of dynamic programming
    Simply put / 펑션 콜과 결과를 저장
    Storing the results of previous function calls to reuse the results again in the future - 결과를 저장
More philosophical sense
    Bottom-up approach for problem-solving in memoization
    
    Recursion: Top-down of divide and conquer
    Dynamic programming: Bottom-up of storing and building


'''

# Chapter 4 - 3 Implementation Example:Fibonacci Sequence in DP
'''Use a dictionary collection variable type for memoization
Memoization
Storing a fibonacci number for a particular index
Now,
We have a new space requirement, the dictionary or the table, of O(N)
We have reduced execution time from O(2n) to O(N)
'''

def FinbonacciDP(n) :
    dicFibonacci = {}
    dicFibonacci[0] = 0
    dicFibonacci[1] = 1

    for itr in range(2, n+1) :
        dicFibonacci[itr] = dicFibonacci[itr-1] + dicFibonacci[itr -2]
    return dicFibonacci[n]

for i in range(10) :
    fibonacci = FinbonacciDP(i)
    print(fibonacci)

# Chapter 4 - 5 Assembly Line Scheduling

# assembly line with recursions
class AssemblyLines :
    timeStation = [[7,9,3,4,8,4],[8,5,6,4,5,7]]
    timeBelt = [[2,2,3,1,3,4,3],[4,2,1,2,2,1,2]]
    intcount = 0
    def Scheduling(self, idxLine, idxStation):
        print("Calculate scheduling : line, station :", idxLine, idxStation, "(", self.intcount, "recursion calls )")
        self.intcount = self.intcount + 1
        if idxStation == 0 :    # escape function
            if idxLine == 1 :
                return self.timeBelt[0][0] + self.timeStation[0][0]
            elif idxLine == 2 :
                return  self.timeBelt[1][0] + self.timeStation[1][0]
        if idxLine == 1 :   # recusrsion call
            costLine1 = self.Scheduling(1, idxStation - 1) + self.timeStation[0][idxStation]
            costLine2 = self.Scheduling(2, idxStation - 1) + self.timeStation[0][idxStation] + self.timeBelt[1][idxStation]
        elif idxLine == 2 :
            costLine1 = self.Scheduling(2, idxStation - 1) + self.timeStation[1][idxStation]
            costLine2 = self.Scheduling(1, idxStation - 1) + self.timeStation[1][idxStation] + self.timeBelt[0][idxStation]

        if costLine1 > costLine2 :
            return costLine2
        else :
            return  costLine1

    def startScheduling(self):
        numStation = len(self.timeStation[0])
        costLine1 = self.Scheduling(1, numStation - 1) + self.timeBelt[0][numStation]
        costLine2 = self.Scheduling(2, numStation - 1) + self.timeBelt[1][numStation]
        if costLine1 > costLine2 :
            return costLine2
        else:
            return costLine1

lines = AssemblyLines()
time = lines.startScheduling()
print("fatest production time :", time)

# assembly line with dp
class AssemblyLines :
    timeStation = [[7,9,3,4,8,4],[8,5,6,4,5,7]]
    timeBelt = [[2,2,3,1,3,4,3],[4,2,1,2,2,1,2]]

    timeScheduling = [list(range(6)),list(range(6))]
    stationTracing = [list(range(6)),list(range(6))]

    def startSchedulingDP(self):
        numStation = len(self.timeStation[0])
        self.timeScheduling[0][0] = self.timeBelt[0][0] + self.timeStation[0][0]
        self.timeScheduling[1][0] = self.timeBelt[1][0] + self.timeStation[1][0]

        for itr in range(1 ,numStation) :
            if self.timeScheduling[0][itr -1] > self.timeScheduling[1][itr-1] + self.timeBelt[1][itr] :
                self.timeScheduling[0][itr] = self.timeScheduling[0][itr] + self.timeScheduling[1][itr-1] + self.timeBelt[1][itr]
                self.stationTracing[0][itr] = 1
            else :
                self.timeScheduling[0][itr] = self.timeScheduling[0][itr] + self.timeScheduling[0][itr - 1]
                self.stationTracing[0][itr] = 0

            if self.timeScheduling[1][itr -1] > self.timeScheduling[0][itr-1] + self.timeBelt[0][itr] :
                self.timeScheduling[1][itr] = self.timeScheduling[1][itr] + self.timeScheduling[0][itr-1] + self.timeBelt[0][itr]
                self.stationTracing[1][itr] = 0
            else :
                self.timeScheduling[1][itr] = self.timeScheduling[1][itr] + self.timeScheduling[1][itr - 1]
                self.stationTracing[1][itr] = 1

        costLine1 = self.timeScheduling[0][numStation - 1] + self.timeBelt[0][numStation]
        costLine2 = self.timeScheduling[1][numStation - 1] + self.timeBelt[1][numStation]
        if costLine1 > costLine2 :
            return costLine2 , 1
        else :
            return costLine1 , 0

    def printTracing(self, lineTracing):
        numStation = len(self.timeStation[0])
        print("line :", lineTracing, ", station :", numStation)
        for itr in range(numStation-1, 0 , -1) :
            lineTracing = self.stationTracing[lineTracing][itr]
            print("line :", lineTracing, "station :", itr)
lines = AssemblyLines()
time, linsTracing = lines.startSchedulingDP()
print("fatest production time :", time)
lines.printTracing(linsTracing)

