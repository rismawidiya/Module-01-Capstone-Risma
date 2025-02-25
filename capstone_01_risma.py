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

# FUNCTION TO DISPLAY EQUIPMENT WITH FILTERING AND SORTING

def display_equipment(filter_status=None, sort_by=None):
    print("\nDisplaying Equipment in Progress...")

    # Copy the equipment list to avoid modifying the original
    filtered_list = equipment_list[:]  

    # Apply filter based on Status
    if filter_status:
        filtered_list = [eq for eq in filtered_list if eq['Status'].lower() == filter_status.lower()]

    # Apply sorting based on Daily Rate
    if sort_by == "most_expensive":
        filtered_list.sort(key=lambda x: x['Daily Rate'], reverse=True)
    elif sort_by == "cheapest":
        filtered_list.sort(key=lambda x: x['Daily Rate'])

    # Extract column names
    columns = ["Code", "Name", "Daily Rate", "Status", "Condition"]

    # Determine column widths dynamically
    col_widths = {col: max(len(col), max((len(str(eq[col])) for eq in filtered_list), default=len(col))) + 2 for col in columns}

    # Create a dynamic divider
    divider = "⫘" * (sum(col_widths.values()) + len(columns) - 1)

    # Display header
    print(f"\n{divider}")
    print(" Equipment List ".center(len(divider)))
    print(f"{divider}\n")

    # Print column headers
    print("".join(f"{col:<{col_widths[col]}}" for col in columns))
    print("⫘" * len(divider))

    # Print each row of filtered equipment data
    if filtered_list:
        for eq in filtered_list:
            print("".join(f"{str(eq[col]):<{col_widths[col]}}" for col in columns))
    else:
        print("\n⌞❕⌝ No equipment found with the given criteria.")

    print(f"\n{divider}")

