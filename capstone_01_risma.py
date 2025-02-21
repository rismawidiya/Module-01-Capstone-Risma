import datetime

# LIST OF EQUIPMENTS
equipment_list = [
    {"Code": "GEO01", "Name": "Seismograph", "Daily Rate": 2250000, "Status": "Available", "Condition": "Good"},
    {"Code": "GEM02", "Name": "Magnetometer", "Daily Rate": 1800000, "Status": "Rented", "Condition": "Good"},
    {"Code": "SCI03", "Name": "Gravimeter", "Daily Rate": 3000000, "Status": "Rented", "Condition": "Good"},
    {"Code": "MAL04", "Name": "GPR", "Daily Rate": 2700000, "Status": "Unavailable", "Condition": "Under Maintenance"},
    {"Code": "DJI05", "Name": "Drone", "Daily Rate": 3750000, "Status": "Available", "Condition": "Good"},
    {"Code": "ABE06", "Name": "ERM", "Daily Rate": 2100000, "Status": "Available", "Condition": "Good"},
    {"Code": "TRI07", "Name": "GPS", "Daily Rate": 1350000, "Status": "Unavailable", "Condition": "Under Maintenance"},
    {"Code": "FLI08", "Name": "Thermal Cam", "Daily Rate": 1650000, "Status": "Rented", "Condition": "Good"},
    {"Code": "GEO09", "Name": "Hydrophone", "Daily Rate": 2625000, "Status": "Available", "Condition": "Good"},
    {"Code": "CAM10", "Name": "Data Logger", "Daily Rate": 1500000, "Status": "Available", "Condition": "Good"}
]

# FUNCTION TO DISPLAY EQUIPMENT WITH FILTER AND SORTING

def display_equipment(filter_status=None, sort_by=None):
    # Display a list of equipment with optional filtering and sorting
    filtered_list = equipment_list[:]  # Copy the equipment list to avoid modifying the original

    # Apply filter based on Status
    if filter_status:
        filtered_list = [eq for eq in filtered_list if eq['Status'].lower() == filter_status.lower()]

    # Apply sorting based on Daily Rate
    if sort_by == "most_expensive":
        filtered_list.sort(key=lambda x: x['Daily Rate'], reverse=True)
    elif sort_by == "cheapest":
        filtered_list.sort(key=lambda x: x['Daily Rate'])

    # Display header
    print("\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘ Equipment List ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘")
    print(f"\n{'Code':<15} {'Name':<15} {'Daily Rate':<15} {'Status':<15} {'Condition':<15}")
    print("¤━━━¤" * 17)

    # Display equipment details
    if filtered_list:
        for eq in filtered_list:
            print(f"{eq['Code']:<15} {eq['Name']:<15} {eq['Daily Rate']:<15} {eq['Status']:<15} {eq['Condition']:<15}")
    else:
        print("\n⌞❕⌝ No equipment found with the given criteria.")

