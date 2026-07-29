'''
7. Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog
year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15
The dog's age in dog's years is 73
'''
human_age =int(input("Input a dog's age in human years: "))
dog_age = 0
if human_age <= 2 :
    dog_age = human_age * 10.5
else:
    dog_age = 21 + (human_age - 2) * 4

print("The dog age is :  " , dog_age)

