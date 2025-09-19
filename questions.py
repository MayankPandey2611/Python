
# num=int(input('enter the number'))

# ans=str(num)
# print(ans[0])
# print(ans[-1])

# QUES 1. ASCENTING ORDER.

# l=[2,1,3,4,1,3,5]

# n=len(l)
# i=0

# while i<n-1:
#     if(l[i]>l[i+1]):
#         l[i],l[i+1] = l[i+1],l[i]
#         i=0
#     else:
#         i+=1
# print(l)



# QUES 2. DESCENTING ORDER

# l=[2,0,1,0,8,0,1,0,2]
# n=len(l)
# i=0
# while i<n-1:
#     if(l[i]<l[i+1]):
#         l[i],l[i+1] = l[i+1],l[i]
#         i=0
#     else:
#         i+=1
# print(l)



# QUES 3. SWAP FIRST AND LAST CHARACTER.

# s='python'

# l=list(s)
# l[0],l[-1] = l[-1],l[0]
# s=''.join(l)
# print(s)


# QUES 4. SWAP FORST AND LAST DIGIT.

# n=12345
# s=str(n)
# s = s[-1] + s[1:-1] + s[0]
# n=int(s)
# print(n)



# QUES 5. MOVE ZEROS IN THE END.

# l=[1,23,0,21,0,9,0,9,0,8]

# l1=[]
# for i in l:
#     if i != 0:
#         l1.append(i)
# n=len(l) - len(l1)

# for i in range(n):
#     l1.append(0)
# print(l1)

#QUES 6. MOVE ODD NUMBERS IN THE END.

# l=[1,2,3,4,5,6,7,8,9,10]
# l1=[]

# for i in l:
#     if i%2==0:
#         l1.append(i)
# for i in l:
#     if i%2 !=0:
#         l1.append(i)
# print(l1)


# QUES 7. PERFECT NUMBER .

# n=int(input('enter number'))

# sum =0

# for i in range(1,n):
#     if n%i == 0:
#         sum+=i

# if n==sum:
#     print('perfect number')
# else:
#     print('not a perfect number')


# QUES 8. PATTERN 1.

# n = int(input('enter no. of rows'))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end='')
#     print()    

# QUES 9. PATTERN 2.

# n = int(input('enter no. of rows'))

# for i in range(1,n+1):
#     ch='A'
#     for j in range(1,i+1):
#         print(ch,end='')
#         ch=chr(ord(ch)+1)
#     print()    

# QUES 10. PATTERN 3.

# n = int(input('enter no. of rows'))

# for i in range(1,n+1):
#     ch='A'
#     for j in range(1,n+1):
#         print(ch,end='')
#         ch=chr(ord(ch)+1)
#     print()    




# TEST QUESTIONS

# def check(n):
#     if n%2==0:
#         print('even')
#     else:
#         print('odd')
# n= int(input())
# check(n)


# def fact(n):
#     res = 1
#     while n>=1:
#         res = res*n
#         n=n-1
#     return res
# n=int(input())
# print(fact(n))


# x=int(input())
# y=int(input())

# if x > y:
#     gre = x
# else:
#     gre = y 

# while(True):
#     if((gre % x ==0) and (gre % y ==0)):
#         lcm = gre
#         break
#     gre+=1

# print(lcm)


# x=int(input()) 
# y=int(input())

# if x>y:
#     small=x
# else:
#     small=y

# for i in range(1,small+1):
#     if( x % i == 0 and y % i ==0):
#         hcf = i
# print(hcf) 


# n = int(input())
# factors =[]
# for i in range(1,n+1):
#     if n%i==0:
#         factors.append(i)
# print(factors)    


# l=[2,1,98,0,89,6,500,45]
# n=len(l)
# max=l[0]
# for i in range(n-1):
#     if max < l[i+1]:
#         max=l[i+1]
#     else:
#         max=l[i]  
# print(max)


# l=[1,4,2,4,12,0,10]

# min = l[0]
# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         min= l[i]
#         l[i],l[i+1] = l[i+1],l[i]
#     else:
#         min=l[i+1]
# print(min)


# def nno(n):
#     for i in range(1,n+1):
#         if i<n:
#             print(i,end=",")
#         else:
#             print(i,end="")
# n=int(input())
# nno(n)

# TEST QUESTION 1.(a)

# l=[{"gfg":2 , "best":4},{"gfg":2}]

# # print(len(l[0]))

# max_i=0
# max_l=0

# for i in range(len(l)):
#     x=len(l[i])

#     if x>max_l:
#         max_i,max_l = i+1,x
# print(max_i)
# print(max_l)



# TEST QUESTION 1.(b)

# d={"a":2,"b":5,"c":"hello","d":9}

# key=int(input())

# l=[]

# for k,v in d.items():
    
#     if v>key:
#         l.append(k) 

# for i in l:
#     d.pop(i)
# print(d)



# s=str(input())


# reverse_s = s[::-1]

# if s==reverse_s:
#     print('Palindrome')
# else:
#     print('not a palindrome')



# l1=[1,2,3]
# l2=[4,5,6]

