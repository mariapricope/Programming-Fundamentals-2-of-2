# ViewInv.py
from Inventory import Inventory
from tabulate import tabulate


class ViewInventory:
    """
    Class to handle viewing items in the inventory.
    """

    def __init__(self, inventory):
        """
        Initialise with an inventory object.
        
        :param inventory: The Inventory object to read from.
        """
        self.inventory = inventory

    def view_inventory(self):
        """
        Displays the current inventory in a tabular format.
        """
        if not self.inventory.inventory:
            print("Inventory is empty.")
            return

        headers = ["Item ID", "Name", "Quantity", "Price"]
        print("\nCurrent Inventory:")
        print(tabulate(self.inventory.inventory, headers=headers, tablefmt="grid"))
