#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. ")
print("Solution:")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a==b or b==c or c==a:
	print("Sum=0")
else:

	print("Sum=: ",a+b+c)
