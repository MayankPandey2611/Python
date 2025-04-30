

# n=int(input())
# for i in range(1,n,1):
#  print(i)


#--------------------------------------------------------------LINEAR SEARCH------------------------------------------------------#

# def linearsearch(n,arr,key):
#     for i in range(0,n,1):
#         if(arr[i]==key):
#             return True
#     return False
    

# n = 5
# arr = [1,2,3,4,5]
# key = int(input())
# print(linearsearch(n,arr,key))


#----------------------------------------------------SWAPPING TWO NUMBERS WITHOUT USING THIRD VARIABLE-------------------------#

# a=5
# b=6
# a=a+b
# b=a-b
# a=a-b
# print(a,b)



arr=[1,2,3,4,5]
i=0
j=0

while i< len(arr) and j< len(arr):
    if i>=j:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    i+=1
    j+=1

print(arr)
        
   

   




