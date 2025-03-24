
class Item:
    def __init__(self, name, blood_price, quantity=1):
        self.name = name
        self.blood_price = blood_price
        self.quantity = quantity

    def steal(self):
        if self.quantity <= 0:
            raise ValueError(f"{self.name} can't be stolen.")
        self.quantity -= 1
    
    def is_available(self):
        return self.quantity > 0
    
    def return_item(self):
        self.quantity += 1

    def __str__(self):
        return f"{self.name} Cost: {self.blood_price} blood, Available: {self.quantity}"



    