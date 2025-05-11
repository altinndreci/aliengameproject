import sqlite3
from ClassUser import User
from ClassStory import Story
from ClassInventory import Inventory
from ClassItem import Item
from ClassGameManager import GameManager
from alien_database import MakeDatabase

#creates user, starts the database and the story
player = User()
MakeDatabase(player)
story = Story(player)
print(story.intro)

#list of stealable items
stealable_items = [
    ("Alien Gun", 50),
    ("Alien Knife", 30),
    ("Alien Snot", 10),
    ("Alien Bomb Launcher", 60),
    ("Alien Shield", 40),
    ("Alien Potion", 20)
]

#function to check if the player's blood level is too low - then night night
def below_blood_level():
    if player.blood <= 0:
        print("You didn't manage your blood.\n GAME OVER.")
        return True
    return False

#creating main CLI
while True:
    print("Main Menu")
    print("1. Current Inventory")
    print("2. Steal Item")
    print("3. Stealable Items")
    print("4. Return an Item")
    print("5. Travel")
    print("6. Map")
    print("7. HP/Blood Levels")
    print("8. View Transaction History")
    print("9. Exit\n")



  
    choice = input("Choose an option: ")
    
    if choice == '1':
        print("Current Inventory:")
        print(player.Inventory.items)
    
    elif choice == '2':
        print("Choose an item to steal: ")
        for i in range(len(stealable_items)):
            item = stealable_items[i]
            print(f"{i + 1}. {item[0]} (Blood Cost: {item[1]})")
        print("\n")

        selected_item = input("Enter item number: ")
        try:
            numbered_item = int(selected_item) - 1
            if 0 <= numbered_item < len(stealable_items):
                item = stealable_items[numbered_item]
                
                #adds item to inventory 
                if player.Inventory.add_item(item[0], item[1]):
                    print(f"You stole: {item[0]} (Blood Cost: {item[1]})")
                    print('\n')

                    #logs a transaction for stealing
                    conn = sqlite3.connect("alien_game.db")
                    cur = conn.cursor()
                    sql = '''INSERT INTO transactions (username, item_name, action, action_time)
                            VALUES (?, ?, ?, julianday('now'))'''#get the current time in julian format(learned from runestone')
                    cur.execute(sql, (player.get_name(), item[0], 'steal'))
                    conn.commit()
                    conn.close()

                    #statement to end the game
                    if below_blood_level():
                        break  
                else:
                    print("Game Over, you ran out of blood. You didn't manage your blood properly.")
                    break
  
            else: 
                print("Invalid choice. Choose a number from the list.")
        except ValueError:
            print("Please enter a correct input.")
    
    elif choice == '3':
        #displays all the stealable items
        print("Items you can steal: ")
        for i in range(len(stealable_items)):
            item = stealable_items[i]
            print(f"{i + 1}. {item[0]} (Blood Cost: {item[1]})")
   
    elif choice == '4':
        #gets the list of items in inventory
        player_items = list(player.Inventory.items.keys())

        if not player_items:
            print("You have no items to return.")
        else:
            print("Choose an item to return: ")
        
        #show each item in the inventory with its blood cost
        for i in range(len(player_items)):
            item_name = player_items[i]
            item_blood_cost = player.Inventory.items[item_name]
            print(f"{i + 1}. {item_name} (Blood Cost: {item_blood_cost})")
        
        print("\n") #creates the space that the students don't wanna sit in(not cuz it's in front of prof sonyl) jk pls don't hurt us
        
        #user selects an item to return
        Returning_item = input("Enter Item number: ")
        try:
            #takes what the user input and match it to the list position
            numbered_item = int(Returning_item) - 1
            
            #if the number the player picked actually exists, then it takes away the item from their inventory
            if 0 <= numbered_item < len(player_items):
                item_name = player_items[numbered_item]
                item_blood_cost = player.Inventory.items[item_name]

                player.Inventory.remove_item(item_name)

                # Refund blood
                player.blood += item_blood_cost

                # Add back to stealable items
                stealable_items.append((item_name, item_blood_cost))

                print(f"You successfully returned: {item_name}")
                print(f"You regained {item_blood_cost} blood. Blood now: {player.blood}")
                print("\n")


                #logs the item returning transaction
                conn = sqlite3.connect("alien_game.db")
                cur = conn.cursor()
                sql = '''INSERT INTO transactions (username, item_name, action, action_time)
                        VALUES (?, ?, ?, julianday('now'))'''
                cur.execute(sql, (player.get_name(), item_name, 'return'))
                conn.commit()
                conn.close()

            else:
                print("Invalid Choice, Choose a number from the list.")
        except ValueError:
            print("Please enter a correct input.")

    #ends the game
    elif choice == '9':
        print("Exiting the game. Goodbye!")
        break
    
    
    elif choice == '8':
        print("Transaction History:\n")
    
        conn = sqlite3.connect("alien_game.db")
        cur = conn.cursor()

        #queries each transaction with time
        sql = '''
            SELECT item_name, action, datetime(action_time), action_time
            FROM transactions
            WHERE username = ?
            ORDER BY action_time ASC
        '''
        cur.execute(sql, (player.get_name(),))
        rows = cur.fetchall()

        if not rows:
            print("No transactions found.")
        else:
            for i, row in enumerate(rows, start=1):
                item_name, action, readable_time, _ = row
                print(f"{i}. {action.title()} - {item_name} at {readable_time[11:]}")  # only HH:MM:SS
        print("\n")

        conn.close()

    elif choice == '6':
        story.draw_map()
        story.show_map()

    elif choice == '5':
        story.travel()

    elif choice == '7':
        print(f"Blood: {player.blood}/100")
        print(f"HP: {story.player_hp}/100\n")

    else:
        print("Wrong move buddy. Try again.")