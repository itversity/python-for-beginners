```
s = 'itversity inc'
type(s)
help(str)
print(dir(str))

# count i's in s
s.count('i')

# get location of first t
# we can use index or find
# if not found index returns ValueError while find returns -1
help(s.index)
s.index('i')

help(s.find)
s.find('i')

# Change the case
s = 'itversity inc'
print(s.upper())

s = 'ITVersity Inc'
print(s.lower())
print(s.swapcase())

# is functions
# check for lower
s = 'itversity inc'
s.islower()

# check for numbers
n = '100'
n.isdigit()

# check for alpha numeric
s = 'itversity inc'
s.isalnum()
n.isalnum()
s = 'itversity&inc'
s.isalnum()
```