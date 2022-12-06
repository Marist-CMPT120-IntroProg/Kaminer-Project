from world import *
from loc import *
from player import *



begin = "\nPress ENTER to begin your quest"
username = None
key = None


def initiation():
    global introduction
    global username
    global W
    global P

    W = World()
    P = Player(username, W)


    title = ("\u0332".join("\nMountain Escape") )
    print(title)
    username = str(input("\nPlease type your username and hit enter: "))
    introduction = "\n"  '\033[33m' "An interactive text adventure where you are stranded on top of a mountain with only one goal. " + username.capitalize() + ", you must find the lost treasure stolen by pirates and escape. Navigate the snow ridden mountain and the ocean to find what you seek and get back to civilization safely." '\033[0m'
    print(introduction)
    start = input(begin)
    print(W.all_locales[0].summary)
    W.all_locales[0].was_visited = True

def ending():
    while True:
        play = input("\nWould you like to replay the game? Yes? No?: ").lower()
        print("\n Total number of locations visited:", P.counter)
        print("\n Total Score:", P.score)
        if play == "yes":
            
            game()

        elif play == "no":

            credits = " \nAs you leave, you hear a voice emenating from all arouind that says, thank you " + username + " for looking for my treasure that was stolen long ago. I bid you farwell."
            copyright = ("\u0332".join("Copyright 2022 by Tyler Kaminer"))
            print("\n" + credits)
            print("\n" + copyright)
            exit()

        else:
            print("\nPlease choose between yes or no")
            continue
def game(): 
    
    global commands
    global direction
   
    initiation()
#########################################

    commands = ["north","south","east","west","examine", "interact","help","quit", "invictus"]
    
    while True:
    
        user_movement = input("\n"  '\033[92m' "Which direction would you like to go next:"  '\033[0m').lower() 
        
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
                if P.talk() == False:
                    print("\n" '\033[91m' "Itin has claimed your soul, goodbye."'\033[0m')
                    break
            elif user_movement == commands[6]: #help
                print("\nValid commands are north, south, east, west, examine, interact, help, and quit")

            elif user_movement == commands[7]: #quit
                break
        
            elif user_movement == commands[8]: # google the quote that vinton mumbled and type in the title of the poem
                    print("\n" '\033[91m' "The floor renches open and you fall into the abyss, looking above you, you spot a treasure chest glinting, grabbing it you open your eyes to realize you have escaped the Shadow Realm"'\033[0m')
                    break 
        else: 
            print("\nPlease enter a valid command")
            continue
    ending()     
game()