class Astronaut:
    def __init__(self, name, role, experience = 0, **kwargs):   #this class is defined with the name, role, experience and additional info. in kwargs
        self.name = name
        self.role = role
        self.experience = experience
        self.more_attributes_ = kwargs


    def gain_experience(self):
        self.experience = self.experience + 1       #experience earned will be captured on this method overriding the default value of 0


    def get_info(self):
        info = {    "name": self.name,      #this section will store the astronuats info in a dictionary
                    "role": self.role,
                    "experience": self.experience   }
        
        info.update(self.more_attributes_) 
        return info





class Spacecraft:
    def __init__(self, name, capacity):     #this class is defined with the name, capacity, and crew list of onboard astronauts 
        self.name = name
        self.capacity = capacity
        self.crew = [] 
    

    def add_astronaut(self, *astronauts):  #simply add astornauts if amount in crew is less than the capacity
        for astronaut in astronauts:
            if len(self.crew) >= self.capacity:
                print(f"Max Capacity Reached! {astronaut.name}, cannot aboard the mothership.")
            else:
                self.crew.append(astronaut)


    def list_crew(self):
        return [astronaut.name for astronaut in self.crew]
    

    def get_info(self):      #this section will store the spacecraft info in a dictionary
        return { "name": self.name,
                 "capacity": self.capacity,
                 "crew": self.list_crew() }







class Mission:
    def __init__(self, name, destination, spacecraft):      #this class is defined with the name, destination, and spacecraft assigned 
        self.name = name                                    
        self.destination = destination
        self.spacecraft = spacecraft
        self.status = "Planned"


    def launch(self):                           #launch status willl change when astornaut count is greater than zero
        if len(self.spacecraft.crew) > 0:
            self.status = "Ongoing"
        else:
            print(f"Minimum astronauts neeeded for mission '{self.name}' to proceed has not been aqcuired")


    def complete(self):
        self.status = "Completed"


    def get_info(self):
        return { "name": self.name,
                 "destination": self.destination,
                 "spacecraft": self.spacecraft.name,
                 "status": self.status }
    









    






