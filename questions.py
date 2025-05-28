
# num=int(input('enter the number'))

# ans=str(num)
# print(ans[0])
# print(ans[-1])

# QUES 1. ASCENTING ORDER.

l=[2,1,3,4,1,3,5]


for i in range(0,6):
    if(i<i+1):
        l[i],l[i+1]=l[i+1],l[i]
     

print(l)