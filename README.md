# Inventory Manager

**Author**: Minqi Chen  
**SID**: 540236635  
**Course**: COMP9001 - Introduction to Programming

---

## 1. Overview

A terminal-based Python application to manage a virtual inventory.  
Users can:

- Add/remove items  
- Restock or deduct quantities  
- Search items by name  
- Save/load inventory to/from CSV  
- View full inventory  
- Use quick commands like `+` and `-`

---

## 2. File Structure

- `main.py` – Main program loop  
- `item.py` – Item class  
- `inventory.py` – Inventory class  
- `command_parser.py` – Command parsing logic  
- `io_handler.py` – File save/load functions  
- `test_item.py` – Unit tests for Item and Inventory  
- `inventory.csv` – Sample inventory  
- `README.md` – Project introduction  


---

## 3. Features & Commands

### 📥 Inventory Management
- `add <id> <name> <quantity> <price>` — Add a new item  
- `remove <id>` — Remove an item  

### 🔄 Quick Stock Update
- `+ <id> <amount>` — Restock item  
- `- <id> <amount>` — Deduct item  

### 🔍 Lookup & Display
- `search <keyword>` — Search for item(s)  
- `list` — Show all items  

### 💾 Save & Load
- `save <filename>` — Save inventory to CSV  
- `load <filename>` — Load inventory from CSV  

### ❓ System Commands
- `help` — Show available commands  
- `exit` — Exit the program  

---

## 4. Run the Program

Run in your terminal or Python environment:

```bash
python3 main.py
```
---

## 5. Notes on Submission

- ✅ **No external libraries used**  
- ✅ **No GUI / media dependencies**  
- ✅ **Fully compatible with Ed’s Python environment**
