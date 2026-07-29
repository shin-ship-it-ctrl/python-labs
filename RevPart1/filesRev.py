'''
with open("input.txt" , 'w') as inputFile:
    for i in range(5):
        print("Enter your line: " , end= "\n")
        line = input()
        inputFile.write(line)
'''

'''
with open("input.txt", 'r') as outputFile:
    content = outputFile.readlines()
    print(content)
'''

'''
    above or this one
        for line in outputFile:
        print(line.strip())
'''




'''
with open("data.txt" , "w") as inputfile:

    num_lines= int(input("Enter number of lines: "))

    for i in range(num_lines):
        line = input("Enter line: ")
        inputfile.write(line)

'''


with open("data.txt" , "r") as outputfile:
    lines = outputfile.readlines()

    for line in lines:
        print(line.split(" "))



















