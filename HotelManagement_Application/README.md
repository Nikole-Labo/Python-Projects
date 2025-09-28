# 🏨 Hotel Management Application

A console-based application that manages hotel operations using layered architecture. Guests can be checked in/out, rooms can be allocated and tracked, reservations can be created, and reports generated. The application demonstrates modular design, domain modeling, repository persistence, services logic, and custom exception handling.

---

## ✅ Key Features & Functionality

- **Guest & Room Management**  
  - Add and remove guests  
  - Add and remove rooms  
  - Assign or release rooms to/from guests  

- **Reservations & Stays**  
  - Make reservations linking guests to rooms for date intervals  
  - Check-in and check-out workflows  
  - Validate date overlaps and availability  

- **Search & Reporting**  
  - Search for guests by name, room number, or reservation status  
  - List rooms by occupancy, availability, or guest assignment  
  - Reports such as current guest lists, room usage, and reservation schedules  

- **Undo / History Support**  
  - Track changes and support undoing operations 
  - Use deep copies or history stacks to rollback state  

- **Persistence Options**  
  - In-memory storage for runtime  
  - Optionally, file-based or database-backed persistence for rooms/guests/reservations  

- **Custom Exceptions & Validation**  
  - Validate guest IDs, room numbers, dates, and reservation logic  
  - Define domain-specific exception classes (e.g. `RoomUnavailableError`, `ReservationConflictError`, `InputValidationError`)

---

