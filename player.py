from world import *
from loc import *


class Player:
    def __init__(self,p_name, world):
        self.p_name = p_name
        self.world = world
        self.current_loc = world.all_locales[0]
        self.counter = 0
        self.score = 100
        
    

    def move(self, direction):
        
        new_loc = self.world.movement[self.world.all_locales.index(self.current_loc)][direction] 
        self.counter +=  1

        return new_loc, self.counter

    

    def points(self,new_loc,score):
        #how do I call the was_visited from loc
        if new_loc.was_visited == False:
            new_loc.was_visited = True
            self.score +=  100
                            
        current_loc = new_loc

        return current_loc, self.score

    def possible(self,direction):
        new_loc, self.counter = self.move(direction)
        if new_loc == None:
            print("You have hit an invisible wall, please pick a different direction")
            
        else:
            print(new_loc)
            self.current_loc,self.score = self.points(new_loc, self.score)
    


