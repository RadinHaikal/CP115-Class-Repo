# CORRECT - Process only even numbers
number = 0

while number < 10:
    number += 1  # Counter BEFORE continue

    if number % 2 != 0:  # If odd
        continue  # Skip odd numbers

    # This only executes for even numbers
    print(f"Processing even number: {number}")