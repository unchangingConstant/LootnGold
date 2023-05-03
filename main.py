from Game import *
from assets import *

#Main game loop

while True:
    Game.title_screen()
    Game.shopping(player, loc_village.places['armory'])
    print(player.backpack)
