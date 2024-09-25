# RemInv.py
from Inventory import Inventory
from Utils import get_input  # Import the helper function


class RemoveInventory:
    """
    Class to handle removing items from the inventory.
    """

    def __init__(self, inventory):
        """
        Initialize with an inventory object.
        
        :param inventory: The Inventory object to modify.
        """
        self.inventory = inventory

    def remove_item(self):
        """
        Removes an item from the inventory by collecting input from the user.
        """
        if not self.inventory.inventory:
            print("Inventory is empty. No item to remove.")
            return

        item_id = int(get_input("Enter item ID to remove (or type 'exit' to quit): ").strip())
        item_found = False

        for i, item in enumerate(self.inventory.inventory):
            if item[0] == item_id:
                item_found = True
                self.inventory.inventory.pop(i)
                self.inventory.export_inventory()
                print(f"Item '{item[1]}' removed successfully.")
                break

        if not item_found:
            print(f"Item ID {item_id} not found.")
