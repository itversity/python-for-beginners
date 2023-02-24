* Quick Revision of Boolean Type
* Conditional Operators
* Boolean Operations on Multiple Conditions
  * Boolean `or`
  * Boolean `and`
  * Evaluation order of Boolean Operations
```python
# Check if the number is positive and even
n = 10
n > 0 and n % 2 == 0
# Check if the number is even or divisible by 3
n = 5
n % 2 == 0 or n % 3 == 0
# Check if the number is positive and also either it is even or divisible by 3
n = -9
n > 0 and n % 2 == 0 or n % 3 == 0 # Returns True due to evaluation order
n > 0 and (n % 2 == 0 or n % 3 == 0) # Correct Solution
```
* Develop logic to check whether the number is positive or not.

```python
n = 10
if n >= 0:
    print(f'{n} is a positive number')
else:
    print(f'{n} is not a positive number')
```
* Develop logic to check whether the number is integer or not.
```python
n = 11 # Test with negative integer or 0

if type(n) == int:
    print(f'{n} is of type integer')
else:
    print(f'{n} is not a valid integer')
```
* Add logic to see if the integer is positive or not
```python
n = 11 # Test with negative integer or 0

if type(n) == int and n > 0:
    print(f'{n} is of type integer and positive')
else:
    print(f'{n} is not a valid integer')

if type(n) == int:
    print(f'{n} is of type integer')
    if n > 0:
        print(f'{n} is positive')
    else:
        print(f'{n} is negative')
else:
    print(f'{n} is not a valid integer')
```

* Check if string is palindrome or not.
```python
s = input('Enter a string: ')

list(s) # string will be converted to list
reversed(s) # creates reversed object
list(reversed(s)) # converts reversed object to list

list(reversed(s)) == list(s)

if s == None or s == '':
    print('String is empty')
elif list(reversed(s)) == list(s):
    print(f'{s} is a palindrome')
else:
    print(f'{s} is not a palindrome')
```
* Ternary Operator or single line if else

```python
n = 10
True if n % 2 == 0 else False
```
* Exercise 1 - Check if the number is positive integer and also if it is divisible by 2 or 3.
  * If all the conditions satisfy, print "{n} is positive integer and is divisible by 2 or 3"
  * If any of the conditions fail, print "{n} is not a valid number"
* Exercise 2 - Check whether candidate is "failed" or "just passed" or "passed with distinciton".
  * If score <= 50, failed
  * If score > 50 and score <= 80, "just passed"
  * Otherwise "passed with distinction"
* Exercise 3 - Leap Year
Accept an integer value using input and assign to variable by name year. If year is negative or 0 print "Entered year {year} is invalid", if year is positive apply below logic to determine leap year. If it is leap year print "Entered year {year} is leap year", if not print "Entered year {year} is not leap year".

Leap Year Formulla: 
To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not. 2024, 2028, 2032 and 2036 are all leap years.

* Solution for Exercise 1
```python
n = 11 # Test with negative integer or 0

if type(n) == int and (n % 2 == 0 or n % 3 == 0):
    print(f'{n} is positive integer and is divisible by 2 or 3')
else:
    print(f'{n} is not a valid number')
```
* Solution for Exercise 2
```python
score = 90

if score <= 50:
    print('failed')
elif score > 50 and score <= 80:
    print('just passed')
else:
    print('passed with distinct')
```
* Solution for Exercise 3
```python
year = int(input('Enter year to check if it is leap year: '))

if year <= 0:
    print(f'Entered year {year} is invalid')
elif year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(f'Entered year {year} is not leap year')
else:
    print(f'Entered year {year} is leap year')
```
