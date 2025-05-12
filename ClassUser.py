import sqlite3
from ClassInventory import Inventory

import time
#Time will be used later as a consequence tool.
class User:
    #User class is made to work with the story class in where the player can input their name.
    #it also establishes the blood level and consequence system set to zero which will be used later on.
    def __init__(self, inventory=None):
        self.name = input("\nWhat is your character's name?: ")
        print("\nYou're finally awake!\n")
        self.blood = 100
        self.Inventory = Inventory(self)
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
        print('\n')
        
        return True

    def total_blood_usage(self):
        return sum(self.Inventory.items.values())
    
    def rest(self):
        #This is a function that lets the user rest to recover blood
        print("You're resting to recover blood.")
        self.blood += 10
        print(f"Blood remaining: {self.blood}/100")
        return self.blood