from world import *
from loc import *
from player import *

begin = "Press ENTER to begin your quest"
username = None

W = World()
P = Player(username, "Shadow Realm")
L = Locale()

mountain = W.all_locales[0]
beach =  W.all_locales[1]
ocean =  W.all_locales[2]
temple =  W.all_locales[3]
ship =  W.all_locales[4]
cliff =  W.all_locales[5]
slope =  W.all_locales[6]
lift =  W.all_locales[7]
lodge =  W.all_locales[8]
lot =  W.all_locales[9]

locations  = [mountain, beach, ocean, temple, ship, cliff, slope, lift, lodge, lot ]

def initiation():
    global introduction
    global username


    title = ("\u0332".join("Mountain Escape"))
    print(title)
    username = str(input("Please type your username and hit enter: "))
    introduction = "An interactive text adventure where you are stranded on top of a mountain with only one goal. " + username.capitalize() + ", you must find the lost treasure stolen by pirates and escape. Navigate the snow ridden mountain and the ocean to find what you seek and get back to civilization safely."
    print(introduction)
    start = input(begin)
    print(mountain.name)
    mountain.was_visted = True
    

def ending():
    credits = "As you leave, you hear a voice emenating from all arouind that says, thank you " + username + " for finding my treasure that was stolen long ago. I bid you farwell."
    copyright = ("\u0332".join("Copyright 2022 by Tyler Kaminer"))
    print("Total number of locations visited:", Player.counter)
   
    print(credits)
    print(copyright)
    print(Player.counter)
    print(Player.score)



def game(): 
    
    global commands
    global direction
   
    initiation()
#########################################

    commands = ["north","south","east","west","examine", "help","quit"]
    
    while True:
    
        user_movement = input("Which direction would you like to go next: ").lower() 
        
        if user_movement in commands:
            
            if user_movement == commands[0]: #north
                direction = 1
                new_loc, counter = Player.move(current_loc,direction)
                if Player.new_loc == None:
                    print("You have hit an invisible wall, please pick a different direction")
                    continue
                else:
                     current_loc,score = Player.points(new_loc, score)
                
            elif user_movement == commands[1]: #south
                direction = 2
                new_loc, counter = Player.move(current_loc,direction)
                if Player.new_loc == None:
                    print("You have hit an invisible wall, please pick a different direction")
                    continue
                else:
                     current_loc,score = Player.points(new_loc, score)
                
                

            elif user_movement == commands[2]: #east
                direction = 3
                new_loc, counter = Player.move(current_loc,direction)
                if Player.new_loc == None:
                    print("You have hit an invisible wall, please pick a different direction")
                    continue
                else:
                     current_loc,score = Player.points(new_loc, score)
                
            elif user_movement == commands[3]: #west
                direction = 4
                new_loc, counter = Player.move(current_loc,direction)
                if Player.new_loc == None:
                    print("You have hit an invisible wall, please pick a different direction")
                    continue
                else:
                     current_loc,score = Player.points(new_loc, score)

            elif user_movement == commands[4]: #examine
                print(current_loc["details"])
                
            elif user_movement == commands[5]: #help
                print("Valid commands are north, south, east, west, help, and quit")
            elif user_movement == commands[6]: #quit
                break
        else: 
            print("Please enter a valid command")
            continue
    ending()     
game()