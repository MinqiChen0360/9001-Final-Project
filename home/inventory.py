# inventory.py

from item import Item
class Inventory:
    """
    Represents a collection of items managed in stock.

    Uses a dictionary to store items by their unique item_id.
    """

    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.items = {}

    def add_item(self, item: Item):
        """
        Add a new item to the inventory.

        Raises:
            KeyError: If the item ID already exists.
        """
        if item.item_id in self.items:
            raise KeyError(f"Item ID '{item.item_id}' already exists.")
        self.items[item.item_id] = item

    def remove_item(self, item_id: str):
        """
        Remove an item from the inventory by ID.

        Raises:
            KeyError: If the item ID does not exist.
        """
        if item_id not in self.items:
            raise KeyError(f"Item ID '{item_id}' not found.")
        del self.items[item_id]

    def restock_item(self, item_id: str, amount: int):
        """
        Restock a specific item.

        Raises:
            KeyError: If the item is not found.
        """
        if item_id not in self.items:
            raise KeyError(f"Item ID '{item_id}' not found.")
        self.items[item_id].restock(amount)

    def deduct_item(self, item_id: str, amount: int):
        """
        Deduct stock from a specific item.

        Raises:
            KeyError: If the item is not found.
        """
        if item_id not in self.items:
            raise KeyError(f"Item ID '{item_id}' not found.")
        self.items[item_id].deduct(amount)

    def search_by_name(self, keyword: str):
        """
        Search for items by name keyword.

        Returns:
            List of matching items.
        """
        return [item for item in self.items.values() if keyword.lower() in item.name.lower()]

    def list_all_items(self):
        """
        Return a list of formatted strings for all items in stock.
        """
        return [str(item) for item in self.items.values()]
