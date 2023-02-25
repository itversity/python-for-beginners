* Exercise 1: Develop a function to get list of transactions with invalid commission percentage (negative or None). Each element should be of type tuple.
* Exercise 2: Develop a function to get list of transactions with commission amounts. Commission amount is equal to `("sale amount" * "commission %") / 100`. Each element should be of type tuple. Each tuple in the list should contain 5 elements. The list should not contain transactions with invalid commission % (negative or none).
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
* Solution for Exercise 1
```python
def get_invalid_sales(sales):
    invalid_sales = [] # Initializing empty list
    for sale in sales:
        if sale[3] == None or sale[3] < 0:
            invalid_sales.append(sale)
    return invalid_sales

get_invalid_sales(sales)
```
* Solution for Exercise 2
```python
def get_sales_with_commission(sales):
    sales_with_commission = [] # Initializing empty list
    for sale in sales:
        if sale[3] != None and sale[3] >= 0:
            l_sale = list(sale)
            l_sale.append((sale[2] * sale[3]) / 100)
            sales_with_commission.append(tuple(l_sale))
    return sales_with_commission

get_sales_with_commission(sales)
```