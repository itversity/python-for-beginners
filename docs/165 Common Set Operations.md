* Create a set
```python
s = {1, 3, 2, 4, 3, 1, 5, 6}
```
* Add elements to the set
```python
s.add(1)
s.add(7)
```
* Check if the element exists in the set
```python
1 in s
10 in s
```
* Remove elements from the set
```python
s.pop()
s.remove(2)
s.remove(10)
```
* Perform set operations
```python
evens = set(range(2, 21, 2))
odds = set(range(3, 21, 3))
ints = set(range(1, 21))
evens.union(odds)
evens.intersection(odds)
evens.issubset(ints)
odds.issubset(evens)

evens.difference(odds)
odds.difference(evens)
```
* Convert list to set
```python
l = [1, 3, 2, 4, 3, 1, 5, 6]
len(l)

set(l) # Eliminates duplicates
len(set(l))
```
* Convert set to list
```python
s = {1, 2, 3, 4}
list(s)
```
* Exercise 1: Get unique characters from a string - `itversity inc`
* Exercise 2: Get common elements from 2 lists as a set.
```python
l1 = [2, 4, 6, 8, 10, 12]
l2 = [3, 6, 9, 12]

# output - {6, 12}
```
* Exercise 3: Get all unique elements from 2 lists as a set.
```python
l1 = [2, 4, 6, 8]
l2 = [3, 6, 9]

# output - {2, 3, 4, 6, 8, 9}
```