from world import *
from loc import *
from sys import exit






class Player:
    def __init__(self,p_name, world):
        self.p_name = p_name
        self.world = world
        self.current_loc = world.all_locales[0]
        self.counter = 0
        self.score = 100
        self.key = False
        
        
        
    

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
            print("\n" '\033[35m' "You have hit an invisible wall, please pick a different direction" '\033[0m')
            
        else:
            print(new_loc)
            self.current_loc,self.score = self.points(new_loc, self.score)
   
        
    def talk(self):
        if self.world.npc[self.world.all_locales.index(self.current_loc)] == ship_npc:
    
            if self.score < 1000:
                print(ship_npc)
                riddle_answer = input("\nWhat is the answer to Vintons Riddle: ").lower() 
                if riddle_answer in self.world.answers:
                    self.score += 1000
                    
                    password = "\n" '\033[91m' "My head is bloody, but unbowed....\n I am the master of my fate;\n I am the captain of my soul."'\033[0m'

                    print("\n" '\033[94m' " HUZZAH! You have guessed correctly."'\033[0m')
                    print("\n" '\033[94m' " As Vinton fades away you hear him mumble, \n"+ password +'\033[0m' "\n")
                    
                    
                    return self.score, password
                else:
                    print("\nYou have guessed wrong, may Davy Jones claim your soul")
            
            else:
                print("\n" '\033[35m' "You have already guessed correctly, Vinton is longer of this world." '\033[0m')

        elif self.world.npc[self.world.all_locales.index(self.current_loc)] == lift_npc:
            print(lift_npc)
            if self.key == True:
                while True:
                    
                    go = input("\n" '\033[94m'"Oh you already have the key, well get it started and hop on."'\033[0m' "\n Would you like to ride the chairlift? Yes? No?: ").lower()
                    if go == "yes":
                        print("\n"'\033[91m'" MWHAHAHAHAHA \nI, Itin will now claim your soul"'\033[0m' )
                        return False
                    elif go == "no": 
                        print("\n" '\033[35m' "The chairlift starts running as you turn the key, you hear a voice beckoning you in the other direction further down the mountain"'\033[0m')
                        break
                    else:
                        print("\nPlease pick yes or no")
                        continue
        elif self.world.npc[self.world.all_locales.index(self.current_loc)] == None:
            print("\n" '\033[35m' "You look around but there is no one in sight"'\033[0m')
        else:
            print(self.world.npc[self.world.all_locales.index(self.current_loc)])

    def inspection(self,current_loc):
        if current_loc.name == self.world.all_locales[5].name:
            self.key = True
            print(current_loc.details)
            
        else: 
            print(current_loc.details)
            
        return self.key
    

    
        

    


