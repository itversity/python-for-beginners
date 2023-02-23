* Print Fibonacci series up to n
```
def print_fibs(n: int) -> None:
    if n < 0:
        raise ValueError
    fib_base1 = 0
    fib_base2 = 1
    fib = fib_base1
    while fib <= n:
        print(fib, end=' ')
        fib = fib_base2
        fib_base2 += fib_base1
        fib_base1 = fib

print_fibs(100)
```
* Check if given number n is prime or not

```
import math

def is_prime(n: int) -> bool:
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

```
for i in range(1, 101):
    if is_prime(i):
        print(i, end=' ')
```
* Print multiplication table for given n up to 10