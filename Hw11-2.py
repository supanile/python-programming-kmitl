class Product:
    def __init__(self, product_name, amount, purchase_date):
        self.product_name = product_name
        self.amount = amount
        self.purchase_date = purchase_date

    def total_price(self, price_per_unit):
        return self.amount * price_per_unit

product_name = input("Enter Product name: ")
amount = int(input("Enter Amount: "))
purchase_date = input("Enter Purchase date from 7-11: ")
price_per_unit = float(input("Enter price per unit: "))

product = Product(product_name, amount, purchase_date)

total_price = product.total_price(price_per_unit)

print(f"Total price for {product.amount} units of {product.product_name} purchased on {product.purchase_date} from 7-11 is: {total_price} THB")
#Supawich Sangrattanayon 64050694

