from world import *
from loc import *
from player import *



begin = "Press ENTER to begin your quest"
username = None
key = None
death = False






W = World()
P = Player(username, W)

def initiation():
    global introduction
    global username


    title = ("\u0332".join("Mountain Escape"))
    print(title)
    username = str(input("Please type your username and hit enter: "))
    introduction = "An interactive text adventure where you are stranded on top of a mountain with only one goal. " + username.capitalize() + ", you must find the lost treasure stolen by pirates and escape. Navigate the snow ridden mountain and the ocean to find what you seek and get back to civilization safely."
    print(introduction)
    start = input(begin)
    print(W.all_locales[0].summary)
    W.all_locales[0].was_visited = True

def ending():
    while True:
        play = input("Would you like to replay the game? Yes? No?: ").lower()
        if play == "yes":
            
            P.score = 100
            P.counter = 0
            P.current_loc = W.all_locales[0] # how do I make the entire game reset 
            game()

        elif play == "no":

            credits = " As you leave, you hear a voice emenating from all arouind that says, thank you " + username + " for finding my treasure that was stolen long ago. I bid you farwell."
            copyright = (" \u0332".join("Copyright 2022 by Tyler Kaminer"))
            print("\n" + credits + "\n")
            print("\n Total number of locations visited:", P.counter)
            print("\n Total Score:", P.score)
            print("\n" + copyright + "\n")
            break

        else:
            print("Please choose between yes or no")
            continue
def game(): 
    
    global commands
    global direction
   
    initiation()
#########################################

    commands = ["north","south","east","west","examine", "interact","help","quit", "invictus"]
    
    while True:
    
        user_movement = input("Which direction would you like to go next: ").lower() 
        
        if user_movement in commands:
            
            if user_movement == commands[0]: #north
                direction = 1
                P.possible(direction)
                
            elif user_movement == commands[1]: #south
                direction = 2
                P.possible(direction)

            elif user_movement == commands[2]: #east
                direction = 3
                P.possible(direction)
                
            elif user_movement == commands[3]: #west
                direction = 4
                P.possible(direction)
                

            elif user_movement == commands[4]: #examine
                P.inspection(P.current_loc)

            elif user_movement == commands[5]: #interact
                
                password = P.talk()

            elif user_movement == commands[6]: #help
                print("Valid commands are north, south, east, west, examine, interact, help, and quit")

            elif user_movement == commands[7]: #quit
                break
        
 
# how do I end the game entirely from inside 
# Make sure are variables that need to be reset if the game restarts are reset  
            elif user_movement == commands[8]: # google the quote that vinton mumbled and type in the title of the poem
                    print("The floor renches open and you fall into the abyss, looking above you, you spot a treasure chest glinting, grabbing it you open your eyes to realize you have escaped the Shadow Realm")
                    break 
        else: 
            print("Please enter a valid command")
            continue
    ending()     
game()