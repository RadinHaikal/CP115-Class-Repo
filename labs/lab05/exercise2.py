import math 
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print("The circumference of the circle is: ", round(circumference, 2))
area = math.pi * radius ** 2
print("The area of the circle is: ", round(area, 2))