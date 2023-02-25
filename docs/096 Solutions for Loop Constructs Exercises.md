Exercise 1: Get sum of all the numbers greater than 100 from the sorted list `[125, 115, 101, 100, 90, 80, 75]`.

Exercise 2: Print all the numbers which are divisible by both 2 and 3 between 1 and 100.

```python
l = [125, 115, 101, 100, 90, 80, 75]
i = 0
total = 0
while l[i] > 100:
    total += l[i]
    i += 1

print(total)
```

```python
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=' ')
```