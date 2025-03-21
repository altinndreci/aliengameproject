from aliengame import Person 
from aliengame import Story
import unittest


class TestInventory(unittest.TestCase):
    

    def tearDown(self):
        print("\n" + "-" * 50 + "\n")


    def setUp(self):
        self.person = Person()
        self.inventory = self.person.inventory
        self.inventory.add_item("Alien Gun", 30)
    

    def test_add_item(self):
        self.inventory.add_item("Alien Knife", 20)
        self.assertIn("Alien Knife", self.inventory.items)
    

    def test_remove_item(self):
        self.inventory.add_item("Alien Snot", 10)
        self.inventory.remove_item("Alien Snot")
        self.assertNotIn("Alien Snot", self.inventory.items)


    def test_total_blood_price(self):
        self.inventory.add_item("Alien Knife", 40)
        self.assertEqual(self.inventory.total_blood_price(), 70)


    def test_insufficient_blood(self):
        self.inventory.add_item("Alien Bomb", 80)
        self.person.blood = 50
        result = self.person.use_blood(80)
        self.assertFalse(result)
        self.assertNotIn('Alien Bomb', self.inventory.items)


unittest.main(argv=[''], exit=False)