num_employees = int(input("จำนวนพนักงานทั้งหมด: "))

for i in range(num_employees):
    name = input("ชื่อ: ")
    income = float(input("เงินได้สุทธิต่อปี (บาท): "))
    
    if income <= 150000:
        tax = 0
    elif income <= 300000:
        tax = (income - 150000) * 0.05
    elif income <= 500000:
        tax = 149999 * 0.05 + (income - 300001) * 0.1
    elif income <= 750000:
        tax = 149999 * 0.05 + 199999 * 0.1 + (income - 500001) * 0.15
    elif income <= 1000000:
        tax = 149999 * 0.05 + 199999 * 0.1 + 249999 * 0.15 + (income - 750001) * 0.2
    elif income <= 2000000:
        tax = 149999 * 0.05 + 199999 * 0.1 + 249999 * 0.15 + 249999 * 0.2 + (income - 1000001) * 0.25
    elif income <= 5000000:
        tax = 149999 * 0.05 + 199999 * 0.1 + 249999 * 0.15 + 249999 * 0.2 + 999999 * 0.25 + (income - 2000001) * 0.3
    else:
        tax = 149999 * 0.05 + 199999 * 0.1 + 249999 * 0.15 + 249999 * 0.2 + 999999 * 0.25 + 3000001 * 0.3 + (income - 5000001) * 0.35
    print(f"ภาษี (บาท) : {tax:,.2f}")
#Supawit Sangrattanayon 64050694


