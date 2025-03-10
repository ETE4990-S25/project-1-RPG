import math
import random

def d6roll():
    return random.randint(1,6)

def d10roll():
    return random.randint(1,10)

def statroll():
    statlist = []
    for i in range(4):
        statlist.append(d6roll())
    statlist.remove(min(statlist))
    finalstat = sum(statlist)
    return finalstat

def hproll():
    hitpoints = 0
    for i in range(5):
        hitpoints += d10roll()
    return hitpoints

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        
        # Generate stats
        self.strength = statroll()
        self.dexterity = statroll()
        self.constitution = statroll()
        self.intelligence = statroll()
        self.wisdom = statroll()
        self.charisma = statroll()
        
        # Calculate HP
        self.hitpoints = hproll() + 5 * (math.floor((self.constitution-10)/2))

        # Hidden level (using name mangling)
        self.__level = 1

        # Initialize inventory and gold
        self.inventory = []  # To hold loot items
        self._gold = 0  # Private gold attribute
    
    def add_gold(self, amount):
        """Add gold to the player."""
        self._gold += amount

    def get_gold(self):
        """Get the current amount of gold the player has."""
        return self._gold

    def add_to_inventory(self, item):
        """Add an item to the player's inventory."""
        self.inventory.append(item)

    def get_inventory(self):
        """Get the player's current inventory."""
        return self.inventory
    
    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}")
        print(f"Hitpoints: {self.hitpoints}")

    def level_up(self):
        self.__level += 1
        print(f"{self.name} has leveled up to Level {self.__level}!")

    def get_level(self):
        print("You're level: ")
        return self.__level



