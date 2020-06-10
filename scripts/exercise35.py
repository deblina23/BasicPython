#!/usr/bin/env python3
def checkVal(a,b):

	if a==b or a+b==5 or a-b==5:
		return True
	else:
		return False

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
17
print(checkVal(a,b))