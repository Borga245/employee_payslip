import re
from datetime import datetime

# Function to validate the date format
def validate_date(date_str):
    date_pattern = r"\d{2}/\d{2}/\d{4}"
    return bool(re.fullmatch(date_pattern, date_str))

# Function to write employee data to the file
def write_employee_data(file, from_date, to_date, name, hours, rate, tax_rate):
    record = f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}\n"
    file.write(record)

# Function to read and process the employee data
def process_employee_data(file, from_date_input):
    total_employees = total_hours = total_tax = total_net_pay = 0
    result = {}
    
    for line in file:
        from_date, to_date, name, hours, rate, tax_rate = line.strip().split('|')
        hours = float(hours)
        rate = float(rate)
        tax_rate = float(tax_rate)
        gross_pay = hours * rate
        income_tax = gross_pay * tax_rate / 100
        net_pay = gross_pay - income_tax
        
        if from_date_input.lower() == 'all' or from_date_input == from_date:
            print(f"From Date: {from_date}, To Date: {to_date}, Name: {name}, Hours: {hours}, "
                  f"Rate: {rate}, Gross Pay: {gross_pay:.2f}, Income Tax Rate: {tax_rate}%, "
                  f"Income Tax: {income_tax:.2f}, Net Pay: {net_pay:.2f}")
            
            total_employees += 1
            total_hours += hours
            total_tax += income_tax
            total_net_pay += net_pay

    result['total_employees'] = total_employees
    result['total_hours'] = total_hours
    result['total_tax'] = total_tax
    result['total_net_pay'] = total_net_pay
    
    return result

# Main program logic
def main():
    # Open the file in append mode to add new data
    with open('employee_data.txt', 'a') as file:
        while True:
            # Get employee information
            from_date = input("Enter the From Date (mm/dd/yyyy): ")
            if not validate_date(from_date):
                print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                continue

            to_date = input("Enter the To Date (mm/dd/yyyy): ")
            if not validate_date(to_date):
                print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                continue

            name = input("Enter employee name: ")
            hours = float(input("Enter hours worked: "))
            rate = float(input("Enter hourly rate: "))
            tax_rate = float(input("Enter income tax rate: "))

            # Write data to file
            write_employee_data(file, from_date, to_date, name, hours, rate, tax_rate)

            # Ask if user wants to continue entering data
            more_data = input("Do you want to enter more data? (y/n): ")
            if more_data.lower() != 'y':
                break

    # Read data from the file for reporting
    with open('employee_data.txt', 'r') as file:
        from_date_input = input("Enter the From Date for the report (or type 'All' to see all records): ")
        if from_date_input.lower() != 'all' and not validate_date(from_date_input):
            print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
            return
        
        totals = process_employee_data(file, from_date_input)
        
        # Display totals
        print("\n--- Totals ---")
        print(f"Total Employees: {totals['total_employees']}")
        print(f"Total Hours: {totals['total_hours']:.2f}")
        print(f"Total Tax: {totals['total_tax']:.2f}")
        print(f"Total Net Pay: {totals['total_net_pay']:.2f}")

if __name__ == "__main__":
    main()
