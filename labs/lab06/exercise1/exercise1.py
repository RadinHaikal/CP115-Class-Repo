# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
# Without \n - everything prints on one line
Coffee_price = 3.50
Coffee_qty = int(input("Enter the quantity of Coffee: "))
Muffin_price = 2.10
Muffin_qty = int(input("Enter the quantity of Muffin: "))
Water_price = 1.05
Water_qty = int(input("Enter the quantity of Water: "))
Total = (Coffee_price * Coffee_qty) + (Muffin_price * Muffin_qty) + (Water_price * Water_qty)
    Receipt = f"""\n========== Receipt ==========\nItem\tPrice\tQty\tTotal\nCoffee\t$3.50\t{Coffee_qty}\t${Coffee_price * Coffee_qty}\nMuffin\t$2.10\t{Muffin_qty}\t${Muffin_price * Muffin_qty}\nWater\t$1.05\t{Water_qty}\t${Water_price * Water_qty}\n------------------------------\nSubtotal\t\t${Total}\nTax (6%)\t\t${Total * 0.06}\nTotal\t\t${Total * 1.06}\n=============================="""
    print(Receipt)

    