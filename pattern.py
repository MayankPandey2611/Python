# PATTERN QUESTIONS

# QUES 1.
# n=5
# i=1

# while i<=n:
#     print('*' * n)
#     i=i+1

# QUES 2. 

# n=5
# i=1

# while i<=n:
#     print('*' * i)
#     i=i+1


# QUES 3. 

# n=5
# i=1

# while i<=n:
#     print(' '*(n-i)+'*' * i)
#     i=i+1


# QUES 4.

# n=5
# i=1

# while i<=n:
#     print(' '*(n-i)+'* ' * i)
#     i=i+1

# QUES 5. 

# n=5
# i=0

# while i<n:
#     print(' ' * i + '*' * (n-i) )
#     i=i+1


# QUES 6. 

# n=5
# i=0

# while i<n:
#     print(' ' * i + ' *' * (n-i) )
#     i=i+1


# QUES 7. 

# n=5

# while n>0:
#     print( '*' * n )
#     n=n-1

# QUES 8. 

# n=5
# i=0

# while i<n:
#     print( '*' * (n-i) + ' ' * i)
#     i=i+1
# i=i-2
# while i>=0:
#     print('*' * (n-i) + ' '* i)
#     i=i-1    


# QUES 9.

# n=5
# i=0

# while i<n:
#     print(  ' ' * i + ' *' * (n-i))
#     i=i+1
# i=i-2
# while i>=0:
#     print( ' ' * i + ' *' * (n-i))
#     i=i-1    



#-------------------------------------------PATTERN USING FOR LOOP----------------------------------------------------#

# QUES 1. 

# n=int(input())
# for i in range(1,n+1):
#     print('*' * i + ' ' * (n-i))


# QUES 2. 

# n=int(input())
# for i in range(1,n+1):
#     print(' ' * (n-i)+'*' * i )    


# QUES 3.


# n=int(input())
# for i in range(1,n+1):
#     print(' ' * (n-i)+ ' *' * i )    

# QUES 4.

# n=int(input())
# for i in range(n):
#     print(' ' * i+'*' * (n-i) )    

# QUES 5.

# n=int(input())
# for i in range(n):
#     print('* ' * (n-i)+' ' * i )    

# QUES 6.

# n=int(input())
# for i in range(n):
#     print(' ' * i +'* ' * (n-i))    


# QUES 7.

# n=int(input())
# for i in range(1,n+1):
#     print('*' * i +' ' * (n-i)) 
# for i in range(n-1,0,-1):
#     print('*' * i+ ' '*(n-i))   


#  QUES 8.

# n=int(input())
# for i in range(1,n+1):
#     print(' ' * (n-i)+'* ' * i ) 
# for i in range(n-1,0,-1):
#     print( ' '*(n-i)+'* ' * i )   


#  QUES 9.

# n=int(input())
# for i in range(0,n):
#     print('*' * (n-i) + ' ' * i)
# for i in range(2,n+1):
#     print('*' * i + ' '* (n-i) )    
  
# QUES 10.

# n=int(input())
# for i in range(0,n):
#     print( ' ' * i+'*' * (n-i) )
# for i in range(2,n+1):
#     print( ' '* (n-i)+'*' * i  )    
  

# QUES 11.

# n=int(input())
# for i in range(0,n):
#     print( ' ' * i+' *' * (n-i) )
# for i in range(2,n+1):
#     print( ' '* (n-i)+' *' * i  )    
  

# QUES 12.

# n=int(input())
# for i in range(1,n+1):
#     print('*' * i + ' '* (n-i) )
# for i in range(1,n):
#     print( ' '* i+'*' * (n-i) )    
  
# QUES 13. 

# n=int(input())
# for i in range(1,n+1):
#     print( ' '* (n-i)+'*' * i  )
# for i in range(1,n):
#     print( '*' * (n-i)+' '* i )    
  
# QUES 14.

# n=int(input())
# for i in range(1,n+1):
#     print( ' '* (n-i)+' *' * i  )
# for i in range(1,n):
#     print(' '* i + ' *' * (n-i))    
  

# QUES 15.

# n=int(input())
# for i in range (1,n+1):
#     print(' ' * i + ' *' * (n-i+1) + ' ' * i)