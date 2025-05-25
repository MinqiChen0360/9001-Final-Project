# test_item.py
import unittest
from item import Item
from inventory import Inventory

class TestItem(unittest.TestCase):
    def test_restock(self):
        item = Item("001", "Pen", 10, 1.5)
        item.restock(5)
        self.assertEqual(item.quantity, 15)

    def test_deduct_valid(self):
        item = Item("002", "Notebook", 20, 3.0)
        item.deduct(5)
        self.assertEqual(item.quantity, 15)

    def test_deduct_invalid(self):
        item = Item("003", "Eraser", 2, 0.5)
        with self.assertRaises(ValueError):
            item.deduct(5)

    def test_negative_restock(self):
        item = Item("004", "Marker", 10, 2.0)
        with self.assertRaises(ValueError):
            item.restock(-3)

class TestInventory(unittest.TestCase):
    def test_add_and_remove_item(self):
        inv = Inventory()
        item = Item("005", "Ruler", 30, 2.5)
        inv.add_item(item)
        self.assertIn("005", inv.items)
        inv.remove_item("005")
        self.assertNotIn("005", inv.items)

    def test_duplicate_add(self):
        inv = Inventory()
        item = Item("006", "Stapler", 5, 6.0)
        inv.add_item(item)
        with self.assertRaises(KeyError):
            inv.add_item(item)

    def test_search(self):
        inv = Inventory()
        inv.add_item(Item("007", "Glue", 12, 1.2))
        inv.add_item(Item("008", "Glue Stick", 8, 1.5))
        results = inv.search_by_name("glue")
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main()
