# TYPES OF FUNCTIONS 
# 1. MAP 
# SYNTAX => MAP(FUNCTION , COLLECTION)

# 1. LIST IN MAP
# l=[2,3,4,5,6]

# def sq(n):
#     return n*n
# x=map(sq,l)
# print(x)  #it prints address of the variable
# print(list(x))

# 2. TUPLE IN MAP
# t=(2,3,4,5,6)

# def sq(n):
#     return n*n
# x=map(sq,t)
# print(tuple(x))

# 3. STRING IN MAP
# s='mayank'
# def ascii(n):
#     x=chr(ord(n))
#     return x
# x=map(ascii,s)
# print(list(x))



# 2. FILTER 
# SYNTAX => FILTER(FUNNCTION , ITERABLE / COLLECTION)

# l=[2,1,3,4,5]

# def check(n):
#     if n>=3:
#         return True
# x=filter(check,l)
# print(list(x))    

# l=[10,9,7,5,3,12,16]

# def check(n):
#     if n%2==0:
#         return True
#     return False
# x=filter(check,l)
# print(list(x))

# 3. REDUCE  => IN THIS WE HAVE TO IMPORT THE REDUCE METHOD AND FUNCTOOLS
# SYNTAX => FUNCTOOLS.REDUCE(FINCTION , COLLECTION)  OR   REDUCE(FUNCTION , COLLECTION WITHOUT EXTRA VARIABLE)

# from functools import reduce
# def pro(x,y):
#     return x*y
# x=reduce(pro , [2,3,4,5])
# print(x)

# import functools
# l=[10,2,4,5,90]

# def gre(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# ans = functools.reduce(gre,l)
# print(ans)
    



# 4. LAMBDA => 
# SYNTAX => LAMBDA PARAMETERS : EXPRESSION 

# x = lambda a,b : a**b
# print(x(2,3))

# x = lambda a,b : print(a+b)
# x(34,10)


# l=[1,2,3,4,5]
# # MAP SYNTAX => MAP(FUNCTION , COLLECTION)
# print(list(map(lambda n :n**2 , l)))

# l1=[1,2,3,4]
# l2=[2,4,3,9,90,78]
# l3=[3,5,5,6,8]

# x= map(lambda p,q,r : p+q+r , l1,l2,l3)
# print(list(x))


# l = [12,2,3,43,1]

# # EVEN NUMBER 
# print(list(filter(lambda n : n%2==0 , l)))

# # ODD NUMBER
# print(list(filter(lambda n : n%2!=0 , l)))

# from functools import reduce 
# l=[1,23,4,2]
# ans= reduce(lambda x ,y : x+y ,l)
# print(ans)

# SYNTAX => LAMBDA VARIABLE : IF KA RESULT PHIR IF KI CONDITION ELSE ELSE KA RESULT.

# from functools import reduce 
# l=[1,2,3,9,89]
# x = reduce(lambda x,y : x if x<y  else y  ,l)
# print(x)


# DEFAULT DECLARATION   

# from functools import reduce 
# l = [1,2,3,4,5]
# print(reduce(lambda x,y : x+y , l , 10))