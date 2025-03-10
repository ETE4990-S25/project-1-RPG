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
        item['AC'] = random.randint(1,3)


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
    for i in range(15):
        item_id = random.randint(1,131)
        loot.append(itemdata['items'][item_id]) 
    return loot, gold





# %%
def store():
    shop = generate_inventory()
    for item in shop:
        print(item['name']) 
        print(item['description'])
        print(item['Value'], 'Gold')
        print('-----------------------------------')



# %%
#def store():
#    shop = generate_inventory()
#    for item in shop['items']:
#        name = item.get('name', '')
#        if 'Pile' in name:
#            shop.pop()
            
#    for item in shop:
#        print(item['name']) 
#        print(item['description'])
#        print(item['Value'], 'Gold')
#        print('-----------------------------------')


#store()

# %% [markdown]
# # Function to open backpack

# %%
def Backpack():
    for item in gear:
        for key, value in item.items():
            if key != 'id':  # Exclude 'ID' key
                print(f"{key}: {value}")
        print('-----------------------------------')





