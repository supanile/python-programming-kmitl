import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\Python-programming-KMITL\\sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='#2B3499', marker='s', markerfacecolor='y', 
      linestyle='-', linewidth=6)
      
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
#Supawit Sangrattanayon 64050694