#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to compute the greatest common divisor (GCD) of two positive integers. ")
print("Solution:")
def gcd(a,b):
	if b==0:
		return a
	else: 
		return gcd(b,a%b)
		
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

print("The greatest common divisor is: ",gcd(a,b))
