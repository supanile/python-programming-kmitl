opr = input("Enter an operator: ")

opr_all = {
    '+': 'num1+num2',
    '-': 'num1-num2',
    '*': 'num1*num2',
    '/': 'num1/num2',
}

result = opr_all.get(opr, 'Unknown operator')
print(result)
#Supawit Sangrattanayon 64050694



