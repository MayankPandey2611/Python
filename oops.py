
# FOUR PROPERTIES =>
# 1. INHERITANCE =>  USED TO INHERIT THE PARENT CLASS BY CHILD CLASS.

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

class Parent:
    x=10
    def __init__(self,name):
        self.n = name
        print(id(self))

    def home(self):
        print('home from parent class')

class Child1(Parent):
    def home(self):
        print('home from child class')
        super().home()
        # SUPER => USED TO OVERCOME METHOD OVERRIDDING . (IT PRINTS THE STATEMENT OF PARENT CLASS.)
class Child2(Parent):
    pass
obj=Child1('mayank')
obj1=Child2('ayush')
print(obj.x)
print(obj1.x)
print(obj.n)
print(obj1.n)
obj.home()
obj1.home()
print(id(obj))

# 5. HYBRID 


# 2. ABSTRACTION
# 3. POLYMORPHISM
# 4. ENCAPSULATION