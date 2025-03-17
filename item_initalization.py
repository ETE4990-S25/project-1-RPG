# %% [markdown]
# ## Import item list for game
# 

# %%
import json
import random
import stat_generator

# %%
with open('ItemData.json', "r") as file:
    itemdata = json.load(file)


# %% [markdown]
# ## Add damage number to items
# 

# %%
valid_types = {'Magic', 'Weapons'}

for item in itemdata['items']:  #iterate through list of dictionaries
# check if category has allowed values
    if item.get('category') in valid_types:
        #exclude arrows
        if "arrow" in itemdata['items']:
            continue
        item['Damage'] = random.randint(1,5)


# %% [markdown]
# # Add money values to items
# 

# %%
for item in itemdata['items']:
    name = item.get('name', '')
    category = item.get('category', '')
    if 'Empty' in name:
        item['Value'] = random.randint(1,5)
    elif 'General' in category:
        item['Value'] = random.randint(1,15)
    elif 'Magic' in category:
        item['Value'] = random.randint(10,20)
    elif 'Weapon' in category:
        item['Value'] = random.randint(10,20)
    elif 'Food' in category:
        item['Value'] = random.randint(1,5)
    else: 
        item['Value'] = random.randint(15,20)

# %% [markdown]
# ## Add AC Values to armor
# 

# %%
valid_armor = {'Armour'}

for item in itemdata['items']:
        # Exclude items with "ring" in the name (case-insensitive)
    if "ring" in item.get("name", "").lower():
        continue  
    if "helmet" in item.get("description", "").lower():
        continue 
    
    if item.get('category') in valid_armor:
        item['AC'] = random.randint(10,16)


# %% [markdown]
# ## Add potion traits
# 
# - Healing
# - Mana
# - General Power (damage boost)
# 

# %%

for item in itemdata['items']:   #Navigate items in each dictionary
    name = item.get('name', '')

    if "Green" in name:
        if "Large" in name:
            item["Mana"] = random.randint(30, 50)  # Large Green Potion gets the most
        elif "Small" in name:
            item["Mana"] = random.randint(5, 10)  # Small Green Potion gets the lowest 
        else:
            item["Mana"] = random.randint(10, 20)  # Default to Regular if no size isn't in name
    elif "Red" in name:
        if "Large" in name:
            item["Health"] = random.randint(20, 30)  
        elif "Small" in name:
            item["Health"] = random.randint(5, 10)  
        else:
            item["Health"] = random.randint(10, 20)
    elif "Pink" in name:
        if "Large" in name:
            item["Health"] = random.randint(15, 20)  
        elif "Small" in name:
            item["Health"] = random.randint(1, 5)  
        else:
            item["Health"] = random.randint(5, 10)
    elif "Black" in name:
        if "Large" in name:
            item["Power"] = random.randint(20, 30) 
        elif "Small" in name:
            item["Power"] = random.randint(5, 10)  
        else:
            item["Power"] = random.randint(10, 20)
    elif "Blue" in name:
        if "Large" in name:
            item["Mana"] = random.randint(20, 30)
            item["Power"] = random.randint(20, 30)  
        elif "Small" in name:
            item["Mana"] = random.randint(5, 10)
            item["Power"] = random.randint(5, 10)  
        else:
            item["Mana"] = random.randint(10, 20)
            item["Power"] = random.randint(10, 20)
    elif "Orange" in name:
        if "Large" in name:
            item["Mana"] = random.randint(20, 30)
            item["Power"] = random.randint(20, 30)  
        elif "Small" in name:
            item["Mana"] = random.randint(5, 10)
            item["Power"] = random.randint(5, 10)  
        else:
            item["Mana"] = random.randint(10, 20)
            item["Power"] = random.randint(10, 20)


# %% [markdown]
# # Generate inventory
# 

# %%
def generate_inventory():
    loot = []
    gold = random.randint(20,50)
    
    # Generate 15 random items
    for i in range(15):
        item_id = random.randint(1, 130)  # Ensure the index is within bounds
        item = itemdata['items'][item_id]
        
        # Add the item to the loot list (we'll add to the player's inventory later)
        loot.append(item)
    
    return loot, gold


