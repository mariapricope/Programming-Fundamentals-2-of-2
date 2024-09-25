# Main.py
from Inventory import Inventory
from AddInv import AddInventory
from EditInv import EditInventory
from RemInv import RemoveInventory
from ViewInv import ViewInventory
from Utils import get_input  

def display_menu():
    """
    Displays the menu options for the Inventory Management System.
    """
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Edit Item")
    print("3. View Inventory")
    print("4. Remove Item")
    print("5. Exit")


def main():
    """
    The main function that handles user input and interacts with the Inventory.
    """
    inventory = Inventory()  # Create the inventory object

    add_inv = AddInventory(inventory)
    edit_inv = EditInventory(inventory)
    remove_inv = RemoveInventory(inventory)
    view_inv = ViewInventory(inventory)

    while True:
        display_menu()
        choice = get_input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_inv.add_item()
        elif choice == '2':
            edit_inv.edit_item()
        elif choice == '3':
            view_inv.view_inventory()
        elif choice == '4':
            remove_inv.remove_item()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
