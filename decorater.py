

def outer_func(main_func):
    def inner_func(p,q):
        p=p+5
        q=q+5
        ans= main_func(p,q)
        return ans
    return inner_func
@outer_func
def add(x,y):
    return x+y
# x=outer_func()
# print(x)
# z=x(10)
# print(z)

z=add(2,10)
print(z)