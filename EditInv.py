# EditInv.py
from Inventory import Inventory
from Utils import get_input  # Import the helper function


class EditInventory:
    """
    Class to handle editing items in the inventory.
    """

    def __init__(self, inventory):
        """
        Initialise with an inventory object.
        
        :param inventory: The Inventory object to modify.
        """
        self.inventory = inventory

    def edit_item(self):
        """
        Edits an item in the inventory by collecting input from the user.
        """
        if not self.inventory.inventory:
            print("Inventory is empty. No item to edit.")
            return

        item_id = int(get_input("Enter item ID to edit (or type 'exit' to quit): ").strip())
        item_found = False

        for i, item in enumerate(self.inventory.inventory):
            if item[0] == item_id:
                item_found = True
                print(f"Current details - Name: {item[1]}, Quantity: {item[2]}, Price: £{item[3]:.2f}")

                # Collect new details from user
                name = get_input("Enter new name (leave blank to keep current or 'exit' to quit): ").strip()
                quantity = get_input("Enter new quantity (leave blank to keep current or 'exit' to quit): ").strip()
                price = get_input("Enter new price (leave blank to keep current or 'exit' to quit): ").strip()

                # Update details only if input is provided
                if name:
                    item = (item[0], name, item[2], item[3])
                if quantity:
                    item = (item[0], item[1], int(quantity), item[3])
                if price:
                    item = (item[0], item[1], item[2], float(price))

                # Update item in the list and export the inventory
                self.inventory.inventory[i] = item
                self.inventory.export_inventory()
                print(f"Item ID {item_id} updated successfully.")
                break

        if not item_found:
            print(f"Item ID {item_id} not found.")
