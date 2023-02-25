* Review Data Set
```python
sales = [
    (1, 101, 500.00, 5),
    (2, 102, 250.00, 3),
    (3, 103, 1000.00, 8),
    (4, 104, 750.00, None),
    (5, 101, 300.00, -1),
    (6, 106, 400.00, 3),
    (7, 104, 200.00, 0),
    (8, 103, 150.00, 1),
    (9, 104, 600.00, 4),
    (10, 101, 800.00, 6)
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
    if sale[1] not in sale_rep_ids:
        sale_rep_ids.add(sale[1])

print(sale_rep_ids)
```
* Develop a function to get list of sale transactions where transaction amount is less than 500. Each element should be of type tuple.
```python
def get_low_revenue_sales(sales):
    low_revenue_sales = [] # Initializing empty list
    for sale in sales:
        if sale[2] < 500:
            low_revenue_sales.append(sale)

    return low_revenue_sales

get_low_revenue_sales(sales)
```
* Exercise 1: Develop a function to get list of transactions with invalid commission percentage (negative or None). Each element should be of type tuple.
* Exercise 2: Develop a function to get list of transactions with commission amounts. Commission amount is equal to `("sale amount" * "commission %") / 100`. Each element should be of type tuple. Each tuple in the list should contain 5 elements. The list should not contain transactions with invalid commission % (negative or none).