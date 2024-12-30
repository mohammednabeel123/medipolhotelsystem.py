managers = {}
rooms = {
101: {"type": "Single", "price": 100, "status": "Available"},
102: {"type": "Double", "price": 150, "status": "Booked"},
103: {"type": "Deluxe", "price": 200, "status": "Available"},
104: {"type": "Single", "price": 120, "status": "Available"},
105: {"type": "Double", "price": 180, "status": "Booked"},
106: {"type": "Single", "price": 100, "status": "Available"},
107: {"type": "Deluxe", "price": 220, "status": "Available"},
108: {"type": "Double", "price": 160, "status": "Available"},
109: {"type": "Single", "price": 90, "status": "Booked"},
110: {"type": "Deluxe", "price": 250, "status": "Available"}
}
bookings = []
def authenticate_admin():
    print("Welcome to Medipol Hotel Management System")
    admin_password = "admin123"
    attempt = 3
    while attempt > 0:
        password = input("Please enter the admin password to continue:\n")
        if password == admin_password:
            print("Acess Granted.")
            return True
        else:
            attempt -=1
            print(f"Incorrect password.{attempt} attempts left.")
    print("Access denied. Exiting the system.")
    return False 
def admin_menu():
    print("\nAdmin Menu:")
    print("1.Add/Remove Manager")
    print("2.Access Hotel Room Mnagement System")
    print("3.Exit")
    try:
        admin_input = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input.please enter a umber. ")
    return admin_input
def add_manager():
    username = input("Enter manager Username: ")
    password = input("Enter manager password: ")
    managers[username] = password
    print(f"Manager {username} has been added successfully.")
def remove_manager():
    username = input("Enter the username of the manager: ")
    if username in managers:
        del managers[username]
        print(f"manager {username} has been removed successfully.")
    else:
        print("manager not found.") 
def add_room():
    room_number = int(input("Enter Room NUmber: "))
    room_type = input("Enter Room Type (Single/Double/Deluxe): ")
    room_price = int(input("Enter Room price: "))
    rooms[room_number] = {"type":room_type, "price":room_price,"status":"Available"}
    print(f"Room {room_number} has been succuessfully added.. ")
def remove_room():
    room_number = int(input("Enter Room Number to remove: "))
    if room_number in rooms:
        del rooms[room_number]
        print(f"Room {room_number} has been removed.")
    else:
        print("Room not found. ")
def update_room_status():
    room_number = int(input("Enter Room Number to update its status..."))
    if room_number in rooms:
        new_status = input("Enter New Status (Available/Booked): ")
        rooms[room_number]["status"] = new_status
        print(f"Room {room_number} status has been updated..")
    else:
        print("Rooon can't be found")
#Booking system
def book_room():
    room_type = input("Enter Room Type (single/Double/Deluxe): ").capitalize()
    price_range = int(input("Enter max Price: "))
    available_rooms = [
        num for num, details in rooms.items()
        if details["type"] == room_type and details["price"] <= price_range and
        details["status"] == "Available"
        ]
    if available_rooms:
        print(f"Available Room: {available_rooms[0]}")
        confirm = input("Do you want to book this room? (Yes/No): ")
        if confirm.lower() == "yes":
            customer_name = input("Enter your name: ")
            stay_period = input("Enter your stay Period (YYYY-MMM-DDD to YYYY-MM-DD): ")
            room_num = available_rooms[0]
            rooms[room_num]["status"] = "Booked"
            bookings.append({
                "customer":customer_name,
                "room":room_num,
                "stay":stay_period
                })
            print(f"Room {room_num} has been successfully booked.")
    else:
        print("No rooms available matching the criteria.")
def cancel_booking():
    customer_name = input("Enter Customer name to cancel booking: ")
    for booking in bookings:
        if booking["customer"] == customer_name:
            room_num = booking["room"]
            rooms[room_num]["status"] = "Available"
            bookings.remove(booking)
            print(f"Booking for {customer_name} has been canceled.")
            return
        else:
            print("Booking not found.")
def generate_report():
    available_rooms = sum(1 for details in rooms.values() if details["status"] == "Available")
    booked_rooms = len(rooms) - available_rooms
    total_revenue = sum(details["price"] for details in rooms.values() if details["status"] == "Booked")
    print(f"Available Rooms : {available_rooms}")
    print(f"Booked Rooms : {booked_rooms}")
    print(f"Total Revenue : ${total_revenue}")
def main():
    if authenticate_admin():
        while True:
            choice = admin_menu()
            if choice == 1:
                print("\nManager Menu:")
                print("1.Add manager")
                print("2.Remove Manager")
                manager_choice = int(input("Make a choice: "))
                if manager_choice == 1:
                    add_manager()
                elif manager_choice == 2:
                    remove_manager()
                else:
                    print("invalid choice.")
            elif choice == 2:
                print("\n Room Management Menu: ")
                print("1. Add Room")
                print("2. Remove Room")
                print("3. update Room Status")
                print("4. Book Room")
                print("5. Cancel Booking")
                print("6. Generate report")
                room_choice = int(input("choose an option: "))
                if room_choice ==1:
                    add_room()
                elif room_choice == 2:
                    remove_room()
                elif room_choice == 3:
                    update_room_status()
                elif room_choice == 4:
                    book_room()
                elif room_choice == 5:
                    cancel_booking()
                elif room_choice == 6:
                    generate_report()
                else:
                    print("Invalid choice.")
            elif choice == 3:
                print("Goodbye! Thank you for using the hotel Manangement System..")
                break
            else:
                print("invalid choice...please Try again..")
if __name__ == "__main__":
    main()