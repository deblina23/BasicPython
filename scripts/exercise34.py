#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. ")
print("Solution:")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if (a+b)>=15 and (a+b)<=20:
	print("The sum is:", 20)
else:

	print(a+b)
