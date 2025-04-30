#-----------------------------------------------------STRIMG METHODS-----------------------------------------------------------------#
# 1. LOWERCASE = lower() => USED TO CONVERT THE NORMAL STRING INTO LOWERCASE.
# 2. UPPERCASE = upper() =>  USED TO CONVERT THE NORMAL STRING INTO UPPERCASE.
# 3. SWAPCASE = swapcase() =>  USED TO CONVERT THE LOWERCASE STRING INTO UPPERCASE OR UPPERCASE TO LOWERCASE.
# 4. CENTER = center()
# 5. TITLE = title() => USED TO CONVERT THE STRING FIRST LETTER INTO CAPITAL LETTER.
# 6. CAPITALIZE  = capitalize() => USED TO CAPITAL THE FIRST ALPHABET OF THE STRING.
# 7. SPLIT  = split() => IT BREAKS THE STRING INTO LIST FORM WITH SOME CONDITION IN THEIR SYNTAX.
# 8. JOIN  = join() => IT JOINS THE MULTIPLE STRING WITH SOME GIVEN SYMBOLS OR SIGNS.
# 9. COUNT  = count() => USED TO COUNT THE NUMBERS OF ALPHABETS OF THE STRING.
# 10. INDEX = index() => USED TO FIND THE PARTICULAR ELEMENT USING INDEXING.
# 11. FIND  = find() => USED TO FIND THE LETTERS OR ALPHABETS IN THE STRING.


s="this is python class"
s1=" of cybrom"
# -------1.---------#
# print(s.lower())

# -------2.---------#
# print(s.upper())

# -------3.---------#
# print(s.swapcase())

# -------4.---------#
# print(s.center(1))

# -------5.---------#
# print(s.title())

# -------6.---------#
# print(s.capitalize())

# -------7.---------#
# print(s.split('*'))

# -------8.---------#
# IN LIST FORM
# print(' '.join((s,s1)))

# IN TUPLE FORM
print(''.join([s,s1]))

# IN SET FORM
# print(' '.join({s,s1}))
# print(type(' '.join({s,s1})))

# -------9.---------#
# print(s.count('h'))

# -------10.---------#
# print(s.index('is'))

# IT SHOWS ERROR
# print(s.index('2'))

# -------11.---------#
# print(s.find("is"))