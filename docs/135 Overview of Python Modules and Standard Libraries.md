* Custom Modules

```python
# sales.py

def validate_commission_pct(commission_pct):
    if commission_pct and (commission_pct <= 0 or commission_pct > 100):
        return False
    return True


def get_commission_amount(sale_amount, commission_pct):
    if validate_commission_pct(commission_pct) == False:
        raise ValueError
    if commission_pct == None:
        return 0
    return ((sale_amount * commission_pct) / 100)


print(get_commission_amount(1500, 12))


def get_sales_revenue(sale_amount, commission_pct):
    if validate_commission_pct(commission_pct) == False:
        raise ValueError
    commission_amount = get_commission_amount(sale_amount, commission_pct)
    return sale_amount - commission_amount


print(get_sales_revenue(1500, 12))
print(f'Name is {__name__}')
```

* Using Custom Modules in other programs

```python
# app.py

import sales # prints the results based on print statements in sales.py
```

* Overview of main

```python
# sales.py

def validate_commission_pct(commission_pct):
    if commission_pct and (commission_pct <= 0 or commission_pct > 100):
        return False
    return True


def get_commission_amount(sale_amount, commission_pct):
    if validate_commission_pct(commission_pct) == False:
        raise ValueError
    if commission_pct == None:
        return 0
    return ((sale_amount * commission_pct) / 100)


def get_sales_revenue(sale_amount, commission_pct):
    if validate_commission_pct(commission_pct) == False:
        raise ValueError
    commission_amount = get_commission_amount(sale_amount, commission_pct)
    return sale_amount - commission_amount


if __name__ == '__main__':
    print(get_commission_amount(1500, 12))
    print(get_sales_revenue(1500, 12))
    print(f'Name is {__name__}')
```
* Best Practices to use functions in modules
  * Make sure to have only global variables, functions, etc in module.
  * Do not have any code snippets outside the functions and if condition related to main.
* Overview of standard libraries (libraries that are part of core python)
  * `datetime`
  * `functools`
  * `sys`
  * `os`
  * `glob`
  * `itertools`
  * `logging`
  * `unittest`
  * `csv`
  * `json`
  * `typing` (related to type hints)
* Overview of 3rd party libraries
  * `requests`
  * `flask`
  * `django`
  * `fastapi`
  * `pandas`
  * `pyspark`
  * `matplotlib`
  * `scikit`
  * `boto3` for AWS