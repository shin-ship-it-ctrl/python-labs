 # Get depth from the user and convert it to a floating-point number
depth_input = input("Enter the depth inside the earth (in km): ")
depth = float(depth_input)

# Ensure the depth is a non-negative number
if depth < 0:
     print("Depth must be a non-negative value.")


# Calculate temperature in Celsius using the formula: Celsius = 10 * depth + 20
celsius_temp = 10 * depth + 20

# Calculate temperature in Fahrenheit using the formula: Fahrenheit = 1.8 * Celsius + 32
fahrenheit_temp = 1.8 * celsius_temp + 32

#Display the results
print(f"At a depth of {depth:.2f} km:")
print(f"Temperature in Celsius: {celsius_temp:.2f}°C")
print(f"Temperature in Fahrenheit: {fahrenheit_temp:.2f}°F")


