# FILE HANDLING =>

# TWO TYPES OF FORMAT => TEXT AND BINARY.

# f=open('n2.txt' , 'x')
# f=open('w1.txt' , 'w')

# f=open('n2.txt' , 'r') #(DEFAULT MODE)
# f=open('n2.py', 'a')

# f=open('n2.txt', 'a')

# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f.write('this is python/n')
# f.write(''' 
#         n=int(input("enter any number" : )
#         i=0
#         while i<=n:
#             print(i)
#             i=i+1)
#         ''')

# f.writelines('this is python','this is java ')

# l=['this is pyhton \n' , 'this is java \n']
# f.writelines(l)


# READ MODE 
# f=open('n2.txt')

# data= f.read()
# print(data)


# f.close()



# f=open('n2.txt')

# data= f.read(9)
# print(data)
# f.close()

# f=open('n2.txt')

# data= f.readlines()  # ITS OUTPUT DATATYPE IS LIST.
# print(data)


# f.close()




# CHECK CURSOR CURRENT POSITION USING TELL METHOD.

# f=open('n2.txt')

# print(f.tell())
# data= f.read(10)
# print(data)
# print(f.tell())

# f.close()

# f=open('n5.txt','x')
# f=open('n5.txt','w')
# f=open('n5.txt','r')
# f=open('n5.txt','a')
# print(f.tell())



# CURSOR MOVEMENT USING SEEK('where to move' , 'from where ') METHOD 

f=open('n2.txt','rb')

print(f.tell())
data= f.read(10)
print(data)
# f.seek(5,1)  # from current position.
f.seek(-5,2)  # from last position.
print(f.tell())
data= f.read(5)
print(data)

f.close()