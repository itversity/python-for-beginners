* Sample test cases

```python
import unittest
from unittest import TestCase
from sales import Sale
class SaleTestCase(TestCase):
    
    def test_get_commission_amount(self):
        sale1 = Sale(1, 1, 1500, 15)
        sale2 = Sale(2, 1, 1500, None)
        sale3 = Sale(3, 1, 1500, -1)

        print(f'Testing get_commission_amount for {sale1.sale_id}')
        self.assertTrue(sale1.get_commission_amount() == 225)
        
        print(f'Testing get_commission_amount for {sale2.sale_id}')
        self.assertTrue(sale2.get_commission_amount() == 0.0)
        
        print(f'Testing get_commission_amount for {sale3.sale_id}')
        with self.assertRaises(ValueError):
            sale3.get_commission_amount()
            
    def test_get_sale_amount(self):
        sale1 = Sale(1, 1, 1500, 15)
        sale2 = Sale(2, 1, 1500, None)
        sale3 = Sale(3, 1, 1500, -1)

        print(f'Testing get_sale_amount for {sale1.sale_id}')
        self.assertTrue(sale1.get_sale_revenue() == 1275)

        print(f'Testing get_sale_amount for {sale2.sale_id}')
        self.assertTrue(sale2.get_sale_revenue() == 1500)

        print(f'Testing get_sale_amount for {sale3.sale_id}')
        with self.assertRaises(ValueError):
            sale3.get_sale_revenue()
    
if _name_ == '_main_':
    unittest.main()
```

* Using `setUp` and `tearDown`

```python
import unittest
from unittest import TestCase
from sales import Sale
class SaleTestCase(TestCase):
    
    def setUp(self) -> None:
        self.sales =[
            Sale(1, 1, 1500, 15),
            Sale(2, 1, 1500, None),
            Sale(3, 1, 1500, -1)
        ]
        return super().setUp()
    

    def test_get_commission_amount(self):
        sale1 = self.sales[0]
        sale2 = self.sales[1]
        sale3 = self.sales[2]

        print(f'Testing get_commission_amount for {sale1.sale_id}')
        self.assertTrue(sale1.get_commission_amount() == 225)
        
        print(f'Testing get_commission_amount for {sale2.sale_id}')
        self.assertTrue(sale2.get_commission_amount() == 0.0)
        
        print(f'Testing get_commission_amount for {sale3.sale_id}')
        with self.assertRaises(ValueError):
            sale3.get_commission_amount()
            

    def test_get_sale_amount(self):
        sale1 = self.sales[0]
        sale2 = self.sales[1]
        sale3 = self.sales[2]

        print(f'Testing get_sale_amount for {sale1.sale_id}')
        self.assertTrue(sale1.get_sale_revenue() == 1275)

        print(f'Testing get_sale_amount for {sale2.sale_id}')
        self.assertTrue(sale2.get_sale_revenue() == 1500)

        print(f'Testing get_sale_amount for {sale3.sale_id}')
        with self.assertRaises(ValueError):
            sale3.get_sale_revenue()
    
    def tearDown(self) -> None:
        return super().tearDown()    


if _name_ == '_main_':
    unittest.main()
```

* Using `setUpClass`

```python
import unittest
from unittest import TestCase
from sales import Sale
class SaleTestCase(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
         cls.sales =[
            Sale(1, 1, 1500, 15),
            Sale(2, 1, 1500, None),
            Sale(3, 1, 1500, -1)
        ]
    

    def test_get_commission_amount(self):
        sale1 = self.sales[0]
        sale2 = self.sales[1]
        sale3 = self.sales[2]

        print(f'Testing get_commission_amount for {sale1.sale_id}')
        self.assertTrue(sale1.get_commission_amount() == 225)
        
        print(f'Testing get_commission_amount for {sale2.sale_id}')
        self.assertTrue(sale2.get_commission_amount() == 0.0)
        
        print(f'Testing get_commission_amount for {sale3.sale_id}')
        with self.assertRaises(ValueError):
            sale3.get_commission_amount()
            

    def test_get_sale_amount(self):
        sale1 = self.sales[0]
        sale2 = self.sales[1]
        sale3 = self.sales[2]

        print(f'Testing get_sale_amount for {sale1.sale_id}')
        self.assertTrue(sale1.get_sale_revenue() == 1275)

        print(f'Testing get_sale_amount for {sale2.sale_id}')
        self.assertTrue(sale2.get_sale_revenue() == 1500)

        print(f'Testing get_sale_amount for {sale3.sale_id}')
        with self.assertRaises(ValueError):
            sale3.get_sale_revenue()
    

if _name_ == '_main_':
    unittest.main()
```