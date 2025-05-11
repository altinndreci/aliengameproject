from ClassUser import User
import random
#story class that has the game map, alien encounter, and main storyline
class Story:
    def __init__(self, user):
        self.user = user
        self.current_location = "Main Hub"

        #alien spaceship map layout
        self.game_map = {
            "Main Hub": {
                "Recovery Chamber": 1,
                "Red Chamber": 2,
                "Green Chamber": 3,
                "Blue Chamber": 4
            },
            "Alien Recovery Chamber": {"Main Hub": 1},
            "Red Chamber": {"Main Hub": 2},
            "Blue Chamber": {"Main Hub": 3},
            "Green Chamber": {"Main Hub": 4}
        }
        #dictionary of alien encounters with location, name, description, weakness and health points(hp) but you knew that
        self.monsters = {
            "Red Chamber": {
                "name": "Darlek the Mutant",
                "description": "A metal war machine rolls toward you. Inside, a hideous mutant glares with hatred. 'EX-TER-MI-NATE.'",
                "weakness": "Alien Bomb Launcher",
                "hp": 100
            },
            "Green Chamber": {
                "name": "Jabba the Hutt",
                "description": "A massive slug-like creature slumps on a throne of slime. It chuckles deeply, flicking its tail with arrogance.",
                "weakness": "Alien Knife",
                "hp": 100
            },
            "Blue Chamber": {
                "name": "Gorn the Reptile",
                "description": "A green-scaled alien steps into view, claws raised. Its eyes lock onto you like prey.",
                "weakness": "Alien Gun",
                "hp": 100
            },
            "Final Chamber": {
                "name": "Darth Khan",
                "description": "A towering figure in black armor stands at the center of the room. His lightsaber ignites as he speaks with chilling calm: 'Superior minds conquer all... with force.'",
                "weakness": "Alien Snot",
                "hp": 100
            }
        }

        #game intro
        self.intro = (
            "\nYou are now in a world, where a species of Aliens are set on world domination and human imprisonment, have arrived on Earth.\n"
            "It is up to one person to escape and save the world to lead the resistance and fight back.\n"
            f"That person is {user.get_name()}.\n"
            "You will be on an alien imprisonment camp located on the mothership hovering over Earth & each of your decisions will have consequences...\n"
            "You will have many items to steal and use them to your best ability, but discreetly, or else bad things will happen...\n"
            "\nYou're starting in the Main Hub of the alien mothership. From here, you can explore the chambers...\n"
        )
    #function teling you where you are and where you can go
    def show_map(self):
        print(f"\nYou are currently in: {self.current_location}")
        print("You can go to:")
        for destination in self.game_map.get(self.current_location, {}):
            print(f"- {destination}")
        print("\n")

        #unlockingthe final chamber where the final boss is after defeating the 3 aliens
        if self.current_location == "Alien Recovery Chamber" and all(
            chamber not in self.monsters for chamber in ["Red Chamber", "Green Chamber", "Blue Chamber"]
        ):
            print("- Final Chamber (Unlocked)")

    #function allowing you to travel around the spaceship
    def travel(self, destination):
        if destination == "Final Chamber":
            if self.current_location != "Alien Recovery Chamber":
                print("You must pass through the Recovery Chamber to access the Final Chamber.")
                return
            if any(chamber in self.monsters for chamber in ["Red Chamber", "Green Chamber", "Blue Chamber"]):
                print("You feel a strong force blocking the path. Defeat all other aliens first.")
                return
            self.current_location = "Final Chamber"
            print("\nYou move to: Final Chamber")
            self.trigger_encounter()
        elif destination in self.game_map.get(self.current_location, {}):
            self.current_location = destination
            print(f"\nYou move to: {destination}")
            self.trigger_encounter()
        else:
            print("You can’t get there from here.")

    #map locations connected to the map using a dictionary
    def draw_map(self):
        location_symbols = {
            "Main Hub": "[Main Hub]",
            "Alien Recovery Chamber": "       [Recovery Chamber]",
            "Red Chamber": "        [Red Chamber]",
            "Green Chamber": "[Green Chamber]",
            "Blue Chamber": "[Blue Chamber]",
            "Final Chamber": "       [Final Chamber]"
        }

        #marks your current location with *
        for key in location_symbols:
            if key == self.current_location:
                location_symbols[key] = "*" + location_symbols[key] + "*"

        #prints the map of the spaceship using key characters
        print("\nAlien Mothership Map:")
        print("         " + location_symbols["Red Chamber"])
        print("                       |")
        print(location_symbols["Green Chamber"] + " - " + location_symbols["Main Hub"] + " - " + location_symbols["Blue Chamber"])
        print("                       |")
        print("         " + location_symbols["Alien Recovery Chamber"])

        if all(chamber not in self.monsters for chamber in ["Red Chamber", "Green Chamber", "Blue Chamber"]):
            print("                       |")
            print("         " + location_symbols["Final Chamber"])
        print()

    #encounter function that has the combat mechanic
    def trigger_encounter(self):
        if self.current_location in self.monsters:
            monster = self.monsters[self.current_location]
            print(f"\nYou encounter {monster['name']}!")
            print(monster['description'])

            player_hp = 100

            #combat loop until player or alien monster is defeated
            while monster["hp"] > 0 and player_hp > 0:
                print("\nBattle Menu:")
                print(f"Your HP: {player_hp}/100")
                print("1. Fight")
                print("2. Run")
                action = input("Choose an action: ")
                print("\n")

                #checks to see if the player has an item to attack with, sorry your hands are not registered weapons here buddy
                if action == "1":
                    if not self.user.Inventory.items:
                        print("You have no items to defend yourself! The alien attacks!")
                        self.user.blood -= 20
                        self.user.consequence += 1
                        print(f"You lost 20 blood. Blood remaining: {self.user.blood}")
                        return

                    print("\nChoose an item to use:")
                    for i, item in enumerate(self.user.Inventory.items.keys(), 1):
                        print(f"{i}. {item}")

                    #player selects a weapon
                    try:
                        selection = int(input("Enter item number: "))
                        print("\n")
                        selected_item = list(self.user.Inventory.items.keys())[selection - 1]

                        #some special effects, that you have to imagine in your head
                        if selected_item == "Alien Gun":
                            print("*Pew Pew!* Energy pulses burst from the Alien Gun!")
                        elif selected_item == "Alien Knife":
                            print("*Shing!* You slash through the air with the Alien Knife!")
                        elif selected_item == "Alien Bomb Launcher":
                            print("*BOOM!* The launcher erupts with a thunderous blast!")
                        elif selected_item == "Alien Snot":
                            print("*Splurt!* Gooey alien slime splashes everywhere!")
                        else:
                            print("*Thwack!* You swing your item with all your might!")

                        #weapon deals damage based on alien monster's weakness
                        if selected_item == monster["weakness"]:
                            monster["hp"] -= 50
                            print("It's super effective!")
                        else:
                            monster["hp"] -= 10
                            print("It hits!")

                        #if monster is still alive, it attacks back
                        if monster["hp"] > 0:
                            player_hp -= 20
                            print(f"{monster['name']} attacks! You lost 20 health points. Remaining HP: {player_hp}/100")
                            if player_hp <= 0:
                                print("You were knocked out in battle!")
                                print("Game Over, you ran out of Health.")
                                exit()
                        else:
                            print(f"\n{monster['name']} has been defeated!")
                            del self.monsters[self.current_location]
                            return

                        #game ends when player health is 0 
                        player_hp -= 20
                        if player_hp <= 0:
                            print(f"{monster['name']} attacks! You lost 20 health points. Remaining HP: {player_hp}/100")
                            print("You were knocked out in battle!")
                            print("GAME OVER, you ran out of Health.")
                            exit()
                        
                    #wrong move gets you killed too
                    except (ValueError, IndexError):
                        print("You fumbled and took damage while panicking!")
                        player_hp -= 20
                        if player_hp <= 0:
                            print(f"You lost 20 health. Remaining HP: {player_hp}/100")
                            print("You were knocked out in battle!")
                            print("Game Over, you ran out of Health.")
                            exit(0)
                        
                #50% chance of a successful escape from the alien monster
                elif action == "2":
                    if random.random() < 0.5:
                        print("You successfully escaped!")
                        print("You retreat to the Main Hub to recover.")
                        print("\n")
                        self.current_location = "Main Hub"
                        return
                    else:
                        print(f"You tried to run, but {monster['name']} blocked your path and struck you!")
                        player_hp -= 20
                        if player_hp <= 0:
                            print("You were knocked out while trying to flee!")
                            print("Game Over, you ran out of Health.")
                            return
                        print(f"You lost 20 health. Remaining HP: {player_hp}/100")
                else:
                    print("Invalid choice. Try again.")
