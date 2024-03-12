N = int(input("Enter N: "))
max_num = float('-inf')  
min_num = float('inf')   
i = 0

while i <= N:
    num = float(input("Enter a number : "))

    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

    i += 1

print("Max :", int(max_num))
print("Min :", int(min_num))