from os import system

class Game:

    def handle_input(request):
        
        while True:
            userInput = input().lower()

            if userInput in request:
                return userInput
            
            print('Invalid input, try again')

    #Handles the title screen
    #NOTE: THIS SHOULD ALSO BE ABLE TO HANDLE THINGS LIKE LOOKING AT SAVES AND STATS and SHIT'
    def title_screen():
        while True:
            print('''
************************************************************************
.____                  __               ________       .__       .___._.
|    |    ____   _____/  |_    ____    /  _____/  ____ |  |    __| _/| |
|    |   /  _ \ /  _ \   __\  /    \  /   \  ___ /  _ \|  |   / __ | | |
|    |__(  <_> |  <_> )  |   |   |  \ \    \_\  (  <_> )  |__/ /_/ |  \|
|_______ \____/ \____/|__|   |___|  /  \______  /\____/|____/\____ |  __
        \/                        \/          \/                  \/  \/
************************************************************************
                            NEW GAME
                            CONTINUE
                            QUIT
            ''')
            if Game.handle_input(['new game', 'profiles', 'quit']) == 'new game':
                break
    
    def shopping(player, shop):

        while True:

            print(shop.shopkeeper.intro, end = '\n')
            print(f'Your gold: {player.wealth}')
            print('Item : Cost\n')

            for item in [*shop.items]:
                print(f'{item} : {shop.items[item].worth}')
            
            request = Game.handle_input([*shop.items] + ['stop'])

            if request == 'stop':
                break
            else:
                player.attain(shop.items[request])

#Handles all things player stats and handling
class Player:

    def __init__(self, name, type):

        self.name = name

        self.health = 100
        self.maxHealth = 100
        self.attack = [0,2]
        self.armor = 0
        self.status = {}
        self.wealth = 100
        self.questLog = {}
        self.backpack = []
        self.equipped = {'rhand':'', 'lhand':'', 'head':'', 'torso':'', 'ring1':'', 'ring2':''}
        
    def equip(self, item):
        
        #Checks if there's an item in the slot
        #If so, unequips the previous item
        #Then, inserts the item into the right item slot in 'equipped'
        for slot in item.slot:
            if self.equipped[slot] != '':
                self.unequip(self.equipped[slot])
            self.equipped.update({slot:item.name})
    
        #Checks the name of the item's effect and modifies the player's respective attribute
        for effectKey in item.effects.keys():
            if effectKey == 'health':
                self.maxhealth += item.effects[effectKey]
            elif effectKey == 'attack':
                self.attack[0] += item.effects[effectKey][0]
                self.attack[1] += item.effects[effectKey][1]
            elif effectKey == 'armor':
                self.armor += item.effects[effectKey]
            elif effectKey == 'status':
                self.status.update(item.effects[effectKey])

    def attain(self, item):
        self.backpack.append({item.name: item})          

    def unequip(self, item):
        pass

class Item:
    
    def __init__(self, name, worth, slot):
        self.name = name
        self.worth = worth
        self.slot = slot
        self.effects = {}

    def add_effect(self, effect):
        self.effects.update(effect)

class Tavern:

    def __init__(self, name):
        self.name = name

class Shop:

    def __init__(self, name, shopkeeper):
        self.name = name
        self.items = {}
        self.shopkeeper = shopkeeper
    
    def add_item(self, item):
        self.items.update({item.name: item})

class ShopKeeper:

    def __init__(self, name):
        self.name = name
        self.intro = 'The name is Buford, what you looking for today?'

class Location:

    def __init__(self, name):
        self.name = name
        self.places = {}

    def add_place(self, place):
        self.places.update({place.name : place})
        
class Dungeon:

    def __init__(self):
        pass



