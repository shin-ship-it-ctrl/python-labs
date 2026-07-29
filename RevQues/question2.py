'''
The University of Mauritius wants to store student records in a Python program.
Each student has:
a student ID
a name
an age
Write a Python program that:

defines a class named Student with attributes:
student_id
name
age

creates a dictionary to store Student objects, where:
the key is the student ID
the value is the corresponding Student object
adds at least to the dictionary

asks the user to enter a student ID

searches for that ID in the dictionary

if the student is found, displays the student's details

if the student is not found, displays:
"Student not found"

Example

If the user enters: 2512324
Output:
ID: 2512324  , Name: Aisha, Age: 20

If the user enters: 2519999
Output:
Student not found
'''

class Student:
    def __init__(self,stud_id, stud_name, stud_age):
        self.stud_id=stud_id
        self.stud_name=stud_name
        self.stud_age=stud_age

    def __str__(self):
        return "ID: " + self.stud_id + ", Name: " + self.stud_name + ", Age: " + self.stud_age
myDict = {}


for i in range(1,2):
    s_id = input("Enter student ID: ")
    s_name = input("Enter student name: ")
    s_age = input("Enter student age: ")
    stud = Student(s_id, s_name, s_age)
    myDict[stud.stud_id] = stud



search_id = str(input("Enter student ID you looking for: "))

if search_id in myDict:
    result = myDict.get(search_id)
    print("Details of ID " + search_id + " are " + str(result))
else:
    print("Student not found")
