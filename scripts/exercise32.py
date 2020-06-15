#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to get the least common multiple (LCM) of two positive integers. ")
print("Solution:")
def gcd(a,b):
	if b==0:
		return a
	else: 
		return gcd(b,a%b)

def lcm(a,b):
	return (a*b)/gcd(a,b)
	
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The LCM is: ",lcm(a,b))

	
