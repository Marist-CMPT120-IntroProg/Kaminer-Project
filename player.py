from world import *
from loc import *


class Player:
    def __init__(self,p_name, world):
        self.p_name = p_name
        self.world = world
        self.current_loc = World.all_locales[0].name
        self.counter = 0
        self.score = 0
        
    

    def move(self,current_loc, direction):
        
        new_loc = self.world.movement[self.world.fetch_names().index(current_loc)][direction] 
        self.counter +=  1

        return new_loc, self.counter

    

    def points(self,new_loc,score):
        #how do I call the was_visited from loc
        if new_loc.was_visited == False:
            new_loc.was_visited = True
            self.score +=  100
                            
        current_loc = new_loc

        return current_loc, self.score
    


