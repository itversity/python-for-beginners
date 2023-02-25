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