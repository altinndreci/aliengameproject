from aliengame import Human 
from aliengame import Story


player = Human()
story = Story(player)  # Pass the player object
print(story.intro)

