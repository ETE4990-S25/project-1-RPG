import random
import time
import item_initalization
import stat_generator
import json

# Load monsters from a JSON file
with open('moblist.json', "r") as file:
    mobinfo = json.load(file)

# Function to get a random monster from the list
def get_random_monster():
    return random.choice(mobinfo)

# Turn-based combat function
def combat(player):
    monster = get_random_monster()
    
    print(f"\n⚔ A wild {monster['Name']} appears! ⚔")
    print(f"AC: {monster['AC']}, HP: {monster['HP']}")
    print(f"Attacks: {', '.join(monster['Attack'])}\n")
    
    monster_hp = monster['HP']
    
    # Determine turn order based on Dexterity
    player_turn = player.dexterity >= 10  # Adjust threshold as needed
    power_buff = 0  # Variable to track power potion effect

    while player.hitpoints > 0 and monster_hp > 0:
        if player_turn:
            print("\nYour turn! Choose an action:")
            print("1 Attack")
            print("2 Use Potion")
            print("3 Run Away")
            choice = input("> ")

            if choice == "1":
                # Apply power buff to damage if it's active
                damage = random.randint(1, 6) + player.strength + power_buff
                print(f"You attack {monster['Name']} for {damage} damage!")
                monster_hp -= damage

            elif choice == "2":
                if player.inventory:  # Ensure there's something to use
                    print("Select potion to use:")
                    for i, item in enumerate(player.inventory.items):
                        if 'Health' in item:
                            print(f"{i+1}. Health Potion ({item['Health']} HP)")
                        elif 'Mana' in item:
                            print(f"{i+1}. Mana Potion ({item['Mana']} Mana)")
                        elif 'Power' in item:
                            print(f"{i+1}. Power Potion (+{item['Power']} Damage)")

                    potion_choice = int(input("> ")) - 1
                    potion = player.inventory.items2[potion_choice]

                    if 'Health' in potion:
                        player.hitpoints += potion['Health']
                        print(f"You used a Health Potion! Healed {potion['Health']} HP")
                        player.inventory.remove(potion)

                    elif 'Mana' in potion:
                        # Example: Mana potion gives the player another attack this turn
                        print(f"You used a Mana Potion! You can attack twice this turn!")
                        # Allow the player to attack twice in this turn
                        damage = random.randint(1, 6) + player.strength
                        print(f"You attack {monster['Name']} for {damage} damage!")
                        monster_hp -= damage
                        player.inventory.remove(potion)

                    elif 'Power' in potion:
                        power_buff = potion['Power']  # Apply power buff to player damage
                        print(f"You used a Power Potion! Your damage is increased by {potion['Power']} this turn.")
                        player.inventory.remove(potion)

                else:
                    print("You have no potions!")

            elif choice == "3":
                if random.random() < 0.5:  # 50% escape chance
                    print("You successfully ran away!")
                    return
                else:
                    print("You failed to escape!")

            else:
                print("Invalid choice, turn wasted!")

        else:
            attack = random.choice(monster["Attack"])
            damage = random.randint(1, 6)  # Monster attack example
            print(f"{monster['Name']} uses {attack} for {damage} damage!")
            player.hitpoints -= damage

        print(f"📊 Player HP: {player.hitpoints} | {monster['Name']} HP: {monster_hp}")

        # Reset power buff after turn
        power_buff = 0

        # Switch turns
        player_turn = not player_turn
        time.sleep(1.5)

    if player.hitpoints <= 0:
        print("\n💀 You have been defeated!")
    elif monster_hp <= 0:
        print(f"\n🏆 You defeated {monster['Name']}!")
    
        # Increment combat count after each encounter
    player.combat_count += 1

    # Check if the player should level up
    player.level_up(player)


# Save the player's progress
def save_game(player):
    with open("save_game.json", "w") as file:
        save_data = {
            "name": player.name,
            "class": player.char_class,
            "stats": player.stats,
            "inventory": player.inventory.items
        }
        json.dump(save_data, file, indent=4)
    print("Game saved successfully.")

# Load the saved game data
def load_game():
    try:
        with open("save_game.json", "r") as file:
            save_data = json.load(file)
            player = stat_generator.Player(save_data["name"], save_data["class"])
            player.stats = save_data["stats"]
            player.inventory = save_data["inventory"]
            print(f"Game loaded: {player.name} the {player.char_class}")
            return player
    except FileNotFoundError:
        print("No saved game found. Starting a new game.")
        return None


# Adventure function that leads to combat encounters
def adventure(player):
    locations = ["exploring caves", "exploring plains", "exploring dungeon"]
    for _ in range(random.randint(3, 6)):
        print(random.choice(locations))
        time.sleep(1)
    combat(player)


# Main encounter loop where the player can choose actions
def encounter(player):
    while True:
        print("\nWhat would you like to do?")
        choice = input('1. Adventure\n2. Trade\n3. Equip gear\n4. Save and Quit\nEnter your choice: ')
        
        if choice == '1':
            adventure(player)
        elif choice == '2':
            item_initalization.store_interaction(player)
        elif choice == '3':
            item_initalization.equip_from_inventory(player)
        elif choice == '4':
            save_game(player)  # Save the game and exit
            break  # Exit the encounter loop, effectively quitting the game
        else:
            print('Invalid choice. Please choose 1, 2, 3, or 4')

            
            

# %%




