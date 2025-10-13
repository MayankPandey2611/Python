
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

# L=[1,23,4]
# b=L
# b.append(5)
# print(L)

# def f(val,l=[]):
#     l.append(val)
#     return l
# print(f(10))
# print(f(10))
# print(f(10))
# print(f(10))

# x=(1,2,3)
# x[0]=10
# print(x)


# a = [[], []] * 2
# a[0].append(10)
# print(a)


# def f1():
#     return "A"
# def f2():
#     yield "B"

# print(type(f1()), type(f2()))


# x = [1, 2, 3]
# y = x
# y = y + [4, 5]
# print(x, y)


# x = (1, 2, [3, 4])
# x[2].append(5)
# print(x)


# for i in range(3):
#     print(i)
# else:
#     print("Done")


# s=str(input())
# s=s.lower()
# s=s.split()
# if s == s[::-1]:
#     print('p')
# else:
#     print('np')


# import re

# def is_palindrome(s):
#     s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#     return s == s[::-1]

# print(is_palindrome("A man, a plan, a canal: Panama"))  



#30. STRONG NUMBER......

# def fact(d):
#     if d <=1:
#         return 1 
#     return d*fact(d-1)

# n=int(input())

# a=n
# sum=0

# while(n>0):
#     d=n%10
#     d=fact(d)
#     sum = sum+d
#     n //= 10

# if a == sum:
#     print('strong number')
# else:
#     print('not a strong number')


#31. 

# from collections import Counter

# def maxf(arr):
#     freq=Counter(arr)
#     maxfr=max(freq.values())
#     ans=0
#     for c in freq.values():
#         if c == maxfr:
#             ans += c
#     return ans


# arr=[1,2,3,4,5]
# print(maxf(arr))



# 32.

# def findtarget(arr,t):
#     i=0
#     j=len(arr)-1

#     while(i <=j):
#         mid = (i+j)//2

#         if (arr[mid] == t):
#             return mid
        
#         if(arr[i] <= arr[mid]):
#             if(arr[i] <= t and t < arr[mid]):
#                 j = mid -1
#             else:
#                 i = mid +1
#         else:
#             if(arr[mid] < t and t <arr[j] ):
#                 i = mid +1
#             else:
#                 j = mid -1
#     return -1

# arr=[4,5,6,0,1,2,3]
# target=int(input())
# print(findtarget(arr,target))




# 33.

# def summaryrange(arr):
#     res = []
#     i =0
#     n = len(arr)
    
#     while i<n:
#         s = arr[i]

#         while i+1 < n and arr[i+1] == arr[i]+1:
#             i += 1
#         e=arr[i]

#         if s == e:
#             res.append(str(s))
#         else:
#             res.append(str(s) + "->" + str(e))
#         i += 1
#     return res


# arr=[0,1,2,4,5,6,8]
# print(summaryrange(arr))




# 34.

# METHOD 1......

# def intersection(nums1,nums2):
#     res=[]
#     i,j=0,0
#     nums1=sorted(nums1)
#     nums2=sorted(nums2)

#     while(i < len(nums1) and j < len(nums2)):
#         if(nums1[i] < nums2[j]):
#             i +=1
#         elif(nums1[i] > nums2[j]):
#             j += 1
#         else:
#             if(len(res) == 0 or res[-1] != nums1[i]):
#                 res.append(nums1[i])
#             i += 1
#             j += 1
#     return res





# nums1=[9,6,5,4]
# nums2=[4,9,9,0,7]

# print(intersection(nums1,nums2))


# METHOD 2.............

# def intersection(n1,n2):
#     return list(set(n1) & set(n2))

# print(intersection([9,8,2,4],[4,9,5]))



# 35.
# METHOD 1..........
# def thirdhighest(nums):
#     f = s = t = float('-inf')

#     for i in nums:
#         if i in(f,s,t):
#             continue
#         if i > f:
#             f,s,t = i,f,s
#         elif i > s:
#             s,t=i,s
#         elif i> t:
#             t=i
#     if t == float('-inf'):
#         return f
#     else:
#         return t



# METHOD 2..................

# def thirdhighest(nums):
#     nums=set(nums)

#     if len(nums) < 3:
#         return max(nums)
#     return sorted(nums,reverse=True)[2]
    
# nums=[0,5,0]
# print(thirdhighest(nums))


# 36. 

# def triangle(nums):
#     nums=sorted(nums)
#     n,count=len(nums),0

#     for c in range(n-1,1,-1):
#         a,b=0,c-1

