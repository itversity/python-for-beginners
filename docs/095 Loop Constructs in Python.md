* Overview of List and Range
```
l = [1, 4, 2, 5]

range(1, 10)
list(range(1, 10))
list(range(1, 10, 2))
```
* Print all the even numbers from a given Range
```
l = range(1, 11)
for n in l:
    print(f'{n} is even number')
```
* Print all the integers from a list of elements
```
l = [1000, 15.25, 'Hello', 225, None, 275]
for i in l:
    if type(i) == int:
        print(i)
```
* Overview of while loops (based on condition)
```
total = 0
cnt = 0
i = 5

while cnt < i:
    total += cnt
    cnt += 1

print(total)
```
* Print all above 100 from sorted list. The list should contain elements in descending order.
```
l = [125, 115, 101, 100, 90, 80, 75]
i = 0

while l[i] > 100:
    print(l[i])
    i += 1
```
* Add numbers until non number is entered. If the number is equal to 0, continue. If a non number is entered exit.
```
total = 0
while True:
    n = input('Enter positive integer to add and non positive integer to exit: ')
    if n.isdigit():
        if int(n) == 0:
            print(f'{n} is equal to 0 and hence continue without adding')
            continue
        total += int(n)
        print(f'Updated total after adding {n} is {total}')
    else:
        print('Breaking')
        break

print(total)
```