from Game import *
import os
import sys
import json
#sets working directory to path of script
os.chdir(sys.path[0])

player = Player('Fighter','wee')

item_sword = Item('sword', 10, 'rHand')
item_sword.add_effect({'attack': [5, 5]})

keeper_buford = ShopKeeper('buford')

shop_armory = Shop('armory', keeper_buford)
shop_armory.add_item(item_sword)

loc_village = Location('village')
loc_village.add_place(shop_armory)


#########################################################################################

#This is the beginning of the asset builder
#This is a function that will build game assets from a file
#This will allow easy modding for players and devs alike
#This code will also likely be used to implement save profiles

#########################################################################################

def cObj(object):
    return object.__dict__

def build(object):
    pass

#profiles (players)



#locations



#places (shops and taverns and shih)



#items
#Scrap this, instead, try creating a dictionary that has all the item names as keys and a list of their attributes as the values
save = open('save.json', 'w+')
json.dump(cObj(item_sword), save)