#         while a<b:
#             if nums[a]+nums[b] > nums[c]:
#                 count += (b-a)
#                 b -=1
#             else:
#                 a += 1
#     return count



# nums=[2,2,3,4]
# print(triangle(nums))


# 37.

# def disapperingnumbers(nums):
#     n = len(nums)

#     for i in range(0,n):
#         idx = abs(nums[i])-1
#         if nums[idx] >0:
#             nums[idx] = -nums[idx]

#     res=[]
#     for j in range(0,n):
#         if nums[j] > 0:
#             res.append(j+1)
#     return res
   

# nums=[1,3,5,7,9,9,7,5,3]
# print(disapperingnumbers(nums))



# 38.

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"name : {self.name} , age : {self.age} ")

# obj = person("mayank" , 22)
# obj.show()
        

# 39. 

# import math
# class circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius
    
#     def cirum(self):
#         return 2 * math.pi * self.radius
    
# obj = circle(5)
# print(obj.area())
# print(obj.cirum())
        


# 40.

# class Student:
#     school_name="SIRT"
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#     def show(self):
#         print(f" name : {self.name} , rollno : {self.rollno} , from {Student.school_name}")

# obj = Student("mayank" , 96)
# obj.show()



# 41.

# class Bankaccount:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount
#         print(f"successfully deposits Rs.{amount} , New Balance is Rs . {self.balance}")

#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("insuffiencent balance !!")
#         elif amount <= 0:
#             print("Very less amount")
#         else:
#             self.balance -= amount
#             print(f"succssfully withdrawn Rs.{amount} , Avaliable Balance : {self.balance} ")
    
#     def check(self):
#         print(f"Balance : {self.balance}")


# obj = Bankaccount("mayank",500)
# obj.check()
# obj.deposit(500)
# obj.withdraw(300)
# obj.withdraw(100)



# 42.

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def get_tax(self,salary):
#         self.salary -= salary * 0.10

#         print(f"after detecting tax your salary is {self.salary}")

# obj= Employee("mayank",500)
# obj.get_tax(500)
        


# 43.

# class Animal:
#     def speak(self):
#         print("I am an Animal....")
# class Dog(Animal):
#     def speak(self):
#         print("baww baww !!")
# class Cat(Animal):
#     def  speak(self):
#         print("meww meww !!")
# obj = Animal()
# obj1 = Dog()
# obj2 = Cat()

# obj.speak()
# obj1.speak()
# obj2.speak()


# 44.


# class shoppingcart:
#     def __init__(self):
#         self.items={}

#     def additem(self,item,price):
#         self.items[item] = price
#         print(f"item added {item} -> {price}")
    
#     def removeitem(self,item):
#         if item in self.items:
#             del self.items[item]
#             print("item deleted !!")
#         else:
#             print(f"{item} not found in the cart !!")
    
#     def totalprice(self):
#         return sum(self.items.values())

# obj = shoppingcart()
# obj.additem("pants" , 1200)
# obj.additem("shirts",540)
# obj.removeitem("pats")
# print(obj.totalprice())
        
        
# 45.

# class Library:
#     def __init__(self):
#         self.books = []

#     def addbook(self,title):
#         self.books.append(title)
#         print(f"New Book {title} added in Library...")

#     def removebook(self,title):
#         if title in self.books:
#             self.books.remove(title)
#             print(f"{title} Successfully Deleted From Library....")
#         else:
#             print(f"Book name {title} not found in library...")
    
#     def display(self):
#         print(f"Here is List of Books {self.books}")


# obj = Library()
# obj.addbook("Harry Potter")
# obj.addbook("Ramayan")
# obj.addbook("ok jaanu")
# obj.addbook("mahabarat")
# obj.removebook("Harr Potter")
# obj.display()




# 46.

# class Math:
#     @staticmethod
#     def factorial(n):
#         res =1 
#         for i in range(1,n+1):
#             res *= i
#         return res
    
#     @classmethod
#     def square(cls,x):
#         return x*x
    
# print(Math.factorial(5))
# print(Math.square(5))
            

# 47.

# class Teacher:
#     def teach(self):
#         print("Teacher Teaches a Lesson.")
    
# class Student:
#     def study(self):
#         print("student learns the lesson.")

# class TeachingAssitant(Student,Teacher):
#     def show(self):
#         print("assitant teacher...")

# obj=TeachingAssitant()
# obj.teach()
# obj.study()
# obj.show()


