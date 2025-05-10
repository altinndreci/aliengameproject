from ClassUser import User

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
        for destination, distance in self.game_map[self.current_location].items():
            print(f"- {destination} (distance: {distance})")

    #function allowing you to travel around the spaceship
    def travel(self, destination):
        if destination in self.game_map[self.current_location]:
            self.current_location = destination
            print(f"\nYou move to: {destination}")
        else:
            print("You can’t get there from here.")

    #draws the map using key characters
    def draw_map(self):
        location_symbols = {
            "Main Hub": "[Main Hub]",
            "Alien Recovery Chamber": "       [Recovery Chamber]",
            "Red Chamber": "        [Red Chamber]",
            "Green Chamber": "[Green Chamber]",
            "Blue Chamber": "[Blue Chamber]"
        }


        # Highlight current location
        for key in location_symbols:
            if key == self.current_location:
                location_symbols[key] = "*" + location_symbols[key] + "*"

        print("\nAlien Mothership Map:")
        print("         " + location_symbols["Red Chamber"])
        print("                       |")
        print(location_symbols["Green Chamber"] + " - " + location_symbols["Main Hub"] + " - " + location_symbols["Blue Chamber"])
        print("                       |")
        print("         " + location_symbols["Alien Recovery Chamber"])
        print()

