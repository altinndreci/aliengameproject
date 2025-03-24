from ClassUser import User

class Story:        #Defining an overview of our story.
    def __init__(self, user):
        self.intro = (
            "\nYou are now in a world, where a species of Aliens are set on world domination and human imprisonment, have arrived on Earth.\n"
            "It is up to one person to escape and save the world to lead the resistance and fight back.\n"
            f"That person is {user.get_name()}.\n"  
            "You will be on an alien imprisonment camp located on the mothership hovering over earth & each of your decisions will have consequences...\n"
            "You will have many items to steal and use them to your best ability, but discreetly, or else bad things will happen...\n"
        )