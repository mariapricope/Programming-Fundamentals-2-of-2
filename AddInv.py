# AddInv.py
from Inventory import Inventory
from Utils import get_input  # Import the helper function


class AddInventory:
    """
    Class to handle adding new items to the inventory.
    """

    def __init__(self, inventory):
        """
        Initialize with an inventory object.
        
        :param inventory: The Inventory object to modify.
        """
        self.inventory = inventory

    def add_item(self):
        """
        Adds a new item to the inventory by collecting input from the user.
        """
        while True:
            name = get_input("Enter item name (or type 'exit' to quit): ").strip()
            if name == "":
                print("Item name must be specified.")
            else:
                break

        quantity = int(get_input("Enter item quantity (or type 'exit' to quit): ").strip())
        price = float(get_input("Enter item price (or type 'exit' to quit): ").strip())

        # Generate next available item ID
        if self.inventory.inventory:
            next_id = max(item[0] for item in self.inventory.inventory) + 1
        else:
            next_id = 1

        # Append the new item
        new_item = (next_id, name, quantity, price)
        self.inventory.inventory.append(new_item)
        self.inventory.export_inventory()
        print(f"Item '{name}' added successfully with Item ID {next_id}.")
