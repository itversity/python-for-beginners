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
print(get_commission_amount(args[0], args[1]))   
print(get_sales_revenue(args[0], args[1]))   
```