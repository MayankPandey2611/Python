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

class student:
    def __init__(self , name , city):
        self.n = name       #INSIDE CONSTRUCTOR (DECLARATION)
        self.c = city
        # print(self.n , self.c)   #ACCESS INSIDE CONSTRUCTOR.

    def add(self,phone):
        self.p = phone   #INSIDE INSTANCE METHOD (DECLARATION)
        print(self.n , self.c , self.p , self.school)  # ACCESS INSIDE INSTANCE METHOD.

obj = student('mayank' ,'bhopal')

obj.school  = 'sirt'    #OUTSIDE OF THE CLASS (DECLARATION)

obj.add(4567891234)

# print(obj.n , obj.c , obj.p , obj.school)  # ACCESS OUTSIDE THE CLASS


# OBJECT
# CONSTRUCTOR





