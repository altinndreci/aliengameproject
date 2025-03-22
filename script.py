from aliengame import User, Story, GameManager, Item

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
        print(player.inventory.items)
    elif choice == '2':



        print("Choose an item to steal: ")
        for item in range(len(stealable_items)):
            print(f"{item + 1}. {stealable_items[item][0]} (Blood Cost: {stealable_items[item][1]}]")

        selected_item = input("Enter item number: ")
        numbered_item = int(selected_item)-1
        if 0 <= numbered_item < len(stealable_items):
            item = stealable_items[numbered_item]
            player.inventory.add_item(item[0], item[1])
            print(f"You stole: {item[0]} (Blood Cost: {item[1]})")
        else: 
            print("Invalid choice. Choose a number from the list.")
    elif choice == '3':
        print("Items you can steal: ")
        for item in range(len(stealable_items)):
            print(f"{item + 1}. {stealable_items[item][0]} (Blood Cost: {stealable_items[item][1]}]")
    elif choice == '4':
        player_items = list(player.inventory.items.keys())

        if not player_items:
            print("You have no items to return.")
        else:
            print("Choose an item to return: ")
        
        for item in range(len(player_items)):
            print(f"{item + 1}. {player_items[item]} (Blood Cost: {player_items[item]}]")
        Returning_item = input("Enter item number: ")
        numbered_item = int(Returning_item)-1

        if 0 <= numbered_item < len(player_items):
            item_name = player_items[numbered_item]
            item_blood_cost = player.inventory.items[item_name]

            player.inventory.remove_item(item_name)

            if (item_name, item_blood_cost) not in stealable_items:
                stealable_items.append((item_name, item_blood_cost))

            print(f"You successfully returned: {item_name}")
        else:
            print("Invalid Choice, Choose a number from the list.")

    elif choice == '5':
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")