#Prompt user to enter his/her mark
print("Please enter your mark: " , end= "")
mark = int(input())
if mark >= 90 and mark <= 100:
    print("You got Grade A! Congratulations!")
elif mark >= 80 and mark <= 89:
    print("You got Grade B! Very Good!")
elif mark >= 70 and mark <= 79:
    print("You got Grade C! Good!")
elif mark >= 60 and mark <= 69:
    print("You got Grade D! Can do better!")
elif mark < 60:
    print("You got F! Have to concentrate more!")
else:
    print("You entered a mark out of range! Try again!")


