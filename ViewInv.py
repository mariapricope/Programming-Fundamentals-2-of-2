# This is the View Inventory file ViewInv.py
def view_inventory():
    """Displays the current inventory in a tabular format."""
    from Inventory import import_inventory
    from tabulate import tabulate

    inventory = import_inventory()

    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory:")
    headers = ["Item ID", "Name", "Quantity", "Price (£)"]  # Updated header
    formatted_inventory = [(item[0], item[1], item[2], f"£{item[3]:.2f}") for item in inventory]
    print(tabulate(formatted_inventory, headers=headers, tablefmt="grid"))
