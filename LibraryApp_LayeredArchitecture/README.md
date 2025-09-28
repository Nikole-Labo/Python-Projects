# 📚 Library — Layered Architecture

**Short description**  
A console-based library application built using a layered architecture. The app manages books, clients and rentals, supports searches and statistics, and includes unit tests and custom exceptions.

---

## ✅ Requirements met
- Menu-driven console UI.
- Layered architecture with clear separation: **domain**, **repository**, **service**, and **ui** modules.
- Procedurally generate **≥ 20** items at startup for each domain class (books, clients, rentals).
- Custom exception classes used throughout the non-UI layers.
- PyUnit test cases for non-UI classes and methods, aim for high unit-test coverage using a coverage tool .

---

## 📦 Domain model
- **Book**: `book_id`, `title`, `author`  
- **Client**: `client_id`, `name`  
- **Rental**: `rental_id`, `book_id`, `client_id`, `rented_date`, `returned_date`

---

## 🧩 Features
### Core functionality
- **Manage books & clients**  
  - Add / remove / update / list books and clients.
  - Each entity validated (IDs unique, required fields present).
- **Rent / Return books**  
  - Rent only if book is available.
  - Return a book (set `returned_date`).
  - Rentals maintain history and permit validation (dates, IDs).
- **Search**  
  - Search books or clients by any field (id / title / author / name).  
  - Case-insensitive and partial-string matching; returns all matches.
- **Statistics**
  - Most rented books (sorted by number of rentals, desc).
  - Most active clients (sorted by total rental-days, desc).
  - Most rented author (authors sorted by total rentals of their books).
- **Undo / history** (optional extension)  
  - Support undo for non-UI operations if implemented in services.

---
