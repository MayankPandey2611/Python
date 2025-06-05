# GENERATOR  => IT USED TO GENERATE THE COLLECTION.

def natural_no(n):
    i=1
    while i<=n:
        yield i
        i=i+1
n=int(input())

x=natural_no(n)

# for i in x:
#     print(i)

print(next(x))
print('hello')
print(next(x))