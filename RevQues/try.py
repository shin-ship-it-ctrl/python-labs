class Student:
    def __init__(self, stud_id, stud_name, stud_age):
        self.stud_id = stud_id
        self.stud_name = stud_name
        self.stud_age = stud_age

    # Adding a __str__ method makes printing details much easier
    def __str__(self):
        return f"Name: {self.stud_name}, Age: {self.stud_age}"


myDict = {}

# We can use a loop to add multiple students
# Let's add 2 students for this example
for i in range(2):
    print(f"\nEntering details for Student {i + 1}:")
    s_id = input("Enter student ID: ")
    s_name = input("Enter student name: ")
    s_age = input("Enter student age: ")

    # Create the object using the variables we just input
    stud = Student(s_id, s_name, s_age)

    # Store in dictionary: Key is the ID, Value is the whole Object
    myDict[stud.stud_id] = stud

# Search Section
print("\n--- Search Utility ---")
search_id = input("Enter student ID you are looking for: ")

if search_id in myDict:
    # Retrieve the object
    result = myDict[search_id]
    # We convert the object to a string to print it with your text
    print("Details of ID " + search_id + " are: " + str(result))
else:
    print("Student not found")


