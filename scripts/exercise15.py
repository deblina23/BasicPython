#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to get the volume of a sphere with radius 6. ")
print("Solution:")
from math import pi
radius=float(input("Enther the radious of the sphere:"))
volume=(4/3)*pi*(radius**3)

print(volume)
