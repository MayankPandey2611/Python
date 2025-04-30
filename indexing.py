#INDEXING => IT GIVES THE POSITION OF THE ELEMENT FROM THE ORDERED COLLECTION.

#-------------------- SYNTAX OF INDEXING-----------------------# 
#  1. collection.index("element",start , stop)
#  2. collection.index("element")
#  3. collection.index("element", start)

#--------------------ORDERED COLLECTION------------------------#

#--------------1. STRING---------------------------#

# s="I LOVE PYTHON"
# print(s.index("E"))
# print(s.index("E",6))
# print(s.index("E",2,5))
# print(s.index("E",2,6))

#-----------------2. LIST-------------------------#

l=[10,20,'python',40,50]
print(l.index('python'))
# print(l.index('p',0,5))
# print(l.index('p',0))


#-----------------3. TUPLE-------------------------#