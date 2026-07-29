'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)


# (i) Define a Queue to represent a line of Employee objects
employee_queue = []

# (ii) Enqueue at least three Employee objects
employee_queue.append(Employee("Alice", 50000))
employee_queue.append(Employee("Bob", 62000))
employee_queue.append(Employee("Charlie", 45000))
employee_queue.append(Employee("Diana", 75000))

print(f"Starting processing for {len(employee_queue)} employees...\n")

# (iii) & (iv) Process the Queue until all employees are handled
while len(employee_queue) > 0:
    # Dequeue the first employee in line
    current_employee = employee_queue.pop(0)

    # Give a salary raise of 10%
    current_employee.apply_raise(10)

    # Print their name and new salary
    print(f"Employee: {current_employee.name} | New Salary: ${current_employee.salary:,.2f}")

print("\nAll employees have been processed.")

'''

'''
dict1 = {12: "One" , 34: "Two",56: "Three",78: "Four",89: "Five" }


mydict = dict1.copy()

for key in mydict: # iterates over keys
    print(key, mydict[key])
print("-" * 20)
for key, value in mydict.items(): # iterates over key-value pairs
    print(key, value)

set1 = set({})
for key, value in mydict.items():
    set1.add(key)
print(set1)
print("-" * 20)
set1.discard("Three")
print(set1)
print("-" * 20)
set1.remove(78)
print(set1)


'''


word = "e  d  r   t   yjnb"
print(word)
print("-" * 20)
print(word.upper())
print("-" * 20)
print(word.startswith("e"))
print("-" * 20)
print(word.endswith("j"))
print("-" * 20)
print(word.replace(" ",""))
print("-" * 20)
print(word.count("j"))
print("-" * 20)
print(word.index("n"))
print("-" * 20)
print(word.split())
print("-" * 20)