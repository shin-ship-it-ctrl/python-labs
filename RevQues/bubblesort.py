items = [23,5,1,30,25,3,20]
print(items)
for x in range(len(items)-1):
    swapFlag = False
    for i in range(len(items)-1-x):
        if items[i] > items[i + 1]:
            items[i],items[i+1] = items[i+1],items[i]
            swapFlag = True
        print(items)
    if swapFlag == False:
        print("List already sorted.")
        break

