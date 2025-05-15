
# 1. CONTINUE => IT SKIPS CURRENT ITERATION.

# n=int(input())
# i=1
# while i<=n:
#     if i==5:
#         i=i+1
#         continue
#     else:
#         print(i)
#     i=i+1


# 2. BREAK =>  IT USED TO TERMINATE THE WHOLE LOOP.

# n=int(input())
# i=1
# while i<=n:
#     if i==5:
#         break
#     else:
#         print(i)
#     i=i+1


# CALCULATOR USING BREAK STATEMENT.

# while True:
#     print(" 1. add \n 2. sub \n 3. div \n 4. off ")
#     n=int(input("enter any options: "))
#     x=(1,2,3,4)
#     if n in x:
#         if n==1: 
#             p=int(input("enter 1st value: ")) 
#             q=int(input("enter 2nd value: ")) 
#             print(p+q)
#         elif n==2:
#             p=int(input("enter 1st value: ")) 
#             q=int(input("enter 2nd value: ")) 
#             print(p-q)
#         elif n==3:
#             p=int(input("enter 1st value: ")) 
#             q=int(input("enter 2nd value: ")) 
#             print(p/q)
#         elif n==4:
#             break
#     else:
#         print("please enter valid option!")    


# HOTEL MENU TASK.

while True:
    print("1. veg \n 2. non-veg  \n ")
    n=int(input("select any option: "))
    x=(1,2)
    if n in x:
        if n==1:
            vegmenu = {' veg biryani':200 , 'dal-roti' :500 ,'normal-thali':800 }
            print(vegmenu)
            n=str(input("select an option: "))
            if n==vegmenu.keys():
                print(vegmenu.values())
            elif n==vegmenu.keys():
                print(vegmenu.get('dal-roti'))
            elif n==vegmenu.keys():
                print(vegmenu.get('normal-thali'))
            else:
                break
        elif n==2:
            nonvegmenu = {'chicken': 550 , 'fried chicken':1000 , 'egg':400}
            print(nonvegmenu)
            n=int(input("select an option: "))
            if n==nonvegmenu['chicken']:
                print(nonvegmenu.get('chicken'))
            elif n==nonvegmenu[" fried chicken"]:
                print(nonvegmenu.get('fried chicken'))
            elif n==nonvegmenu['egg']:
                print(nonvegmenu.get('egg'))
            else:
                break

    else:
        print("enter valid option!")

# 3. PASS => IT SKIPS CURRENT BLOCK.


# n=int(input())
# i=1
# while i<=n:
#     if i==5:
#         pass
#     else:
#         print(i)
#     i=i+1