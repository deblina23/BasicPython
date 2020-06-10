#!/usr/bin/env python3
def gcd(a,b):
	if b==0:
		return a
	else: 
		return gcd(b,a%b)
		
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
16
print("The greatest common divisor is: ",gcd(a,b))