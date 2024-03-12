import math

radius_str = input("Enter the radius of the circle: ")

if radius_str.isdigit() and int(radius_str) > 0:
    radius = int(radius_str)

    area = math.pi * radius ** 2

    print("พื้นที่ของวงกลมคือ:", area)
else:
    print("Error: the radius must be a positive number")