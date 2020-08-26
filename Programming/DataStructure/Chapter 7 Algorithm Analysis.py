# Chapter 7 Algorithm Analysis

# Chapter 7 - 1 Factors of Program's Efficiency

'''
Weekly Objective
This week, we learn how to analyze the efficiency of our program
Algorithm analysis
Objectives are
Memorizing the definition and the rules of the big-Oh notation
Understanding what determines the efficiency of programs
Understanding simple algorithms
Memorizing the insert and the delete of lists, stacks, and queues
Memorizing the bubble sort
Able to apply the big-Oh notation analysis to programs
'''

'''
Factors of program’s efficiency
Algorithm
    A clearly specified set of simple instructions to be followed to solve a problem
    Takes a set of values as inputs
    Produces a set of values as outputs
    Specified in
    English
    A computer program
    Pseudo-code
Data structures	 = Methods of organizing data
Program = algorithms + data structures  
'''
# Chapter 2 - Bublle sort algorithm

'''
Examples of algorithms
    Insertion, deletion, search of linked lists, stacks, queues…
    Sorting of linked lists…
        Various sorting methods
        Bubble sort, Quick sort, Merge sort…
    Bubble Sort(list)
    For itr1=0 to length(list)
        For itr2=itr+1 to length(list)
            If list[itr1] < list[itr2]
                Swap list[itr1], list[itr2]
        Return list
    This program uses
        Data structure: List 
        Algorithm: Bubble sort
'''

# bubble = data structure = list
import random

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)
print(lstNumbers)

def performSelectionSort(lstNumbers) :
    for itr1 in range(0, N) :
        for itr2 in range(itr1+1, N) :
            if lstNumbers[itr1] < lstNumbers[itr2] :
                lstNumbers[itr1], lstNumbers[itr2] =\
                lstNumbers[itr2], lstNumbers[itr1]
    return lstNumbers

 performSelectionSort(lstNumbers)

 # total iteration = 9+8... = n(n-1)/2
 # we can calculate how it costs

# Chapter 7 -3 Importance of Efficiency
'''
Why do we care about efficiency?
    Writing a working program is not good enough
        The program could be inefficient
        If the program runs on a large data, the running time becomes a big issue
        Sometimes, a program may not be usable because of the efficiency
        Imagine a transaction system of a financial company
        1 transaction = 0.001 sec
        10 transactions by 10,000 account holders = 100 sec
        Side effect  If there is no reaction from the system, the users click the request again! Increased requests when there is a delay
            Imagine a bubble sorting function for bank accounts
            10,000 accounts  roughly 50,000,000 iterations for sorting
    Therefore, we need a guarantee of the worst-case scenario
    The worst-case running time of a single transaction
    The worst-case transaction request numbers of a single day
'''

# Chapter 7-4 Definition of Algorithm Analysis and Examples
'''
Analyzing an algorithm
    Estimating the resources that the algorithm requires
        Memory ,Communication bandwidth
        Computational time (the most important resource in the most of cases)
Factors affecting the running time
    Computer used for executions, Algorithms
    Data structures,Input data size
After analyzing the algorithms
    We estimate the worst-case of the costs by the factors
    i.e. Computational time by input data size
    i.e. Iterations by input data size
'''

def calculateIntergerRangeSum(intFrom, intTo) :
    intSum = 0

    for itr in range(intFrom, intTo) :
        intSum = intSum + itr

    return intSum

print(calculateIntergerRangeSum(0,10)) # 2n + 2 = O(N)

def performSelectionSort(lstNumbers) :
    for itr1 in range(0, N) : # N번
        for itr2 in range(itr1+1, N) :
            if lstNumbers[itr1] < lstNumbers[itr2] : # assuming that if always results in true
                lstNumbers[itr1], lstNumbers[itr2] =\
                lstNumbers[itr2], lstNumbers[itr1]
    return lstNumbers
# 3/2n^2 - 3/2n +n + 1

# Chapter 7-5 Big-Oh Notation
'''
Asymptotic notation: Big-Oh

What do O(N) and O(N2) mean? - That’s the Big-Oh notation
Notation to show the worst-case running time
    Do you remember?
    Assuming that “if” always results in true
    So, this is a worst scenario for the run-time
    Because the program should run the statements in the “if” block
Definition of the Big-Oh notations
    f(N) = O(g(N))
    There are positive constants c and n0 such that 
    f(N) ≦ c g(N) when N ≧ n0
    The growth rate of f(N) is less than or equal to the growth rate of g(N)
    g(N) is an upper bound on f(N)
'''

# 7 - 6 Growth rate
'''
Definition of the Big-Oh notations
    f(N) = O(g(N))
There are positive constants c and n0 such that 
f(N) ≦ c g(N) when N ≧ n0
The growth rate of f(N) is less than or equal to the growth rate of g(N)
g(N) is an upper bound on f(N)
'''

# 7 - 7 Examples & Rules of Big-Oh Notation
'''
Rules of Big-Oh notation
When considering the growth rate of a function using Big-Oh
    Ignore the lower order terms and the coefficients of the highest-order term
    When we have N3, then N2 and N means nothing in terms of Big-Oh
    From the growth rate order
    cN > Nk > N2 > NlogN > N > logN > C
    C >= 2 and k > 2
    No need to specify the base of logarithm
    O(logN) = O(logCN)
If T1(N) = O(f(N)) and T2(N) = O(g(N)), then
    T1(N) + T2(N) = max(O(f(N)),  O(g(N)))
    max(O(N), O(N2)) = O(N2)
    T1(N) * T2(N) = O(f(N) * g(N))
    O(N) * O(logN) = O(NlogN)
'''
