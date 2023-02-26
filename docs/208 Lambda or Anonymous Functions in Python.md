* Overview of lambda functions
* Develop a function to compute some of integers in a list
```python
def sum_of_integers(l):
    total = 0
    for i in l:
        total += i
    return total

sum_of_integers([1, 2, 4, 3, 1])
```
* Develop a function to compute sum of squares of integers in a list
```python
def sum_of_squares(l):
    total = 0
    for i in l:
        total += (i * i)
    return total

sum_of_squares([1, 2, 4, 3, 1])
```
* Develop a function to compute sum of commission amounts from a list where each element is a tuple which contain **sale amount** and **commission %**.
```python
def get_commission_amount(l):
    total = 0
    for i in l:
        total += ((i[0] * i[1]) / 100)
    return total

get_commission_amount([(1000, 15), (1200, 20), (1000, 12)])
```
* Switch to one function **my_sum** and invoke using lambda functions.
```python
def my_sum(l, f):
    total = 0
    for i in l:
        total += f(i)
    return total

my_sum([1, 2, 4, 3, 1], lambda i: i)
my_sum([1, 2, 4, 3, 1], lambda i: i * i)
my_sum([(1000, 15), (1200, 20), (1000, 12)], lambda i: ((i[0] * i[1]) / 100))
```
* Advantages of lambda functions
* Usage of lambda functions
* Example of `filter` function
```python
l = [1, 2, 4, 3, 1]
filter(lambda i: i % 2 == 0, l)
list(filter(lambda i: i % 2 == 0, l))
```
* Example of `map` function
```python
l = [1, 2, 4, 3, 1]
map(lambda i: i ** 2, l)
list(map(lambda i: i ** 2, l))
```