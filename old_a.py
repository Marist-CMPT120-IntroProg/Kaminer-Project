from world import *
from loc import *
from player import *

counter = 0 
score = 0


begin = "Press ENTER to begin your quest"

mountain = World.all_locales[0]
beach =  World.all_locales[1]
ocean =  World.all_locales[2]
temple =  World.all_locales[3]
ship =  World.all_locales[4]
cliff =  World.all_locales[5]
slope =  World.all_locales[6]
lift =  World.all_locales[7]
lodge =  World.all_locales[8]
lot =  World.all_locales[9]

locations  = [mountain, beach, ocean, temple, ship, cliff, slope, lift, lodge, lot ]
current_loc = locations[0]

movement = [
#current_loc north south east west
[mountain, beach, None, cliff, slope],
[beach, ocean, mountain, None, None],
[ocean, temple, beach, None, None],
[temple, None, ocean, ship, None],
[ship, None, cliff, None, temple],
[cliff, None, None, None, mountain],
[slope, None, lift, mountain, lodge],
[lift, slope, None, None, lodge],
[lodge, None, None, slope, lot],
[lot, None, None, lodge, None],

]

def initiation():
    global introduction
    global username


    title = ("\u0332".join("Mountain Escape"))
    print(title)
    username = str(input("Please type your username and hit enter: "))
    introduction = "An interactive text adventure where you are stranded on top of a mountain with only one goal. " + username.capitalize() + ", you must find the lost treasure stolen by pirates and escape. Navigate the snow ridden mountain and the ocean to find what you seek and get back to civilization safely."
    print(introduction)
    start = input(begin)
    print(mountain["summary"])
    mountain["was-visited"] = True
    

def ending():
    credits = "As you leave, you hear a voice emenating from all arouind that says, thank you " + username + " for finding my treasure that was stolen long ago. I bid you farwell."
    copyright = ("\u0332".join("Copyright 2022 by Tyler Kaminer"))
    print("Total number of locations visited:", counter)
   
    print(credits)
    print(copyright)
    print(counter)
    print(score)

def move(current_loc, direction):
    global new_loc
    
    new_loc = movement[locations.index(current_loc)][direction]
    return new_loc

def arrived(current_loc,counter):
    print(current_loc["summary"])
    counter = counter +  1
    return counter

def visited(new_loc,score):
    if new_loc["was_visited"] == False:
        new_loc["was_visited"] = True
        score = score + 100
                        
    current_loc = new_loc

    return current_loc, score

def game(): 
    global counter
    global current_loc 
    global commands
    global direction
    global score
   
    initiation()
#########################################

    commands = ["north","south","east","west","examine", "help","quit"]
    
    while True:
    
        user_movement = input("Which direction would you like to go next: ").lower() 
        
        if user_movement in commands:
            
            if user_movement == commands[0]: #north
                direction = 1
                move(current_loc,direction)
                if new_loc == None:
                    print("You have hit an invisible wall, please pick a different direction")
                    continue
                else:
                    current_loc,score = visited(new_loc,score)
                
                counter = arrived(current_loc,counter)
                
                
            elif user_movement == commands[1]: #south
                direction = 2
                move(current_loc,direction)

                if new_loc == None:
                    print("You have hit an invisible wall, please pick a different direction")
                    continue
                else:
                    current_loc,score = visited(new_loc,score)

                counter = arrived(current_loc,counter)
                
                

            elif user_movement == commands[2]: #east
                direction = 3
                move(current_loc,direction)

                if new_loc == None:
                    print("You have hit an invisible wall, please pick a different direction")
                    continue
                else:
                    current_loc,score = visited(new_loc,score)

                counter = arrived(current_loc,counter)
                
            elif user_movement == commands[3]: #west
                direction = 4
                move(current_loc,direction)

                if new_loc == None:
                    print("You have hit an invisible wall, please pick a different direction")
                    continue
                else:
                    current_loc,score = visited(new_loc,score)

                counter = arrived(current_loc,counter)

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