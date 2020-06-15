#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. ")
print("Solution:")
str=input("Enter the input String: ")
if str.find("Is")==0 or str.find("is")==0:
	print("true")
else:

	print("Is "+str)
