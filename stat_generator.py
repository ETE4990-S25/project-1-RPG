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
        self.gold = 50  # Private gold attribute
    
    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, amount):
        if amount < 0:
            print("Gold cannot be negative.")
        else:
            self._gold = amount

    def add_to_inventory(self, item_name, quantity=1):
    # Check if item already exists in inventory
        for item in self.inventory:
            if item["name"] == item_name:
                item["quantity"] += quantity
                break
        else:
            # If item does not exist, add a new one
            self.inventory.append({"name": item_name, "quantity": quantity})


    def get_inventory(self):
        key_to_omit = ['id']  # List of keys to omit from printing
        if not self.inventory:
            return "Inventory is empty."

        inventory_str = "Inventory:\n"
        for item in self.inventory:
            item_info = ', '.join(f"{key}: {value}" for key, value in item.items() if key not in key_to_omit)
            inventory_str += f"- {item_info}\n"

        return inventory_str.strip()
    
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
        hp_gain = hproll() + math.floor((self.constitution-10)/2)
        self.hitpoints += max(hp_gain,1)
        print(f"{self.name} has leveled up to Level {self.__level}!")
        print(f"{self.name} gained {hp_gain} hitpoints")

    def get_level(self):
        print("You're level: ")
        return self.__level



