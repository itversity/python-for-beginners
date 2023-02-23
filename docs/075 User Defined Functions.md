* Syntax for defining functions
* Overview of scoping using indentation
* Sum of integers from 1 to n
```python
def sum_n(n):
    res = (n * (n + 1)) / 2
    return res

sum_n(5)
```
* Sum of integers from lower bound to upper bound
```python
def sum_range(lb, ub):
    res_lb = sum_n(lb - 1)
    res_ub = sum_n(ub)
    return res_ub - res_lb

sum_range(4, 10)
```
* Overview of Parameters or Arguments
* Overview of return statement
* Common Pitfalls
```python
def sum_n(n):
    res = (n * (n + 1)) / 2
    print(res)

res = sum_n(4)
print(res) # Prints nothing
type(res) # None as there is no return statement (returns None by default)

def sum_n(n):
    res = (n * (n + 1)) / 2
    return print(res)

res = sum_n(4)
print(res) # Prints nothing
type(res) # None, as print in function sum_n returns None. 
```
* Advantages of Type Hints
* Exercise and Solution for User Defined Functions

Exercise 1: Create a function by name my_add. It should accept 2 parameters of type integer and return the sum of the 2 parameters. Validate by invoking the function using 2 arguments.

Exercise 2: Create a function by name sum_of_squares from 1 to n. It should accept 1 parameter of type integer and return the sum of squares from 1 to n. Use the relevant formula for the same. Validate by invoking the function using one argument.
Formulla: (n * (n + 1) * (2n + 1)) / 6

* Exercise 1: Solution
```python
def my_add(a, b):
    res = a + b
    return res

my_add(10, 20)
```

* Exercise 2: Solution
```python
def sum_of_squares(n):
    if n <= 0:
        raise ValueError
    res = (n * (n + 1) * ((2 * n) + 1)) / 6
    return res

sum_of_squares(4) # 30
```