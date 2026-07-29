# Get user input for trip details
trip_distance = float(input("Enter the total distance of the trip in miles: "))
mpg = float(input("Enter your car's miles per gallon (MPG) estimate: "))
gas_cost_per_gallon = float(input("Enter the average cost of a gallon of gas: "))

# Input validation to ensure non-negative values
if trip_distance < 0 or mpg <= 0 or gas_cost_per_gallon < 0:
      print("\nError: Please enter non-negative values for distance and cost, and a positive value for MPG.")


# Calculate the number of gallons needed
gallons_needed = trip_distance / mpg

# Calculate the estimated cost of the trip
estimated_cost = gallons_needed * gas_cost_per_gallon

# Display the results
print(f"Gallons of gas needed: {gallons_needed:.2f}")
print(f"Estimated cost of the trip: ${estimated_cost:.2f}")


