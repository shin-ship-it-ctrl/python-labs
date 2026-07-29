items=[23,5,10,30,25]
pos = 0
for i in range(1,len(items)):
    if items[i] < items[pos]:
        pos = i


print("Minimum is ", items[pos])
