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

def add_item_barrel():
    add_item_id = input("What Item ID would you like to add? ")
    if add_item_id == 1:
        barrel_inventory += "Wooden Sword"
        print("Added", ItemID(1), "To the barrel.")
        step_1()
    else:
        step_1()

def remove_item_barrel():
    remove_item_id = input("What Item ID would you like removed? ")
    if remove_item_id == 1:
        barrel_inventory -= "Wooden Sword"
        print("Removed", ItemID(1), "from the barrel.")
        step_2()
    else:
        step_2()

def step_1():
    step_1_question = input("Would you like to add any items to the barrel? ")
    if step_1_question.lower == "yes":
        add_item_barrel()
    elif step_1_question.lower == "no":
        step_2()

def step_2():
    step_2_question = input("Would you like to remove anything from the barrel? ")
    if step_2_question.lower == "yes":
        remove_item_barrel()
        

start()
step_1()