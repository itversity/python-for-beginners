* Create a dict
* Add elements to the dict
* Get number of elements in the dict
* Check if the key exists in the dict
* Get keys, values and items from the dict
* Access elements in the dict using key
* Remove elements from the dict
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