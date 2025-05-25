### Run this file to start the Inventory Manager program

from item import Item
from inventory import Inventory
from command_parser import parse_command
from io_handler import save_inventory, load_inventory

print("Welcome to Inventory Manager!")
print("Type 'help' for a list of commands.")

def print_help():
    print("""
Supported Commands:
  add <id> <name> <quantity> <price>       Add a new item
  remove <id>                              Remove an item
  + <id> <amount>                          Restock an item (shorthand)
  - <id> <amount>                          Deduct stock (shorthand)
  search <keyword>                         Search items by name
  list                                     List all items
  save <filename>                          Save inventory to CSV file
  load <filename>                          Load inventory from CSV file
  help                                     Show this message
  exit                                     Exit the program
    """)

def main():
    inventory = Inventory()
    print("=== Welcome to Inventory Manager ===")
    print("Type 'help' for a list of commands.\n")

    while True:
        try:
            user_input = input("> ")
            command = parse_command(user_input)

            if command.name == 'exit':
                print("Exiting program.")
                break

            elif command.name == 'help':
                print_help()

            elif command.name == 'add':
                if len(command.args) != 4:
                    raise ValueError("Usage: add <id> <name> <quantity> <price>")
                item_id, name, quantity, price = command.args
                item = Item(item_id, name, int(quantity), float(price))
                inventory.add_item(item)
                print(f"Item '{name}' added.")

            elif command.name == 'remove':
                if len(command.args) != 1:
                    raise ValueError("Usage: remove <id>")
                inventory.remove_item(command.args[0])
                print("Item removed.")

            elif command.name == '+':
                item_id, amount = command.args
                inventory.restock_item(item_id, int(amount))
                print(f"Stock updated: +{amount}")

            elif command.name == '-':
                item_id, amount = command.args
                inventory.deduct_item(item_id, int(amount))
                print(f"Stock updated: -{amount}")

            elif command.name == 'search':
                if len(command.args) != 1:
                    raise ValueError("Usage: search <keyword>")
                results = inventory.search_by_name(command.args[0])
                for item in results:
                    print(item)
                if not results:
                    print("No matching items found.")

            elif command.name == 'list':
                for item_str in inventory.list_all_items():
                    print(item_str)
                if not inventory.items:
                    print("(No items in inventory)")

            elif command.name == 'save':
                if len(command.args) != 1:
                    raise ValueError("Usage: save <filename>")
                filename = command.args[0]
                save_inventory(filename, inventory)

            elif command.name == 'load':
                if len(command.args) != 1:
                    raise ValueError("Usage: load <filename>")
                filename = command.args[0]
                inventory = load_inventory(filename)

            else:
                print(f"Unknown command: {command.name}")
        
        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    main()
