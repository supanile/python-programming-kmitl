import pandas as pd
df = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\Python-programming-KMITL\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers['company','average-mileage'].mean()
print(mileageDf)
#Supawit Sangrattanayon 64050694