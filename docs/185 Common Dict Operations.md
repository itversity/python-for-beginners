* Create a dict
```python
sales = {
  1: 1000.50,
  2: 750.0,
  3: 800.0,
  4: 1250.0,
  5: 800.0
}
```
* Add elements to the dict
```python
sales[6] = 750.0
sales[2] = 775.0
sales.update({5: 810.0, 7: 1100}) # Update as well as add
```
* Updating existing element 
* Get number of elements in the dict
```python
len(sales)
```
* Check if the key exists in the dict
```python
1 in sales
10 in sales
```
* Get keys, values and items from the dict
```python
sales.keys()
sales.values()
sales.items()
```
* Access elements in the dict using key
```python
sales[1]
sales[10] # throws KeyError

sales.get(1)
sales.get(10) # returns None
```
* Remove elements from the dict
```python
help(sales.pop)
sales.pop(6)

help(sales.popitem)
sales.popitem()
```
* Exercise 1: Get unique list of values from a dict.
```python
d = {
    1: 100,
    2: None,
    3: 105,
    4: 100,
    5: 105
}
```
* Exercise 2: Get unique list of values which are not None. Use the above dict for the same.
* Solution for Exercise 1
```python
list(set(d.values()))
```
* Solution for Exercise 2
```python
l = []
for i in d.values():
  if i:
    l.append(i)

list(set(l))
```