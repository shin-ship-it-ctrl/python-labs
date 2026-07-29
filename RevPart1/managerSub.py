'''
from empMain import Employee
class Manager(Employee):
    def __init__(self,sid,name,position,salary,hrs_worked):
        super().__init__(sid,name,position,salary)
        self.hrs_worked = hrs_worked



from empMain import my_dict

'''

'''
def linear_search(target,items):

    i = 0

    for i in range(len(items)):
        if items[i] == target:
            return  i , True
    return -1, False

num = int(input("Enter a number: "))
val,found = linear_search(num,list_1)

if found:
    print("Found at Position: " + str(val))
else:
    print(str(num) + " not Found!")
    
def linearSearch(target,items):
    positions = []
    i = 0
    for i in range(len(items)):
        if items[i] == target:
            positions.append(i)
    if len(positions) > 0:
        return positions , True
    else:
        return positions, False

num = int(input("Enter a number: "))

val , found =linearSearch(num,list_1)

if found:
    print("Found at Position(s): " + str(val))
else:
    print(str(num) + " not Found!")

'''


'''
def selection_sort(items):

    n = len(items)

    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if items[j] < items[min_index]:
                min_index=j

        items[i],items[min_index] = items[min_index],items[i]
    return "Items sorted in list: " + str(items)

print(selection_sort(list_1))

'''


'''
def insertion_sort(items):

    for i in range(1,len(items)):
        key = items[i]
        j = i - 1

        while j >= 0 and items[j] > key:
            items[j+1] = items[j]
            j = j - 1

        items[j+1] = key
    return "Items sorted in list: " + str(items)

list_1 = [23,45,7,1,23,9,45,89,45,98]
print(insertion_sort(list_1))
'''



'''
def insertion_sort_2d(items):
    for i in range(1, len(items)):
        column_index = 0
        key = items[i]  # This is the entire sub-list, e.g., [23, 101]
        j = i - 1

        # Compare the specific column value
        while j >= 0 and items[j][column_index] > key[column_index]:
            items[j + 1] = items[j]
            j -= 1
            column_index = column_index + 1
        items[j + 1] = key

    return items


# Example: Sorting by age (index 0)
students = [[23, 105,107], [19, 101,98], [21, 102,45]]
print(insertion_sort_2d(students))
# Output: [[19, 101], [21, 102], [23, 105]]


'''

'''

items1= ["a","b","c","d","e","f"]
revervesed_items=items1[::-1]
print(revervesed_items)

'''
'''
numbers = [23, 45, 12, 89, 34, 7]

# Initialize with the first element
current_max = numbers[0]

for num in numbers:
    if num > current_max:
        current_max = num

print(f"The maximum value is: {current_max}")

'''




'''
list1.extend(list2)
list3 = sorted(list1)
print(list3)
list4=list1+ list2
print(list4)
del list1[4]
print(list1)
del list1[2:4]
print(list2.index(56))

list4.insert(2,56)
print(list4)
list3 = list(reversed(list4))
print(list3)
print(sorted(list2))

print("")

tuple1 = (1,2,3,4,5,5,6,7,8)
print(tuple1)
tuple2 = tuple(reversed(tuple1))
print(tuple2)
tuple3 = (0,7,5,3,2,5,23,45,11)
tuple4 = tuple(sorted(tuple3))
print(tuple4)


print(dict1.keys())
print(dict1.items())
print(dict1.values())

'''
'''
for i in range(len(list1)):
    key = list1[i]
    j=i-1

    while j >= 0 and list1[j] > key:
        list1[j+1] = list1[j]
        j-=1
    list1[j+1] = key
print("Sorted list1: " + str(list1))

'''




'''
list1=[[78,2,64],
       [7,56,13],
       [56,7,90],
       [5,72,18]]
target = int(input("Enter a number: "))
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] == target:
            print("Found: " +str(target) + " at Row: "  + str([i]) + " and Column: " + str([j]))
'''

'''
def calculate_diagonal(items):

    first_diagonal = 0
    second_diagonal = 0
    total = 0

    for i in range(len(items)):
        first_diagonal += items[i][i]
        second_diagonal += items[i][len(items)-1-i]
        total = abs(first_diagonal - second_diagonal)

    return total


list1=[[1,5,9],
       [5,2,0],
       [3,5,9]]

print(calculate_diagonal(list1))
'''



'''
for country in country_list:
    if "i" in country.lower():
        new_list.append(country)
        
country_list=["Mauritius","Seychelles","Maldives","Singapore","Kenya","Togo","Italy"]
new_list = [country for country in country_list if "i" in country.lower()]


print(country_list)
print(new_list)
'''















