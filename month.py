month_all = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

num = int(input("Enter a number (1-12): "))

month_name = month_all.get(num)

if month_name:
    print(f"The number {num} match with the month of {month_name}")
else:
    print("Please enter just the numbers 1-12")
#Supawit Sangrattanayon 64050694
    

    