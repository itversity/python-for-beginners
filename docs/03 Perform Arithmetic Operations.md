Here are the details related performing arithmetic operations using Python.
* Overview of Arithmetic Operations
* Adding or Multiplication of 2 or more integers
* Performing Multiple Arithmetic Operations following BODMAS Rule
* Assigning result to a variable and print
* Overview of input and print
* Exercise and Solution

## Overview of Arithmetic Operations
Here are the arithmetic operations typically we perform.
* Addition
* Subtraction
* Multiplication
* Division
* Power

## Adding or Multiplication of 2 or more integers

```
10 + 20
10 * 20
```

## Performing Multiple Arithmetic Operations

Let us perform multiple arithmetic operations using formula for getting sum of integers between 1 and 5.

```
(5 * (5 + 1)) / 2
```

## Assigning result to a variable and print

```
a = 10
b = 20

res_sum = a + b
print(res_sum)

res_mul = a * b
print(res_mul)

n = 5
sum_of_integers = (n * (n + 1)) / 2
print(sum_of_integers)
```

## Overview of input and print

```
a = input('Enter value for a: ')
b = input('Enter value for b: ')

res = a + b # Fails as a and b are of type strings
type(a)
type(b)

res = int(a) + int(b)

print(f'Sum of {a} and {b} is {res}')
```

## Exercise - Perform Arithmetic Operations
Here are the details for the exercise to compute sum of integers based on input value.
* Make sure to accept input for `n`.
* Compute sum of integers using formula `(n * (n + 1))/2`.
* Assign to a variable `res` and print.

```
n = int(input('Enter value for n: '))
res = (n * (n + 1)) / 2

print(f'Sum of integers up to {n} is {res}')
```