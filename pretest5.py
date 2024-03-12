message = "PYTHON OK"

# ใช้ method ต่อกัน
result = message.replace(" ", "").lower().capitalize()
result = result.upper().replace("O", " ")

# แสดงผลลัพธ์
print(result)
