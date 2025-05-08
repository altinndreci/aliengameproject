import unittest
from aliengame import User, Inventory, Story, Item, GameManager

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.user = User.__new__(User)
        self.user.name = "Joe Schmoe"
        self.user.blood = 100
        self.user.inventory = Inventory(self.user)
        self.inventory = self.user.inventory
        self.inventory.add_item("Alien Gun", 30)

    def tearDown(self):
        print("\n" + "-" * 50 + "\n")

    def test_add_item(self):
        initial_blood = self.user.blood
        self.inventory.add_item("Alien Knife", 20)
        self.assertIn("Alien Knife", self.inventory.items)
        self.assertEqual(self.user.blood, initial_blood - 20)

    def test_remove_item(self):
        self.inventory.add_item("Alien Snot", 10)
        self.inventory.remove_item("Alien Snot")
        self.assertNotIn("Alien Snot", self.inventory.items)

    def test_total_blood_price(self):
        self.user.inventory.items = {}
        self.inventory.add_item("Alien Knife", 40)
        self.inventory.add_item("Alien Gun", 30)
        self.assertEqual(self.inventory.total_blood_price(), 70)

    def test_insufficient_blood(self):
        self.user.blood = 50
        self.inventory.add_item("Alien Bomb Launcher", 80)
        self.assertNotIn("Alien Bomb Launcher", self.inventory.items)
        result = self.user.use_blood(80)
        self.assertFalse(result)

unittest.main(argv=[''], exit=False)