# 48. Create a class MaxFinder that identifies the largest number in a list.

# class maxfinder:
#     def __init__(self,numbers):
#         self.numbers = numbers
    
#     def maxelement(self):
#         if not self.numbers:
#             return None
#         else:
#             return max(self.numbers)
        
# l=[1,43,2,56,7,8,0]
# obj=maxfinder(l)
# print(obj.maxelement())



# 49.  Last Digit in Words: Write a class with a method that takes an integer and prints the last digit of that
#  number in words.

# class numinwords:
#     d=['zero','one','two','three','four','five','six','seven','eight','nine']

#     def __init__(self,n):
#         self.n = n

#     def givelastd(self):
#         ld=abs(self.n) % 10
#         print(self.d[ld])
       
# obj=numinwords(50)
# obj.givelastd()


# 50. Student Grade Calculator: Implement a Student class with attributes for name and a list of
#  marks(for 5 subjects). Include a method to calculate the average and determine the grade.

# class Student:
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def findavg(self):
#         return sum (self.marks) / len(self.marks)

#     def findgrade(self):
        
#         avg = self.findavg()

#         if avg >=95 and avg <= 100:
#             print(f"grade of {self.name} is ' A+ '")
#         elif avg >= 85 and avg < 95 :
#             print(f"grade of {self.name} is ' A '")

#         elif avg >= 75 and avg < 85:
#             print(f"grade of {self.name} is ' B+ '")
#         elif avg >= 65 and avg < 75:
#             print(f"grade of {self.name} is ' B '")
#         elif avg >= 55 and avg < 65:
#             print(f"grade of {self.name} is ' C+ '")
#         elif avg >= 45 and avg < 55:
#             print(f"grade of {self.name} is ' C '")
#         elif avg >= 33 and avg < 45:
#             print(f"grade of {self.name} is ' D '")
#         else:
#             print(f"{self.name} is fail !!")

# l=[30,33,33,33,33]
# obj = Student('mayank',l)
# obj.findgrade()



# 51.  Define an abstract base class Polygon with an abstract method area. Implement this in derived
#  classes Rectangle and Triangle.

# from abc import ABC , abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Polygon):
#     def __init__(self,l,w):
#         self.l  = l
#         self.w  = w
    
#     def area(self):
#         return self.l * self.w

# class Triangle(Polygon):
#     def __init__(self,b,h):
#         self.b = b
#         self.h = h
    
#     def area(self):
#         return 0.5 * self.b * self.h

# obj1 = Rectangle(10,20)
# obj2 = Triangle(70,90)

# print(obj1.area())
# print(obj2.area())
        
        
# 52. Design a class that tracks how many objects have been created from it and has a method to display
#  this count

# class objectcounter:
#     count=0
#     def __init__(self):
#         objectcounter.count += 1

#     @classmethod
#     def display(cls):
#         print("No of Objects created is : " , cls.count)
        

# obj=objectcounter()
# obj1=objectcounter()
# obj2=objectcounter()
# obj3=objectcounter()
# obj4=objectcounter()
# obj5=objectcounter()
# obj6=objectcounter()
# obj7=objectcounter()
        
# objectcounter.display()


# 53.  Implement a class Account with a private attribute balance and provide methods to deposit and
#  withdraw safely, checking for sufficient funds.

# class Account:
#     def __init__(self,balance=0):
#         self.__balance = balance

#     def deposit(self,balance):
#         if balance > 0:
#             self.__balance += balance
#             print(f"Succfully Deposit Rs.{balance} , New Balance : {self.__balance} ")
#         else:
#             print("Amount should be positive !!")

#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("Insufficent Balance !!")
#         else:
#             self.__balance -= amount
#             print(f"Successfully Withdrawn Rs.{amount} , Remaining Fund is Rs.{self.__balance}")
    
#     def checkb(self):
#         print(f"Avaliable Amount is Rs. {self.__balance}")
        
# obj = Account()
# obj.deposit(1000)
# obj.withdraw(100)
# obj.checkb()
    


# 54. Static and Class Methods Demonstrate the use of static and class methods in a class Calculator
#  with methods to add and multiply numbers.

# class Calulator:
#     @staticmethod
#     def add(a,b):
#         return a+b
    
#     @classmethod
#     def multi(cls,a,b):
#         return a*b
    
# print(Calulator.add(2,1))
# print(Calulator.multi(2,5))

        

# 55.  Write a Python program to create a person class. Include attributes like name, country and date of
#  birth. Implement a method to determine the person's age.

