from AddInv import add_item
from EditInv import edit_item
from RemInv import remove_item
from ViewInv import view_inventory

def display_menu():
    """Displays the main menu for the Inventory Management System."""
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Edit Item")
    print("3. View Inventory")
    print("4. Remove Item")
    print("5. Exit")

def main():
    """Main function that runs the inventory system in a loop until the user exits."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5) or type 'exit' to abort: ").strip().lower()
        
        if choice == '1':
            add_item()
        elif choice == '2':
            edit_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice == '5' or choice == 'exit':
            print("Exiting the system.")
            break  # Exit the loop and end the programme
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()  # Run the main function if this file is executed directly
