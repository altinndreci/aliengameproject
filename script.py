from aliengame import Person, Story


player = Person()
story = Story(player)  # Pass the player object
print(story.intro)

player.inventory.add_item("Alien Gun", 30)
print (player.inventory.items)