# from datetime import datetime

# class Person:
#     def __init__(self,name,country,DOB):
#         self.name = name
#         self.country = country
#         self.DOB = datetime.strptime(DOB,"%Y-%M-%d")

#     def findage(self):
#         today = datetime.today()
#         age = today.year - self.DOB.year

#         if (today.month , today.day) < (self.DOB.month , self.DOB.day):
#             age -= 1
#         print(f"{self.name} Your current age is {age}")

# obj = Person('mayank','india','2018-08-11')
# obj.findage()
        

# 56. Write a Python program that checks if one class is a subclass of another.


# class Staff:
#     def __init__(self):
#         print("Staff")
    
# class Teacher(Staff):
#     def __init__(self):
#         print("Teacher(staff)")

# obj = Staff()
# print(issubclass(Staff,Teacher))
# print(issubclass(Teacher,Staff))
        

# 57.  Write a Python program that overloads the operator + and > for a custom class.

# class Box:
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height

#     def __add__(self, other):
#         return Box(self.length + other.length, self.width + other.width, self.height + other.height)
    
#     def __gt__(self, other):
#         return self.volume() > other.volume()
    
#     def volume(self):
#         return self.length * self.width * self.height
    
# def __str__(self):
#         return f"Box({self.length}, {self.width}, {self.height})"


# obj1 = Box(2, 3, 4)
# obj2 = Box(1, 2, 5)
# obj3 = obj1 + obj2
# print("After addition:", obj3)  

# if obj1 > obj2:
#     print("obj1 is bigger than obj2")
# else:
#     print("obj2 is bigger than or equal to obj1")



# 58.  1518. PROBLEM NUMBER (WATER BOTTLES EXCHANGE...)

# def drinkwater(bottles,exchange):
#     total = bottles
#     empty = bottles

#     while(empty >= exchange):
#         newB = empty // exchange
#         total += newB
#         empty = newB + (empty % exchange)

#     return total

# bottles=15
# exchange =4

# print(drinkwater(bottles,exchange))



# 59. MAXIMIMUM CONSECUTIVE ONES....

# def countones(nums):
#     size,maxsize=0,0

#     for i in range(len(nums)):
#         if nums[i] == 1:
#             size += 1
#             maxsize = max(maxsize,size)
#         else:
#             size = 0    
#     return maxsize

# nums=[1,1,0,1,1,1,0]
# print(countones(nums))



# 60.


# def maxbd(b : int,e:int)->int:
#     total = b
#     empty =b

#     while(empty >= e):
#         empty -= e
#         e += 1
#         total += 1
#         empty += 1
#     return total

# b=13
# e=6
# print(maxbd(b,e))


# 61. TEEMO ATTACKING....

# def findseconds(time,duration):
#     if not time:
#         return 0
    
#     total = 0

#     for i in range(1,len(time)):
#         total += min(time[i] - time[i-1] , duration)
#     return total + duration


# time=[1,2]
# duration = 2
# print(findseconds(time,duration))



# 62. FIND NEXT GREATER ELEMENT....

# def findgreater(num1,num2):
#     st=[]
#     greater={}
#     res=[]

#     for num in reversed(num2):
#         while st and st[-1] <=num:
#             st.pop()
#         greater[num] = st[-1] if st else -1
#         st.append(num)

#     return [greater[num] for num in num1]
    
 



# num1=[4,1,2]
# num2=[1,3,4,2]

# print(list(findgreater(num1,num2)))



# 63.  KEYWORD ROW ....


# def keywordrow(words):
    
#     ans =[]

#     r1=set("qwertyuiop")
#     r2=set("asdfghjkl")
#     r3=set("zxcvbnm")


#     for w in words:
#         lwords = set(w.lower())
#         if lwords <= r1 or lwords <= r2 or lwords <= r3:
#             ans.append(w)
#     return ans



# words = ["dadgkgd","kalaa","roqwertyuio"]
# print(list(keywordrow(words)))


# 64. ARRAY PARTITION.....

# def arraypartition(nums):
#     # METHOD 1...(OPTIMIZED)
#     # return sum(sorted(nums)[::2])

#     # METHOD 2...
#     nums.sort()
#     ans = 0
#     for i in range(0,len(nums),2):
#         ans += nums[i]
#     return ans



# nums=[6,1,2,2,5,6]
# print(arraypartition(nums))


# 65.  Minimum Index Sum of Two Lists

