#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to get a string which is n (non-negative integer) copies of a given string. ")
print("Solution:")
str=input("Enter the string:")
copy=int(input("Enter the number of copy you want: "))
if len(str)==0:
	print("Empty String")
	
elif copy>=0 and len(str)>0:
	print(str*copy)
else:

	print("non negetive integer value required")
