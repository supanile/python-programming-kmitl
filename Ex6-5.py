max_num = float('-inf')
max_pos = 0

for i in range(1,11):
    num = int(input("Enter a number %d: " % i))
    
    if num > max_num:
        max_num = num
        max_pos = i

print("The maximum value entered in the sequence is:", max_num)
print("Position of the maximum value:", max_pos)
#Supawit Sangrattanayon 64050694


