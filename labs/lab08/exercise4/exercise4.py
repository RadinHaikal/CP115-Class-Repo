current_reading = int(input())
previous_reading = int(input())

consumption = current_reading-previous_reading

if consumption >= 20:
    water_cost = 0.57

print(consumption)
print(water_cost)
print(total_bill)
