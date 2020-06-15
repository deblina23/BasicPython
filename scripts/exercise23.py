#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. ")
print("Solution:")
def subStrng(pos,strVal):
	subStr=strVal[:pos]
	return subStr
	
str=input("Enter the string:")
copy=int(input("Enter the number of copy:"))
if len(str)>2:
	print("The Substring value is: "+subStrng(2,str)*copy)
else:

	print("The length is less than or equal to 2:"+(str*copy))
