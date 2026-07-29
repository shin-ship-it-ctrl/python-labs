'''
6. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[Formula: c/5 = f-32/9 [where c = temperature in Celsius and f = temperature in
Fahrenheit]. Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
'''
celcius = int(input("Enter the temperature in Celcius: "))
fahrenheit = int(input("Enter the temperature in Fahrenheit: "))

'''
celcius to fahrenheit formula: 
f - 32 / 9 = c/5
f /9 = c/ 5 + 32
f = (c + 32 * 9)/ 5
f = (celcius * 9/5) + 32

fahrenheit to celcius formula:
c/5 = f-32/9 
c = (fahreinheit - 32 * 5) / 9
'''
c = int((fahrenheit - 32) * 5 / 9)
f = int((celcius * 9/5) + 32)

print("The temperature of Celcius to Fahrenheit is ", str(f))
print("The temperature of Fahrenheit to Celcius is ", str(c))
