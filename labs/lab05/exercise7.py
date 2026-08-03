import math
one_number = float(input("Enter the first number: "))
from math import sqrt, pow, sin

square_root = sqrt(one_number)
squared = pow(one_number, 2)
cubed = pow(one_number, 3)
sine_value = sin(one_number)

print("The square root of", one_number, "is:", round(square_root, 2))
print("The square of", one_number, "is:", round(squared, 2))
print("The cube of", one_number, "is:", round(cubed, 2))
print("The sine of", one_number, "is:", round(sine_value, 2))

