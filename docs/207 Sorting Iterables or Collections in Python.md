* Overview of sorting (sort and sorting)
* Using `sort` to sort list
* Disadvantages of using `sort`
* Overview of `sorted`
* Sort iterable of integers
* Reverse Sorting
* Sort below list of tuples based on **sale amount**.
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

sorted(sales, key=lambda i: i[2])

from pprint import pprint
pprint(sorted(sales, key=lambda i: i[2]))

pprint(sorted(sales, key=lambda i: i[2], reverse=True))
```
* Sort below list of dicts based on **sale amount**.
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

sorted(sales, key=lambda i: i['sale_amount'])

from pprint import pprint
pprint(sorted(sales, key=lambda i: i['sale_amount']))

pprint(sorted(sales, key=lambda i: i['sale_amount'], reverse=True))
```
* Exercise 1: Sort the students data based on reverse order of total score.
* Exercise 2: Get total score along with other details as part of sorted output. Use `total_score` as key for **total score**.
```python
students = [
    {'student_id': 1, 'scores': [80, 92, 85]},
    {'student_id': 2, 'scores': [75, 99, 82]},
    {'student_id': 3, 'scores': [92, 80, 77]},
    {'student_id': 4, 'scores': [63, 88, 70]},
    {'student_id': 5, 'scores': [92, 94, 91]}
]
```
* Solution for Exercise 1
```python
student = students[0]
student['scores']
sum(student['scores'])
student['total_score'] = sum(student['scores'])

sorted(students, key=lambda student: sum(student['scores']))
from pprint import pprint
pprint(sorted(students, key=lambda student: sum(student['scores'])))

pprint(sorted(students, key=lambda student: sum(student['scores']), reverse=True))
```
* Solution for Exercise 2
```python
student = students[0]
student['scores']
sum(student['scores'])
student['total_score'] = sum(student['scores'])
from pprint import pprint
pprint(student)

students_with_total = []
for student in students:
    student['total_score'] = sum(student['scores'])
    students_with_total.append(student)

pprint(students_with_total)

sorted(students_with_total, key=lambda student: student['total_score'])
pprint(sorted(students_with_total, key=lambda student: student['total_score']))

pprint(sorted(students_with_total, key=lambda student: student['total_score'], reverse=True))
```

