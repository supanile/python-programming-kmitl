def divide(dividend, divisor):
    # ตรวจสอบว่าตัวหารไม่เป็นศูนย์
    if divisor != 0:
        quotient = dividend // divisor  # หารตัวตั้งด้วยตัวหารและได้ผลหาร
        remainder = dividend % divisor  # หาเศษจากการหาร
        return quotient, remainder
    else:
        print("Error: Division by zero")

def main():
    # รับค่าตัวตั้ง (Dividend) และตัวหาร (Divisor) จากผู้ใช้
    dividend = int(input("Enter Dividend: "))
    divisor = int(input("Enter Divisor: "))
    
    # เรียกใช้ฟังก์ชัน divide เพื่อหาร
    result = divide(dividend, divisor)
    
    # ตรวจสอบว่าการหารสำเร็จหรือไม่
    if result:
        quotient, remainder = result
        print(f"Quotient: {quotient}, Remainder: {remainder}")

# เรียกใช้ฟังก์ชัน main()
main()
