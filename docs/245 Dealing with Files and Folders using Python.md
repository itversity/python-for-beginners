* Manage folders
```python
help(os.mkdir)
help(os.makedirs)
```
* Validating paths
```python
help(os.path.isdir)
os.path.isdir('data/retail_db')
os.path.isdir('data/README.md')

help(os.path.isfile)
os.path.isfile('data/retail_db')
os.path.isfile('data/README.md')

help(os.path.split)
os.path.split('data/retail_db/orders/part-00000')

help(os.path.splitext)
os.path.splitext('data/nyse_all/nyse_data/NYSE_1997.txt.gz')
```
* Walk through folder recursively
```python
import os

os.walk('data') #walks through recursively

for i in os.walk('data/retail_db'):
    print(i) # tuple with path, [folders] and [files]
```