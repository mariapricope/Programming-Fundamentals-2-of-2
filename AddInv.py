def add_item():
    """Adds a new item to the inventory or updates an existing item."""
    from Inventory import import_inventory, export_inventory

    name = input("Enter item name: ").strip()
    quantity = int(input("Enter item quantity: ").strip())
    price = float(input("Enter item price: ").strip())

    inventory = import_inventory()

    # Check if the item already exists in the inventory
    existing_item = next((item for item in inventory if item[1].strip().lower() == name.lower()), None)

    if existing_item:
        # Update the existing item's quantity and price
        item_id, old_name, old_quantity, old_price = existing_item
        inventory = [(item_id, name, old_quantity + quantity, price) if item[0] == item_id else item for item in inventory]
    else:
        # Assign a new ID to the new item
        next_id = max(item[0] for item in inventory) + 1 if inventory else 1
        inventory.append((next_id, name, quantity, price))

    export_inventory(inventory)
    print(f"Item '{name}' added/updated successfully.")
