
'''
num1 = 10
num2 = 5
result = num1 + num2
print(result)



number =int(input("Enter a number: "))
if number % 2 == 0:
    print("Number is even! ")
else:
    print("Number is odd! ")



total = 0
i = 1
while i <= 100:
    total = total + i
    i +=1
print(total)


for i in range(4):
    for j in range(6):
        print("*" , end="   ")
    print()


name = input("Enter your name: ")
score1 = int(input("Please enter your score in ICDT 1016Y: "))
score2 = int(input("Please enter your score in ICDT 1201: "))

total = score1 + score2
average = total / 2

print("Name: " + name + " Average: " + str(average))


s1 = int(input("Enter speed 1: "))
s2 = int(input("Enter speed 2: "))
s3 = int(input("Enter speed 3: "))
d1=int(input("Enter distance 1: "))
d2=int(input("Enter distance 2: "))
d3=int(input("Enter distance 3: "))

total_distance = d1 + d2 + d3
total_time_taken = (d1/s1) + (d2/s2) + (d3/s3)
average_speed = total_distance / total_time_taken

print("Total distance: " + str(total_distance))
print("Total time taken: " + str(total_time_taken))
print("Average speed: " + str(average_speed))


pi = 3.142
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

area = (2 * pi * (radius ** 2)) + (2 * pi * radius * height)
print("Area: " + str(area))



depth = float(input("Enter depth: "))

celcius = 10 * depth + 20
fahrenheit = 1.8 * celcius + 32

final_celcius = round(celcius, 2)

print("Celcius: " + str(final_celcius))
print("Fahrenheit: " + str(round(fahrenheit,2)))


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is even!")
else:
    print("Number is odd!")



num1= int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

total = num1 + num2

if (total >= 15) and (total <= 20):
    total = 20
print("Total: " + str(total))



result = 0

for i in range(0,101,5):
    result = result + i
print("Result: " + str(result))


n = int(input("Enter a number: "))

if n > 100:
    print("Wrong Input")
else:
    for i in range(1, n + 1):
        if n % i ==0:
            print("Factor of " + str(n) + " : " + str(i))




pi = 3.14
radius = float(input("Enter the radius: "))
area = 0
if radius < 0:
    print("Radius cannot be negative")
else:
    area = 4 * pi * radius * 2

print("Area: " + str(area))



c = int(input("Enter temperature in celcius: "))
f = int(input("Enter temperature in fahrenheit: "))


celcius = 5 * (f - 32)/9
fahrenheit = (9/5 * c) + 32

print("Fahrenheit into Celcius: " + str(round(celcius)))
print("Celcius into Fahrenheit: " + str(round(fahrenheit)))


dog_year = int(input("Enter a dog year: "))

if dog_year == 1:
    dog_age = 10.5
elif dog_year == 2:
    dog_age = 10.5 + 10.5
else:
    dog_age = 21 + (dog_year - 2) * 4

print("Dog Age: " + str(dog_age))
def func(x, y=[]):
    y.append(x)
    return y
print(func(10))
print(func(20, []))
print(func(30))

def calculate_order(items=[] , discount_percent = 0):
    total = 0
    for item in items:
        value = item[0] * item[1]
        total = total + value
    print("Total order: " + str(total))

items1 = [(25.99, 2), (10.50, 1)]
result1 = calculate_order(items1)




def prime_number(num):
    if num < 2:
        print("Not a prime number: " + str(num))
        return

    for i in range(2, num):
         if num % i ==0:
            print("Not a prime number: " + str(num))
            return
    print("Prime number: " + str(num))

for j in range(1,11):
    prime_number(j)



    def is_password(password):
    if len(password) < 8:
        return False , "too short"
    has_upper = False
    has_digits = False
    for char in password:
        if char.isupper():
            has_upper= True
        if char.isdigit():
            has_digits = True
    if has_upper and has_digits:
        return True , "Meets all rules."
    elif not has_upper:
        return False, "Missing uppercase."
    else:
        return False, "Missing digits."



print(is_password("shbhSDFGjhjhQ"))
print(is_password("weak"))
print(is_password("dfaghGJ2"))
print(is_password("wdafgshb1"))
'''

'''
mylist=[]
for i in range(1,11):
    mylist.append(i)

new_list=[]
for i in range(11,21):
    new_list.append(i)

mylist.extend(new_list)
print(mylist)
print("")
mylist.remove(11)
print(mylist)
print("")
the_list=[]
thelist = mylist + new_list
print(thelist)
print("")
del mylist[12]
print(mylist)
print("")
print(mylist.index(7))
print("")
value=[4,7,0,2,5,14,6,8,21,5,8,90]
print(value)
print("")
value.sort()
print(value)
print("")
sort_list = sorted(value)
print(sort_list)
print("")
value.reverse()
print(value)
print("")
newlist=reversed(value)
print(newlist)
print("")
L = [3,2,1]
print(sorted(L))
print(L)
'''


