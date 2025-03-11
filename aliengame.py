import unittest
        
class Story:
    def __init__(self, Person):  
        self.intro = (
            "In a world, where a species of Aliens set on world domination have arrived on Earth.\n"
            "It is up to one person to saßve the world and lead the resistance to fight back.\n"
            f"That person is {Person.get_name()}.\n"  
            "You as a player will be on an alien mothership hovering over the earth and each of your decisions will have consequences...\n"
            "You will have many items to steal and use them to your best ability, but discreetly, or else bad things will happen..."
        )

class Person:
    def __init__(self, inventory=None):
        self.__name = input("What is your character's name?: ")
        print("Hello Prisoner,", self.__name)
        self.blood = 100
        self.inventory = Inventory(self)

    def get_name(self):
        return self.__name
    
    def use_blood(self, amount):    #Blood is drained when foerign items are picked up
        if amount > self.blood:
            print("Not enough blood to make this purchase!")
            return False
        self.blood -= amount
        print(f"Blood remaining: {self.blood}/100")
        return True
    
    def total_blood_usage(self):
        return sum(self.items.values())

class Inventory:
    def __init__(self, Person):
        self.items = {}
        self.person = Person 
    
    def add_item(self, name, blood_price):
        if blood_price < 0:
            raise ValueError("Blood secretion cannot be negative, person is already dead!")
        self.items[name] = blood_price
        print(f"{name} added to your inventory!")

    
    def remove_item(self, name):
        if name not in self.items:
            raise KeyError("Item not in inventory")
        del self.items[name]
        print(f"{name} removed from your inventory.")

    
    def total_blood_price(self):
        return sum(self.items.values())



class TestInventory(unittest.TestCase):
    
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
