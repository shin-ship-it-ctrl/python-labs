'''
A small shop sells the following items:
pen - Rs 15
pencil - Rs 10
eraser - Rs 8
ruler - Rs 25
Write a Python program that:

stores the items and their prices in a dictionary

asks the user to enter the name of an item

checks whether the item exists in the dictionary

displays the price of the item if found

displays "Item not available" if the item is not found

Input: pen
Output: The price of pen is Rs 15
Input: book
Output: Item not available
'''

items = {"pen": "Rs 15", "pencil": "Rs 10", "eraser": "Rs 8", "ruler":"Rs 25"}
print("Enter the name of the item you want to check: ",end="")
user = input()
if user in items:
    print("The price of " + user + " is " + items.get(user))
else:
    print("The item " + user + " is not available")





