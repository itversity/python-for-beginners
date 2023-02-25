* Overview of `sys`
* Reading arguments
```python
# sales.py
import sys

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


print(sys.argv)
args = sys.argv
print(get_commission_amount(int(args[1]), float(args[2])))   
print(get_sales_revenue(int(args[1]), float(args[2])))   
```
* Using `argparse`
```python
import argparse

parser = argparse.ArgumentParser(description='Enter Sale Amount and Commission %')
parser.add_argument('--sale_amount', type=int, default=1000,
                    help='Enter Sale Amount')
parser.add_argument('--commission_pct', type=float, default=10.0,
                    help='Enter Commission %')

args = parser.parse_args()
args.sale_amount
args.commission_pct
```
* Process arguments using `argparse`
```python
import argparse


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


parser = argparse.ArgumentParser(description='Enter Sale Amount and Commission %')
parser.add_argument('--sale_amount', type=int, default=1000,
                    help='Enter Sale Amount')
parser.add_argument('--commission_pct', type=float, default=10.0,
                    help='Enter Commission %')

args = parser.parse_args()
print(get_commission_amount(args.sale_amount, args.commission_pct))   
print(get_sales_revenue(args.sale_amount, args.commission_pct))
```
* Validate by running program with arguments
```
python3 sales.py --sale_amount=1500 --commission_pct=12.5
python3 sales.py --sale_amount 1500 --commission_pct 12.5
```
* Exercise: Develop a program to compute sum of integers using lower bound and upper bound.
  * The file name should be `my_sum.py`.
  * The program should take 2 arguments by names `--lower_bound` and `--upper_bound`.
  * The program should have 2 functions, `sum_n` and `sum_range` (as we have seen earlier).
  * `sum_n` should compute sum of integers from 1 to n.
  * `sum_range` should compute some of integers from lower bound to upper bound.
  * Make sure to validate by running `python my_sum.py --lower_bound=4 --upper_bound=10`