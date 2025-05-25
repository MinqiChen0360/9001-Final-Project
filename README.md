===========================================
Inventory Manager - COMP9001 Final Project
===========================================

Author: Minqi Chen
SID: 540236635
Course: COMP9001 - Introduction to Programming

1. Project Overview
-----------------------
It allows users to manage a collection of items in a virtual inventory, supporting operations such as:
- Add/remove items
- Restock or deduct item quantities
- Search items by name
- Save/load inventory to/from CSV file
- Display item list
- Quick commands using '+' and '-'


2. File Structure
-----------------------
.
├── main.py               # Main program loop
├── item.py               # Item class
├── inventory.py          # Inventory class
├── command_parser.py     # Command parsing logic
├── io_handler.py         # File save/load functions
├── test_item.py          # Unit tests for Item and Inventory
├── inventory.csv         # Sample inventory
└── README.txt            # Project Introduction


3. Features & Commands
-----------------------
📥 Inventory Management:
  • add <id> <name> <quantity> <price>      → Add a new item  
  • remove <id>                             → Remove item  

🔄 Quick Stock Update:
  • + <id> <amount>                         → Restock item  
  • - <id> <amount>                         → Deduct item  

🔍 Lookup & Display:
  • search <keyword>                        → Search items  
  • list                                    → Display all items  

💾 Persistence:
  • save <filename>                         → Save inventory as CSV  
  • load <filename>                         → Load inventory from CSV  

❓ System Help:
  • help                                    → Show command list  
  • exit                                    → Quit program


4. Run
-----------------------
In your terminal or Python IDE:

```bash
python3 main.py


5.Notes on Submission
-----------------------
No external libraries used.
No GUI, web, video, or audio dependencies.
Fully compatible with Ed's Python environment.
