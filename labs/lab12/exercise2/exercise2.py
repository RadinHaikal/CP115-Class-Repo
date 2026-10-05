current_number = 0
for i in range (100):
    current_number += 1 
    if (current_number % 7 == 0) and (current_number % 13 == 0):
        found_number = current_number
        break



print(found_number)
