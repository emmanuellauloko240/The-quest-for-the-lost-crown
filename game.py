hero_identity = {
    "nickname": "",
    "health": 100
}

hero_identity["nickname"] = input("What's your hero name: ").strip().lower()

health = 100

inventory_list = ["map", "Torch", "potion"]

print(f"Welcome, {hero_identity['nickname']}! Your journey beginns.")

loop = True

while loop:
    Menu = input("\n[1] Explore the dark hallway\n[2] Quit game\n[3] Check Stats\n[4] Drink potion\nEnter your choice: " ).strip() 
    
    if Menu == "[1]" or  Menu == "1":
        if "Torch" in inventory_list:
            print("\n🔥 Your torch lights the dark hallway! You walk safely through.")
        else:
            print("\n🙈 It's pitch black! You trip in the dark and lose 20 health.")
            hero_identity["health"] -= 20
        
    elif Menu == "[2]" or Menu == "2":
        print("\nGame over. Exiting.....")
        loop = False
    elif Menu == "[3]" or Menu == "3":
        print("\n--- HERO STATS ---")
        print(f"Name: {hero_identity['nickname']}")
        print(f"Health: {hero_identity['health']}")
        print("Inventory:")
        for item in inventory_list:
            print(f"  - {item}")
        print("------------------")
    elif Menu == "4" or Menu == "[4]":
        # Check if the player has a potion
        if "potion" in inventory_list:
            hero_identity["health"] += 25
            if hero_identity["health"] > 100:
                hero_identity["health"] = 100 
            
            inventory_list.remove("potion")
            print(f"\n🧪 You drank a health potion! Health restored to {hero_identity['health']}.")

        else:
            print("\n❌ You don't have any potions left in your inventory!")
        




        
    else:
        print("invalid menu option🙂......Please try again")
