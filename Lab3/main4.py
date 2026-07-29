
# Request user input for the distances and speeds for each segment
d1 = float(input("Enter the distance for segment 1 (in km): "))
s1 = float(input("Enter the speed for segment 1 (in km/h): "))
d2 = float(input("Enter the distance for segment 2 (in km): "))
s2 = float(input("Enter the speed for segment 2 (in km/h): "))
d3 = float(input("Enter the distance for segment 3 (in km): "))
s3 = float(input("Enter the speed for segment 3 (in km/h): "))

 # Calculate the total distance
total_distance = d1 + d2 + d3

 # Calculate the time taken for each segment and the total time
# Timer = Distance / Speed
time1 = d1 / s1
time2 = d2 / s2
time3 = d3 / s3
total_time = time1 + time2 + time3

# Calculate the average speed over the whole journey
# Average Speed = Total Distance / Total Time
average_speed = total_distance / total_time

'''
.2f: This is the actual formatting code.
.2 specifies the precision, or how many digits should be displayed after the decimal point.
f specifies that the number should be formatted as a "fixed-point" floating-point number.

'''

# Display the results
print(f"Total distance travelled: {total_distance:.2f} km")
print(f"Total time taken for the whole journey: {total_time:.2f} hours")
print(f"Average speed over the journey: {average_speed:.2f} km/h")


