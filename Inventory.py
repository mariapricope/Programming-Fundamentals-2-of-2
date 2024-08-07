import openpyxl

def import_inventory(excel_file='inventory.xlsx'):
    """Imports inventory from an Excel file."""
    try:
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active
        inventory = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            inventory.append(row)
        return inventory
    except FileNotFoundError:
        print("No existing Excel file found. Starting with an empty inventory.")
        return []

def export_inventory(inventory, excel_file='inventory.xlsx'):
    """Exports inventory to an Excel file."""
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Inventory"
    sheet.append(["Item ID", "Name", "Quantity", "Price"])
    for item in inventory:
        sheet.append(item)
    workbook.save(excel_file)
    print("Inventory saved to Excel file.")
