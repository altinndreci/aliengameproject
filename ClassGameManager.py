

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
