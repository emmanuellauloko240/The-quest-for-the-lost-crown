hero_identity = {
    "nickname": "",
    "health": 100
}

hero_identity["nickname"] = input("What's your hero name: ").strip().lower()

health = 100

inventory_list = ["map", "Torch"]

print(f"Welcome, {hero_identity["nickname"]}! Your journey beginns.")

loop = True

Menu = input("[1] Explore the dark hallway, [2] Quit game: " ) 
while loop:
    if Menu == "[1]":
        print("uhmmmm..enjoy your game")
        break
    elif Menu == "[2]":
        print("Game over. Exiting.....")
        break
    else:
        print("invalid menu option🙂")
        break
