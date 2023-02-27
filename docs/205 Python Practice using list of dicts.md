* Review Data Set
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
* Get number of elements in the list
```python
len(sales)
```
* Get unique sale_rep_ids.
```python
sale_rep_ids = set() # Initializing a set
for sale in sales:
    if sale['sale_rep_id'] not in sale_rep_ids:
        sale_rep_ids.add(sale['sale_rep_id'])

print(sale_rep_ids)
```
* Develop a function to get list of sale transactions where transaction amount is less than 500. Each element should be of type dict.
```python
def get_low_revenue_sales(sales):
    low_revenue_sales = [] # Initializing empty list
    for sale in sales:
        if sale['sale_amount'] < 500:
            low_revenue_sales.append(sale)
    return low_revenue_sales

get_low_revenue_sales(sales)
```
* Exercise 1: Develop a function to get list of transactions with invalid commission percentage (negative or None). Each element should be of type dict.
* Exercise 2: Develop a function to get list of transactions with commission amounts. Commission amount is equal to `("sale amount" * "commission %") / 100`. Each element should be of type dict. Each dict in the list should contain 5 elements. The list should not contain transactions with invalid commission % (negative or none). The last element in each of the dict should be named as `commission_amount`.
