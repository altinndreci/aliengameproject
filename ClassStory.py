from ClassUser import User
import random
#story class that has the game map, alien encounter, and main storyline
class Story:
    def __init__(self, user):
        self.user = user
        self.current_location = "Main Hub"
        self.player_hp = 100
        player_name=self.user.get_name()

        #alien spaceship map layout
        self.game_map = {
            "Main Hub": {
                "Recovery Chamber": 1,
                "Red Chamber": 2,
                "Green Chamber": 3,
                "Blue Chamber": 4
            },
            "Recovery Chamber": {"Main Hub": 1},
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
            "The Final Chamber": {
                "name": "Darth Khan",
                "description": "A towering figure in black armor stands at the center of the room. His lightsaber ignites as he speaks with chilling calm: 'Superior minds conquer all... with force.'",
                "weakness": "Alien Snot",
                "hp": 100
            }
        }

        #game intro
        self.intro = (
            "A dead silence hangs over Earth. An alien military has swept in,\n"
            "herding the last of humanity into iron cells aboard a vast, sun‑eclipsing mothership.\n"
            f"{user.get_name()}, you are the last hope to spark the final rebellion in a world drowning in dread.\n"
            "Each corridor throbs with otherworldly whispers and the distant echo of tortured screams.\n"
            "By day’s flicker, you’ll scavenge forbidden tools, beak alien locks with shaking hands.\n"
            "One misstep summons a shriek that chills your blood—and then, oblivion.\n"
            "\n"
            "Make your way through the twisted chambers, breach the Final Chamber, and face the tyrant known only as Darth.\n"
            "There is no retreat. One spark of courage, one act of defiance—everything rides on you.\n"
        )

    #function teling you where you are and where you can go
    def show_map(self):
        print(f"\nYou are currently in: {self.current_location}")
        print("You can go to:")
        for destination in self.game_map.get(self.current_location, {}):
            print(f"- {destination}")

        #unlocking the final chamber where the final boss is after defeating the 3 aliens
        if self.current_location == "Main Hub" and all(
            chamber not in self.monsters for chamber in ["Red Chamber", "Green Chamber", "Blue Chamber"]
        ):
            print("- The Final Chamber (Unlocked)")
        print()
        
    #function allowing you to travel around the spaceship
    def travel(self, destination=None):
        #Always show available destinations first
        print("\nAvailable destinations:")
        available_destinations = list(self.game_map.get(self.current_location, {}).keys())
        
        #Add Final Chamber option if conditions are met
        if (self.current_location == "Recovery Chamber" and 
            all(chamber not in self.monsters for chamber in ["Red Chamber", "Green Chamber", "Blue Chamber"])):
            available_destinations.append("The Final Chamber")

        if not available_destinations:
            print("There are no available destinations from your current location.")
            return

        #Display numbered menu of destinations
        for i, dest in enumerate(available_destinations, 1):
            print(f"{i}. {dest}")

        #Get user choice
        while True:
            try:
                choice = input("\nEnter the number of your destination: ")
                choice_num = int(choice)
                
                if 1 <= choice_num <= len(available_destinations):
                    destination = available_destinations[choice_num - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(available_destinations)}")
            except ValueError:
                print("Please enter a valid number")

        #Handle Final Chamber access
        if destination == "The Final Chamber":
            if self.current_location != "Recovery Chamber":
                print("You must pass through the Recovery Chamber to access The Final Chamber.")
                return
            if any(chamber in self.monsters for chamber in ["Red Chamber", "Green Chamber", "Blue Chamber"]):
                print("You feel a strong force blocking the path. Defeat all other aliens first.")
                return
            self.current_location = "The Final Chamber"
            print("\nYou have entered: The Final Chamber")
            self.trigger_encounter()
        elif destination in self.game_map.get(self.current_location, {}):
                self.current_location = destination
                print(f"\nYou have entered: {destination}")

                #notifying player of the boss
                if destination == "Main Hub" and all(
                    chamber not in self.monsters for chamber in ["Red Chamber", "Green Chamber", "Blue Chamber"]):
                    print("A distant *BOOM* echoes through the walls...")
                    print("You turn your head. It came from the Recovery Chamber.")
                    print("Something... or someone... has awakened.\n")

        #recover HP if in Recovery Chamber
                if destination == "Recovery Chamber":
                    if self.player_hp < 100:
                        self.player_hp = 100
                        print("You rest in the chamber and recover your health. HP fully restored to 100!")
                    else:
                        print("You are already at full health. You take a quick breather anyway.")
                self.trigger_encounter()
        
        else:
            print("You can't get there from here.")

    #map locations connected to the map using a dictionary
    def draw_map(self):
        location_symbols = {
            "Main Hub": "[Main Hub]",
            "Recovery Chamber": "       [Recovery Chamber]",
            "Red Chamber": "        [Red Chamber]",
            "Green Chamber": "[Green Chamber]",
            "Blue Chamber": "[Blue Chamber]",
            "The Final Chamber": "       [The Final Chamber]"
        }

        #prints the map of the spaceship using key characters
        print("\nAlien Mothership Map:")
        print("         " + location_symbols["Red Chamber"])
        print("                       |")
        print(location_symbols["Green Chamber"] + " - " + location_symbols["Main Hub"] + " - " + location_symbols["Blue Chamber"])
        print("                       |")
        print("         " + location_symbols["Recovery Chamber"])

        if all(chamber not in self.monsters for chamber in ["Red Chamber", "Green Chamber", "Blue Chamber"]):
            print("                       |")
            print("         " + location_symbols["The Final Chamber"])
        print()

    #encounter function that has the combat mechanic
    def trigger_encounter(self):
        if self.current_location in self.monsters:
            monster = self.monsters[self.current_location]
            print(f"\nYou encounter {monster['name']}!")
            print(monster['description'])

            #combat loop until player or alien monster is defeated
            while monster["hp"] > 0 and self.player_hp > 0:
                print("\nBattle Menu:")
                print(f"Your HP: {self.player_hp}/100")
                print("1. Fight")
                print("2. Run")
                action = input("Choose an action: ")
                print("\n")

                #checks to see if the player has an item to attack with, sorry your hands are not registered weapons here buddy
                if action == "1":
                    if not self.user.Inventory.items:
                        print("You have no items to defend yourself! The alien attacks!")
                        self.player_hp -= 20
                        self.user.consequence += 1
                        print(f"You lost 20 hp. Remaining HP: {self.player_hp}/100")
                        if self.player_hp <= 0:
                            print("You were knocked out in battle!")
                            print("Game Over, you ran out of Health.")
                            exit()
                        continue
                    
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
                            self.player_hp -= 20
                            print(f"{monster['name']} attacks! You lost 20 health points. Remaining HP: {self.player_hp}/100")
                            if self.player_hp <= 0:
                                print("You were knocked out in battle!")
                                print("Game Over, you ran out of Health.")
                                exit()
                        else:
                            print(f"\n{monster['name']} has been defeated!")
                            print(f'Remaining player HP: {self.player_hp}/100')
                            print(f'The {self.current_location} is now empty...\n{self.user.get_name()}:"Is it over yet?..."\n')
                            del self.monsters[self.current_location]

                            #The Final Chamber has been passed then provide the victory & exit game, THE END.
                            if self.current_location == "The Final Chamber":
                                print("\nAs Darth Khan collapses, his blade clatters to the ground, pulsing faintly with dying alien energy...")
                                print(f"{self.user.get_name()} steps over the fallen tyrant, bloodied but unbroken.")
                                print("You take a final breath as alarms blare across the mothership.")
                                print("\n[!] THE CORE HAS BEEN DESTABILIZED")
                                print("With seconds left, you sprint to the nearest escape pod.")
                                print("As you blast away from the mothership, it erupts in a silent, cosmic fireball above Earth.")
                                print("\nEarth is safe. For now...")
                                print("\n                    XenoBlood: Attack on Aliens")
                                print("                        Thank you for playing.")
                                print("                            THE END.\n")
                                exit(0)
                            return

                        #game ends when player health is 0 
                        if self.player_hp <= 0:
                            print("You were knocked out in battle!")
                            print("GAME OVER, you ran out of Health.")
                            exit()
                        
                    #wrong move gets you killed too
                    except (ValueError, IndexError):
                        print("You fumbled and took damage while panicking!")
                        self.player_hp -= 20
                        if self.player_hp <= 0:
                            print(f"You lost 20 health. Remaining HP: {self.player_hp}/100")
                            print("You were knocked out in battle!")
                            print("Game Over, you ran out of Health.")
                            exit(0)
                        
                #50% chance of a successful escape from the alien monster
                elif action == "2":
                    if random.random() < 0.5:
                        print("You successfully escaped!")
                        print("You retreated to the Main Hub.")
                        print("\n")
                        self.current_location = "Main Hub"
                        return
                    else:
                        print(f"You tried to run, but {monster['name']} blocked your path and struck you!")
                        self.player_hp -= 20
                        if self.player_hp <= 0:
                            print("You were knocked out while trying to flee!")
                            print("Game Over, you ran out of Health.")
                            return
                        print(f"You lost 20 health. Remaining HP: {self.player_hp}/100")
                else:
                    print("Invalid choice. Try again.")