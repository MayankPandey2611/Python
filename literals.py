#-------------------------------------------------NATURE OF LITERALS----------------------------------------------------------#

# EX 1. GIVEN EXAMPLE IS IMMUTABLE / SAME (INTEGERS)
# x=10
# y=10
# print(id(x),id(y))


#EX 2. (DIFFERENT) LIST
# x=[]
# y=[]
# print(id(x),id(y))
# print(type(x),type(y))


#EX 3. (SAME) TUPLE
# x=()
# y=()
# print(id(x),id(y))
# print(type(x),type(y))

#EX 4. (SAME) STRING
# x=''
# y=''
# print(id(x),id(y))
# print(type(x),type(y))


#EX 5. (SAME) FLOAT
# x=10.5
# y=10.5
# print(id(x),id(y))
# print(type(x),type(y))


#EX 6. (DIFFERENT) DICTIONARY
# x={}
# y={}
# print(x,y)
# print(id(x),id(y))
# print(type(x),type(y))


# EX 7. (DIFFERENT) SET
# x={""}
# y={""}
# z=set()
# print(id(x),id(y))
# print(type(x),type(y))


# EX 8. (SAME)  FROZENSET

# x=frozenset()
# y=frozenset()
# print(id(x),id(y))
# print(type(x),type(y))

# EX 9. (SAME) COMPLEX

# x=complex(3,4)
# y=complex(4,3)
# print(id(x),id(y))
# print(type(x))


# EX 10. (SAME) BOOLEAN

# x=True
# y=True
# print(id(x),id(y))
# print(type(x))