# Function to sort equipment
def sort_equipment():
    # Allow user to choose a sorting method and display results
    while True:
        print("\nSorting Options:")
        print("1. Most Expensive First")
        print("2. Cheapest First")
        print("3. Return to Previous Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_equipment(sort_by="most_expensive")
        elif choice == "2":
            display_equipment(sort_by="cheapest")
        elif choice == "3":
            return  # Goes back to the submenu
        else:
            print("\n⌞❕⌝ Invalid choice! Please enter 1, 2, or 3.")

# Function to filter equipment
def filter_equipment():
    # Allow user to filter equipment by status and display results
    while True:
        print("\nFilter Options:")
        print("1. Available Equipment")
        print("2. Rented Equipment")
        print("3. Unavailable Equipment")
        print("4. Return to Previous Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_equipment(filter_status="Available")
        elif choice == "2":
            display_equipment(filter_status="Rented")
        elif choice == "3":
            display_equipment(filter_status="Unavailable")
        elif choice == "4":
            return  # Goes back to the submenu
        else:
            print("\n⌞❕⌝ Invalid choice! Please enter 1, 2, 3, or 4.")

# FUNCTION TO ADD EQUIPMENT

def add_equipment():
    global equipment_list  # Ensure modifications apply to the global list
    print("\nAdding Equipment in Progress...")

    while True:
        code = input("\nEnter product code (e.g., GEO01, CAM10) or type 'Back' to return: ").strip().upper()

        # Check if input is empty
        if not code:
            print("\n⌞❕⌝ Input cannot be empty. Please enter a valid product code.")
            continue

        if code == "BACK":
            return

        # Format check
        if not (len(code) == 5 and code[:3].isalpha() and code[3:].isdigit()):
            print("\n⌞❕⌝ Invalid format! Use 3 letters followed by 2 digits (e.g., GEO01, CAM10). Please try again.")
            continue

        # Check for duplicate code
        if any(eq['Code'] == code for eq in equipment_list):
            print("\n⌞❕⌝ Equipment with this code already exists.")
            more = input("\nAdd another equipment? (Yes/No): ").strip().lower()
            if more != 'yes':
                return  # Exit function if user does not want to add more
            continue

        # New equipment input
        name = input("\nEnter equipment name: ").strip().title()

        while True:
            rate_input = input("\nEnter rental rate (must be a positive number): ").strip()
            if rate_input.isdigit() and int(rate_input) > 0:
                rate = int(rate_input)
                break
            else:
                print("\n⌞❕⌝ Invalid input! Rental rate must be a positive number.")

        # Default status and condition
        status = "Available"
        condition = "Good"

        new_equipment = {
            "Code": code,
            "Name": name,
            "Daily Rate": rate,
            "Status": status,
            "Condition": condition
        }

        equipment_list.append(new_equipment)
        print(f"\n⌞✔⌝ {name} added successfully!")

        display_equipment()  # Show updated list

        # Ask user if they want to add more
        more = input("\nAdd another equipment? (Yes/No): ").strip().lower()
        if more != 'yes':
            return  # Exit function if user does not want to add more

# FUNCTION TO REMOVE EQUIPMENT

def remove_equipment():
    global equipment_list  # Ensure modifications apply to the global list
    print("\nRemoving Equipment in Progress...")

    while True:
        code = input("\nEnter product code (e.g., GEO01, CAM10) or type 'Back' to return: ").strip().upper()

        # Check if input is empty
        if not code:
            print("\n⌞❕⌝ Input cannot be empty. Please enter a valid product code.")
            continue

        if code == "BACK":
            return

        # Format check
        if not (len(code) == 5 and code[:3].isalpha() and code[3:].isdigit()):
            print("\n⌞❕⌝ Invalid format! Use 3 letters followed by 2 digits (e.g., GEO01, CAM10). Please try again.")
            continue

        # Search for equipment
        found = False
        for index, eq in enumerate(equipment_list):
            if eq['Code'] == code:
                found = True

                if eq['Status'] == "Rented":
                    print("\n⌞❕⌝ Cannot remove rented equipment.")
                    break

                while True:
                    confirm = input(f"\nAre you sure you want to remove '{eq['Name']}'? (Yes/No): ").strip().lower()
                    if confirm == 'yes':
                        del equipment_list[index]  # Remove safely using index
                        print(f"\n⌞✔⌝ Equipment '{eq['Name']}' removed successfully!")
                        display_equipment() # Show updated list
                        break
                    elif confirm == 'no':
                        print("\n⌞✘⌝ Removal cancelled.")
                        break
                    else:
                        print("\n⌞❕⌝ Invalid input! Please enter 'Yes' or 'No'.")

                break  # Exit loop after processing one item

        if not found:
            print("\n⌞❕⌝ Equipment not found! No changes were made.")

        # Ask user if they want to remove another
        more = input("\nRemove another? (Yes/No): ").strip().lower()
        if more != 'yes':
            return  # Exit function if user does not want to remove another

# FUNCTION TO RENT OUT EQUIPMENT

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def rent_equipment():
    print("\nRenting Out Equipment in Progress...")
    
    while True:
        code = input("\nEnter product code (e.g., GEO01, CAM10) or type 'Back' to return: ").strip().upper()

        # Check if input is empty
        if not code:
            print("\n⌞❕⌝ Input cannot be empty. Please enter a valid product code.")
            continue

        if code == 'BACK':
            return

        # Format check
        if not (len(code) == 5 and code[:3].isalpha() and code[3:].isdigit()):
            print("\n⌞❕⌝ Invalid format! Use 3 letters followed by 2 digits (e.g., GEO01, CAM10). Please try again.")
            continue
        
        # Search availability
        selected_equipment = next((eq for eq in equipment_list if eq['Code'] == code and eq['Status'] == "Available"), None)

        if selected_equipment:
            # Customer details
            while True:
                name = input("\nEnter customer name: ").strip().title()
                if not name:
                    print("\n⌞❕⌝ Customer name cannot be empty.")
                    continue
                break

            while True:
                contact = input("\nEnter contact info (phone number): ").strip()
                if not contact.isdigit():
                    print("\n⌞❕⌝ Invalid input! Contact info should contain only numbers.")
                    continue
                if not (8 <= len(contact) <= 12):
                    print("\n⌞❕⌝ Invalid phone number length! Must be between 8 and 12 digits.")
                    continue
                break

            # Start date input
            while True:
                start_date_str = input("\nEnter rental start date (DD-MM-YYYY): ").strip()
                if not is_valid_date(start_date_str):
                    print("\n⌞❕⌝ Invalid date format! Please use DD-MM-YYYY.")
                    continue

                start_date = datetime.datetime.strptime(start_date_str, "%d-%m-%Y").date()
                today = datetime.date.today()

                if start_date < today:
                    print("\n⌞❕⌝ Start date cannot be in the past. Please enter a valid future date.")
                    continue
                
                break

            # End date input
            while True:
                end_date_str = input("\nEnter rental end date (DD-MM-YYYY): ").strip()
                if not is_valid_date(end_date_str):
                    print("\n⌞❕⌝ Invalid date format! Please use DD-MM-YYYY.")
                    continue

                end_date = datetime.datetime.strptime(end_date_str, "%d-%m-%Y").date()

                if end_date <= start_date:
                    print("\n⌞❕⌝ End date must be after start date. Please enter a valid end date.")
                    continue
                
                break

            # Validate and calculate rental fee
            try:
                daily_rate = int(selected_equipment['Daily Rate'])
            except (ValueError, KeyError, TypeError):
                print("\n⌞❕⌝ Equipment daily rate is missing or invalid.")
                return
            
            days = (end_date - start_date).days
            total_fee = days * daily_rate
            
            selected_equipment["Status"] = "Rented"

            # Rental Summary
            print("\n⫘⫘⫘⫘⫘⫘⫘⫘⫘ Rental Summary ⫘⫘⫘⫘⫘⫘⫘⫘⫘")
            print(f"{'Customer Name':<20}: {name}")
            print(f"{'Contact Info':<20}: {contact}")
            print(f"{'Equipment Name':<20}: {selected_equipment['Name']}")
            print(f"{'Rental Start Date':<20}: {start_date.strftime('%d-%m-%Y')}")
            print(f"{'Rental End Date':<20}: {end_date.strftime('%d-%m-%Y')}")
            print(f"{'Total Days':<20}: {days}")
            print(f"{'Total Fee':<20}: IDR {total_fee}")
            print("⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘\n")

        else:
            print("\n⌞❕⌝ Equipment currently rented or not available.")

        # Ask user if they want to rent out another
        while True:
            more = input("\nRent out another? (Yes/No): ").strip().lower()
            if more == 'yes':
                break
            elif more == 'no':
                return
            else:
                print("\n⌞❕⌝ Invalid input! Please enter 'Yes' or 'No'.")

# FUNCTION TO RETURN EQUIPMENT

def return_equipment():
    print("\nReturning Equipment in Progress...")
    
    while True:
        code = input("\nEnter product code (e.g., GEO01, CAM10) or type 'Back' to return: ").strip().upper()

        # Check if input is empty
        if not code:
            print("\n⌞❕⌝ Input cannot be empty. Please enter a valid product code.")
            continue

        if code == 'BACK':
            return

        # Format check
        if not (len(code) == 5 and code[:3].isalpha() and code[3:].isdigit()):
            print("\n⌞❕⌝ Invalid format! Use 3 letters followed by 2 digits (e.g., GEO01, CAM10). Please try again.")
            continue
        
        # Search availability
        found = False
        for eq in equipment_list:
            if eq['Code'] == code:
                found = True  # Equipment found in the list
                
                if eq['Status'] != "Rented":
                    print(f"\n⌞❕⌝ Equipment '{eq['Name']}' is not currently rented.")
                else:
                    # Ask for condition input
                    while True:
                        condition = input("\nCondition on return (Good/Damaged): ").strip().lower()
                        if condition in ["good", "damaged"]:
                            eq['Status'] = "Unavailable" if condition == "damaged" else "Available"
                            eq['Condition'] = "Under Maintenance" if condition == "damaged" else "Good"
                            print(f"\n⌞✔⌝ Equipment '{eq['Name']}' is now marked as {eq['Status']} (Condition: {eq['Condition']}).")
                            break
                        else:
                            print("\n⌞❕⌝ Invalid input! Please enter 'Good' or 'Damaged'.")
                break  # Exit loop after processing the first found match

        if not found:
            print("\n⌞❕⌝ Equipment not found.")
        
        # Ask user if they want to return another
        while True:
            more = input("\nReturn another? (Yes/No): ").strip().lower()
            if more == 'yes':
                break
            elif more == 'no':
                return
            else:
                print("\n⌞❕⌝ Invalid input! Please enter 'Yes' or 'No'.")

# FUNCTION TO DISPLAY MAIN MENU

def main_menu():
    attempts = 0  # Initialise counter for invalid inputs

    while True:
        print("\n𖥔 Welcome to Geophysical Equipment Rental Manager 𖥔")
        print("\nMain Menu:")
        print("1. Display Equipment List")
        print("2. Add New Equipment")
        print("3. Remove Existing Equipment")
        print("4. Rent Out Equipment")
        print("5. Return Equipment")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_equipment_submenu()
            attempts = 0  # Reset attempts after a valid input
        elif choice == "2":
            add_equipment()
            attempts = 0
        elif choice == "3":
            remove_equipment()
            attempts = 0
        elif choice == "4":
            rent_equipment()
            attempts = 0
        elif choice == "5":
            return_equipment()
            attempts = 0
        elif choice == "6":
            print("\nExiting programme... Goodbye!")
            break  # Ends the loop and programme
        else:
            print("\n⌞❕⌝ Invalid choice! Please enter a number between 1 and 6.")

            # Exit programme after 3 invalid attempts
            if attempts >= 3:
                print("\n⌞❕⌝ Too many invalid attempts! Exiting programme...")
                break  # Exit programme

# Function to display submenu
def display_equipment_submenu():
    while True:
        print("\nEquipment Display Menu:")
        print("1. Show All Equipment")
        print("2. Sort Equipment")
        print("3. Filter Equipment")
        print("4. Return to Main Menu")

        sub_choice = input("Enter your choice: ").strip()

        if sub_choice == "1":
            display_equipment()  # Displays all equipment without conditions
        elif sub_choice == "2":
            sort_equipment()  # Calls sorting function
        elif sub_choice == "3":
            filter_equipment()  # Calls filtering function
        elif sub_choice == "4":
            return  # Goes back to the main menu
        else:
            print("\n⌞❕⌝ Invalid choice! Please enter 1, 2, 3, or 4.")

# Ensure main menu is called first when the programme starts
if __name__ == "__main__":
    main_menu()