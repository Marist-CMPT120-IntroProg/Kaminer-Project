
counter = 1 

next = "Press ENTER to continue your quest"
begin = "Press ENTER to begin your quest"
closer = "Hit enter to take a closer look" 

d_mountain = "You slowly open your eyes and look around, all you see is clouds, there is a path to a cliff to your left, a path leading down straight ahead, and on your right a slope."
e_mountain = "The path on the left leads towards a beach and the one on the right drops down with a pair of skis at the top."
d_beach = "You decide to head down to the left towards the beach that goes in either direction as far as you can see."
counter = 1 

begin = "Press ENTER to begin your quest"
d_mountain = "You slowly open your eyes and look around, all you see is clouds, there is a path to a cliff to your left, a path leading down straight ahead, and on your right a slope."
e_mountain = "The path on the left leads towards a beach and the one on the right drops down with a pair of skis at the top."
d_beach = "You decide to head down to the left towards the beach that goes in either direction as far as you can see."
e_beach = "Upon closer inspection you see some chairs and beach umbrellas along the beach, glancing at the ocean you see a giant shadow of a structure looming underwater."
d_ocean = "You enter the ocean to swim towards the mysterious underwater building."
e_ocean = "Taking a moment to stop and glance around underwater, you see beatiful coral all around almost as if the ocean is glowing. Fish dart in and out of the coral, you notice some sharks in the distance."
d_temple = "Inside the temple it's overgrown with coral, sharks dart in and out of the columns that look like they are about to fall any second."
e_temple = "Further in, swimming around the decrepit colums, you come upon a dias with a diagram depicitng a pathway to a ship."
d_ship = "Following the map, you surface next a half sunken ship, once on board all you see is how time has eaten away at the once beatiful craftsmanship."
e_ship = "Looking through the rotten deck of the ship you see the treasure you have been searching for."
d_cliff = "You can see the mast of a ship in the distance and an ocean that stretches as far as the eye can see."
e_cliff = "Around you is rocky terrain dotted with small plants. Behind one of the rocks you see a key glinting in the setting sun."
d_slope = "Going past where you started, taking the path on the right, you hop on the skis and start to descend"
e_slope = "Through the bottom of the clouds you see the snow covered landscape with sun beating down on it and a chairlift in the distance."
d_lift = "Once at the base of the chairlift, you can see rust covering the chairs."
e_lift = "Upon a closer look you see that the door to the control room is open and you spot a keyhole."
d_lodge ="Stopping right before the parking lot, you enter an old ski lodge."
e_lodge = "Once inside you see cans of food and mice scurrying around. Trays and utensils are strewn everywhere, as if people left in a hurry. Grabbing some of the untouched cans of food, you continue on skis down towards the parking lot."
d_lot = "You kick off your skis. Running through the parking lot, you glance around seeing how some of the cars are ensnared by vines. One even has a tree going through it. You begin to wonder not where you are but how long it has been."
e_lot = "Finally in the second to last row you find a car that stands alone, getting in and flipping down the visor a key falls in your lap. Turning the key in the ignition the car miracously sputters to life."




def initiation():
    global introduction
    global username

    title = ("\u0332".join("Mountain Escape"))
    print(title)
    username = str(input("Please type your username and hit enter: "))
    introduction = "An interactive text adventure where you are stranded on top of a mountain with only one goal. " + username.capitalize() + ", you must find the lost treasure stolen by pirates and escape. Navigate the snow ridden mountain and the ocean to find what you seek and get back to civilization safely."
    print(introduction)
    start = input(begin)
    print(d_mountain)

def ending():
    credits = "As you leave, you hear a voice emenating from all arouind that says, thank you " + username + " for finding my treasure that was stolen long ago. I bid you farwell."
    copyright = ("\u0332".join("Copyright 2022 by Tyler Kaminer"))
    print("Total number of locations visited:", counter)
    print("All locations visited: ", *visited)
    print(credits)
    print(copyright)


