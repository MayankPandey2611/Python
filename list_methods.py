#-------------------------------------------------LIST METHODS---------------------------------------------------------------------#
# 1. APPEND() => IT ADDS IN LAST POSITION.
# 2. EXTEND() => IT ALSO ADDS IN LAST POSITION.
# 3. INSERT() => IT ADDS IN TARGETED POSITION.
# 4. POP() => IT REMOVES THE LAST ELEMENT.
# 5. REMOVE() => IT REMOVES THE TARGETED ELEMENT.
# 6. INDEX() => IT USED TO FIND OUT THE INDEX NUMBER OF THE ELEMENT.
# 7. COUNT() => IT USED TO COUNT THE NUMBER OF GIVEN ELEMENT.
# 8. REVERSE() => IT USED TO REVERSE THE LIST.
# 9. SORT() => IT USED TO SORT THE LIST OF SAME DATATYPES ELEMENT.
# 10. COPY() => IT USED TO COPY THE LIST .
# 10. CLEAR() => IT USED TO COPY THE LIST .

#-------APPEND-----------#
# l=[1,2,3,4,5]
# l1=[12,34,'PYTHON']
# l.append(l1)
# print(l)

#-------EXTEND-----------#
# t=(10,20,30)
# l2=[12,34]
# s='python'
# # l.extend(10,20)  # ITS SHOWS ERROR.
# # l.extend(l1)
# print(l)

# -----INSERT----------#
# l3 =[1,2,3,4,5]
# l3.insert(0,'python')
# l3.insert(1,['php','java'])
# print(l3)


#-------POP-----------#
# l=[1,2,3,4,5]
# print(l.pop())
# print(l)


#------REMOVE--------#
# l=[1,2,3,45,50]
# l.remove(45)
# print(l)

#------INDEX---------#
# l=[1,2,3,4,5]
# # print(l.index(2,2))
# print(l.index(2))


#------COUNT----------#
# l=[1,2,3,4,5,5]
# print(l.count(5))


#------REVERSE---------#
# l=[1,2,3,4,5]
# l.reverse()
# print(l)
# print(l.reverse())


#-------SORT---------#
# l=['a','pk','java','ba','lk']
# # FOR ASCENTING ORDER
# l.sort()
# # FOR DECENTING ORDER
# l.sort(reverse=True)
# print(l)

#--------COPY-------#
# l=[1,2,34,5,6,7]
# l1=l.copy()
# print(id(l),id(l1))


#--------CLEAR--------#
# l=[1,2,34,5,6,7]
# l.clear()
# print(l)
# del l  # USED FOR DELETING THE EMPTY LIST.
# print(id(l))