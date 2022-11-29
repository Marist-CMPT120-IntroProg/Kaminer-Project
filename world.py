import loc

s_mountain = "You slowly open your eyes and look around, all you see is clouds, there is a path to a cliff to your left, a path leading down straight ahead, and on your right a slope."
e_mountain = "The path on the left leads towards a beach and the one on the right drops down with a pair of skis at the top."
s_beach = "You decide to head down to the left towards the beach that goes in either direction as far as you can see."
e_beach = "Upon closer inspection you see some chairs and beach umbrellas along the beach, glancing at the ocean you see a giant shadow of a structure looming underwater."
s_ocean = "You enter the ocean to swim towards the mysterious underwater building."
e_ocean = "Taking a moment to stop and glance around underwater, you see beatiful coral all around almost as if the ocean is glowing. Fish dart in and out of the coral, you notice some sharks in the distance."
s_temple = "Inside the temple it's overgrown with coral, sharks dart in and out of the columns that look like they are about to fall any second."
e_temple = "Further in, swimming around the decrepit colums, you come upon a dias with a diagram depicitng a pathway to a ship."
s_ship = "Following the map, you surface next a half sunken ship, once on board all you see is how time has eaten away at the once beatiful craftsmanship."
e_ship = "Looking through the rotten deck of the ship you see the treasure you have been searching for."
s_cliff = "You can see the mast of a ship in the distance and an ocean that stretches as far as the eye can see."
e_cliff = "Around you is rocky terrain dotted with small plants. Behind one of the rocks you see a key glinting in the setting sun."
s_slope = "Going past where you started, taking the path on the right, you hop on the skis and start to descend"
e_slope = "Through the bottom of the clouds you see the snow covered landscape with sun beating down on it and a chairlift in the distance."
s_lift = "Once at the base of the chairlift, you can see rust covering the chairs."
e_lift = "Upon a closer look you see that the door to the control room is open and you spot a keyhole."
s_lodge ="Stopping right before the parking lot, you enter an old ski lodge."
e_lodge = "Once inside you see cans of food and mice scurrying around. Trays and utensils are strewn everywhere, as if people left in a hurry. Grabbing some of the untouched cans of food, you continue on skis down towards the parking lot."
s_lot = "You kick off your skis. Running through the parking lot, you glance around seeing how some of the cars are ensnared by vines. One even has a tree going through it. You begin to wonder not where you are but how long it has been."
e_lot = "Finally in the second to last row you find a car that stands alone, getting in and flipping down the visor a key falls in your lap. Turning the key in the ignition the car miracously sputters to life."


mountain_npc = "Welcome to the shadow realm weary traveler, my names Axel, to find the treasure that you seek, Polaris will start you down the right path. Let it be known while a riddle will give you an escape, beware the chair."
beach_npc = "Surfs up dude, you got to ride the wave all the way out, cause everyone\'s surfing"
ocean_npc = "You are underwater why would there be anyone here"
ship_npc = "A riddle for though who dares tread upon my ship, for I am Vinton \'Blunderbuss\' Holmes and this be my ship ye walk on. \n This item has shiny things inside,\n You\'d have to wait to figure out what,\n Once you have found \'X\' which marks the spot.\n What object is it?" 
lift_npc = "Rhonda is the name. \n This use to be a mountain of popularity before Itin, the God of Obsucirty, decided to punish pirates for stealing his treasure. The lift will still run, I lost the key near the mountain top many moons ago."  



class World:
    def __init__(self):
   
        
        self.all_locales = [
            loc.Locale("Mountain Top", s_mountain, e_mountain, False), 
            loc.Locale("Beach", s_beach, e_beach, False),
            loc.Locale("Ocean", s_ocean, e_ocean, False),
            loc.Locale("Temple", s_temple, e_temple, False),
            loc.Locale("Ship", s_ship,e_ship, False),
            loc.Locale("Cliff", s_cliff, e_cliff, False),
            loc.Locale("Ski Slope", s_slope, e_slope, False),
            loc.Locale("ChairLift", s_lift, e_lift, False),
            loc.Locale("Ski Lodge", s_lodge, e_lodge, False),
            loc.Locale("Parking Lot", s_lot, e_lot, False),

        ]

        self.movement = [
        #current_loc north south east west
        [self.all_locales[0], self.all_locales[1], None, self.all_locales[5], self.all_locales[6]], #mountain
        [self.all_locales[1], self.all_locales[2], self.all_locales[0], None, None], #beach
        [self.all_locales[2], self.all_locales[3], self.all_locales[1], None, None], #ocean
        [self.all_locales[3], None, self.all_locales[2], self.all_locales[4], None], #temple
        [self.all_locales[4], None, self.all_locales[5], None, self.all_locales[3]], #ship
        [self.all_locales[5], None, None, None, self.all_locales[0]], #cliff
        [self.all_locales[6], None, self.all_locales[7], self.all_locales[0], self.all_locales[8]], #slope
        [self.all_locales[7], self.all_locales[6], None, None, self.all_locales[8]], #lift
        [self.all_locales[8], None, None, self.all_locales[6], self.all_locales[9]], #lodge
        [self.all_locales[9], None, None, self.all_locales[8], None], #lot

        ]

        self.npc = [mountain_npc, beach_npc, ocean_npc, None, ship_npc, None, None, lift_npc, None, None]

        self.answers = ["treasure chest","treasure","buried treasure","chest"]
    
    def fetch_names(self):
        list_locations = []
        for i in range(0, len(self.all_locales)):
            list_locations.append(self.all_locales[i].name)
        return list_locations
    def lift_on(self):
        key = None
        if key == True:
            self.movement[8][3] = "Mountain Top"
        else:
            print("You are not carrying the key for this, go find it")
