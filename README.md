# Python Fundamentals Application: Building Geophysical Equipment Rental Manager (GERM)

## Project Overview
The **Geophysical Equipment Rental Manager (GERM)** is a console-based Python application developed to replace inefficient manual logs and spreadsheets with a structured, reliable system.  

Small businesses, laboratories, and universities often struggle with tracking equipment usage, availability, and payments, which lead to lost time, errors, and missed revenue. This project provides a streamlined solution that digitises inventory and rental workflows, ensuring accuracy, accountability, and ease of use.

The system enables users to:
- View, sort, and filter equipment  
- Add new equipment with validation rules  
- Remove items when no longer needed  
- Rent out and return equipment seamlessly  
- Track rental history, client details, and payments  

---

## Features

### Equipment Management
- **Display Equipment List**: View inventory with sorting (by daily rate) and filtering (by availability).  
- **Add Equipment**: Add new items with unique codes, names, and daily rates.  
- **Remove Equipment**: Safely remove items only when they are not currently rented.  

### Rental Operations
- **Rent Equipment**: Record transactions with client details, rental period, and automatically calculated fees.  
- **Return Equipment**: Mark items as returned, update condition (Good/Damaged), and close the rental record.  

### Rental Records Management
- **Display Rental Records**: Access complete transaction history with sorting (by total fee) and filtering (by client ID or name).  
- **Dynamic Summaries**: Generate detailed transaction summaries for reporting and verification.  

---

## How to Run

1. Ensure you have **Python 3.7+** installed.  
2. Download the project files.  
3. Open a terminal/command prompt in the project directory.  
4. Run the main program:  
   ```bash
   python main.py
5. Follow the Main Menu prompts to manage equipment, rentals, and records.

---

## Input Formats & Constraints
- **Equipment Code**: 3 letters followed by 2 digits (e.g., `GEO01`, `CAM10`)  
- **Client ID**: 'CLI' followed by 2 digits (e.g., `CLI01`, `CLI02`)  
- **Dates**: DD-MM-YYYY format  
- **Contact Info**: Numbers only, 8–12 digits  
- **Rental Rate**: Positive integer

---

## Notes
- Items cannot be removed while rented.
- Equipment condition must be updated upon return.
- Rental fees are calculated as *number of days × daily rate*.

---

## Dependencies
- Python standard libraries only (`datetime`)

---

## Example Workflow
1. Add a new seismograph (`GEO01`) to the inventory.  
2. Rent the seismograph to a client for 5 days.  
3. View all rental records, sorted by highest total fee.  
4. Return the seismograph and update its condition if needed.  
5. Remove any damaged equipment that requires maintenance.

---

## Impact
GERM demonstrates how a data-driven, rule-based system can transform routine operations into an efficient, transparent process. By designing this project, I applied my skills in Python programming, data validation, workflow design, and usability-focused problem-solving to deliver a tool that reduces errors, saves time, and supports better decision-making.

---

- Presentation: [GERM Presentation](https://drive.google.com/file/d/1C-regRqSA5F-qkRF1GglHilzfG3i38-8/view?usp=sharing)
