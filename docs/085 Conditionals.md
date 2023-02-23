* Develop logic to check whether the input value is integer or not.

```
n = input('Enter an integer: ')
if n.isdigit():
    print(f'{n} is an integer')
else:
    print(f'{n} is of type {type(n)}')
```

* Develop logic to checks whether an integer is even or odd.
```
n = 11 --Test with negative number or 0

if int(n) <= 0:
    print(f'{n} is not positive integer')
elif int(n) % 2 == 0:
    print(f'{n} is even integer')
else:
    print(f'{n} is odd integer')
```