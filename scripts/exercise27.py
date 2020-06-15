#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to concatenate all elements in a list into a string and return it. ")
print("Solution:")
def inputLst():
	lst=list(input("Enter the list elements with comma seperated: ").split(","))
	return lst
	
	

sum=""
for i in inputLst():
	sum=sum+i
	

print(sum)
