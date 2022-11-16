import world
import loc


class player:
    def __init__(self,p_name, world = "Shadow Realm",current_loc = "Mountain Top",counter = 0,score = 0):
        self.name = p_name
        self.world = world
        self.current_loc = current_loc
        self.count = counter
        self.score = score
        
    def username(self, p_name):
       self.p_name = str(input("Please type your username and hit enter: "))
       return self.p_name

    def move(current_loc, direction):
        
        new_loc = world.all_locales[locations.index(current_loc)][direction]

        return new_loc

    def arrived(self,counter):
        if loc.was_visted == False:
        counter = counter +  1
        return counter

    def points(new_loc,score):
        if new_loc["was_visited"] == False:
            new_loc["was_visited"] = True
            score = score + 100
                            
        current_loc = new_loc

        return current_loc, score
    


