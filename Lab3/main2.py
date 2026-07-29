# Assume pi is 3.142
pi = 3.142

# Prompt user input for the radius and from string to float
radius = float(input("Please enter the radius of the circle: "))

# Calculate the area of the circle using the formula: Area = pi * r^2
area = pi * (radius * 2)

'''
.2f: This is the actual formatting code.
.2 specifies the precision, or how many digits should be displayed after the decimal point.
f specifies that the number should be formatted as a "fixed-point" floating-point number.

'''
 # Display the calculated area
print(f"The area of a circle with radius {radius} is {area:.2f}")



