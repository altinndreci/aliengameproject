import sqlite3
from ClassUser import User
from ClassStory import Story
from ClassInventory import Inventory
from ClassItem import Item
from ClassGameManager import GameManager
from alien_database import MakeDatabase
        
player = User()
story = Story(player)
print(story.intro)

stealable_items = [
    ("Alien Gun", 50),
    ("Alien Knife", 30),
    ("Alien Snot", 10),
    ("Alien Bomb", 60),
    ("Alien Shield", 40),
    ("Alien Potion", 20),
]
def below_blood_level():
    if player.blood <= 0:
        print("You didn't manage your blood.\n GAME OVER.")
        return True
    return False

while True:
    print("Main Menu")
    print("1. Show Stealing Inventory")
    print("2. Steal Item")
    print("3. Show Stealable Items")
    print("4. Return an Item")
    print("5. Exit")
  
    choice = input("Choose an option: ")
    
    if choice == '1':
        print("Stealing Inventory:")
        print(player.Inventory.items)
    
    elif choice == '2':
        print("Choose an item to steal: ")
        for i in range(len(stealable_items)):
            item = stealable_items[i]
            print(f"{i + 1}. {item[0]} (Blood Cost: {item[1]})")

        selected_item = input("Enter item number: ")
        try:
            numbered_item = int(selected_item) - 1
            if 0 <= numbered_item < len(stealable_items):
                item = stealable_items[numbered_item]
                
                if player.Inventory.add_item(item[0], item[1]):
                    print(f"You stole: {item[0]} (Blood Cost: {item[1]})")
                
                    if below_blood_level():
                        break  
                else:
                    print("Can't steal item due to blood level.")
                    if below_blood_level():
                        break  
            else: 
                print("Invalid choice. Choose a number from the list.")
        except ValueError:
            print("Please enter a correct input.")
    
    elif choice == '3':
        print("Items you can steal: ")
        for i in range(len(stealable_items)):
            item = stealable_items[i]
            print(f"{i + 1}. {item[0]} (Blood Cost: {item[1]})")
   
    elif choice == '4':
        player_items = list(player.Inventory.items.keys())

        if not player_items:
            print("You have no items to return.")
        else:
            print("Choose an item to return: ")
        
        for i in range(len(player_items)):
            item_name = player_items[i]
            item_blood_cost = player.Inventory.items[item_name]
            print(f"{i + 1}. {item_name} (Blood Cost: {item_blood_cost})")
        
        Returning_item = input("Enter Item number: ")
        try:
            numbered_item = int(Returning_item) - 1
            if 0 <= numbered_item < len(player_items):
                item_name = player_items[numbered_item]
                item_blood_cost = player.Inventory.items[item_name]

                player.Inventory.remove_item(item_name)

                stealable_items.append((item_name, item_blood_cost))

                print(f"You successfully returned: {item_name}")
            else:
                print("Invalid Choice, Choose a number from the list.")
        except ValueError:
            print("Please enter a correct input.")

    elif choice == '5':
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")