def game(): 
    global counter
    global visited
    initiation()
#########################################

    commands = ["north","south","east","west","examine", "help","quit"]
    mountain = "mountain top"
    beach = "beach"
    ocean = "ocean"
    temple = "temple"
    ship = "ship"
    cliff = "cliff"
    slope = "ski slope"
    lift = "chairlift"
    lodge = "ski lodge"
    lot = "parking lot"
    location = "mountain top"
    visited = [mountain] 
    




    while True:
    
        user_movement = input("Which direction would you like to go next: ").lower() 
        
        if user_movement in commands:
            
            if user_movement == commands[0]: #north
                if location == mountain:
                    location = beach
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_beach)
                        visited.append(location)
                        counter += 1
                    
                elif location == beach:
                    location = ocean
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_ocean)
                        visited.append(location)
                        counter += 1 
                    
                elif location == ocean:
                    location = temple
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_temple)
                        visited.append(location)
                        counter += 1
                    
                    
                elif location == lift:
                    location = slope
                    print("You are back on the slope")
                else: 
                    print("You bump into an invisible wall and hear a voice telling you to go in a diffrent direction")  
            elif user_movement == commands[1]: #south
                if location == ship:
                    location = cliff
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_cliff)
                        visited.append(location)
                        counter = counter + 1
                    
                    
                elif location == slope:
                    location = lift
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_lift)
                        visited.append(location)
                        counter += 1 
                    
                elif location == temple:
                    location = ocean
                    print("You are back in the ocean")
                elif location == ocean:
                    location = beach
                    print("You are back at the beach")
                elif location == beach:
                    location = mountain
                    print("You are back at the mountain top") 
                else: 
                    print("You bump into an invisible wall and hear a voice telling you to go in a diffrent direction")
            elif user_movement == commands[2]: #east
                if location == mountain:
                    location = cliff
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_cliff)
                        visited.append(location)
                        counter += 1 
                   
                elif location == temple:
                    location = ship 
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_ship)
                        visited.append(location)
                        counter += 1

                elif location == slope:
                    location = mountain
                    print("You are back at the mountain top")
                elif location == lodge:
                    location = slope
                    print("You are back on the slope")
                elif location == lot:
                    location = lodge
                    print("You are back at the lodge")
                else: 
                    print("You bump into an invisible wall and hear a voice telling you to go in a diffrent direction")
            elif user_movement == commands[3]: #west
                if location == mountain:
                    location = slope
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_slope)
                        visited.append(location)
                        counter += 1
                    
                elif location == slope:
                    location = lodge
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_lodge)
                        visited.append(location)
                        counter += 1
                    
                elif location == lodge:
                    location = lot
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_lot)
                        visited.append(location)
                        counter += 1
                    
                elif location == cliff:
                    location = mountain
                    print("You are back at the mountain top")

                elif location == lift:
                    location = lodge
                    if location in visited:
                        print("You are back at the " + location)
                        continue
                    else: 
                        print(d_lodge)
                        visited.append(location)
                        counter += 1

                elif location == ship:
                    location = temple
                    print("You are back in the temple")

                elif location == lot:
                    print("Do you have the treasure you are searching for? If yes type quit as your next direction to break the simulation.")
                else: 
                    print("You bump into an invisible wall and hear a voice telling you to go in a diffrent direction")

            elif user_movement == commands[4]: #examine
                if location == mountain:
                    print(e_mountain)
                elif location == beach:
                    print(e_beach)
                elif location == ocean:
                    print(e_ocean)
                elif location == temple:
                    print(e_temple)
                elif location == ship:
                    print(e_ship)
                elif location == cliff:
                    print(e_cliff)
                elif location == slope:
                    print(e_slope)
                elif location == lift:
                    print(e_lift)
                elif location == lodge:
                    print(e_lodge)
                elif location == lot:
                    print(e_lot)
                
            elif user_movement == commands[5]: #help
                print("Valid commands are north, south, east, west, help, and quit")
            elif user_movement == commands[6]: #quit
                break
        else: 
            print("Please enter a valid command")
            continue
    ending()     
