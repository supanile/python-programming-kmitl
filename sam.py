message = "Do you like Python language (Y or N): "

while True:
    user_input = input(message).upper()

    if user_input == 'Y' or user_input == 'N':
        break
    else:
        message = "Please Enter only Y/y or N/n: "