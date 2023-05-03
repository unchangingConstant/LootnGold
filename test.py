#Tree checker function

import assets as a
import pprint

item_sword = a.Item('sword', 10, 'rHand')
item_sword.add_effect({'attack': [5, 5]})

player = a.Player('Fighter','wee')

def convertObject(object):
    return object.__dict__

pprint.pprint(convertObject(item_sword))
pprint.pprint(convertObject(player))