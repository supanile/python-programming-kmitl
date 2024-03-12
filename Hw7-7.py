def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

def main():
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    
    quotient, remainder = divide(dividend, divisor)
    
    print(f"Quotient: {quotient}, Remainder: {remainder}")

main()
#Supawit Sangrattanayon 64050694                                