class Person:
    def __init__(self, inventory=None):
        self.name = input("What is your character's name?: ")
        print("You're finally awake!")
        print("Hello Prisoner,", self.name)
        self.blood = 100
        self.inventory = Inventory(self)


    def get_name(self):
        return self.name
    

    def use_blood(self, amount):    #Blood is drained when foerign items are picked up
        if amount > self.blood:
            print("Not enough blood to make this purchase!")
            return False
        self.blood -= amount
        print(f"Blood remaining: {self.blood}/100")
        return True
    
    
    def total_blood_usage(self):
        return sum(self.inventory.items.values())






class Story:
    def __init__(self, Person):  
        self.intro = (
            "\nYou are now in a world, where a species of Aliens are set on world domination and human imprisonment, have arrived on Earth.\n"
            "It is up to one person to escape and save the world to lead the resistance and fight back.\n"
            f"That person is {Person.get_name()}.\n"  
            "You will be on an alien imprisonment camp located on the mothership hovering over earth & each of your decisions will have consequences...\n"
            "You will have many items to steal and use them to your best ability, but discreetly, or else bad things will happen...\n"
        )






class Inventory:
    def __init__(self, Person):
        self.items = {}
        self.person = Person 
    

    def add_item(self, name, blood_price):
        if blood_price < 0:
            raise ValueError("Blood secretion cannot be negative, person is already dead!")
        if not self.person.use_blood(blood_price):
            print(f"Cannot add {name} due to low blood.")
            return
        self.items[name] = blood_price
        print(f"{name} added to your inventory for the cost of {blood_price} units of blood!")
    

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError("Item not in inventory")
        del self.items[name]
        print(f"{name} removed from your inventory.")

    
    def total_blood_price(self):
        return sum(self.items.values())