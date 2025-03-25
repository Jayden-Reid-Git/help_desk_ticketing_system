import csv
import os

# Define the CSV file name
CSV_FILE = "tickets.csv"

# Check if the file exists, if not, create it with headers
if not os.path.exists(CSV_FILE):
  with open(CSV_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Ticket ID", "User", "Issue", "Status"]) # Header row

def submit_ticket():
    """Allows a user to submit a new IT support ticket."""
    user = input("Enter your name: ")
    issue = input("Describe your issue: ")

    # Check if the file exists and create it with headers if needed
    file_exists = os.path.exists(CSV_FILE)
    if not file_exists:
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Ticket ID", "User", "Issue", "Status"])  # Write headers

    # Determine the correct Ticket ID
    ticket_id = 0  # Default Ticket ID if no tickets exist
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row
        for row in reader:
            if row:  # Ensure the row is not empty
                ticket_id = int(row[0]) + 1  # Get the last ID and increment it

    # Append the new ticket to the CSV file
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ticket_id, user, issue, "Open"])

    print(f"✅ Ticket {ticket_id} submitted successfully!")

def view_tickets():
  """Displays all submitted tickets."""
  with open(CSV_FILE, mode="r", newline="") as file:
    reader = csv.reader(file)
    tickets = list(reader)

  if len(tickets) <= 1: # If only header exists
    print("📭 No tickets found.")
    return
  print("\n📋 Open Tickets:")
  print("-" * 40)
  for ticket in tickets[1:]: # Skip the header row
    print(f"🎫 Ticket ID: {ticket[0]}")
    print(f"👤 User: {ticket[1]}")
    print(f"💬 Issue: {ticket[2]}")
    print(f"📌 Status: {ticket[3]}")
    print("-" * 40)

def update_ticket():
  """Updates the status of a ticket."""
  ticket_id = input("Enter the Ticket ID to update: ")

  with open(CSV_FILE, mode="r", newline="") as file:
    reader = csv.reader(file)
    tickets = list(reader)

  for ticket in tickets:
    if ticket[0] == ticket_id:
      print(f"Current Status: {ticket[3]}")
      new_status = input("Enter new status (Open/In Progress/Resolved): ").strip()

      if new_status in ["Open", "In Progress", "Resolved"]:
        ticket[3] = new_status
        with open(CSV_FILE, mode="w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(tickets) # Write updated tickets back
        print(f"✅ Ticket {ticket_id} updated to '{new_status}'")
        return
      else:
        print("⚠️ Invalid status. Try again.")
        return
      
  print("❌ Ticket ID not found.")

def main():
  """Main menu to navigate the Help Desk system."""
  while True:
    print("\n🎫 Help Desk Ticketing System")
    print("1️⃣ Submit a Ticket")
    print("2️⃣ View Tickets")
    print("3️⃣ Update Ticket Status")
    print("4️⃣ Exit")
    choice = input("Select an option: ")

    if choice =="1":
      submit_ticket()
    elif choice == "2":
      view_tickets()
    elif choice == "3":
      update_ticket()
    elif choice == "4":
      print("👋 Exiting... Goodbye!")
      break
    else:
      print("⚠️ Invalid option. Try again.")
    
if __name__ == "__main__":
  main()