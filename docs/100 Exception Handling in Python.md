* Overview of Exceptions or Run Time Errors
* Pre-defined Exceptions
  * `ValueError`
  * `TypeError`
  * `KeyError`
* Raising Exception
```python
def sum_n(n):
    if type(n) != int or n <= 0:
        raise ValueError
    res = (n * (n + 1)) / 2
    return res


sum_n(10)
sum_n(-10)
```
* Raising Exception with Custom Message
```python
def sum_n(n):
    if type(n) != int or n <= 0:
        raise ValueError('Invalid Type or Value')
    res = (n * (n + 1)) / 2
    return res


sum_n(10)
sum_n(-10)
```
* Using `try` and `except` for general exception.
```python
def sum_n(n):
    try:
        res = (n * (n + 1)) / 2
        return res
    except:
        raise


sum_n('10')
```
* Handling Specific Exceptions
```python
def sum_n(n):
    try:
        if n <= 0 or type(n) != int:
            raise ValueError
        res = (n * (n + 1)) / 2
        return res
    except ValueError:
        print('Invalid Value')
    except TypeError:
        print('Invalid Type')
    return 0

n = '10'
print(f'Sum of integers up to {n} is {sum_n(n)}')

n = 10.5
print(f'Sum of integers up to {n} is {sum_n(n)}')
```
* Using `finally`
```python
def sum_n(n):
    try:
        if n <= 0 or type(n) != int:
            raise ValueError
        res = (n * (n + 1)) / 2
        return res
    except ValueError:
        print('Invalid Value')
    except TypeError:
        print('Invalid Type')
    finally:
        print('With or Without Exception or Error')
    return 0

n = '10'
print(f'Sum of integers up to {n} is {sum_n(n)}')

n = 10.5
print(f'Sum of integers up to {n} is {sum_n(n)}')
```
* Overview of Custom Exceptions
```python
class InvalidNumberError(Exception):
    pass

def sum_n(n):
    if type(n) != int or n <= 0:
        raise InvalidNumberError('Invalid Error')
    res = (n * (n + 1)) / 2
    return res

sum_n(10)
sum_n(-10)

def sum_n(n):
    try:
        if n <= 0 or type(n) != int:
            raise InvalidNumberError
        res = (n * (n + 1)) / 2
        return res
    except InvalidNumberError:
        print('Invalid Value')
    except TypeError:
        print('Invalid Type')
    finally:
        print('With or Without Exception or Error')
    return 0

n = '10'
print(f'Sum of integers up to {n} is {sum_n(n)}')

n = 10.5
print(f'Sum of integers up to {n} is {sum_n(n)}')
```
