

class Inventory:
    def __init__(self, user):
        self.items = {}
        self.user = user

    def add_item(self, name, blood_price):
        if blood_price < 0:
            raise ValueError("Blood secretion cannot be negative, user is already dead!")
        
        if not self.user.use_blood(blood_price):
            print(f"Cannot steal {name} due to low blood.")
            return False
        
        self.items[name] = blood_price
        print(f"{name} added to your inventory for the cost of {blood_price} units of blood!")
        return True
    
    def remove_item(self, name):
        if name not in self.items:
            raise KeyError("Item not in inventory")
        del self.items[name]
        print(f"{name} removed from your inventory.")

    def total_blood_price(self):
        return sum(self.items.values())