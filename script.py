from aliengame import Person 
from aliengame import Story


player = Person()
story = Story(player)  # Pass the player object
print(story.intro)
