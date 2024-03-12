def day_of_week(day_num):
    days = [
        "Sunday", 
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday"
    ]
    return days[day_num]

day_num = int(input("Enter the day number (0-6): "))

result = day_of_week(day_num)
print("The day that matches the number you entered is:", result)
#Supawit Sangrattanayon 64050694

