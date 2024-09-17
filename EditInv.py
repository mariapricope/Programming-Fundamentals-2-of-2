# This is the Edit Inventory file EditInv.py
def edit_item():
    """Edits an existing item in the inventory by name."""
    from Inventory import import_inventory, export_inventory

    inventory = import_inventory()

    if not inventory:
        print("Inventory is empty. No item to edit.")
        return

    name = input("Enter item name to edit (or type 'exit' to cancel): ").strip().lower()
    if name == "exit":
        print("Edit operation cancelled.")
        return

    # Find item by name
    item_found = False
    for i, item in enumerate(inventory):
        if item[1].strip().lower() == name:
            item_found = True
            print(f"Current details - Name: {item[1]}, Quantity: {item[2]}, Price: £{item[3]:.2f}")
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_quantity = input("Enter new quantity (leave blank to keep current): ").strip()
            new_price = input("Enter new price (leave blank to keep current): ").strip()

            # Update item details if provided
            if new_name:
                inventory[i] = (item[0], new_name, inventory[i][2], inventory[i][3])
            if new_quantity:
                inventory[i] = (item[0], inventory[i][1], int(new_quantity), inventory[i][3])
            if new_price:
                inventory[i] = (item[0], inventory[i][1], inventory[i][2], float(new_price))

            export_inventory(inventory)
            print(f"Item ID {item[0]} updated successfully.")
            break

    if not item_found:
        print(f"No items with the name '{name}' found.")
