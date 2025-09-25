# Apartment Expenses Management System  

This project implements a **console-based application** to manage apartment utility expenses.  
It allows users to track, update, and filter expenses efficiently, supporting multiple operations and undo functionality.  

## Features:
- Generate **random expenses** for testing purposes
- **Add, remove, or replace** apartment expenses
- List all expenses or filter by apartment number, expense type, or total amount
- Track history of changes and **undo operations**
- Menu-driven console interface with easy-to-use commands
- Validates user input to prevent invalid operations

## Supported Commands:
- `add <apartment_number> <expense_type> <amount>` – Add a new expense
- `remove <apartment_number>` – Remove all expenses for an apartment
- `remove <expense_type>` – Remove all expenses of a given type
- `replace <apartment_number> <expense_type> <new_amount>` – Replace an expense amount
- `list` – List all expenses
- `list <apartment_number>` – List expenses for a specific apartment
- `list <comparison> <total_amount>` – List apartments by total expense comparison
- `filter <amount/type>` – Filter expenses by amount or type
- `undo` – Undo the last operation
- `exit` – Exit the program

## Learning Goals:
- Practice **Python data structures** (lists, dictionaries)
- Implement **command parsing** and **input validation**
- Manage **history for undo operations**
- Handle **real-world-like problem modeling** for apartment expense tracking
