# Chapter 2 Object-oriented paradigm and software design
# Chapter 2 - 1 Design and Programming

'''
Weekly Objectives - this week, we learn the object-oriented paradigm(OOP) and the basic of software design.
Objectives are
1. understanding object-oriented concepts = class, instance, inheritance, encapsulation, polymorphism
2. understanding a formal representation of soft ware design - memorizing a number of unified modeling language(UML) notations
3. understanding a number of software design patterns - factory, adapter, bridge, composite, observer, semantics and structures

'''

'''
Good Soft ware Design
Correntness - meet the purposes, without errors
Robustness - Execute under expected overloads
Flexibility - Enable the future updates and expansions of functions
Usability and Reusability - good support for the designed, easy to use for other purpose of context
Efficiency - easy to implement, smaller size, fater execution

object-oriented design : real world concepts를 programming도 가지고 있어야 한다.
software design entities - 개념 이름, 개념 특성, 행동

what are Class and Instance
Class : result of design and implementation, conceptualization, corresponds to desighn abstractions
Instance : result of execution, realization, corresponds to real world entities
'''


# Chapter 2 - 2 UML Notation
'''
Software Design as House Floorplan
after your graduation, some of you will be developing software - mainly design, some coding
need to learn how to communicate your colleagues - learn standard, learn how to represent your design
in software engineering, UML(Unified Modeling Language
'''
'''
UML notation : Class and Instance
Class : Customer
Named instance - Park::Customer
member variables. attribute, property - +-#(name):(type)  / + public # protected - private    
method, member function - +-#(name)(arguments, input parameters):(type)
'''


# Chapter 2 - 3 Encapsulation and Inheritance
'''
Encapsulation - 클레스내에 모든 내용이 쌓여져 있고 외부에서 메소드로 
Object = Data(attribute) + Behavior(method)
Delegating the implementation responsibility! - bring me a sausage, and i dont care how you made it
Utilizing the visibility - prive(only i can see) protected public(many can see)
Python does not support the visibility options!
'''

'''
Inheritance
Giving my attributes to my descendants - my attributes include member variables, method
My dsecendants may have new attributes of their own
My descendants may mask the received attributes
But if not specified, sons follow their father

Superclass
My ancestors, specifically my father
Generalized from the concoptual view

Subclass
my descendants, specifically my son
specialized from the conceptual view

How about having a mother? - it is possible in python
'''

# Inheritance in Python
class Father(object) : # object를 통해 상속, fundamental한 class
    strHometown = "Jeju"
    def __init__(self,paramHome):
        self.strHometown = paramHome
        print("Father is created")
    def doFatherThing(self):
        print("Father's action")
    def doRunning(selfs):
        print("Slow")

class Mother(object) :
    strHometown = "Seoul"
    def __init__(self):
        print("Mother is created")
    def doMotherThing(self):
        print("Mother's action")

class Child(Father, Mother) :
    strName = "Moon"
    def __init__(self):
        super(Child, self).__init__() # 상위 단계를 call
        print("Child is created")
    def doRunning(self): # overwring
        print("Fast")

me = Child()
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHometown)
print(me.strName)

''' self and super
self : reference variable pointing the instance itself
super : reference variable pointing the base class instance
    super is used to call the base class methods'''

class Child2(Father, Mother) :
    strName = "Moon"
    def __init__(self, paramName, paramHome):
        super(Child2, self).__init__(paramHome) # 상위 단계를 call / father.__init__(paramhone) home이 update
        self.strName = paramName
        print("Child is created")
    def doRunning(self): # overwring
        print("Fast")

me = Child2("sun", "universe")


# Chapter 2 - 3 Polymorphism and Abstract Class

''' 
Polymorphism = Poly(many) Morph(Shape)
Different behaviors with similar signature(Method name + Parameter list)
Sub1)
    Method Overriding - Base class has a method A(num), and its derived class has a method A(num)
    parent class 무시하고 child class 에서 새로 call 하는 것
Sub2)
    Method Overloading - A class has a method A(num), A(num,name), and A(num,name,home)
    class가 하나의 메소드 이름에 다양한 방식을 존재
'''

class Building :
    strAddress = "Deajeon"
    def openDoor(self):
        print("Door opened")

class Hotel :
    def openDoor(self): # overriding
        print("Dellboy opens a door")

    def checkin(selfs, days =1): # overloading
        print("someone check in for", days, "days")

lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkin()
lotteHotel.checkin(2)

'''
Abstract Class 
A class with an abstract method
what is the abstract method - method with signature, but with no implement
why use it then? i wnat to have a window here, but i dont know how it look like, but you should have

Abstract class in not a complete, half-made produce
Therefore, you cant make an instance out of it


The concrete class with full implementations and inheriting the abstract class will be a basis for instances
'''

import abc

class Room(object) :
#    __metaclass__abc.ABC

    # ab.cabstract method
    def openDoor(self) :
        pass
    #abc.abstract method
    def openWindow(self) :
        pass

class BedRoom(Room) :
    def openDoor(self):
        print("open bedroom door")
    def openWindow(self):
        print("open bedroom window")

Room1 = BedRoom()
Room1.openDoor()

'''
Overriding Methods in object
All of Python classes are the descendants of object
if you dont specify the base class of your class, then your class is the direct derived class of object

Obhect has many hidden methods
__init__ = consturctor , with override
__del__ = destructor
__eq__ = equality , is랑은 다르게 메모리 스페이스가 아닌 값을 비교
, __cmp__, __add__

You override them to make the methods behave as you please
'''

class Room :
    numWidth = 100
    numHeight = 100
    numDepth = 100
    def __init__(self, parWidth, parHeight, parDepth):
        self.numWidth = parWidth
        self.numHeight = parHeight
        self.numDepth = parDepth
    def getVolume(self):
        return self.numDepth * self.numHeight * self.numWidth
    def __eq__(self, other):
        if isinstance(other, Room) :
            if self.getVolume() == other.getVolume() : # Duck Typing : eiser to ask for forgiveness the Permission
                return True                            # 막 치는 것..?
        return False

Room1 = Room(100, 20 , 30)
Room2 = Room(100, 10, 60)
print(Room1 == Room2)

# Chapter 2 - 4 UML Notation2
'''
More about UML Notations
Many types of UML diagrams used for different stages of development. If I name a few of them…
    Use-case diagram
    Class diagram
    State diagram
    Deployment diagram
We are dealing with OOP(object oriented paradaim) in this week
    Mainly, class and instances
    Also, some of software design patterns
    Hence, we focus on Class diagram

method signature same -> method override, similar -> method overload
hollow arrow : generalization, -> association, 마름모 : augmentation
'''


# Chapter 2 - 5 Structure and Relationship
'''
Generalization between classes is-a relationship

Inheritance relationship -> super class, subclass
Customer  Person :From subclass To superclass, Direction of generalization
Hollow triangle shape
Base class: Person
Leaf class: Park::Customer…
'''

'''
Association between classes has-a relationship / 음 그냥 관계형 db같은 느낌..
Member variables
    A customer has a number of holding accounts
    An account has an account holder customer
Simple line
If a simple arrow is added
    A customer has a reference to bank accounts
    A bank account has a reference to a customer
    Navigability
Line ends are tagged by roles
    Account holder
    Holding accounts
    With prefix showing the visibiliy
    +: public , -: private, #: protected
'''

class Customer :
    ID = "No one"
    lstAccount = []
    def addBankAccount(self, account):
        self.lstAccount.append(account)

class BankAccount :
    strAccountHolder = "No one"
    def changeAccountHolder(self, holder):
        self.strAccountHolder = holder

'''
Multiplicity of Association

In computer science and engineering
    * often means many
    Hence,
    1..* = 1 to Many
    * = 0 to Many
Naturally
    1 = Exactly one
    0..1 = One or zero
If not specified, it means one
'''

'''
Aggregation / unary relationship 같은 느낌

Special case of association
Special has-a relationship
More like, part-whole or part-of relationship
A family member is a part of a family
    The existence of the family depends on the aggregation of the family member
    If nothing to aggregate, there is no family
    Hollow diamond shape
Aggregation often occur 
    when an aggregating class is a collection class
    When the collection class’s life cycle depends on the collected classes
'''

'''
Dependency

Dependency between classes
    use relationship
    An engineer uses a calculator
May use for
    Local variables
    Method signatures
        Parameter types
    Method return types
Something that you import for the implementation
'''

class Calculaor :
    def calculSomething(self):
        return ...

class Engineer :
    def drawFloorplan(self):
        calc = Calculaor()
        value = calc.calculSomething()
        return value

