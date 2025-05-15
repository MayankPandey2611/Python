
#------------------------------------------SYNTAX  OF FUNCTION----------------------------------------------------#

# def function_name(parameters):
# opertions
# return
# function_name(argument)

# BASICS 

# def hello():
#     print("hello") 
#     return "hello"

# x=hello()
# print(x)
# print(hello())

# QUES 1. PRINT N NATURAL NUMBERS.

# def naturalno(n):
#     for i in range(1,n+1):
#         print(i)

# n=int(input())
# naturalno(n)


# QUES 2. PRINT N EVEN NUMBERS.

# def naturalno(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)

# n=int(input())
# naturalno(n)


# QUES 3. PRINT SUM OF N NATURAL NUMBERS.

# def naturalno(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     return sum

# n=int(input())
# x=naturalno(n)
# print(x)


# QUES 4. PRINT SUM OF EVEN  NUMBERS.

# def naturalno(n):
#     sum=0
#     for i in range(1,n+1):
#         if i%2==0:
#             sum=sum+i
#     return sum

# n=int(input())
# x=naturalno(n)
# print(x)


# QUES 5. PRINT SUM OF N NATURAL NUMBERS.


# def naturalno(n):
#     sum=0
#     for i in range(1,n+1):
#         if i%2!=0:
#             sum=sum+i
#     return sum

# n=int(input())
# ans=naturalno(n)
# print(ans)


# QUES 6. FACTORIAL OF A NUMBER.

# def fact(n):
#     for i in range(1,n+1):
#         ans=n*(n-1)
#     return ans


        

# n=int(input())
# ans = fact(n)
# print(ans)


def checkleap(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        print("leap year")
    else:
        print("Not a leap year")    

n=int(input())
checkleap(n)