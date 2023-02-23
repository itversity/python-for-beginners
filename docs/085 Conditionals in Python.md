* Develop logic to check whether the input value is integer or not.

```python
n = input('Enter an integer: ')
if n.isdigit():
    print(f'{n} is an integer')
else:
    print(f'{n} is of type {type(n)}')
```
* Develop logic to checks whether an integer is even or odd.
```python
n = 11 --Test with negative number or 0

if int(n) <= 0:
    print(f'{n} is not positive integer')
elif int(n) % 2 == 0:
    print(f'{n} is even integer')
else:
    print(f'{n} is odd integer')
```
* Check if string is palindrome or not.
```python
s = input('Enter a string: ')

if s == None or s == '':
    print('String is empty')
elif list(reversed(s)) != list(s):
    print(f'{s} is not a palindrome')
else:
    print(f'{s} is a palindrome')
```
* Ternary Operator or single like if else

```python
n = 10
True if n % 2 == 0 else False
```
* Exercise - Conditionals
Accept an integer value using input and assign to variable by name year. If year is negative or 0 print "Entered year {year} is invalid", if year is positive apply below logic to determine leap year. If it is leap year print "Entered year {year} is leap year", if not print "Entered year {year} is not leap year".

Leap Year Formulla: 
To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not. 2024, 2028, 2032 and 2036 are all leap years.

```python
year = int(input('Enter year to check if it is leap year: '))

if year <= 0:
    print(f'Entered year {year} is invalid')
elif year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(f'Entered year {year} is not leap year')
else:
    print(f'Entered year {year} is leap year')
```