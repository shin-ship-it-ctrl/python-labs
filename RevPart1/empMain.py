class Employee:
    def __init__(self,sid,name,position,salary):
        self.sid = sid
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        print("ID: " + self.sid)
        print("Name: " + self.name)
        print("Position: " + self.position)
        print("Salary: " + self.salary)

employee_list=[]
employee1 = Employee( "J6566","John Smith" , "Manager" , 60000)
employee_list.append(employee1)
employee2 = Employee( "C7888","Cheong Yong"  , "Worker" , 35000)
employee_list.append(employee2)
employee3 = Employee( "S4532","Sunil Khan"  , "Secretary" , 45000)
employee_list.append(employee3)

'''
total_salary = 0
for item in employee_list:
    total_salary = total_salary + item.salary

print("Total Salary " + str(total_salary))

my_dict= {}
def conver_dict(obj):
    value = ""
    for i in obj:
        key = i.sid
        value = str(i.name) + "|" + str(i.position) + "|" + str(i.salary)
        my_dict[key] = value
    print(my_dict)

print(conver_dict(employee_list))

def find_values(target):

    value = my_dict.get(target)
    details = value.split("|")
    if len(details )== 3:
        nam,pos,sal = details
        print("Name: " + str(nam))
        print("Position: " + str(pos))
        print("Salary: " + str(sal))
    else:
        print("SID not found.")


print(find_values("J6566"))


'''



total = 0

for item in employee_list:
    total+= item.salary
print("Total salary: " + str(total))
print("")

employee_dict={}

for item in employee_list:
    key = item.sid
    value = str(item.name) +  "|" + str(item.position) + "|" + str(item.salary)
    employee_dict[key] = value

print(employee_dict)
print("")

search_id = input("Enter the ID of employee you want to search: ")

if search_id in employee_dict:
    data = employee_dict.get(search_id)
    details = data.split("|")
    if len(details) == 3:
        nam,pos,sal = details
        print("Name: " + str(nam))
        print("Position: " + str(pos))
        print("Salary: " + str(sal))
    else:
        print("Incorrect format! ")
else:
    print("SID not found!")














