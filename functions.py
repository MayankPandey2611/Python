
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
#     ans=1
#     for i in range(1,n+1):
#         ans=ans*i
#     return ans

# n=int(input())
# ans = fact(n)
# print(ans)


# QUES 7. CHECK LEAP YEAR.

# def checkleap(year):
#     if(year%4==0 and year%100!=0 or year%400==0):
#         print("leap year")
#     else:
#         print("Not a leap year")    

# n=int(input())
# checkleap(n)


# QUES 8. FACTOR OF A NUMBER.

# def factor(n):
#         i=1
#         while i<=n:
#             if n%i==0:
#                 print(i,end=' ')  
#             i=i+1
# n=int(input())
# factor(n)


# QUES 9. CHECK PALINDROME.

# def cp(n):
#     a=n
#     rev =0
#     while n>0:
#         d=n%10
#         rev = rev * 10 +d
#         n=n//10
#     if a==rev:
#         print("palindrome")
#     else:
#         print("Not a palindrome")    

# n=int(input())
# cp(n)

# QUES 10. CHECK ARMSTRONG

# def arm(n):
#     x=y=n
#     digit = 0
#     sum =0
#     while n>0:
#         digit = digit +1
#         n=n//10


#     while x>0:
#         ld = x%10
#         sum = sum +ld**digit
#         x=x//10


#     if y==sum:
#         print(f'given no {y} is armstrong number.')
#     else:
#         print(f'given no {y} is not a armstrong.')        

# n=int(input())
# arm(n)


# QUES 11. FIBONACCI SERIES.

# def fib(n):
#     x,y=0,1
#     i=1
#     print(x,end="," )
#     print(y,end="," )
#     while i<=n:
#         z=x+y
#         if i<n:
#             print(z , end=',')
#         else:
#             print(z , end=' ')
#         x,y=y,z
#         i=i+1

# n=int(input())
# fib(n)
