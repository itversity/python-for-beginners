* Syntax for defining functions
* Overview of scoping using indentation
* Sum of integers from 1 to n

```
def sum_n(n):
    res = (n * (n + 1)) / 2
    return res

sum_n(5)
```

* Sum of integers from lower bound to upper bound

```
def sum_range(lb, ub):
    res_lb = sum_n(lb - 1)
    res_ub = sum_n(ub)
    return res_ub - res_lb

sum_range(4, 10)
```

* Exercise and Solution for User Defined Functions

Create a function by name my_add. It should accept 2 parameters and return the sum of the 2 parameters. Validate by invoking the function using 2 arguments.

```
def my_add(a, b):
    res = a + b
    return res

my_add(10, 20)
```
* Advantages of Type Hints
