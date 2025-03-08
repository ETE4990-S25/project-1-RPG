#stat generator
def d6roll():
    return random.randint(1,6)

import random

def statroll ():
    statlist = []
    for i in range(4):
        statlist.append(d6roll())
    statlist.remove(min(statlist))
    finalstat = sum(statlist)
    return(finalstat)

STR = statroll()
DEX = statroll()
CON = statroll()
INT = statroll()
WIS = statroll()
CHA = statroll()

print("Here are your stats: ")
print("Strength:", STR)
print("Dexterity:", DEX)
print("Constitution:", CON)
print("Intelligence:", INT)
print("Wisdom:", WIS)
print("Charisma:", CHA)