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