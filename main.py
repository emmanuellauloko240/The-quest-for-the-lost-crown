# # # data = [True, False, True, True, False, True]
# # # true_count = sum(data) 
# # # print(true_count)  

# # # value = int(True)
# # # print(value)

# # # value = ("Hello")
# # # for values in value:
# # #     print(value)

# # # value = float(False)
# # # print(value)

# # # value = float("1.5e2")
# # # print(value)


# # print(bool(0))    
# # print(bool(1))    
# # print(bool(-5))   
# # print(bool(0.0))  
# # print(bool(3.14)) 
# # # Strings
# # print(bool(""))   
# # print(bool("hi")) 
# # print(bool(" "))  
# # # Collections
# # print(bool([]))   
# # print(bool([1]))  
# # print(bool({}))   
# # print(bool({"a": 1}))  
# # print(bool(()))   
# # print(bool((1,))) 
# # # None
# # print(bool(None)) 

# # name = "Amina"
# # current_location = "Otukpo"
# # energy = 85
# # game_running = True

# # print(name)
# # print(current_location)
# # print(energy)
# # print(game_running)

# # nickname = input("Enter your nickname: ")

# # print(f"Welcome, {nickname}!")

# # score = 0 

# # print (f"Your starting score is: {score}")

# # bonus_input = int(input("Enter bonus points to add: "))

# # current_score = 50

# # new_score = current_score + bonus_input

# # print(f"New score: {new_score}")

# # energy = 30

# # if energy < 50:
# #     print("Warning: Your energy is low! find some food.")
# # else:
# #     print("You're full of energy and ready to explore!")

# # game_running = True

# # if game_running == True: 
# #     print("The game loop is active. Have fun playing!")
# # else:
# #     print("Game over.")

# # has_key = True

# # if has_key:
# #     print("The door opens with a click!")
# # else:
# #     print("The door is locked. Find a key!")

# # A list of items in the player's inventory
# # inventory = ["magic sword", "health potion", "shield", "rusty key"]

# # print(inventory[0])  
# # print(inventory[5])  
# # shop_items = ["health potion", "mana potion", "iron sword", "magic ring"]

# # print(shop_items[-2])

# # inventory = ["magic sword", "health potion", "shield", "rusty key"]

# # print("You are carrying the following items:")
# # for item in inventory:

# #     print(f"- {item}")

# # enemies = ["Goblin","Orc", "Skeleton"]

# # for enemy in enemies:
# #     print(f"Watch out! a {enemy} is approaching!")

# # nickname = input("Enter your nickname: ")

# # print(f"Welcome, {nickname}!")

# # energy = 80

# # inventory = ["map","bread","torch"]

# # if energy >= 50:
# #     print("You're ready for the journey")
# # else:
# #     print("Warning: you're not eligible  for this journey🚫")

# # for invent in inventory:
# #     print(f"- {invent}")

# # def function_name(parameter):
# #     print(parameter)

# # function_name("Hello World!")

# # def greet_player(name):
# #     print(f"welcome back to the quest, {name}!")
# # greet_player("Amina")
# # greet_player("Chinedu")

# # def check_level(level):
# #     if level >= 10:
# #         print ("You are a master adventurer!")
# #     else:
# #         print("Keep training to level up!")
# # check_level(1)

# # game_running = True

# # while game_running:
# #     choice = input("Menu: [1] Status [2] Quit > ")
# #     if choice == "1":
# #         print("Energy: 100")
# #     elif choice == "2":
# #         print ("Goodbye!")
# #         game_running = False

# # loop = True

# # while loop:
# #     choice = input("Enter direction ('north', 'south') or 'quit': ").strip().lower()

# #     if choice == "quit":
# #         print("Game Over. Exiting...")
# #         break
# #     elif choice == "north" or choice == "south":
# #         print(f"You walked {choice}.")
# #     else:
# #         print("Invalid input! Please enter 'north', 'south', or 'quit'.")
# #         continue

# # secret_passphrase = input("Enter the secret_passphrase: ").strip().lower()

# # if secret_passphrase == "open sesame":
# #     print("Access granted!")
# # else:
# #     print("Access  denied!")

# # items = ["map"]

# # if "rope" not in items:
# #     items.append("rope")
# # print(f"Total items in inventory: {len(items)}")
# # print(f"Current items: {items}")

# # if "map" in items:
# #     items.remove("map")
# #     print("You used/dropped the map!")
# # print(f"Updated items: {items}")

# # player = {
# #     "name": "Emiene",
# #     "gold": 50,
# #     "weapon": "iron sword"
# # }

# # shield_status = player.get("shield")
# # print(shield_status)

# player_inventory = {
#     "potion": 3,
#     "sword": 1
# }

# # if "magic-ring" in player_inventory:
# #     print("You have a magic ring")
# # else:
# #     print("You don't have a magic ring")

# bool = None
# if player_inventory.get("magic-ring") != bool:
#     print("you have a magic ring")
# else:
#     print("You don't have magic ring")