game()
e_beach = "Upon closer inspection you see some chairs and beach umbrellas along the beach, glancing at the ocean you see a giant shadow of a structure looming underwater."
d_ocean = "You enter the ocean to swim towards the mysterious underwater building."
e_ocean = "Taking a moment to stop and glance around underwater, you see beatiful coral all around almost as if the ocean is glowing. Fish dart in and out of the coral, you notice some sharks in the distance."
d_temple = "Inside the temple it's overgrown with coral, sharks dart in and out of the columns that look like they are about to fall any second."
e_temple = "Further in, swimming around the decrepit colums, you come upon a dias with a diagram depicitng a pathway to a ship."
d_ship = "Following the map, you surface next a half sunken ship, once on board all you see is how time has eaten away at the once beatiful craftsmanship."
e_ship = "Looking through the rotten deck of the ship you see the treasure you have been searching for."
d_cliff = "You can see the mast of a ship in the distance and an ocean that stretches as far as the eye can see."
e_cliff = "Around you is rocky terrain dotted with small plants. Behind one of the rocks you see a key glinting in the setting sun."
d_slope = "Going past where you started, taking the path on the right, you hop on the skis and start to descend"
e_slope = "Through the bottom of the clouds you see the snow covered landscape with sun beating down on it and a chairlift in the distance."
d_lift = "Once at the base of the chairlift, you can see rust covering the chairs."
e_lift = "Upon a closer look you see that the door to the control room is open and you spot a keyhole."
d_lodge ="Stopping right before the parking lot, you enter an old ski lodge."
e_lodge = "Once inside you see cans of food and mice scurrying around. Trays and utensils are strewn everywhere, as if people left in a hurry. Grabbing some of the untouched cans of food, you continue on skis down towards the parking lot."
d_lot = "You kick off your skis. Running through the parking lot, you glance around seeing how some of the cars are ensnared by vines. One even has a tree going through it. You begin to wonder not where you are but how long it has been."
e_lot = "Finally in the second to last row you find a car that stands alone, getting in and flipping down the visor a key falls in your lap. Turning the key in the ignition the car miracously sputters to life."


# start = input(begin)
       # counter = counter + 1

       # print(d_mountain) #1
      #  more = input(closer)
       # print(cmountain) #1.5

     #   start = input(next)
     #   counter = counter + 1

     #   print(d_beach) #2
     #   more = input(closer)
     #   print(cbeach) #2.5

     #   start = input(next)
     #   counter = counter + 1

     #   print(d_ocean) #3
     #   more = input(closer)
     #   print(cocean) #3.5


     #   start = input(next)
     #   counter = counter + 1

     #  print(d_temple) #4
     #   more = input(closer)
     #   print(ctemple) #4.5


     #   start = input(next)
     #   counter = counter + 1

     #   print(d_ship) #5
     #   more = input(closer)
     #   print(cship) #5.5


     #   start = input(next)
     #   counter = counter + 1

     #   print(d_cliff) #6
     #   more = input(closer)
     #  print(ccliff) #6.5


     #  start = input(next)
     #   counter = counter + 1

     #   print(d_slope) #7
     #   more = input(closer)
     #   print(cslope) #7.5


     #   start = input(next)
     #   counter = counter + 1

     #   print(d_lift) #8
     #   more = input(closer)
     #   print(clift) #8.5


     #   start = input(next)
     #   counter = counter + 1

     #   print(d_lodge) #9
     #   more = input(closer)
     #   print(clodge) #9.5


     #   start = input(next)
     #   counter = counter + 1

     #   print(d_lot) #10
     #   more = input(closer)
     #   print(clot) #10.5


     #   start = input(next)
    


     #   print("Total number of stops:", counter)

     #   print(credits)