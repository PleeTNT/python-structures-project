'''
Barrels and Backpacks
Preston Anderson
This is intended to be the backend code for the inventory systems,
however eventually I will make this visual and forego the whole console situation.
Please excuse the jank! It'll be better I swear!
'''
#(personal note) Python Programming, for the absolute beginner - Michael Dawson, second edition

#dictionary for item ids
items = [
    {'ItemID': 1, 'Name': "Wooden Sword", 'MaxQuantity': 1},
    {'ItemID': 2, 'Name': "Health Potion", 'MaxQuantity': 5},
    {'ItemID': 3, 'Name': "Wooden Round Shield", 'MaxQuantity': 1},
    {'ItemID': 4, 'Name': "Gold Coin", 'MaxQuantity': 999},
    {'ItemID': 5, 'Name': "Leather Armor", 'MaxQuantity': 1}
]

def start():
    global backpack_inventory
    global barrel_inventory  
    barrel_inventory = ()
    backpack_inventory = ()  
    
    print("Greetings!")
    print("There is currently", len(backpack_inventory), "items in the backpack.")
    print("There is currently", len(barrel_inventory), "items in the barrel.")

    print("Let's help get you started, yes?")
    backpack_inventory = (
        "Wooden Sword",
        "Leather Armor",
        "Gold Coin",
    )
    print("I've added", backpack_inventory, "to the backpack.")

#def step_1():


start()