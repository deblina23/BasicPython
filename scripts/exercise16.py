#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. ")
print("Solution:")
number=int(input())
if number>17 :
	print(abs(17-number)*2)
else :

	print(17-number)
