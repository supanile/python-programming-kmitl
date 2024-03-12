def CtoF(C):
    F = 32 + C * (180.0/100.0)
    return F

def main():
    C = float(input("Enter Celsius: "))
    F = CtoF(C)
    print(f"Celsius: {C}, Fahrenheit: {F}")

main()
#Supawit Sangrattanayon 64050694                                