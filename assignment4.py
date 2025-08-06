# Build a basic inventory system for a small shop using Python. It will allow users to:

# View all items

# Add a new item

# Update item stock

# Delete an item

#  ** Calculate total stock value

#1. View all items
    # Inventory dictionary to hold items
inventory = {
    "Bread": {"remaining": 10, "price": 25},
    "Milk": {"remaining": 15, "price": 9},
    "Eggs": {"remaining": 48, "price": 3},
    "Milo": {"remaining": 20, "price": 5},
    "Gari": {"remaining": 5, "price": 6},
    "Sugar": {"remaining": 10, "price": 2}

}

def view_items():
    print("inventory:")
    for item, more_info in inventory.items():
        print(f"{item} - Remaining: {more_info['remaining']}, Price: GHC {more_info['price']}")

view_items()



#2. Add a new item

def add_item():
    item_name = input("Enter item name: ")
    
    if item_name in inventory:
        print(f"{item_name} already exists in inventory.")
        return
    
    remaining = int(input("Enter remaining stock: "))
    price = float(input("Enter price (GHC): "))
    
    inventory[item_name] = {"remaining": remaining, "price": price}
    print(f"{item_name} added to inventory.")

add_item()
view_items()


#3. Update item stock


def update_stock():
    item_name = input("Enter item name to update: ")
    
    if item_name in inventory:
        new_stock = int(input("Enter new stock amount: "))
        inventory[item_name]["remaining"] = new_stock
        print(item_name, "stock updated to", new_stock)
    else:
        print(item_name, "not found in inventory.")

update_stock()
view_items()


#4. Delete an item

def delete_item():
    item_name = input("Enter item name to delete: ")
    
    if item_name in inventory:
        del inventory[item_name]
        print(item_name, "has been deleted from inventory.")
    else:
        print(item_name, "not found in inventory.")

delete_item()
view_items()


#5.  ** Calculate total stock value

def total_value():
    total = 0
    for item in inventory:
        total += inventory[item]["remaining"] * inventory[item]["price"]
    print("Total stock value: GHC", total)

total_value()
view_items()
