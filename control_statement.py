# ----------------------------------------------CONTROL STATEMENTS-------------------------------------------------------------#

# 1. CONDITIONAL STATEMENT =>
#  IF STATEMENT
#  IF-ELSE STATEMENT
#  IF-ELIF STATEMENT
#  IF-ELIF-ELSE STATEMENT

# 2. ITERATIVE / LOOPING STATEMENT =>
# WHILE
# FOR


# 3. TRANSFORM STATEMENT =>
# CONTINUE
# BREAK
# PASS

# ------------------------------------------------SYNTAX--------------------------------------------------------------------------#

# IF SYNTAX

# n = int(input("enter a number: "))
# if n%2==0:
#     print(f'given number {n} is even')
   



# IF-ELSE SYNTAX

# n = int(input("enter a number: "))
# if n%2==0:
#     print(f'given number {n} is even')
# else:
#     print(f'given number {n} is odd')     
    

# IF-ELIF-ELSE SYNTAX

# a,b,c=int(input("enter a: ")),int(input("enter b: ")),int(input("enter c: "))


# if(a>b and a>c):
#     print(f'{a} is a greater number')
# elif(b>a and b>c):
#     print(f'{b} is a greater number')  
# elif(a==b and a==c):
#     print(f'all {a,b,c} are same')    
# else:
#     print(f'{c} is a greater number')      


# year = int(input("enter the year: "))

# if(year%4==0 and year%100!=0 or year%400==0):
#     print(f'given year {year} is a leap year.')   
# else:
#     print(f'given year {year} is not a leap year.')    



#-----------CALCULATE  DIVISIONS---------------#

# h,e,m = float(input("enter marks of hindi: ")),float(input("enter marks of english: ")),float(input("enter marks of maths: "))

# if(h>=0 and h<=100 and e>=0 and e<=100 and m>=0 and m<=100):
    
#     avg = (h+e+m)/3

#     if(avg>=60):
#         print(f'you got A grade.')

#     elif(avg>=45 and avg<=59):
#         print(f'you got B grade.')

#     elif(avg>=35 and avg<=44):
#         print(f'you got C grade.')

#     else:
#         print(f'you are falied.') 

# else:
#     print(f'entered marks are invalid.')


#-----------FIND DATATYPE OF INPUT---------------#

# n=eval(input("enter value: "))

# if(n>=0 or n<0):
#     print(f'{type(n)}')
# elif(n==a or ):
#     print(f'{type(n)}')
# else:
#     print(f'invalid input')



# DEFAULT SYNTAX OF PRINT (SEP=' ',END = '\N')

# print('hello' , end='\n')
# print('hello' , end=',')
# print('welcome')


# x=10
# y=20
# print(x,y,sep=',')


#-----------PRINT COUNTING---------------#

# n=int(input("enter number: "))
# i=1

# FIRST APPROACH
# while i<=n:
#     print(i)
#     i=i+1

# SECOND APPROACH
# sum=0
# while i<=n:
#     sum=sum+i
#     if i<=(n-1):
#         print(i,end=' + ')
#     else:
#         print(i,end=' = ')    
#     i=i+1
# print(sum)

# multi = 1
# while i<=n:
#     multi = multi*i
#     if i<=(n-1):
#         print(i,end='*')
#     else:
#         print(i,end='=')    
#     i=i+1    
# print(multi)    

# a=n
# fact =1
# while n>0:
#     fact=fact*n
#     n=n-1
# print(f'factorial of given number {a} is {fact}')    



#QUES(1). WAP TO PRINT N EVEN NATURAL NUMBER

# n=int(input("enter a number: "))
# i=2
# while i<=2*n:
#     if i%2==0 and i<(2*n-1):
#         print(i,end=',')
#     else:
#         print(i,end=' ')    
#     i=i+2    


#QUES(2). WAP TO PRINT EVEN NO UPTO N NATURAL NUMBER

# n=int(input("enter a number: "))
# i=2
# while i<=n:
#     if i%2==0 and i<(n-1):
#         print(i,end=',')
#     else:
#         print(i,end=' ')    
#     i=i+2


#QUES(3). WAP TO PRINT SUM OF N EVEN NUMBERS


# n=int(input("enter a number: "))
# i=2
# sum=0
# while i<=2*n:
#     sum=sum+i
#     if i%2==0 and i<(2*n-1):
#         print(i,end='+')
#     else:
#         print(i,end='=')    
#     i=i+2    
# print(sum)


#QUES(4). WAP TO PRINT SUM OF EVEN NO UPTO N NATURAL NUMBERS


# n=int(input("enter a number: "))
# i=2
# sum=0
# while i<=n:
#     sum=sum+i
#     if i%2==0 and i<(n-1):
#         print(i,end='+')
#     else:
#         print(i,end='=')    
#     i=i+2    
# print(sum)




#QUES(5). WAP TO PRINT N ODD  NATURAL NUMBER

# n=int(input("enter a number: "))
# i=1
# while i<=2*n:
#     if i%2!=0 and i<(2*n-1):
#         print(i,end=',')
#     else:
#         print(i,end=' ')    
#     i=i+2    



#QUES(6). WAP TO PRINT ODD NO UPTO N NATURAL NUMBER

# n=int(input("enter a number: "))
# i=1
# while i<=n:
#     if i%2!=0 and i<(n-1):
#         print(i,end=',')
#     else:
#         print(i,end=' ')    
#     i=i+2



#QUES(7). WAP TO PRINT SUM OF N ODD NUMBERS

# n=int(input("enter a number: "))
# i=1
# sum=0
# while i<=2*n:
#     sum=sum+i
#     if i%2!=0 and i<(2*n-1):
#         print(i,end='+')
#     else:
#         print(i,end='=')    
#     i=i+2    
# print(sum)


#QUES(8). WAP TO PRINT SUM OF ODD NO UPTO N NATURAL NUMBERS

# n=int(input("enter a number: "))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     if i%2!=0 and i<(n-1):
#         print(i,end='+')
#     else:
#         print(i,end='=')    
#     i=i+2    
# print(sum)


# QUES(9).  FABONACCI SERIES.

# n=int(input("enter no."))

# x,y=0,1
# i=1
# print(x,end="," )
# print(y,end="," )
# while i<=n:
#     z=x+y
#     if i<n:
#         print(z , end=',')
#     else:
#         print(z , end=' ')
#     x,y=y,z
#     i=i+1



# QUES(10). ARMSTRONG NUMBER.

# n=int(input("check no. "))
# x=y=n
# digit = 0
# sum =0
# while n>0:
#     digit = digit +1
#     n=n//10


# while x>0:
#     ld = x%10
#     sum = sum +ld**digit
#     x=x//10


# if y==sum:
#     print(f'given no is {y} armstrong number.')
# else:
#     print(f'given no is {y} not a armstrong.')        



# QUES(11). PALINDROME NUMBER

#1. USING INBULIT METHOD SLICE.
# n= input("enter no.")

# if n == n[::-1]:
#     print(f'given no {n} is a palindrome')
# else:
#     print(f'given no {n} is not a palindrome.')    

# 2. WITHOUT SLICING

n=int(input("enter no. "))

x=n
rev=0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n=n//10

if x == rev:
    print(f'yes')
else:
    print(f'no')        