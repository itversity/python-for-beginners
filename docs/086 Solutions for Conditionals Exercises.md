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

if (type(n) == int and n > 0) and (n % 2 == 0 or n % 3 == 0):
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
