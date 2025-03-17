import math
import random

def statroll():   # Roll 4 d6 and add the highest 3
    return sum(sorted(random.randint(1,6) for _ in range(4))[1:])

def hproll():
    return sum(random.randint(1,10) for _ in range(5))

class Inventory:
    def __init__(self):
        self.items = []  # Store inventory items

    def add_item(self, item_name, quantity=1):
        """Add a single item to the inventory"""
        for item in self.items:
            if item["name"] == item_name:
                item["quantity"] += quantity
                return
        self.items.append({"name": item_name, "quantity": quantity})

    def add_items(self, items):
        """Add multiple items at once"""
        for item in items:
            self.add_item(item["name"], item.get("quantity", 1))  # Ensure quantity is handled properly

    def get_inventory(self):
        """Return a formatted string of inventory contents"""
        if not self.items:
            return "Inventory is empty."
        return "\n".join(f"{item['name']} (x{item['quantity']})" for item in self.items)


class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        
        #Initalize the equipped weapon, armor | AC and base damage
        self.equipped_weapon = None
        self.equipped_armor = None
        self.base_AC = 10  # Default AC without armor
        self.base_damage = 1  # Default damage if unarmed
        self.combat_count = 0  # Track combat encounter
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
        self.inventory = Inventory()  # To hold loot items
        self._gold = 50  # Private gold attribute
    
    @property
    def gold(self):
        return self._gold



    @gold.setter
    def gold(self, amount):
        if amount < 0:
            print("Gold cannot be negative.")
        else:
            self._gold = amount
    
    def display_stats(self):
        equipped_AC = self.equipped_armor["AC"] if self.equipped_armor else 0
        equipped_Damage = self.equipped_weapon["Damage"] if self.equipped_weapon else 0

        
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}")
        print(f"Hitpoints: {self.hitpoints}")

        # Display modified AC and Damage
        print(f"Armor Class: {self.base_AC + equipped_AC}")
        print(f"Damage: {self.base_damage + equipped_Damage}")
        
        # Show equipped items
        print(f"Equipped Weapon: {self.equipped_weapon['name'] if self.equipped_weapon else 'None'}")
        print(f"Equipped Armor: {self.equipped_armor['name'] if self.equipped_armor else 'None'}")


    def level_up(self):
        self.__level += 1
        hp_gain = hproll() + math.floor((self.constitution-10)/2)
        self.hitpoints += max(hp_gain,1)
        print(f"{self.name} has leveled up to Level {self.__level}!")
        print(f"{self.name} gained {hp_gain} hitpoints")

    def get_level(self):
        print("You're level: ")
        return self.__level

    def add_to_inventory(self, items):
        """Add items to inventory (supports single item or list)"""
        if isinstance(items, list):  # Check if items is a list
            self.inventory.add_items(items)
        else:  # Otherwise, assume it's a single item
            self.inventory.add_item(items)

    def remove_item(self, item_name, quantity=1):
        """Remove an item from the inventory"""
        for item in self.inventory.items:
            if item["name"] == item_name:
                item["quantity"] -= quantity
                if item["quantity"] <= 0:
                    self.items.remove(item)
                return



    def display_inventory(self):
        """Display the player's inventory"""
        if not self.inventory.items:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory.items:
                print(f"{item['name']} (x{item['quantity']})")
    
    def level_up(player):
        # Define the number of encounters required for each level-up
        encounters_per_level = 3  # This can be adjusted or scaled based on player level

        # Check if player has reached the required encounters for a level up
        if player.combat_count >= encounters_per_level:
            player.level += 1
            player.combat_count = 0  # Reset combat count after leveling up
            print(f"\n🎉 {player.name} has leveled up to Level {player.level}!")

            # Allow player to allocate stat points on level up
            allocate_stat_points(player)

def allocate_stat_points(player):
    # This function can be customized to allow the player to choose how to allocate their points
    points_to_allocate = 5  # You can increase this number per level or based on player needs
    print(f"You have {points_to_allocate} stat points to allocate!")

    while points_to_allocate > 0:
        print(f"Current Stats: Strength: {player.strength}, Dexterity: {player.dexterity}, Intelligence: {player.intelligence}")
        print("Choose a stat to increase (1 for Strength, 2 for Dexterity, 3 for Intelligence):")
        choice = input("> ")

        if choice == "1":
            player.strength += 1
        elif choice == "2":
            player.dexterity += 1
        elif choice == "3":
            player.intelligence += 1
        else:
            print("Invalid choice. Try again.")
            continue

        points_to_allocate -= 1
        print(f"You have {points_to_allocate} stat points left.")

    print(f"New Stats: Strength: {player.strength}, Dexterity: {player.dexterity}, Intelligence: {player.intelligence}")





