# FILE HANDLING =>

# TWO TYPES OF FORMAT => TEXT AND BINARY.

# f=open('n2.txt' , 'x')
# f=open('w1.txt' , 'w')

f=open('n2.txt' , 'r') #(DEFAULT MODE)
f=open('n2.txt', 'a')

print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.encoding)
print(f.closed)