```python
# sales.py

def validate_commission_pct(commission_pct):
    if commission_pct and (commission_pct <= 0 or commission_pct > 100):
        return False
    return True


def get_commission_amount(sale_amount, commission_pct):
    if validate_commission_pct(commission_pct) == False:
        raise ValueError('Invalid Number')
    if commission_pct == None:
        return 0
    return ((sale_amount * commission_pct) / 100)


print(get_commission_amount(1500, 12))


def get_sales_revenue(sale_amount, commission_pct):
    if validate_commission_pct(commission_pct) == False:
        raise ValueError('Invalid Number')
    commission_amount = get_commission_amount(sale_amount, commission_pct)
    return sale_amount - commission_amount


print(get_sales_revenue(1500, 12))   
```