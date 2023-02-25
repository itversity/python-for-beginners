* Develop a function to check if the number belongs to Fibonacci series or not.
```python
def is_fibonacci(n: int) -> bool:
    if n < 0 or type(n) != int:
        raise ValueError 
    fib_base1 = 0
    fib_base2 = 1
    fib = fib_base1
    while fib < n:
        fib = fib_base2
        fib_base2 += fib_base1
        fib_base1 = fib 

    return fib == n

is_fibonacci(-10)

for i in range(1, 11):
    print(i)
    print(f'{i} is Fibonacci: {is_fibonacci(i)})') 
```
* Print Fibonacci series up to n
```python
for i in range(1, 11):
    if is_fibonacci(i):
        print(i, end=' ')
```
* Check if given number n is prime or not

```python
import math

def is_prime(n: int) -> bool:
    if n < 0 or type(n) != int:
        raise ValueError 

    if (n != 2 and n % 2 == 0) or n in (0, 1):
        return False
    
    if n == 3 or n == 2:
        return True
    
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
* Print multiplication table for given n up to 10.
```python
def mul_table(n, t=10):
    if n < 0 or type(n) != int:
        raise ValueError 
    for i in range(1, t + 1):
        print(f'{n} * {i} = {n * i}')

mul_table(5)
```