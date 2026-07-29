'''

class Employee:
    def __init__(self,name,nid,position,basic_salary):
        self.name = name
        self.nid = nid
        self.position = position
        self.basic_salary = basic_salary

    def display(self):
        print("Name: " + str(self.name))
        print("NID: " + str(self.nid))
        print("Position: " + str(self.position))
        print("Basic salary: " + str(self.basic_salary))
employee_list=[]

employee1 = Employee("John" , "J6566" , "Manager" , 60000)
employee_list.append(employee1)
employee2 = Employee("Cheong" , "C7888" , "Worker" , 35000)
employee_list.append(employee2)
employee3 = Employee("Sunil" , "S4532" , "Secretary" , 45000)
employee_list.append(employee3)

for emp in employee_list:
    emp.display()
    print("--------------------")

total = 0
for i in employee_list:
    total = total + i.basic_salary
print("Total salary of all 3: " + str(total))
print("")

emp_dict= {}
for lists in employee_list:
    key = lists.nid
    value = str(lists.name) + "#" + str(lists.position) + "#" + str(lists.basic_salary)
    emp_dict[key] =value
print(emp_dict)
print("")

search_id = input("Enter the id of employee you want to search: ")

if search_id in emp_dict:
    data = emp_dict[search_id]
    details = data.split("#")
    if len(details)==3:
        name, pos, salary = details

        print("Name: " + name)
        print("Position: " + pos)
        print("Salary: " + salary)
    else:
        print("Not correct format")
else:
    print("Employee not found")




'''



the_list = [["Ria", 67, 87, 65], ["Paul", 56, 45, 87], ["Ryan", 87, 56, 45]]
'''
num_stud=int(input("Enter the number of student you want to search: "))
for i in range(1,num_stud+1):
    stud_name = input("Enter the student name: ")
    score1 = int(input("Enter the student score: "))
    score2 = int(input("Enter the student score: "))
    score3 = int(input("Enter the student score: "))

    inner_loop = [stud_name,score1,score2,score3]

    the_list.append(inner_loop)

'''

# 1. Initialization
text = "pythonisAmazing!"
clean_text = text.strip()
sorted_chars = sorted(clean_text)
sorted_str = "".join(sorted_chars)
print(sorted_str)

print(text[2:8:1])




























