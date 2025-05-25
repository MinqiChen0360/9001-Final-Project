# item.py

class Item:
    """
    Represents a single item in the inventory.
    Attributes:
        item_id (str): Unique identifier for the item.
        name (str): Name of the item.
        quantity (int): Number of units in stock.
        price (float): Price per unit.
    """

    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        """
        Initialize a new item with the given attributes.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def restock(self, amount: int):
        """
        Increase the quantity in stock.
        """
        if amount < 0:
            raise ValueError("Restock amount must be non-negative.")
        self.quantity += amount

    def deduct(self, amount: int):
        """
        Decrease the quantity in stock.
        """
        if amount < 0:
            raise ValueError("Deduct amount must be non-negative.")
        if amount > self.quantity:
            raise ValueError("Insufficient stock to deduct.")
        self.quantity -= amount

    def __str__(self):
        """
        Return a formatted string of the item details.
        """
        return f"{self.item_id}: {self.name} | Qty: {self.quantity} | ${self.price:.2f}"

