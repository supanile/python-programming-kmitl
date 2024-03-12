def addInterest(balances, rate): # ฟังก์ชันที่ใช้ในการเพิ่มดอกเบี้ยในลิสต์
    # ทำการวนลูปผ่านทุกตัวแปรในลิสต์ balances
    for i in range(len(balances)):
        # ทำการคูณค่าที่อยู่ในลิสต์ที่ดัชนี i ด้วย (1 + rate) เพื่อเพิ่มดอกเบี้ย
        balances[i] = balances[i] * (1 + rate)

def test(): # ฟังก์ชันที่เป็นที่เรียกในการทดสอบโปรแกรม
    amounts = [1000, 2200, 800, 360] # สร้างลิสต์ชื่อ amounts ที่มีค่าตั้งต้นคือ [1000, 2200, 800, 360]
    rate = 0.05 # กำหนดค่า rate เป็น 0.05
    addInterest(amounts, rate) # เรียกใช้ฟังก์ชัน addInterest เพื่อเพิ่มดอกเบี้ยในลิสต์ amounts
    print(amounts) # แสดงผลลัพธ์ของลิสต์ amounts

test()  # การเรียกใช้ฟังก์ชัน test เพื่อเริ่มการทำงานของโปรแกรม
#Supawit Sangrattanayon 64050694

