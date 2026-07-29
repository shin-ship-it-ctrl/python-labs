min_sleep = 9999
min_date = 0
for day in range(1,30):
    print("Enter sleephours: " , end= "")
    sleephours = float(input())
    if float(sleephours < min_sleep):
        min_sleep = sleephours
        min_date = day

print("Loop finished")

print("The minimum sleep time is day ",min_date , " with ", min_sleep, " hour(s)")
