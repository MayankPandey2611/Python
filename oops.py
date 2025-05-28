
# FOUR PROPERTIES =>
# --------------------------------1. INHERITANCE =>  USED TO INHERIT THE PARENT CLASS BY CHILD CLASS.

# TYPES => 

# 1. SINGLE-LEVEL =>  PARENT ------------> CHILD

# class Parent:
#     x=10
#     def __init__(self,name):
#         self.n = name
#         print(id(self))

#     def home(self):
#         print('home from parent class')

# class Child(Parent):
#     def home(self):
#         print('home from child class')
#         super().home()
#         # SUPER => USED TO OVERCOME METHOD OVERRIDDING . (IT PRINTS THE STATEMENT OF PARENT CLASS.)
   
# obj=Child('mayank')
# print(obj.x)
# print(obj.n)
# obj.home()
# print(id(obj))



# 2. MULTI-LEVEL =>  GRANDPARENT ------> PARENT ---------> CHILD 

# class GParent:
#     def car(self):
#         print('car from Gparent class')
#         print(id(self))

# class Parent(GParent):
#     x=10
#     def __init__(self,name):
#         self.n = name
#         print(id(self))

#     def home(self):
#         print('home from parent class')

# class Child(Parent):
#     def home(self):
#         print('home from child class')
#         super().home()
#         # SUPER => USED TO OVERCOME METHOD OVERRIDDING . (IT PRINTS THE STATEMENT OF PARENT CLASS.)
   
# obj=Child('mayank')
# print(obj.x)
# print(obj.n)
# obj.home()
# print(id(obj))
# obj.car()



# 3. MULTIPLE => PARENT 1 ------->  PARENT 2 ---------> CHILD

# class Parent1:
#     def car(self):
#         print('car from parent1 class')

# class Parent2:
#     x=10
#     def __init__(self,name):
#         self.n = name
#         print(id(self))

#     def home(self):
#         print('home from parent class')

# class Child(Parent1,Parent2):
#     def home(self):
#         print('home from child class')
#         super().home()
#         # SUPER => USED TO OVERCOME METHOD OVERRIDDING . (IT PRINTS THE STATEMENT OF PARENT CLASS.)
   
# obj=Child('mayank')
# print(obj.x)
# print(obj.n)
# obj.home()
# print(id(obj))
# obj.car()

# 4. HIERARICHICAL => PARENT ------. CHILD 1-------> CHILD 2

# class Parent:
#     x=10
#     def __init__(self,name):
#         self.n = name
#         print(id(self))

#     def home(self):
#         print('home from parent class')

# class Child1(Parent):
#     def home(self):
#         print('home from child class')
#         super().home()
#         # SUPER => USED TO OVERCOME METHOD OVERRIDDING . (IT PRINTS THE STATEMENT OF PARENT CLASS.)
# class Child2(Parent):
#     pass
# obj=Child1('mayank')
# obj1=Child2('ayush')
# print(obj.x)
# print(obj1.x)
# print(obj.n)
# print(obj1.n)
# obj.home()
# obj1.home()
# print(id(obj))

# 5. HYBRID  => 

# class A :
#     def first(self):
#         print('from class A')
# class B:
#     def first(self):
#         print('from class B')
# class C(A):
#     pass
# class D(B):
#     pass

# class E(D,C):  #MRO => METHOD REDUCTION 
#     pass

# obj = E()
# obj.first()



# -----------------------------------------------2. ABSTRACTION => 
# ABSTRACT CLASS => IF ABC IS IMPORT AND USES MORE THAN 2 METHODS IN CLASS ANS ATLEAST ONE ABSTRACT METHOD THEN IT IS CALLED AS ABSTRACT CLASS.
#  , ABSTRACT METHOD , CANCREATE METHOD 
# ABC = ABSTRUCT BASE CLASS

# from abc import ABC , abstractmethod

# class Senior(ABC):
#     def add(self,x,y):
#         print(x+y)
#     def sub(self,x,y):
#         print(x-y)
#     def multi(self,x,y):
#         print(x*y)
#     @abstractmethod
#     def div(self):
#         pass
# class Junior(Senior):
#     def div(self,x,y):
#         print(x/y)
# obj= Junior()
# obj.add(10,2)
# obj.sub(10,2)
# obj.multi(10,2)
# obj.div(10,2)

#-------------------------------------------3. POLYMORPHISM =>

# METHOD OVERLOADING IS NOT SUPPORTED IN PYTHON. 

# MULIPLY BEHAVIOER (MANY FORMS) OF A SINGLE FUNCTION IS POLYMORPHISM.


class XYZ :
    def __init__(self):
        print('from 1st constructor')    
    def __init__(self,x,y):
        print('from 2nd constructor')
obj = XYZ()

# -------------------------------------------4. ENCAPSULATION =>

#   MULTIPLY VARIABLES AND VALUES ARE KEPT IN A SINGLE CLASS THEN IT IS CALLED AS ENCAPSULATION.

# ACCESS SPECIFER / MODIFIER =>  NOT RECOMMANDED BY PYHTON . 

#  PUBLIC  (X / SHOW())

# class P:
#     x=10
#     def show(self):
#         print('from p class')
# class C(P):
#     pass
# obj = C()
# print(obj.x)
# print(obj.show())


# PROTECTED(PYTHON NOT SUPPORTED)  (_X / _SHOW())

# class P:
#     _x=10
#     def _show(self):
#         print('from p class')
# class C(P):
#     pass
# obj = C()
# print(obj._x)
# print(obj._show())


# PRIVATE  (__X / __SHOW )

# class P:
#     __x=10
#     def __show(self):
#         print('from p class')
# class C(P):
#     print(P.__x)
# obj = C()
# print(obj.__x)
# print(obj.__show())


# ALL THE CLASS CAN BE ACCESSABLE (DIR) .

# class P:
#     __x=10
#     def __show(self):
#         print('from p class')
# class C(P):
#     pass
# obj = C()
# # print(dir(C))
# print(obj._P__x)
# print(obj._P__show())