# def findcommon(l1,l2):
#     res=[]
#     index_map = {name: i for i, name in enumerate(l1)}
#     min_sum = float('inf')

#     for j,name in enumerate(l2):
#         if name in index_map:
#             s = j + index_map[name]
#             if s < min_sum:
#                 min_sum = s
#                 res=[name]
#             elif s== min_sum:
#                 res.append(name)
#     return res
 

# l1 = ["sad","happy","good"]
# l2 = ["happy","sad","good"]
# print(findcommon(l1,l2))


# 66. MAXIMUM PRODUCT OF THREE NUMBERS....

# def maxproduct(nums):
#     nums.sort()
#     n=len(nums)
#     return max(nums[n-1]*nums[n-2]*nums[n-3] , nums[0]*nums[1]*nums[n-1])

# nums=[-5,12,0,-1,-6,90]
# print(maxproduct(nums))


# 67. MAXIMUM AVERAGE SUBARRAY....

# def findmaxavg(nums,k):
#     sum =0
#     for i in range(k):
#         sum += nums[i]
#     maxsum = sum

#     for i in range(k,len(nums)):
#         sum += nums[i] - nums[i-k]
#         maxsum = max(maxsum,sum)
#     return maxsum / k

# nums=[5]
# k=1
# print(findmaxavg(nums,k))


# 68. MINIMUM COST OF CLIMBING STAIRS.........


# def mincost(cost):
#     n=len(cost)
#     s,e=0,0

#     for i in range(2,n+1):
#         c=min(s + cost[i-1] , e + cost[i-2])
#         e=s
#         s=c
#     return s

# cost = [10,15,20,1,0]
# print(mincost(cost))


# 69. HOUSE ROBBER....

# def maxmoney(nums):
#     n=len(nums)
#     if n==0: return 0
#     if n == 1: return nums[0]
#     if n ==2: return max(nums[0],nums[1])

#     e=nums[0]
#     s=max(nums[0],nums[1])
    
#     for i in range(2,n):
#         c=max(s,e+nums[i])
#         e=s
#         s=c
#     return s

# houses=[2,1,1,2]
# print(maxmoney(houses))



# 70.Successful Pairs of Spells and Potions

# def findpairs(s,p,success):
#     n=len(s)
#     m=len(p)
#     p.sort()
#     ans=list()

#     for i in range(0,n):
#         s1=s[i]
#         l=0
#         r=m-1
#         while l <= r:
#             mid = l + (r -l)//2
#             product = s1 * p[mid]
#             if product >= success:
#                 r=mid-1
#             else:
#                 l=mid+1

#         ans.append(m-l)
#     return ans

# s=[3,1,2]
# p=[8,5,8]
# success=16
# print(findpairs(s,p,success))


# 71. Longest Continuous Increasing Subsequence

# def findlongest(nums):
#     count = 1
#     maxc = 1

#     if len(nums) == 0:
#         return 0

#     for i in range(1,len(nums)):
#         if nums[i]  > nums[i-1]:
#             count += 1
#         else:
#             count =1
#         maxc= max(count,maxc)
#     return maxc

# nums=[2,5,7,1,4,6,9]
# print(findlongest(nums))


# 72. BASEBALL GAME..

# def points(op):
#     st=[]
    
#     for i in op:
#         if i == "C":
#             st.pop()
#         elif i == "D":
#             st.append(st[-1] * 2)
#         elif i == "+":
#             st.append(st[-1] + st[-2])
#         else:
#             st.append(int(i))
#     return sum(st)


# op = ["5","-2","4","C","D","9","+","+"]
# print(points(op))


# 73. find degree....

# def degree( nums):
#         freq = {}
#         first = {}
#         last = {}

#         for i, n in enumerate(nums):
#             if n not in freq:
#                 freq[n] = 0
#                 first[n] = i
#             freq[n] += 1
#             last[n] = i

#         degree = max(freq.values())
#         min_len = float('inf')

#         for n in freq:
#             if freq[n] == degree:
#                 min_len = min(min_len, last[n] - first[n] + 1)

#         return min_len

# nums=[1, 5, 2, 3, 5, 4, 5, 6]
# print(degree(nums))



# 74. 

# def notanagram(w):
#     def is_ana(s , t):
#         return sorted(s) == sorted(t)

#     ans=[]
#     for i in w:
#         if not ans or not is_ana(ans[-1] , i):
#             ans.append(i)
#     return ans


# words=["abba","baba","bbaa","cd","dc",""]
# print(list(notanagram(words)))
