'''
3. Write a program that displays the sum of all multiples of 5 between 0 and 100 inclusive.
'''

total = 0
for i in range(1,101):
    if i % 5 ==0:
        total = total + i

print("Total multiples of 5 is " + str(total))
