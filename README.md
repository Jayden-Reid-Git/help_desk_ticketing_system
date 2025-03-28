# Help Desk Ticketing System
The Help Desk Ticketing System is a simple command-line tool that allows users to submit IT issues, track them, and mark them as resolved. It simulates a basic help desk system commonly used in IT support environments.

## Features
1. Submit new tickets with issue details.
2. View all submitted tickets.
3. Mark tickets as resolved.
4. Stores tickets in a CSV file (`tickets.csv`) for easy tracking.

## Technologies Used
1. Python: Core language.
2. CSV Module: Used for storing and managing tickets.
3. File Handling: Reads/writes data to `tickets.csv`.

## How to Use
1. Run the Script (python help_desk.py)
2. Select an Option
 Once the script runs, you can:
  (1) Submit a Ticket: Enter details like name, issue, and urgency.
  (2) View Tickets: Displays all open tickets.
  (3) Resolve a Ticket: Marks a selected ticket as resolved.
  (4) Exit: Closes the program.

## Example Ticket Entry
Ticket ID: 1
Name: John Doe
Issue: Unable to connect to Wi-Fi
Status: Open

## Future Enhancements
1. Implement a GUI for easier interaction.
2. Add email notifications when a ticket is created or resolved.
3. Store tickets in a database instead of CSV.