#--------------------------------------------------STARTING OF PYTHON-----------------------------------------#

# x=input("name")
# print(x)

# print(type(x))
# print(max(x))
# print(min(x))


#--------------------------------------------------TOKENS TYPE IN PYTHON---------------------------------------#
# 1. KEYWORDS

# import keyword
# key = keyword.kwlist
# print(key)
# print(len(key))

# 2. SOFTKEYWORDS

# import keyword
# key = keyword.softkwlist
# print(key)
# print(len(key))


# 3. Punctuation (SPECIAL SYMBOLS)

# import string
# spe_symbols = string.punctuation
# print(spe_symbols)
# print(len(spe_symbols))



# ---------------------------------------------------SEQUENCELY COMPONENTS-----------------------------------#

# 1. LIST = COLLECTION OF SAME HOMOGENOUS AND HETROGENOUS ELEMENTS.

# l=[10,20,'python',10.5,['java','sql']]
# print(type(l))

# l1=[10,20,3,4,5]
# print(l1)
# print(type(l1))


# 2. TUPLE = COLLECTION OF SAME HOMOGENOUS AND HETROGENOUS ELEMENTS.

# t=(10,20,'ok',['html','css'])
# print(t)
# print(type(t))


# 3. DICTIONARY = COLLECTION OF ELEMENTS .(WHERE ELEMENTS DEPENDS ON  PAIR OF KEY VALUES)

# d = {'name':'mayank','age':21,'gender':'male'}
# print(type(d))





#----------------------------------------------------UNSEQUENCELY COMPONENTS--------------------------------------#

# 1.SET = COLLECTION OF UNIQUE/UNORDERED ELEMENTS.

# s = {10,20,10,20,"java","php","css"}
# print(s)
# print(type(s))

# 2. FROZENSET = IT USED TO FREEZE ANY COLLECTION.

# s1 = {10,20,10,20,"java","php","css"}
# x = frozenset(s1)
# print(x)
# print(type(x))

y = "python"
y = frozenset(y)
print(y)
print(type(y))