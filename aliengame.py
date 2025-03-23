import time
#Time will be used later as a consequence tool.
class User:
    #User class is made to work with the story class in where the player can input their name.
    #it also establishes the blood level and consequence system set to zero which will be used later on.
    def __init__(self, inventory=None):
        self.name = input("What is your character's name?: ")
        print("You're finally awake!")
        print("Hello Prisoner,", self.name)
        self.blood = 100
        self.inventory = Inventory(self)
        self.consequence = 0

    def get_name(self):
        #This is defined so we can implement it in our story message
        return self.name

    def use_blood(self, amount):
        #We have the use_blood defined so we can affectively have a consequence in the game when blood level drops too low.
        if amount > self.blood:
            print("Not enough blood to make this purchase!")
            return False
        self.blood -= amount
        print(f"Blood remaining: {self.blood}/100")
        return True

    def total_blood_usage(self):
        return sum(self.inventory.items.values())
    
    def rest(self):
        #This is a function that lets the user rest to recover blood
        print("You're resting to recover blood.")
        self.blood += 10
        print(f"Blood remaining: {self.blood}/100")
        return self.blood
    




class Story:        #Defining an overview of our story.
    def __init__(self, user):
        self.intro = (
            "\nYou are now in a world, where a species of Aliens are set on world domination and human imprisonment, have arrived on Earth.\n"
            "It is up to one person to escape and save the world to lead the resistance and fight back.\n"
            f"That person is {user.get_name()}.\n"  
            "You will be on an alien imprisonment camp located on the mothership hovering over earth & each of your decisions will have consequences...\n"
            "You will have many items to steal and use them to your best ability, but discreetly, or else bad things will happen...\n"
        )


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


class GameManager:
    def __init__(self):
        self.available_items = {} 
        self.steal_records = {}  
        self.max_steal_duration = 10 
        self.penalty_rate = 2         

    def add_item(self, item):
        if item.name in self.available_items:
            self.available_items[item.name].quantity += item.quantity
        else:
            self.available_items[item.name] = item

    def steal_item(self, user, item_name):  
        if item_name not in self.available_items:
            print("Item not found in stealing system.")
            return False
        item = self.available_items[item_name]
        if not item.is_available():
            print(f"{item_name} is not available for stealing.")
            return False
        try:
            item.steal()  
        except ValueError as e:
            print(e)
            return False
        if user.name not in self.steal_records: 
            self.steal_records[user.name] = {}
        self.steal_records[user.name][item_name] = time.time() #Creates a time record of when the player's steals an item
        print(f"{user.name} stole {item_name}.")
        return True

    def return_item(self, user, item_name):
        if user.name not in self.steal_records or item_name not in self.steal_records[user.name]:
            print(f"{user.name} did not steal {item_name}.")
            return False
        steal_time = self.steal_records[user.name].pop(item_name)  #creates a var recording when the item was stolen
        duration = time.time() - steal_time #current time minus the time it was stolen
        penalty = 0
        if duration > self.max_steal_duration: 
            penalty = (duration - self.max_steal_duration) * self.penalty_rate #the player is increasingly punished for how long they held the itme using the times recorded previously
            print(f"Returned {item_name} late. Penalty: {penalty:.2f} blood units.")
            if not user.use_blood(penalty):
                print("User could not pay the late penalty!")
            user.consequence += 1
            print("Consequence: Your delay has attracted alien attention!")
        else:
            print(f"{user.get_name()} returned {item_name} on time.")
        self.available_items[item_name].return_item()
        return True

    def show_available_items(self):
        print("Available Items for Stealing")
        for item in self.available_items.values():
            print(item)

    