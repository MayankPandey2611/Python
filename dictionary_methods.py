#-----------------------------------------------DICTIONARY METHODS----------------------------------------------------------------#

# 1. COPY() => USED TO CREATE THE NEW OBJECT.
# 2. CLEAR() => USED TO REMOVE ALL THE PAIRS FROM THE DICTIONARY.
# 3. POP() => IT REMOVES THE TARGETED KEY FROM THE DICTIONARY.
# 4. POPITEM() => USED TO REMOVE THE LAST ELEMENT/ITEM FROM THE DICTIONARY.
# 5. GET() => USED TO GET VALUE OF TARGETED KEY.
# 6. KEYS() => USED TO COLLECT ALL THE KEYS FROM THE DICTIONARY.
# 7. VALUES() => USED TO GET THE VALUE FROM THE DICTIONARY.
# 8. ITEMS() => USED TO GET BOTH KEY AND VALUES FROM THE DICT.
# 9. FROMKEYS =>  IS ASSIGN SAME VALUE TO THE MULTIPLY KEYS.
# 9. SETDEFAULT() => IT WORKS ACCORDING TO THE VALUES OF DICTIONARY IF THE KEY IS EXISTED IN DICT THEN IT RETURNS THE DICT WITHOUR ADDING THE GIVEN KEY VALUE PAIR.
# 10. UPDATE() => IT UPDATES THE VALUES OF THE DICT WITH VALUES OF NEW DICT.


# d={'name':'mayank','age':'21','city':'bhopal'}

#------COPY()-------#
# d1 = d.copy()
# print(d , d1)
# print(id(d),id(d1))

#-----CLEAR()------
# d1.clear()
# print(d1)
# print(id(d1))
# del d1
# print(d1)

# -----POP()-------#
# d.pop('name')
# print(d)

#-----POPITEM()----#
# d.popitem()
# print(d)

#------GET()------#
# new=d.get('city')
# print(new)
# print(d.get('city'))


#------KEYS()-----#
# print(d.keys())

#-----VALUES()-----#
# print(d.values())

#-------ITEMS()-----#
# print(d.items())


#-----FROMKEYS()-----3

# s='python'
# d = dict.fromkeys(s)
# d = dict.fromkeys(s,10)
# print(d)


#------SETDEFAULT()------#
# d.setdefault('college', 'SIRT')
# print(d)


# ------UPDATE---------#
# d1={'x':10,'y':20}
# d.update(d1)
# print(d)


#-------------------------------------------CRUD OPERATIONS----------------------------------------------#
#----CREATE EMPTY DICt------#
d={}
#---ADD---#
# d['key'] = 'value'
# print(d)

# ----UPDATE--------#
d['key'] = 'newvalue'
print(d)

#-----GET / READ ------#
x=d['key']
print(x)

# ------DELETE--------#
d.pop('key')
print(d)