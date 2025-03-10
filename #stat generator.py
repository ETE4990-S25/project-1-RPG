#stat generator
import math
def d6roll():
    return random.randint(1,6)

def d10roll():
    return random.randint(1,10)

import random

def statroll ():
    statlist = []
    for i in range(4):
        statlist.append(d6roll())
    statlist.remove(min(statlist))
    finalstat = sum(statlist)
    return(finalstat)

def hproll ():
    hitpoints = 0
    for i in range(5):
        hitpoints += d10roll()
    print(hitpoints)
    return(hitpoints)



STR = statroll()
DEX = statroll()
CON = statroll()
INT = statroll()
WIS = statroll()
CHA = statroll()
HP = hproll() + 5 * (math.floor((CON-10)/2))

print("Here are your stats: ")
print("Strength:", STR)
print("Dexterity:", DEX)
print("Constitution:", CON)
print("Intelligence:", INT)
print("Wisdom:", WIS) 
print("Charisma:", CHA)
print("Hitpoints:", HP)