# d={}

# for i in range(len(l1)):
#     d[l1[i]] = l2[i]
# print(d)


# 1. 

# s=str(input())
# ans= s[::-1]
# print(ans)


# 2.

# s=str(input())

# rev_s=s[::-1]

# if s == rev_s:
#     print(True)
# else:
#     print(False)

# 3. 

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# n=int(input())
# ans=fact(n)
# print(ans)

# 4.

# s=str(input())
# a=s.lower()
# count=0

# vowels = "aeiou"

# for char in a:
#     if char in vowels:
#         count += 1
# print(count)

# 5. 

# l1=[1,3,4,6,10,8]
# max=l1[0]

# for i in range(len(l1)):
#     if (l1[i] > max):
#         max = l1[i]
# print(max)


# 6. 

# n=int(input())
# f=0
# s=1
# i=1
# while(i<=n):
#     print(f,end=' ')
#     nx=f+s
#     f=s
#     s=nx
#     i=i+1


# 7. 

# n=int(input())
# a=n
# m=a
# s=0
# while(n>0):
#     s+=1
#     n //= 10

# sum=0

# while(a>0):
#     d=a%10
#     sum += d**s
#     a //= 10
    
# if m == sum:
#     print('armastrong number')
# else:
#     print('not an armstrong')


# 8. 

# l=[1,1,2,3,3,4,5,6,7,8,8,8,9,9,9]
# s=set(l)
# l1=list(s)
# print(l1)


# 9. 

# d={'a':2 , 'b':1 , 'c':3}
# d1=dict(sorted(d.items(), key=lambda x : x[1]))
# print(d1)

# 10.  

# s=str(input())
# t=str(input())

# if len(s) != len(t):
#     print('Not an anagram !!')
# else:
#     if sorted(s) == sorted(t):
#         print('anagram !!')
#     else:
#         print('not an anagram !!')
    
# 11 . 

# l=[1,2,6,5,9,4,90,89,10,11,23,543]
# m=max(l)
# l.remove(m)
# print(max(l))

# 12. 

# arr=[1,2,4,6,8]
# n=len(arr)

# for i in range(n-1):
#     diff = arr[i+1] - arr[i]

#     if diff > 1:
#         for m in range(arr[i]+1 , arr[i+1]):
#             print(m)


# 13. FIRST METHOD.....


# n = int(input("Enter n: "))

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
    
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i+2) == 0:
#             return False
#         i += 6
#     return True

# for i in range(2, n+1):
#     if is_prime(i):
#         print(i, end=" ")


# 13. SECOND METHOD....

# n = int(input("Enter n: "))

# for i in range(2, n+1):
#     is_prime = True
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i, end=" ")



# 14. 

# arr=[2,3,4,5,6]
# t=int(input())
# n=len(arr)
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]+arr[j] == t:
#             print(i,j)


# 15. 

# def length(s:str)->int:
#     cset=set()
#     mlen=0
#     l=0

    
#     for right in range(len(s)):
#         while s[right] in cset:   
#             cset.remove(s[l])
#             l += 1
#         cset.add(s[right])
#         mlen = max(mlen, right - l + 1)

#     return mlen
# s=str(input())
# print(length(s))



# 16. 

# def flatten(l):
#     res=[]

#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res


# l=[[1,2],[3,4],[5,[6,7]]]

# print(flatten(l))



# 17.

# d1={'a':1}
# d2={'b':2}
# d1.update(d2)

# print(d1)


# 18. 

# n=int(input())
# l=[]
# for i in range(1,n+1):
#     l.append(i*i)
# print(l)


# 19. 

# from collections import Counter
# s=str(input())
# words=s.split()
# ans=Counter(words)
# print(dict(ans))


# 20. 

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()              # record start time
#         result = func(*args, **kwargs)   # run the function
#         end = time.time()                # record end time
#         print(f"{func.__name__} executed in {end - start:.6f} seconds")
#         return result
#     return wrapper

# @timer
# def slow_function():
#     total = 0
#     for i in range(10**6):
#         total += i
#     return total

# print(slow_function())

# 21. 

# l=[1,2,3,10,11,23,21]
# l1=[5,6,7,9,8,4]

# for i in range(len(l)):
#     if l[i] in l1:
#         print(l[i])
    
        
# 22.


# arr=[1,2,1,3,4]

# s=set()
# ans=set()

# for i in arr:
#     if i in s:
#         ans.add(i)
#     else:
#         s.add(i)
# print(list(ans))


# 23.

# l1=[1,3,2,4,6,2]
# stack=[]
# for i in l1:
#     stack.push(i)
# print(stack)

# 24. 

# l=[3,2,1,5,3,1]
# print(sorted(l,reverse=True))


# 25.

# import os

# print(os.path.isfile('eample.py'))


# 26. 
# s="madam"
# if s == s[::-1]:
#     print('palindrome')
# else:
#     print('not a palindrome')


# 27. 
# ans=",".join(["a","b","c"])
# print(ans)

# 28. 

# s="  mayank  "
# print(s.strip())



# 29.  