# %% [markdown]
# # Store interaction Version 2

# %%
def store_interaction(player):
    shop, shop_gold = generate_inventory()  
    
    print('Welcome to my shop, adventurer!')
    print('Please have a look at my wares:\n')
    print(f'If you wish to sell, I have {shop_gold} gold on hand.\n')
    
    # Display player's gold
    print(f'You have {player._gold} Gold to spend.\n')

    # Display the shop items with numbers
    for index, item in enumerate(shop, start=1):
        print(f"{index}. {item['name']}")
        print(item['description'])
        print(f"{item['Value']} Gold")
        print('-----------------------------------')
    
    # Display player inventory
    print("\nYour current inventory:")
    player.display_inventory()

    # Purchase loop
    while True:    
        # Get the item choice from the player
        choice = input("Enter the number of the item you wish to buy (or type 'exit' to leave): ")
        
        if choice.lower() == 'exit':
            print("You leave the shop.")
            break
        
        # Validate input for item choice
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(shop):
            print("Invalid choice. Please choose a valid item number.")
            continue
        
        # Input to index
        item_index = int(choice) - 1
        item_to_buy = shop[item_index]
        
        # Ask how many they want to buy
        quantity = input(f"How many {item_to_buy['name']}s do you want to buy? ")
        
        # Validate quantity input
        if not quantity.isdigit() or int(quantity) < 1:
            print("Please enter a valid quantity.")
            continue
        
        quantity = int(quantity)
        total_cost = item_to_buy['Value'] * quantity
        
        # Check if player has enough gold
        if player._gold >= total_cost:
            print(f"You bought {quantity} {item_to_buy['name']}(s) for {total_cost} Gold.")
            
            # Add the correct quantity of the item to the player's inventory (gear)
            for _ in range(quantity):
                player.inventory.add_item(item_to_buy['name'], quantity)
            
            # Deduct gold from the player
            player._gold -= total_cost

            # Remove the bought item from the shop
            del shop[item_index]
            
        else:
            print("You don't have enough gold to buy that many.")
        
        # If the shop is empty, end the interaction
        if not shop:
            print("The shop is now empty. You leave.")
            break





# %%
def equip_from_inventory(player):
    weapons = []
    armor = []

    # Find full item data based on stored inventory names
    for item in player.inventory.items:
        full_item = next((i for i in itemdata['items'] if i.get("name") == item["name"]), None)
        if full_item:
            if "Damage" in full_item:
                weapons.append(full_item)
            elif "AC" in full_item:
                armor.append(full_item)

    # Display available weapons
    print("Weapons available to equip:")
    if weapons:
        for idx, weapon in enumerate(weapons, 1):
            print(f"{idx}. {weapon['name']} (Damage: {weapon['Damage']})")
    else:
        print("No weapons available.")

    # Display available armor
    print("\nArmor available to equip:")
    if armor:
        for idx, arm in enumerate(armor, 1):
            print(f"{idx}. {arm['name']} (AC: {arm['AC']})")
    else:
        print("No armor available.")

    # Ask the player to equip an item
    item_type = input("\nWhat would you like to equip? (weapon/armor): ").strip().lower()
    
    if item_type == "weapon" and weapons:
        choice = input(f"Enter the number of the weapon you want to equip (1-{len(weapons)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(weapons):
            selected_weapon = weapons[int(choice) - 1]
            player.equipped_weapon = selected_weapon  # Equip the weapon
            print(f"You have equipped {selected_weapon['name']} (Damage: {selected_weapon['Damage']})!")
        else:
            print("Invalid selection, no weapon equipped.")
    
    elif item_type == "armor" and armor:
        choice = input(f"Enter the number of the armor you want to equip (1-{len(armor)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(armor):
            selected_armor = armor[int(choice) - 1]
            player.equipped_armor = selected_armor  # Equip the armor
            print(f"You have equipped {selected_armor['name']} (AC: {selected_armor['AC']})!")
            player.base_AC += selected_armor['AC']  # AC should exist on Player
        else:
            print("Invalid selection, no armor equipped.")
    
    else:
        print("Invalid item type or no items available.")
