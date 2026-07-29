'''
5. Write a Python program to calculate the surface area of a sphere. The program should
prompt the user to enter the radius of a sphere and then calculate the surface area of the
sphere. The surface area of a sphere is given by the formula, area = 4πr2. (Use π = 3.14).
The program should only accept non-zero positive values for the radius and display an error
message if the user tries to input a zero or negative value.
'''
pi = 3.14
radius = int(input("Enter the radius of a sphere: "))
if radius < 0:
    print("The radius of a sphere should not be less than or equal to zero.")

area = 4 * pi * (radius ** 2)
print("The surface area of a sphere is ", area)