'''
mydict={34:"John", 56: "Smith","name": "Ria"}
print(mydict["name"])
print("")
print(mydict.get("name"))
print("")
mydict.update({"city": "New York"})
print(mydict)
print("")
mydict.pop(56)
print(mydict)
print("")
mydict.popitem()
print(mydict)
print("")
print(mydict.items())
print("")
for key,value in mydict.items():
    print(key, value)
print("")
'''

'''
mytuple= ()
for i in range(1,11):
    mytuple = mytuple + (i,)
print(mytuple)
print("")
print(type(mytuple))
print("")
print(mytuple.index(4))
print("")
new_list = list(mytuple)
print(new_list)
print("")
'''


'''
word = "soobrayen"
print(len(word))
print("")
print(word[0:8:5])
print("")
print(word.startswith("soob"))
print("")
new_word="   whwheuj  sjmsjm   "
print(len(new_word))
print("")
print(new_word)
print("")
print(word.upper())
print("")
words="abcdefghijklmnopqrstuvwxyz"
word1 = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
word2 = words + " " + word1
print(word2.split())
'''

'''
year = int(input("Enter year you were born: "))
now_age = 2026 - year
if now_age < 18:
    print("You are a child aged: " + str(now_age) + " years old")
else:
    print("You are an adult aged: " + str(now_age) + " years old")


myList=[0,1,2,3,4,5,6,]
print(len(myList))
'''

'''



my_list=[]

for i in range(11):
    num=int(input("Enter number : "))
    my_list.append(num)
max_num=max(my_list)
print(max_num)
print("")
min_num=min(my_list)
print(min_num)

'''

'''
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

# Step 1: Just use one flat list to store all data
data = []
for i in range(rows * cols):
    item = input("Enter item : ")
    data.append(item)

# Step 2: Display in Row Major order using math
print("Row Major Output:")
for c in range(cols):
    for r in range(rows):
        # Calculate the index to skip rows and grab the column items
        print(data[c * rows + r], end=", ")

# Step 2: Display in Column Major order using math
print("Row Major Output:")
for c in range(cols):
    for r in range(rows):
        # Calculate the index to skip rows and grab the column items
        print(data[r * cols + c], end=", ")

'''

'''

mytuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
total = 0
count = 0
for inner in mytuple:
    for item in inner:
        total += item
        count += 1
        

average = total/count
print("Average: " + str(average))

'''
'''
mytuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

# Identify how many elements are in each inner tuple (the columns)
num_columns = len(mytuple[0])
# Identify how many inner tuples there are (the rows)
num_rows = len(mytuple)

averages = []

# Loop through each column index (0, 1, 2, 3)
for i in range(num_columns):
    column_sum = 0
    # Loop through each row to get the element at the current column index
    for row in mytuple:
        column_sum += row[i]

    # Calculate the average for this specific column
    averages.append(column_sum / num_rows)

print("Average value of the numbers of the said tuple of tuples: " + str(averages))

'''
'''
tuples = (('333', '33'), ('1416', '55'))

# Create a list to store the converted inner tuples
new_list = []

for inner_tuple in tuples:
    # Convert each string in the inner tuple to an integer
    converted_items = []
    for item in inner_tuple:
        converted_items.append(int(item))

    # Convert the inner list back to a tuple and add it to our main list
    new_list.append(tuple(converted_items))
    print(converted_items)
    print(new_list)

# Final conversion to a tuple of tuples
final_result = tuple(new_list)

print(f"Original: {tuples}")
print(f"Converted: {final_result}")

'''

'''

my_tuple=(1,2,3)
val = ""
for item in my_tuple:
    val = val + str(item)
print("Tuple: " + str(my_tuple) + " into integer: " + str(val))
'''

'''
mydict= {}
items = int(input("Enter number of items: "))

def insert_data(n):
    for i in range(n):
        key = input("Enter Barcode Number : ")
        name = input("Enter Item Name : ")
        price = float(input("Enter Item Price : "))
        mydict[key] = (name, price)


def search_value(target):
    value = mydict.get(target)
    print("Values of Barcode Number : " + str(target) + " are: " + str(value))

    if value:
        print("Results for Barcode: " + str(target))
        name, price = value
        print("Name  :  " + str(name))
        print("Price : $" + str(price))
    else:
        print("Error: Barcode " + str(target) + " not found in the system.")

print(insert_data(items))
print(search_value("J6789"))

'''



'''
def priceCheck(barCodeDS)
    while True:
    barCode=scanBarCode() # this function returns the scanned barcode.
    #Missing Code to fetch article’s details from barCodeDS and display name and price.
    value = barcodeDS.get(barCode)
    if value:
        product_info = value.split("|")
        name = product_info[0]
        price = product_info[1]
        
        print("Results for barcode: " + str(barCode))
        print("Name  :  " + str(name))
        print("Price : $" + str(price))
'''





list_1 = [[23,45,7],[1,23,9],[45,89,98]]

def bubble_sort(items):

    for i in range(len(items)-1):
        swapped = False
        for j in range(0,len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j+1], items[j] = items[j], items[j+1]
                swapped = True

        if not swapped:
            break

    return "Items in sorted list: " + str(items)

print(bubble_sort(list_1))



