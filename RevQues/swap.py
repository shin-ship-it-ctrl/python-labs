items= [23,5,10,30,25,3]


print(items)
for x in range(len(items)):
    pos = x
    for i in range(1,len(items)):
        if items[i]< items[pos]:
                pos=i
                temp = items[i]
                items[i] = items[pos]
                items[pos] = temp



print(items)
