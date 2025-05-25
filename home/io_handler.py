# io_handler.py

import csv
from item import Item
from inventory import Inventory

def save_inventory(filename: str, inventory: Inventory):
    """
    Save the current inventory to a CSV file.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["item_id", "name", "quantity", "price"])
            for item in inventory.items.values():
                writer.writerow([item.item_id, item.name, item.quantity, item.price])
        print(f"Inventory saved to '{filename}'.")
    except Exception as e:
        print(f"[Error] Failed to save file: {e}")

def load_inventory(filename: str) -> Inventory:
    """
    Load inventory data from a CSV file.
    """
    new_inventory = Inventory()
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = Item(
                    item_id=row["item_id"],
                    name=row["name"],
                    quantity=int(row["quantity"]),
                    price=float(row["price"])
                )
                new_inventory.add_item(item)
        print(f"Inventory loaded from '{filename}'.")
    except Exception as e:
        print(f"[Error] Failed to load file: {e}")
    return new_inventory
