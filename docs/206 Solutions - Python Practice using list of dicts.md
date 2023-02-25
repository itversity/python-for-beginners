* Exercise 1: Develop a function to get list of transactions with invalid commission percentage (negative or None). Each element should be of type dict.
* Exercise 2: Develop a function to get list of transactions with commission amounts. Commission amount is equal to `("sale amount" * "commission %") / 100`. Each element should be of type dict. Each tuple in the list should contain 5 elements. The list should not contain transactions with invalid commission % (negative or none). The last element in each of the dict should be named as `commission_amount`.
```python
sales = [
    {'sale_id': 1, 'sale_rep_id': 101, 'sale_amount': 500.00, 'commission_pct': 5},
    {'sale_id': 2, 'sale_rep_id': 102, 'sale_amount': 250.00, 'commission_pct': 3},
    {'sale_id': 3, 'sale_rep_id': 103, 'sale_amount': 1000.00, 'commission_pct': 8},
    {'sale_id': 4, 'sale_rep_id': 104, 'sale_amount': 750.00, 'commission_pct': None},
    {'sale_id': 5, 'sale_rep_id': 101, 'sale_amount': 300.00, 'commission_pct': -1},
    {'sale_id': 6, 'sale_rep_id': 106, 'sale_amount': 400.00, 'commission_pct': 3},
    {'sale_id': 7, 'sale_rep_id': 104, 'sale_amount': 200.00, 'commission_pct': 0},
    {'sale_id': 8, 'sale_rep_id': 103, 'sale_amount': 150.00, 'commission_pct': 1},
    {'sale_id': 9, 'sale_rep_id': 104, 'sale_amount': 600.00, 'commission_pct': 4},
    {'sale_id': 10, 'sale_rep_id': 101, 'sale_amount': 800.00, 'commission_pct': 6}
]
```
* Solution for Exercise 1
```python
def get_invalid_sales(sales):
    invalid_sales = [] # Initializing empty list
    for sale in sales:
        if sale['commission_pct'] == None or sale['commission_pct'] < 0:
            invalid_sales.append(sale)
    return invalid_sales

get_invalid_sales(sales)
```
* Solution for Exercise 2
```python
def get_sales_with_commission(sales):
    sales_with_commission = [] # Initializing empty list
    for sale in sales:
        if sale['commission_pct'] != None and sale['commission_pct'] >= 0:
            sale['commission_amount'] = (sale['sale_amount'] * sale['commission_pct']) / 100
            sales_with_commission.append(sale)
    return sales_with_commission

get_sales_with_commission(sales)
```