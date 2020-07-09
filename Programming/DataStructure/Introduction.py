## lecture 1
# procedure oriented program <-> object oriented(by_Class)

def main() : # def : function declarition keyword  main : is name of fucntion, can have parameter
    print("hello world")
    print("this program copmute the average of two exam so")

    score1, score2 = map(int, input("enter two scores seperated by ,").split(","))
    average = (score1 + score2) / 2.0;
    print("the average of the score is :", average)

main()


# second python - object-oriented -> class


# deficition part
class HelloWorld :
    def __init__(self):
        print("hello world just one more time")
    def __del__(self):
        print("good bye")
    def performAverage(self,val1,val2): # parameter
        average = (val1 + val2) / 2.0
        print("the average of she score is :", average)

def main() :
    world = HelloWorld()
    score1, score2 = map(int, input("enter two scores seperated by a comma ,").split(","))
    world.performAverage(score1,score2) # self is world / ahead of dot

main() # executuion part


## Naming and Styling

'''
Naming and Styling
Camel Casing : HelloWorld 새로운 단어에 대문자 시작 
Variable name : 어떤 내용인지 파악 : 시작을 소문자, 형을 사전에 부여하지 않음
Method name : Verb for the method action, 소문자 시작 ex. performAverage(self,,)

Indentation : 4 spaces per cash level
'''

## Variable Statements and Operators

# Data Types
'''
numeric : 
integer 32bit /  longinteger : end with L
float 64bit
octal integer : base 8 integer
hexadeciaml integer base 16 integer
complex

string : character

collection data : list dictionary tuples
'''

def main() :
    numBase10 = 2011
    numBase8 = 1548
    numBase16 = 0x7DB

    print("the year base 10 : %d, by base 8 : %d, by base 16 : %d" % (numBase10 \
                                                                      ,numBase8,numBase16))

    numComplex1 = complex(3,4)
    numComplex2 = 4+3j

    print("complex value :", numComplex1)
    print("real value: ", numComplex1.real)
    print("cmage value :", numComplex1.imag)

    strDeptName = "djgkle"
    print("full nae of act :", strDeptName)

main()

# operator

def main() :
    numTest1 = 10
    numTest2 = 3.0
    numDivide = numTest1 / numTest2
    numModula = numTest1 % numTest2
    print("%d, %d" % (numDivide, numModula))

    numDivideint = numTest1/ int(numTest2)
    print(numDivide,numDivideint)

    numTest2, numTest1 = numTest1, numTest2
    print(numTest1, numTest2)

    print(numTest1 == numTest2)
    print(type(numTest1))

    numTest1 = str(numTest1)
    print(type(numTest1))

    strFormula = "2011/ 7"
    print(eval(strFormula))

main()