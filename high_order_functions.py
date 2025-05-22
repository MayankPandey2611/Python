# TYPES OF FUNCTIONS 
# 1. MAP 
# SYNTAX => MAP(FUNCTION , COLLECTION)




# 2. FILTER 
# 3. REDUCE 

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