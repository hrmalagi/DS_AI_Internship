item_name=input("Enter the Item Name:")
quantity=int(input("Enter the quantity of the item:"))
price=float(input("price of the item:"))
in_stock=True
print(f"Item: {item_name}, Qty: {quantity}, Price: {price}, Available: {in_stock}")
Totalcost= quantity*price
print(f"Total Cost: {Totalcost}")