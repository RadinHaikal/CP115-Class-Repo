item_name = str(input("Enter the name of the item: "))
item_price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
subtotal = item_price * quantity
tax_rate = 0.06
total_tax = subtotal * tax_rate
total_cost = subtotal + total_tax
print("subtotal: RM", round(subtotal, 2))
print("tax amount: RM", round(total_tax, 2))
print("total cost: RM", round(total_cost, 2))