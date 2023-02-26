* Develop a function to check if the positive integer belongs to Fibonacci series or not.
  * Raise `ValueError` exception with message "Invalid Value" if the argument passed is not valid positive integer.
```python
def is_fibonacci(n: int) -> bool:
    if n < 0 or type(n) != int:
        raise ValueError('Invalid Number') 
    fib1 = 0
    fib2 = 1
    fib = fib1
    while fib < n:
        fib = fib2
        fib2 += fib1
        fib1 = fib 

    return fib == n

is_fibonacci(-10)

for i in range(1, 11):
    print(i)
    print(f'{i} is Fibonacci: {is_fibonacci(i)})') 
```
* Print Fibonacci numbers between 1 to n
```python
for i in range(1, 11):
    if is_fibonacci(i):
        print(i, end=' ')
```
* Develop a function to check if given positive integer n is prime or not
  * Raise `ValueError` exception with message "Invalid Value" if the argument passed is not valid positive integer.
```python
import math

def is_prime(n: int) -> bool:
    if n < 0 or type(n) != int:
        raise ValueError('Invalid Number') 

    if (n != 2 and n % 2 == 0) or n in (0, 1):
        return False
    
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

print(is_prime(7))
print(is_prime(9))
```
* Print Prime Numbers up to n
```python
for i in range(1, 101):
    if is_prime(i):
        print(i, end=' ')
```
* Develop a function to print multiplication table for given positive integer n from 1 up to 10.
  * Raise `ValueError` exception with message "Invalid Value" if the argument passed is not valid positive integer.
```python
def mul_table(n, t=10):
    if n < 0 or type(n) != int:
        raise ValueError('Invalid Number') 
    for i in range(1, t + 1):
        print(f'{n} * {i} = {n * i}')

mul_table(5)
```
