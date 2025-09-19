# ----------------------------------OOPS TOPICS----------------------------------------------------------//
# PYHTON VARIABLE HOLDES CALL BY REFERENCE.
# VARIABLE  => CONTAINER WHICH HOLDS VALUES ADDRESS.
# TYPES OF VARIABLES => 1. INSTANCE 2. CLASS/STATIC 3. LOCAL 
# METHODS => INSTANCE METHOD , CLASS METHODS , LOCAL  METHODS 

# 1. CLASS 
# SYNTAX => 
#  CLASS CLASS_NAME :
#           'DOC STRING'
#           VARIABLE
#           METHODS
#           CONSTRUCTOR
# __INIT__ => PREDEFINED CONSTRUCTOR
# SELF => VARIABLE 
# class student:
#     def __init__(self,name,city,contact):
#         self.n = name 
#         self.c = city
#         self.p = contact

# # FOR ERROR
# # obj = student
# # print(obj.n , obj.c , obj.p)

# # CONSTRUCTOR CALL
# obj1= student('MAYANK' , 'BHOPAL' , 4546486654)
# obj2= student('AYUSH' , 'REWA' , 789455123)
# print(obj1.n , obj1.c , obj1.p)
# print(obj2.n , obj2.c , obj2.p)

#--------------------------------------------INSTANCE VARIABLE DECLARATION AND ACCESS------------------------------------------------#

# class student:
#     def __init__(self , name , city):
#         self.n = name        #INSIDE CONSTRUCTOR (DECLARATION)
#         self.c = city
#         # print(self.n , self.c)   #ACCESS INSIDE CONSTRUCTOR.

#     def add(self,phone):
#         self.p = phone    #INSIDE INSTANCE METHOD (DECLARATION)
#         print(self.n , self.c , self.p , self.school)  # ACCESS INSIDE INSTANCE METHOD.

# obj = student('mayank' ,'bhopal')

# obj.school  = 'sirt'     #OUTSIDE OF THE CLASS (DECLARATION)

# obj.add(4567891234)

# print(obj.n , obj.c , obj.p , obj.school)    # ACCESS OUTSIDE THE CLASS


# QUESTION => ADD TWO NUMBERS IN CLASS.
# class sum:
#     def __init__(self,a,b):
#         self.f=a
#         self.s=b
#         print(self.f+self.s)

# obj = sum(12,10)


# -------------------------------------------------------CLASS / STATIC METHODS---------------------------------------------------#

# class student:
#     school ='sirt'  #DECLARATION INSIDE THE CLASS BODY.
#     def __init__(self,name):
#         self.n = name
    
# obj = student('mayank')
# obj1 = student('yash')
# print(obj.n , obj.school)
# print(obj1.n , obj1.school)


# class student:
#     school='sirt'     #DECLARATION INSIDE THE CLASS BODY.
#     def __init__(self,name):
#         self.n = name  
#         student.code = 601      #DECLARATION INSIDE THE CONSTRUCTOR.
#         print(student.school)
#     def addnew(self):
#         student.city = "bhopal"     #DECLARATION INSIDE INSTANCE METHOD.
#         print(student.school , student.code , student.city)
#     def show(self):
#         print(student.grade)

# student.grade  = '12'
# obj = student('mayank')
# obj.addnew()
# obj.show()
# print(obj.n)


#-----------------------------------------------  LOCAL METHOD ---------------------------------------------#

class student:
    def __init__(self,name):
        grade='12'
        self.n = name
        print(grade)
    def new(self):
        print(student.grade)   # LOCAL VARIABLE CANNOT BE ACCESSED INSIDE INSTANCE METHOD.
obj  = student('mayank')
obj.new('12')

# OBJECT
# CONSTRUCTOR


# METHODS => 1. INSTNCE


#  2. CLASS METHODS

# class student:
#     school='sirt'
#     grade='10th'
#     def __init__(self,name):
#         self.n=name
#     def show(self):
#         print(self.n)
#         print(self.school)
#         print(self.grade)
#         print(self.city)
#     @classmethod  # INBULIT DECORATER (@ adds the cls with student class)
#     def update(cls,updated):
#         cls.grade = updated

#     @classmethod
#     def add(cls,city):
#         cls.city = city

# obj = student('mayank')
# # obj.show()

# student.update('11th')

# # obj2=student('ayush')
# # obj2.show()

# student.add('bhopal')
# obj.show()


#  3. STATIC METHODS


# class student:
#     school='sirt'
#     grade='10th'
#     def __init__(self,name):
#         self.n=name
#     def show(self):
#         print(self.n)
#         print(self.school)
#         print(self.grade)
        
#     @staticmethod
#     def add(cls,city):
#         print(cls)
#         print(city)

# obj = student('mayank')
# student.add('bhopal','rewa')
# obj.show()


# class greet:
#     def __init__(self,name):
#         self.n = name
#     @staticmethod
#     def welcome():
#         print('welcome to our web page')

#     @staticmethod
#     def bye():
#         print('Thanks for visting')

# obj = greet("mayank")
# obj.welcome()
# obj.bye()