def calgrade(score):
    if score >= 80:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    else:
        return 'F'

score = float(input("Enter your score: "))

grade = calgrade(score)
print("Your grade is:", grade)
#Supawit Sangrattanayon 64050694


