

title = "Mountain Escape"
introduction = "- An interactive text adventure where you are stranded on top of a mountain with only one goal. Find the lost treasure stolen by pirates and escape. Navigate the snow ridden mountain and the ocean to find what you seek and get back to civilization safely. "
next = "Press ENTER to begin your quest"
mountain = "You slowly open your eyes and look around, all you see is clouds, there is a path to a cliff behind you, ahead there are two paths. One path on the left leading towards a beach and another drops down with a pair of skis at the top."
beach = "You decide to head down to the left towards the beach, that goes in either direction as far as you can see, once there in the distance you can see a structure underwater."
ocean = "Once you enter the ocean to swim towards the mysterious underwater building, there is beatiful coral all around, almost as if the ocean is glowing."
temple = "Inside the temple it is overgrown with coral, sharks darting in and out of the columns that look like they are about to fall any second. Further in you see a diagram depicitng a pathway to a ship."
ship = "Following the map, you surface next a half sunken ship, once on board all you see is how time has eaten away at the once beatiful craftsmanship. Looking through the rotten deck of the ship you see the treasure you have been searching for."
cliff = "After grabbing the treasure, you look around and see a rope ladder on the side of the mountain. Climbing up the ladder you see the area where you started. Around you is rocky terrain dotted with small plants."
slope = "Going past where you started, you hop on the skis and start to descend clutching the treasure.Finally below the clouds you see the snow covered landscape with sun beating down on it and a chairlift in the distance."
lift = "Once at the base of the chairlift, you hear it creaking along and realize ever so slowly its operational, choosing to continue down the slope towards a ski lodge and parking lot dotted with vehicles."
lodge ="Stopping right before the parking lot, you enter an old ski lodge. Once inside you see cans of food and mice scurrying around. Trays and utensils are strewn everywhere, as if people left in a hurry. You grab some closed cans of food and continue on skis down towards the parking lot."
lot = "Realizing escape is near, you kick off your skis. As you run through the parking lot, you glance around seeing how some of the cars are ensnared by vines. One even has a tree going through it. You begin to wonder not where you are but how long it has been"
credits = "As you pick a car that is not destroyed, you hear a voice emenating from all arouind that says, thank you and goodbye."
def game(): 
    

    print(title + introduction)

    start = input(next)

    print(mountain) #1

    start = input(next)

    print(beach) #2

    start = input(next)

    print(ocean) #3

    start = input(next)

    print(temple) #4

    start = input(next)

    print(ship) #5

    start = input(next)

    print(cliff) #6

    start = input(next)

    print(slope) #7

    start = input(next)

    print(lift) #8

    start = input(next)

    print(lodge) #9

    start = input(next)

    print(lot) #10

    start = input(next)

    print(credits)
game()