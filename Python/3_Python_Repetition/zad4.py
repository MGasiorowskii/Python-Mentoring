days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
print(days_of_week)

print(days_of_week.get((int(input("Select the day of the week: "))), "Lack of such a day!"))
