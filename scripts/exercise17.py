#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to test whether a number is within 100 of 1000 or 2000. ")
print("Solution:")
number=int(input())
if number>=100 and number<=1000:
	print("the number is between 100 and 1000")
elif number >1000 and number<2000:
	print("number is between 1000 and 2000")
else:
	print("the number is either less than 100 or greater than 2000")
	

print(((abs(1000-number)<=100)or (abs(2000-number)<=100)))
