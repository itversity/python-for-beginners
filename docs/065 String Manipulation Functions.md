* Define String type Variables
* Getting type and help
* Using count to find occurrences
* Find for a character or substring from main string
* Dealing with case of string such as lower case and upper case
* String validate functions which start with is
* Check if the string is integer

```python
s = 'itversity inc'
type(s)
help(str)
print(dir(str))

# count i's in s
s.count('i')

# count spaces in s
s.count(' ')

# get location of first i
# we can use index or find
# if not found index returns ValueError while find returns -1
help(s.index)
s.index('i')

help(s.find)
s.find('i')

# get location of first space
s.find(' ')

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
