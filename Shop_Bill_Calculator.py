item_name = input("Item name is : ")
item_price = float(input("Item price is : "))
item_quantity = int(input("Item quantity is : "))
item_total = item_price*item_quantity
tax = (item_total*10)/100
print(f"The Item name is {item_name} and the quantity is {item_quantity} so the total price is {item_total }")
print(f"Now 10 % tax of the total price is {tax} So, Now you have the total payment is {tax+item_total}")