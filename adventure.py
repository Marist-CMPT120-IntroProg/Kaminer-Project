
counter = 0 
score = 0


begin = "Press ENTER to begin your quest"

mountain = {"name": "Mountain Top", "summary": "You slowly open your eyes and look around, all you see is clouds, there is a path to a cliff to your left, a path leading down straight ahead, and on your right a slope.", "details": "The path on the left leads towards a beach and the one on the right drops down with a pair of skis at the top.", "was_visited": True }
beach = {"name": "Beach", "summary": "You decide to head down to the left towards the beach that goes in either direction as far as you can see.", "details": "Upon closer inspection you see some chairs and beach umbrellas along the beach, glancing at the ocean you see a giant shadow of a structure looming underwater.", "was_visited": False }
ocean = {"name": "Ocean", "summary": "You enter the ocean to swim towards the mysterious underwater building.", "details": "Taking a moment to stop and glance around underwater, you see beatiful coral all around almost as if the ocean is glowing. Fish dart in and out of the coral, you notice some sharks in the distance.", "was_visited": False }
temple = {"name": "Temple", "summary": "Inside the temple it's overgrown with coral, sharks dart in and out of the columns that look like they are about to fall any second.", "details": "Further in, swimming around the decrepit colums, you come upon a dias with a diagram depicitng a pathway to a ship.", "was_visited": False }
ship = {"name": "Ship", "summary": "Following the map, you surface next a half sunken ship, once on board all you see is how time has eaten away at the once beatiful craftsmanship.", "details": "Looking through the rotten deck of the ship you see the treasure you have been searching for.", "was_visited": False }
cliff = {"name": "Cliff", "summary": "You can see the mast of a ship in the distance and an ocean that stretches as far as the eye can see.", "details": "Around you is rocky terrain dotted with small plants. Behind one of the rocks you see a key glinting in the setting sun.", "was_visited": False }
slope = {"name": "Ski Slope", "summary": "Going past where you started, taking the path on the right, you hop on the skis and start to descend", "details": "Through the bottom of the clouds you see the snow covered landscape with sun beating down on it and a chairlift in the distance.", "was_visited": False }
lift = {"name": "Chairlift", "summary": "Once at the base of the chairlift, you can see rust covering the chairs.", "details": "Upon a closer look you see that the door to the control room is open and you spot a keyhole.", "was_visited": False }
lodge = {"name": "Ski Lodge", "summary": "Stopping right before the parking lot, you enter an old ski lodge.", "details": "Once inside you see cans of food and mice scurrying around. Trays and utensils are strewn everywhere, as if people left in a hurry. Grabbing some of the untouched cans of food, you continue on skis down towards the parking lot.", "was_visited": False }
lot = {"name": "Parking Lot", "summary": "You kick off your skis. Running through the parking lot, you glance around seeing how some of the cars are ensnared by vines. One even has a tree going through it. You begin to wonder not where you are but how long it has been.", "details": "Finally in the second to last row you find a car that stands alone, getting in and flipping down the visor a key falls in your lap. Turning the key in the ignition the car miracously sputters to life.", "was_visited": False }

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