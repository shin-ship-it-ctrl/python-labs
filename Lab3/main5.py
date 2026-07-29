#Prompt user hours worked and convert to a floating-point number
hours_worked = float(input("Enter the number of hours worked: "))

# Prompt user for pay and convert to a floating-point number
pay_rate = float(input("Enter the hourly pay rate: "))

# Check for valid input
if hours_worked < 0 or pay_rate < 0:
    print("Error: Hours worked and pay rate must be positive values.")


# Calculate the salary using the provided formula
salary = hours_worked * pay_rate

'''
.2f: This is the actual formatting code.
.2 specifies the precision, or how many digits should be displayed after the decimal point.
f specifies that the number should be formatted as a "fixed-point" floating-point number.

'''

# Display the calculated salary, formatted to two decimal places
print(f"Total salary: ${salary:.2f}")

