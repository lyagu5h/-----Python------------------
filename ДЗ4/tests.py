import unittest
from script import Store, Product, Order

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.product1 = Product("Laptop", 1000, 5)
        self.product2 = Product("Smartphone", 500, 10)
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)

    def test_add_product(self):
        self.assertIn(self.product1, self.store.products)
        self.assertIn(self.product2, self.store.products)

    def test_list_products(self):
        self.assertEqual(len(self.store.products), 2)
        self.assertEqual(self.store.products[0].name, "Laptop")
        self.assertEqual(self.store.products[1].name, "Smartphone")

    def test_create_order(self):
        order = self.store.create_order()
        self.assertIsInstance(order, Order)

if __name__ == '__main__':
    unittest.main()
