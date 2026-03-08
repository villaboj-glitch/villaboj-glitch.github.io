# Josue VillaBonilla
# 8 MAR 26
# Assignment Name: Circle Formulas Lab
# This program asks the user for the radius of a circle (as a float),
# then calculates and displays the diameter, circumference,
# and area using the correct formulas.

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("The diameter of the circle is", format(diameter, ".1f"))
print("The circumference of the circle is", format(circumference, ".2f"))
print("The area of the circle is", format(area, ".3f"))