#Prompting user to enter length and width
print("Please enter length of your garden: " , end = " ")
garden_length = int(input())
print("Please enter width of your garden: " , end = " ")
garden_width = int(input())
#Calculating area of the garden
area = garden_length * garden_width
#Printing result of calculation
print("The area of your garden is: ", area)