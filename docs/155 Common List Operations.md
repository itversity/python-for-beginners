* Create a list
* Append elements to the list
* Get number of elements in the list
* Check if the element exists in the list
* Get number of occurrences of an element in the list
* Access elements in the list using index or index range
* Remove elements from the list

```python
# Create a list
l = [1, 6, -1, 2, 1, 3]

# Append elements to the list
l.append(5)

# Get number of elements in the list
len(l)

# Check if the element exists in the list
1 in l # returns True
10 in l # returns False

# Get number of occurrences of an element in the list
l.count(1)

# Access elements in the list using index or index range
l[0] # First Element
l[-1] # Last Element
l[:3] # First 3 Elements
l[1:3] # Second element till 3rd element
l[-3:] # Last 3 elements

# Remove elements from the list
l.pop(1) # Removes 2nd element
l.remove(1) # Removes first occurrence of 1
```

* Exercise 1: Return list of Fibonacci numbers up to the positive integer entered. Use below code to check if the given number is a fibonacci number.
```python
def is_fibonacci(n: int) -> bool:
    if n < 0 or type(n) != int:
        raise ValueError('Invalid Number')
    fib_base1 = 0
    fib_base2 = 1
    fib = fib_base1
    while fib < n:
        fib = fib_base2
        fib_base2 += fib_base1
        fib_base1 = fib 
    return fib == n
```

* Exercise 2: Return list of Prime numbers up to the positive integer entered. Use below code to check if the given number is a prime number.
```python
import math

def is_prime(n: int) -> bool:
    if n < 0 or type(n) != int:
        raise ValueError('Invalid Number')
    if (n != 2 and n % 2 == 0) or n in (0, 1):
        return False
    if n == 3 or n == 2:
        return True
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
```

* Solution for Exercise 1
```python
def get_fibs(n=10):
    fibs = []
    for i in range(1, n + 1):
        if is_fibonacci(i):
            fibs.append(i)
    return fibs

get_fibs(100)
```

* Solution for Exercise 2:
```python
def get_primes(n=20):
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

get_primes(100)
```