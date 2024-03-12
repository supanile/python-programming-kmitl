user_input = int(input("Enter Number: "))

price_dict = {
    1: user_input * 100,
    2: user_input * 95,
    3: user_input * 90,
}

result = price_dict.get(user_input, user_input * 80)

print(result)