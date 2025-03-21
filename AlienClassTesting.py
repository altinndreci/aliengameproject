import unittest
from aliengame import Person, Inventory, Story

class TestInventory(unittest.TestCase):

    def tearDown(self):
        print("\n" + "-" * 50 + "\n")
        
    def setUp(self):
        self.person = Person.__new__(Person)
        self.person.name = "Joe Schmoe"
        self.person.blood = 100
        self.person.inventory = Inventory(self.person)
        self.inventory = self.person.inventory
        self.inventory.add_item("Alien Gun", 30)

    def test_add_item(self):
        initial_blood = self.person.blood
        self.inventory.add_item("Alien Knife", 20)
        self.assertIn("Alien Knife", self.inventory.items)
        self.assertEqual(self.person.blood, initial_blood - 20)

    def test_remove_item(self):
        self.inventory.add_item("Alien Snot", 10)
        self.inventory.remove_item("Alien Snot")
        self.assertNotIn("Alien Snot", self.inventory.items)

    def test_total_blood_price(self):
        self.person.inventory.items = {}
        self.inventory.add_item("Alien Knife", 40)
        self.inventory.add_item("Alien Gun", 30)
        self.assertEqual(self.inventory.total_blood_price(), 70)

    def test_insufficient_blood(self):
        self.person.blood = 50
        self.inventory.add_item("Alien Bomb", 80)
        self.assertNotIn("Alien Bomb", self.inventory.items)
        result = self.person.use_blood(80)
        self.assertFalse(result)

unittest.main(argv=[''], exit=False)