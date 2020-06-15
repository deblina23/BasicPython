#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. ")
print("Solution:")
def checkVal(a,b):

	if a==b or a+b==5 or a-b==5:
		return True
	else:
		return False

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

print(checkVal(a,b))
