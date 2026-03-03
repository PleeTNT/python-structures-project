#Backpacks and Barrels
#This project was fun :)

#dictionary for item ids
items = [
    {'ItemID': 1, 'Name': "Wooden Sword", 'MaxQuantity': 1},
    {'ItemID': 2, 'Name': "Health Potion", 'MaxQuantity': 5},
    {'ItemID': 3, 'Name': "Wooden Round Shield", 'MaxQuantity': 1},
    {'ItemID': 4, 'Name': "Gold Coin", 'MaxQuantity': 999},
    {'ItemID': 5, 'Name': "Leather Armor", 'MaxQuantity': 1},
    {'ItemID': 6, 'Name': "Stone Sword", 'Max Quantity': 1}
]

#Start dialogue, gives you items to start off with and moves to the menu
def start():
    barrel_inventory = []
    backpack_inventory = []  
    
    print("Greetings!")
    print("There is currently", len(backpack_inventory), "items in the backpack.")
    print("There is currently", len(barrel_inventory), "items in the barrel.")

    print("Let's help get you started, yes?")
    backpack_inventory += [
        "Wooden Sword",
        "Leather Armor",
        "Gold Coin",
    ]
    print("I've added", backpack_inventory, "to the backpack.")
    return backpack_inventory, barrel_inventory

#The menu, pretty self explanitory here
def menu(backpack_inventory, barrel_inventory):
    print("\n"
          "\n"
          "\n"
          "1: Add an item to the backpack\n"
          "2: Remove an item from the backpack\n"
          "3: Move an item from the backpack to the barrel\n"
          "4: Move an item from the barrel to the backpack\n"
          "5: List both inventories\n"
          "6: Show Item IDs\n"
          "7: Exit"
          "\n"
          "\n"
          "\n")
    menu_option = input("What would you like to do? ")
    if menu_option == "1":
        add_item_backpack(backpack_inventory)
    elif menu_option == "2":
        remove_item_backpack(backpack_inventory)
    elif menu_option == "3":
        move_backpack_to_barrel(backpack_inventory, barrel_inventory)
    elif menu_option == "4":
        move_barrel_to_backpack(backpack_inventory, barrel_inventory)
    elif menu_option == "5":
        list_inventories(backpack_inventory, barrel_inventory)
    elif menu_option == "6":
        list_item_ids(items)
    elif menu_option == "7":
        print("Goodbye!")
        return False
    else:
        print("Invalid option. Please try again.")
    return True

#Ask for the item the user would want to be added, and also how many will be added
def add_item_backpack(backpack_inventory):
    try:
        add_item_id = int(input("What Item ID would you like to add? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if not (1 <= add_item_id <= len(items)):
        print("Item ID not recognized.")
        return
    try:
        quantity = int(input("How many would you like to add? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return
    item = items[add_item_id - 1]
    name = item["Name"]
    max_qty = item.get("MaxQuantity")
    current_count = backpack_inventory.count(name)
    if current_count + quantity > max_qty:
        print(f"Cannot add {quantity} {name}: would exceed max quantity ({max_qty}). Current: {current_count}")
        return
    for _ in range(quantity):
        backpack_inventory.append(name)
    print(f"Added {quantity} {name} to the backpack.")
    return backpack_inventory

#Remove items
def remove_item_backpack(backpack_inventory):
    try:
        remove_item_id = int(input("What Item ID would you like removed? "))
    except ValueError:
        print("That's not possible, try again.")
        return
    if not (1 <= remove_item_id <= len(items)):
        print("Item ID not recognized.")
        return
    try:
        quantity = int(input("How many would you like to remove? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return
    name = items[remove_item_id - 1]["Name"]
    current_count = backpack_inventory.count(name)
    if current_count == 0:
        print(f"Cannot remove {name}: not in the backpack.")
        return
    if quantity > current_count:
        print(f"Cannot remove {quantity} {name}: only have {current_count}.")
        return
    for _ in range(quantity):
        backpack_inventory.remove(name)
    print(f"Removed {quantity} {name} from the backpack.")
    return backpack_inventory

#Move items from the backpack to the barrel, can crash if you are trying to move a ghost item
def move_backpack_to_barrel(backpack_inventory, barrel_inventory):
    try:
        move_item_id = int(input("What Item ID would you like to move to the barrel? "))
    except ValueError:
        print("That isn't possible, please try again.")
        return
    if not (1 <= move_item_id <= len(items)):
        print("Item ID not recognized.")
        return
    name = items[move_item_id - 1]["Name"]
    if name not in backpack_inventory:
        print(f"Cannot move {name}: not in the backpack.")
        return
    backpack_inventory.remove(name)
    barrel_inventory.append(name)
    print("Moved", name, "to the barrel.")
    return backpack_inventory, barrel_inventory

#Move items from the barrel to the backpack, can crash if you are trying to move a ghost item
def move_barrel_to_backpack(backpack_inventory, barrel_inventory):
    try:
        move_item_id = int(input("What Item ID would you like to move to the backpack? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if not (1 <= move_item_id <= len(items)):
        print("Item ID not recognized.")
        return
    name = items[move_item_id - 1]["Name"]
    if name not in barrel_inventory:
        print(f"Cannot move {name}: not in the barrel.")
        return
    barrel_inventory.remove(name)
    backpack_inventory.append(name)
    print("Moved", name, "to the backpack.")

#Shows inventories of the barrel and backpack
def list_inventories(backpack_inventory, barrel_inventory):
    print("Backpack Inventory:", backpack_inventory)
    print("Barrel Inventory:", barrel_inventory)

#Displays the IDs of the items and the names of the items
def list_item_ids(items):
    for item in items:
        print(f"{item['ItemID']}: {item['Name']}")

#Pulls all of the tuples down and runs the start code, then loops everything to the menu
if __name__ == "__main__":
    backpack_inventory, barrel_inventory = start()
    repeat = True
    while repeat == True:
        repeat = menu(backpack_inventory, barrel_inventory)