kwh = int(input())
if kwh <= 100:
    totalBill = kwh * 0.3
else:
    if kwh <= 200:
        totalBill = 30 + kwh - 100 * 0.5
    else:
        totalBill = 80 + kwh - 200 * 0.75
print(totalBill)
