* Get Squares of all elements in the list
```python
l = list(range(1, 11))

l2 = [] # Conventional loop
for i in l:
    l2.append(i)
print(l2)

l2 = [i * i for i in l]
print(l2)
```
* Sum of Squares of list of integers
```python
s1 = sum(l)
print(s1)

s2 = sum([i * i for i in l])
print(s2)
```
* Compute total sale amount from list of tuples
```python
sales = [
    (1, 101, 500.00, 5),
    (2, 102, 250.00, 3),
    (3, 103, 1000.00, 8),
    (4, 104, 750.00, None),
    (5, 101, 300.00, -1),
    (6, 106, 400.00, 3),
    (7, 104, 200.00, 0),
    (8, 103, 150.00, 1),
    (9, 104, 600.00, 4),
    (10, 101, 800.00, 6)
]
sale_amount = sum([sale[2] for sale in sales])
print(sale_amount)
```