# Assignment 2

# Task 1

service_tickets = {
    "Ticket001": {"Customer": "Emily", "Issue": "Duplicate order", "Status": "open"},
    "Ticket002": {"Customer": "Brad", "Issue": "Missing item", "Status": "closed"}
}

# open a new service ticket

def open_new_ticket(service_tickets):
    ticket_id = input("Enter ticket ID: ")
    customer_name = input("Enter customer name: ")
    customer_issue = input("Enter customer issue: ")

    ticket_info = {
        "Customer": customer_name,
        "Issue": customer_issue,
        "Status": "open"
    }

    service_tickets[ticket_id] = ticket_info
    print(f"Ticket {ticket_id} has been added successfully!")

# update a ticket

def update_ticket_status(service_tickets):
    ticket_id = input("Enter the ticket ID: ")

    if ticket_id in service_tickets:
        new_status = input("Enter the new status (open/closed): ")

        if new_status in ["open", "closed"]:
            service_tickets[ticket_id].update({"Status": new_status})
            print(f"Ticket {ticket_id} status updated to {new_status}.")
        else:
            print("Invalid status. Please enter 'open' or 'closed'.")
    else:
        print(f"Ticket {ticket_id} does not exist.")


def display_tickets(service_tickets):
    filter_choice = input("Would you like to filter tickets by status (yes/no)? ").lower()

    if filter_choice == "yes":
        status_filter = input("Enter the status to filter by (open/closed): ").lower()
        
        if status_filter in ["open", "closed"]:
            print(f"Displaying all {status_filter} tickets:")
            for ticket_id, ticket_info in service_tickets.items():
                if ticket_info["Status"].lower() == status_filter:
                    print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
        else:
            print("Invalid status. Please enter 'open' or 'closed'.")
    
    else:
        print("Displaying all tickets:")
        for ticket_id, ticket_info in service_tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

while True:
    print("\nOptions:")
    print("1. Open a new ticket")
    print("2. Update ticket status")
    print("3. Display tickets")
    print("4. Exit")
    
    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        open_new_ticket(service_tickets)
    elif choice == "2":
        update_ticket_status(service_tickets)
    elif choice == "3":
        display_tickets(service_tickets)
    elif choice == "4":
        print("Goodbye!")
        break  
    else:
        print("Invalid choice, please try again.")