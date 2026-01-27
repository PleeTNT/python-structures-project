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
    barrel_inventory = ()
    backpack_inventory = ()  
    
    print("Greetings!")
    print("There is currently", len(backpack_inventory), "items in the backpack.")
    print("There is currently", len(barrel_inventory), "items in the barrel.")

    print("Let's help get you started, yes?")
    backpack_inventory += (
        "Wooden Sword",
        "Leather Armor",
        "Gold Coin",
    )
    print("I've added", backpack_inventory, "to the backpack.")

def menu(backpack):
    print("1: Add an item to the backpack"
          "2: Remove an item from the backpack"
          "3: Move an item from the backpack to the barrel"
          "4: Move an item from the barrel to the backpack"
          "5: List both inventories"
          "6: Exit")
    menu_option = input("What would you like to do? ")
    if menu_option == "1":
        



def add_item_backpack(backpack_inventory):
    add_item_id = input("What Item ID would you like to add? ")
    if add_item_id == 1:
        backpack_inventory += items(0)
        print("Added", items(0), "To the backpack.")

    else:


def remove_item_backpack(backpack_inventory):
    remove_item_id = input("What Item ID would you like removed? ")
    if remove_item_id == 1:
        backpack_inventory -= items(0)
        print("Removed", items(0), "from the backpack.")

    else:



start()  
menu()