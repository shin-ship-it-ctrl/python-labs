# Assume pi to be 3.142 as requested
pi = 3.142

 # Request user input for the radius and height
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Check for non-negative values
if radius < 0 or height < 0:
   print("Error: Radius and height must be non-negative values.")

# Calculate the area using the formula: TSA = 2*pi*r*(r+h)
area = 2 * pi * radius * (radius + height)

# Display the calculated area, formatted to two decimal places
print(f"\nThe total surface area of the cylinder is: {area:.2f}")



