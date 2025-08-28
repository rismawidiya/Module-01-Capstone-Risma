# Geophysical Equipment Rental Manager

## Project Overview
The **Geophysical Equipment Rental Manager** is a console-based Python application designed to help small businesses, laboratories, universities, and other organizations efficiently manage their rental equipment. The system allows users to:

- View, sort, and filter equipment
- Add new equipment to the inventory
- Remove existing equipment
- Rent out and return equipment
- Track rental records, including client and payment details

This project is ideal for organizations that need a simple yet effective tool to manage inventory and rental operations.

## Features

### Equipment Management
- **Display Equipment List**: View all equipment with optional sorting (by daily rate) and filtering (by availability status).  
- **Add Equipment**: Add new items to the inventory with unique codes, names, and daily rental rates.  
- **Remove Equipment**: Remove equipment that is not currently rented.  

### Rental Operations
- **Rent Equipment**: Record rental transactions with client details, start and end dates, and automatically calculate total fees.  
- **Return Equipment**: Mark equipment as returned, update condition (Good/Damaged), and remove corresponding rental records.  

### Rental Records Management
- **Display Rental Records**: View all rental transactions with optional sorting (by total fee) and filtering (by client ID or name).  
- **Dynamic Summaries**: Generates rental summaries for each transaction for easy tracking and verification.

## How to Run

1. Ensure you have **Python 3.7+** installed.
2. Download the project files.
3. Open a terminal/command prompt in the project directory.
4. Run the main program.
5. Follow the Main Menu prompts to navigate through the system.

## Input Formats & Constraints
- **Equipment Code**: 3 letters followed by 2 digits (e.g., GEO01, CAM10)  
- **Client ID**: 'CLI' followed by 2 digits (e.g., CLI01, CLI02)  
- **Dates**: DD-MM-YYYY format  
- **Contact Info**: Numbers only, 8–12 digits  
- **Rental Rate**: Positive integer

## Notes
- Rented equipment cannot be removed until returned.  
- Equipment condition must be updated upon return.  
- Rental calculations are based on the number of rental days multiplied by the daily rate.

## Dependencies
- Built-in Python libraries only (`datetime`)

## Example Workflow
1. Add a new seismograph (`GEO01`) to the inventory.  
2. Rent the seismograph to a client for 5 days.  
3. View all rental records, sorted by highest total fee.  
4. Return the seismograph and update its condition if needed.  
5. Remove any damaged equipment that requires maintenance.

---

- Presentation: [GERM Presentation](https://drive.google.com/file/d/1C-regRqSA5F-qkRF1GglHilzfG3i38-8/view?usp=sharing)
