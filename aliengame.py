class Human:
    def __init__(self):
        self.__name = input("What is your character's name?: ")
        print("Hello Prisoner,", self.__name)

    def get_name(self):
        return self.__name
        
class Story:
    def __init__(self, player):  
        self.intro = (
            "In a world, where a species of Aliens set on world domination have arrived on Earth.\n"
            "It is up to one person to saßve the world and lead the resistance to fight back.\n"
            f"That person is {player.get_name()}.\n"  
            "You as a player will be on an alien mothership hovering over the earth and each of your decisions will have consequences...\n"
            "You will have many items to steal and use them to your best ability, but discreetly, or else bad things will happen..."
        )

