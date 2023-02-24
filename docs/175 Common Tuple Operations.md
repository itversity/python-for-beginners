* Create a tuple
* Check if the element exists in the tuple
* Get list of supported functions on the tuple
* Convert tuple to list
* Convert list to tuple
* Exercise 1: Get list of integers from a tuple.
```python
t = (1, 'Foo', 'Bar', 2, 1, 2, 3)
```
* Exercise 2: Get unique integers from a tuple. Use the above tuple.
* Solution for Exercise 1
```python
l = []
for i in t:
    if type(i) == int:
        l.append(i)

print(l)
```
* Solution for Exercise 2
```python
s = set()
for i in t:
    if type(i) == int:
        s.add(i)

print(s)
```