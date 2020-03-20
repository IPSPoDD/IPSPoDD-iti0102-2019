"""Ask user a shape and a radius or a side length and calculate the shape area."""

import math

shape = input("Please insert geometric shape: ")


if shape == "triangle":
    a = float(input("Please insert side length in cm: "))
    sa = a**2 * math.sqrt(3) / 4
    print("The area is " + str(round(sa, 2)) + " cm^2")

elif shape == "square":
    b = float(input("Please insert side length in cm: "))
    sb = b**2
    print("The area is " + str(round(sb, 2)) + " cm^2")

elif shape == "circle":
    c = float(input("Please insert radius in cm: "))
    sc = math.pi * (c**2)
    print("The area is " + str(round(sc, 2)) + " cm^2")

else:
    print("Shape is not supported.")
