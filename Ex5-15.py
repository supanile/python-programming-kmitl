num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))

while True:
    print("=====Menu=====")
    print("1. Lowest")
    print("2. Highest")
    print("3. Summation")
    print("4. Average")
    print("5. Exit")
    print("==============")

    choice = input("Select a choice (1-5): ")

    if choice == '1':
        result = min(num1, num2, num3, num4, num5)
        print(f"The lowest number is: {result}")
    elif choice == '2':
        result = max(num1, num2, num3, num4, num5)
        print(f"The highest number is: {result}")
    elif choice == '3':
        result = num1 + num2 + num3 + num4 + num5
        print(f"The summation is: {result}")
    elif choice == '4':
        result = (num1 + num2 + num3 + num4 + num5) / 5
        print(f"The average is: {result}")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
#Supawit Sangrattanayon 64050694





