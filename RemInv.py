# This is the Remove Inventory file RemInv.py
def remove_item():
    """Removes all records of an item from the inventory based on item name."""
    from Inventory import import_inventory, export_inventory

    inventory = import_inventory()

    if not inventory:
        print("Inventory is empty. No item to remove.")
        return

    name = input("Enter item name to remove (or type 'exit' to cancel): ").strip().lower()
    if name == "exit":
        print("Remove operation cancelled.")
        return

    # Create a new inventory list excluding all items with the specified name
    new_inventory = [item for item in inventory if item[1].strip().lower() != name]

    if len(new_inventory) == len(inventory):
        print(f"No items with the name '{name}' were found in the inventory.")
    else:
        print(f"All items with the name '{name}' have been removed.")
        export_inventory(new_inventory)
