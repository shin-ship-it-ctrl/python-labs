class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def displaydetails(self):
        return "Name: " + self.name + "\nGrade: " + self.grade



students_list= [Student("John","A") , Student("Alicia","E"), Student("Bob","C"), Student("Caren","D")]

'''
def selection_sort(students_list):
    n=len(students_list)
    for i in range(n):
        the_max= i
        for j in range(i + 1,n):
            if students_list[j].grade < students_list[the_max].grade:
               the_max  = j
        students_list[i], students_list[the_max] = students_list[the_max], students_list[i]

    return [student.displaydetails() for student in students_list]

results = selection_sort(students_list)
for info in results:
    print(info)
'''

'''
def insertion_sort(students_list):
    for i in range(1, len(students_list)):
        the_student = students_list[i]
        j = i - 1
        while j >= 0 and students_list[j].grade > the_student.grade:
            students_list[j+1] = students_list[j]
            j -= 1
        students_list[j+1] = the_student

    return [student.displaydetails() for student in students_list]

for info in insertion_sort(students_list):
    print(info)
'''

'''
def bubbleSort(students_list):
    n=len(students_list)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - 1 - i):
            if students_list[j].grade > students_list[j+1].grade:
                
                students_list[j], students_list[j+1] = students_list[j+1], students_list[j]
                swapped = True

        if not swapped:
            break

    return [student.displaydetails() for student in students_list]

results = bubbleSort(students_list)
for info in results:
    print(info)




'''
'''
for i  in range(3):
    print("Enter student name: ")
    name = input()
    print("Enter student grade: ")
    grade = input()
    newStudent = Student(name,grade)
    students_list.append(newStudent)



for student in students_list:
    print(student.displaydetails())
'''

'''
target_name = input("Enter student name: ")
def find_student_by_name(students_list, target_name):
    for student in students_list:
        if student.name.lower() == target_name.lower():
        return student
    return None
'''