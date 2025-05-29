
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

n = int(input('enter no. of rows'))

for i in range(1,n+1):
    ch='A'
    for j in range(1,n+1):
        print(ch,end='')
        ch=chr(ord(ch)+1)
    print()    