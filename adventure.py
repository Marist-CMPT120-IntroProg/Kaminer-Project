
counter = 0 
title = "Mountain Escape"
introduction = "- An interactive text adventure where you are stranded on top of a mountain with only one goal. Find the lost treasure stolen by pirates and escape. Navigate the snow ridden mountain and the ocean to find what you seek and get back to civilization safely. "
next = "Press ENTER to continue your quest"
begin = "Press ENTER to begin your quest"
closer = "Hit enter to take a closer look" 
mountain = "You slowly open your eyes and look around, all you see is clouds, there is a path to a cliff behind you, ahead there are two paths."
cmountain = "The path on the left leads towards a beach and the one on the right drops down with a pair of skis at the top."
beach = "You decide to head down to the left towards the beach that goes in either direction as far as you can see."
cbeach = "Upon closer inspection you see some chairs and beach umbrellas along the beach, glancing at the ocean you see a giant shadow of a structure looming underwater."
ocean = "You enter the ocean to swim towards the mysterious underwater building."
cocean = "Taking a moment to stop and glance around underwater, you see beatiful coral all around almost as if the ocean is glowing. Fish dart in and out of the coral, you notice some sharks in the distance."
temple = "Inside the temple it's overgrown with coral, sharks dart in and out of the columns that look like they are about to fall any second."
ctemple = "Further in, swimming around the decrepit colums, you come upon a dias with a diagram depicitng a pathway to a ship."
ship = "Following the map, you surface next a half sunken ship, once on board all you see is how time has eaten away at the once beatiful craftsmanship."
cship = "Looking through the rotten deck of the ship you see the treasure you have been searching for."
cliff = "After grabbing the treasure, you look around and see a rope ladder on the side of the mountain. Climbing up the ladder you see the area where you started."
ccliff = "Around you is rocky terrain dotted with small plants. Behind one of the rocks you see a key glinting in the setting sun."
slope = "Going past where you started, taking the path on the right, you hop on the skis and start to descend clutching the treasure."
cslope = "Through the bottom of the clouds you see the snow covered landscape with sun beating down on it and a chairlift in the distance."
lift = "Once at the base of the chairlift, you can see rust covering the chairs."
clift = "Upon a closer look you see that the door to the control room is open and you spot a keyhole. Using the key you found at the cliff, you slowly turn it and hear the ski lift start to turn on and creak alive."
lodge ="Stopping right before the parking lot, you enter an old ski lodge."
clodge = "Once inside you see cans of food and mice scurrying around. Trays and utensils are strewn everywhere, as if people left in a hurry. Grabbing some of the untouched cans of food, you continue on skis down towards the parking lot."
lot = "Realizing escape is near, you kick off your skis. As you run through the parking lot, you glance around seeing how some of the cars are ensnared by vines. One even has a tree going through it. You begin to wonder not where you are but how long it has been."
clot = "Finally in the second to last row you find a car that stands alone, getting in and flipping down the visor a key falls in your lap. Turning the key in the ignition the car miracously sputters to life."
credits = "As you leave, you hear a voice emenating from all arouind that says, thank you and goodbye."

def game(): 
    global counter

    print(title + introduction)

    start = input(begin)
    counter = counter + 1

    print(mountain) #1
    more = input(closer)
    print(cmountain) #1.5

    start = input(next)
    counter = counter + 1

    print(beach) #2
    more = input(closer)
    print(cbeach) #2.5

    start = input(next)
    counter = counter + 1

    print(ocean) #3
    more = input(closer)
    print(cocean) #3.5


    start = input(next)
    counter = counter + 1

    print(temple) #4
    more = input(closer)
    print(ctemple) #4.5


    start = input(next)
    counter = counter + 1

    print(ship) #5
    more = input(closer)
    print(cship) #5.5


    start = input(next)
    counter = counter + 1

    print(cliff) #6
    more = input(closer)
    print(ccliff) #6.5


    start = input(next)
    counter = counter + 1

    print(slope) #7
    more = input(closer)
    print(cslope) #7.5


    start = input(next)
    counter = counter + 1

    print(lift) #8
    more = input(closer)
    print(clift) #8.5


    start = input(next)
    counter = counter + 1

    print(lodge) #9
    more = input(closer)
    print(clodge) #9.5


    start = input(next)
    counter = counter + 1

    print(lot) #10
    more = input(closer)
    print(clot) #10.5


    start = input(next)
   


    print("Total number of stops:", counter)

    print(credits)
game()