# Function to sort equipment
def sort_equipment():
    print("\nSorting Equipment in Progress...")

    while True:
        print("\nSorting Options:")
        print("1. Sort by Highest Daily Rate")
        print("2. Sort by Lowest Daily Rate")
        print("3. Return to Previous Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_equipment(sort_by="most_expensive")
        elif choice == "2":
            display_equipment(sort_by="cheapest")
        elif choice == "3":
            return
        else:
            print("\n⌞❕⌝ Invalid choice! Please enter 1, 2, or 3.")

# Function to filter equipment
def filter_equipment():
    print("\nFiltering Equipment in Progress...")

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
            return
        else:
            print("\n⌞❕⌝ Invalid choice! Please enter 1, 2, 3, or 4.")

# LIST OF RENTAL RECORDS

rental_records = [
    {"Client ID": "CLI01", "Client Name": "Angling Dharma", "Contact Info": "098111222333", "Equipment Code": "GEM02", "Equipment Name": "Magnetometer", "Daily Rate": 1800000, "Start Date": "24-02-2025", "End Date": "01-03-2025", "Total Days": 5, "Total Fee": 9000000},
    {"Client ID": "CLI02", "Client Name": "Blair Waldorf", "Contact Info": "089000222666", "Equipment Code": "SCI03", "Equipment Name": "Gravimeter", "Daily Rate": 3000000, "Start Date": "25-02-2025", "End Date": "26-02-2025", "Total Days": 1, "Total Fee": 3000000},
    {"Client ID": "CLI03", "Client Name": "Cersei Lannister", "Contact Info": "031665775885", "Equipment Code": "FLI08", "Equipment Name": "Thermal Cam", "Daily Rate": 1650000, "Start Date": "01-01-2025", "End Date": "07-01-2025", "Total Days": 6, "Total Fee": 9900000},
]

# FUNCTION TO DISPLAY RENTAL RECORDS

def display_rental_records(rental_records, filter_query=None, sort_by=None):
    print("\nDisplaying Rental Records in Progress...")

    if not rental_records:
        print("\n⌞❕⌝ No rental records available.")
        return

    filtered_list = [record.copy() for record in rental_records]

    # Apply filtering based on either Client ID or Client Name
    if filter_query:
        filter_query = filter_query.strip().lower()
        filtered_list = [
            record for record in filtered_list 
            if (record['Client ID'].strip().lower().startswith(filter_query) or
                record['Client Name'].strip().lower().startswith(filter_query))
        ]

    # Apply sorting based on Total Fee
    if sort_by == "highest_fee":
        filtered_list.sort(key=lambda x: int(x['Total Fee']), reverse=True)
    elif sort_by == "lowest_fee":
        filtered_list.sort(key=lambda x: int(x['Total Fee']))

    # Debugging: Check filtered records
    print(f"\nDebug: Found {len(filtered_list)} matching records.")

    # Define table columns
    columns = ["Client ID", "Client Name", "Contact Info", "Equipment Code", "Equipment Name", "Daily Rate", "Start Date", "End Date", "Total Days", "Total Fee"]
    
    # Calculate column widths dynamically
    col_widths = {col: max(len(col), max((len(str(record[col])) for record in filtered_list), default=len(col))) + 2 for col in columns}
    
    # Generate dynamic divider
    divider = "⫘" * (sum(col_widths.values()) + len(columns) - 1)
    
    # Display header
    print(f"\n{divider}")
    print(" ".join(f"{col:<{col_widths[col]}}" for col in columns))
    print(divider)
    
    if filtered_list:
        for record in filtered_list:
            print(" ".join(f"{str(record[col]):<{col_widths[col]}}" for col in columns))
    else:
        print("\n⌞❕⌝ No rental records found with the given criteria.")
    
    print(divider)

# Function to sort rental records by total fee
def sort_rental_records(rental_records):
    print("\nSorting Rental Records in Progress...")
    print("\nSort Rental Records:")
    print("1. Sort by Highest Fee")
    print("2. Sort by Lowest Fee")
    print("3. Return to Previous Menu")

    sort_choice = input("Enter your choice: ").strip()

    if sort_choice == "1":
        display_rental_records(rental_records, sort_by="highest_fee")
    elif sort_choice == "2":
        display_rental_records(rental_records, sort_by="lowest_fee")
    elif sort_choice == "3":
        return
    else:
        print("\n⌞❕⌝ Invalid choice! Please enter 1, 2, or 3.")

# Function to filter rental records by Client ID or Name
def filter_rental_records(rental_records):
    print("\nSearching Rental Records in Progress...")
    print("\nSearch Rental Records:")
    filter_query = input("Enter Client ID or Client Name (minimum 3 characters): ").strip()

    if len(filter_query) < 3:
        print("\n⌞❕⌝ Please enter at least 3 characters.")
        return

    display_rental_records(rental_records, filter_query=filter_query)

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

# FUNCTION TO RENT EQUIPMENT

import datetime

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def rent_equipment():
    print("\nRenting Equipment in Progress...")

    while True:
        code = input("\nEnter product code (e.g., GEO01, CAM10) or type 'Back' to return: ").strip().upper()

        if not code:
            print("\n⌞❕⌝ Input cannot be empty. Please enter a valid product code.")
            continue

        if code == 'BACK':
            return
        
        selected_equipment = next((eq for eq in equipment_list if eq['Code'] == code and eq['Status'] == "Available"), None)

        if not selected_equipment:
            print("\n⌞❕⌝ Equipment currently rented or not available.")
            continue  # Continue the loop to ask for another product code

        while True:
            client_id = input("\nEnter Client ID (e.g., CLI01, CLI02): ").strip().upper()

            if not client_id:
                print("\n⌞❕⌝ Client ID cannot be empty.")
                continue

            if not (len(client_id) == 5 and client_id[:3] == "CLI" and client_id[3:].isdigit()):
                print("\n⌞❕⌝ Invalid format! Use 'CLI' followed by 2 digits (e.g., CLI01, CLI02). Please try again.")
                continue

            existing_ids = {record["Client ID"] for record in rental_records}
            if client_id in existing_ids:
                print("\n⌞❕⌝ Client ID already exists. Please enter a unique Client ID.")
                continue
            break

        while True:
            name = input("\nEnter client name: ").strip().title()
            if not name:
                print("\n⌞❕⌝ Client name cannot be empty.")
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
        
        try:
            daily_rate = int(selected_equipment['Daily Rate'])
        except (ValueError, KeyError, TypeError):
            print("\n⌞❕⌝ Equipment daily rate is missing or invalid.")
            return
        
        days = (end_date - start_date).days
        total_fee = days * daily_rate
        
        selected_equipment["Status"] = "Rented"

        rental_record = {
            "Client ID": client_id,
            "Client Name": name,
            "Contact Info": contact,
            "Equipment Code": code,
            "Equipment Name": selected_equipment['Name'],
            "Daily Rate": selected_equipment["Daily Rate"],
            "Start Date": start_date.strftime('%d-%m-%Y'),
            "End Date": end_date.strftime('%d-%m-%Y'),
            "Total Days": days,
            "Total Fee": total_fee
        }

        rental_records.append(rental_record)
        
        # Rental summary generation
        summary_lines = [
            f"{'Client ID':<20}: {client_id}",
            f"{'Client Name':<20}: {name}",
            f"{'Contact Info':<20}: {contact}",
            f"{'Equipment Name':<20}: {selected_equipment['Name']}",
            f"{'Daily Rate':<20}: {daily_rate}",
            f"{'Rental Start Date':<20}: {start_date.strftime('%d-%m-%Y')}",
            f"{'Rental End Date':<20}: {end_date.strftime('%d-%m-%Y')}",
            f"{'Total Days':<20}: {days}",
            f"{'Total Fee':<20}: IDR {total_fee}"
        ]

        # Determine max width
        max_width = max(len(line) for line in summary_lines)

        # Generate dynamic divider
        divider = "⫘" * max_width

        print(f"\n{divider}")
        print(" Rental Summary ".center(max_width))
        print(f"{divider}")

        for line in summary_lines:
            print(line)

        print(f"{divider}\n")

        while True:
            more = input("\nRent another? (Yes/No): ").strip().lower()
            if more == 'yes':
                break  # Restart the process
            elif more == 'no':
                return  # Exit the function
            else:
                print("\n⌞❕⌝ Invalid input! Please enter 'Yes' or 'No'.")

# FUNCTION TO RETURN EQUIPMENT

def return_equipment():
    print("\nReturning Equipment in Progress...")

    # Get client input
    client_input = input("\nEnter Client ID or Name (minimum 3 characters) or type 'Back' to return: ").strip().lower()
    
    if client_input == 'back':
        return

    if len(client_input) < 3:
        print("\n⌞❕⌝ Please enter at least 3 characters for Client ID or Name.")
        return
    
    # Filter rental records based on input
    matching_records = [record for record in rental_records if client_input in record['Client ID'].lower() or client_input in record['Client Name'].lower()]

    if not matching_records:
        print("\n⌞❕⌝ No rental records found for the given input.")
        return

    print("\nMatching Rental Records:")
    for i, record in enumerate(matching_records, start=1):
        print(f"{i}. {record['Client Name']} (ID: {record['Client ID']}) - {record['Equipment Name']} [{record['Equipment Code']}]")

    while True:
        try:
            choice = int(input("\nSelect the number of the record to return (or 0 to cancel): ").strip())
            if choice == 0:
                return
            if 1 <= choice <= len(matching_records):
                selected_record = matching_records[choice - 1]
                break
            else:
                print("\n⌞❕⌝ Invalid selection. Please choose a valid number.")
        except ValueError:
            print("\n⌞❕⌝ Please enter a valid number.")

    equipment_code = selected_record["Equipment Code"]

    # Find the equipment in the list
    for eq in equipment_list:
        if eq["Code"] == equipment_code:
            if eq["Status"] != "Rented":
                print(f"\n⌞❕⌝ Equipment '{eq['Name']}' is not currently rented.")
                return
            
            # Ask for condition input
            while True:
                condition = input("\nCondition on return (Good/Damaged): ").strip().lower()
                if condition in ["good", "damaged"]:
                    eq["Status"] = "Unavailable" if condition == "damaged" else "Available"
                    eq["Condition"] = "Under Maintenance" if condition == "damaged" else "Good"
                    print(f"\n⌞✔⌝ Equipment '{eq['Name']}' is now marked as {eq['Status']} (Condition: {eq['Condition']}).")
                    break
                else:
                    print("\n⌞❕⌝ Invalid input! Please enter 'Good' or 'Damaged'.")

            # Remove the rental record
            rental_records.remove(selected_record)
            print(f"\n⌞✔⌝ Rental record for '{selected_record['Client Name']}' has been removed.")
            break

    # Ask user if they want to return another equipment
    while True:
        more = input("\nReturn another? (Yes/No): ").strip().lower()
        if more == 'yes':
            return_equipment()
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
        print("4. Rent Equipment")
        print("5. Return Equipment")
        print("6. Display Rental Records")
        print("7. Exit")

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
            display_rental_records_submenu()
            attempts = 0
        elif choice == "7":
            print("\nExiting programme... Goodbye!")
            break  # Ends the loop and programme
        else:
            attempts += 1  # Increment attempts on invalid input
            print(f"\n⌞❕⌝ Invalid choice! Please enter a number between 1 and 6. (Attempt {attempts}/3)")
            
            # Exit programme after 3 invalid attempts
            if attempts >= 3:
                print("\n⌞❕⌝ Too many invalid attempts! Exiting programme...")
                break  # Exit programme

# Function to display submenu 1
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

# Function to display submenu 6
def display_rental_records_submenu():
    while True:
        print("\nRental Records Menu:")
        print("1. Show All Rental Records")
        print("2. Sort Rental Records")
        print("3. Filter Rental Records")
        print("4. Return to Main Menu")

        sub_choice = input("Enter your choice: ").strip()

        if sub_choice == "1":
            display_rental_records(rental_records)  # Show all rental records
        elif sub_choice == "2":
            sort_rental_records(rental_records)  # Call sorting function
        elif sub_choice == "3":
            filter_rental_records(rental_records)  # Call filtering function
        elif sub_choice == "4":
            return  # Return to main menu
        else:
            print("\n⌞❕⌝ Invalid choice! Please enter 1, 2, 3, or 4.")

# Ensure main menu is called first when the programme starts
if __name__ == "__main__":
    main_menu()
