#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to count the number 4 in a given list. ")
print("Solution:")
def inputList():
	lst=[]
	n=int(input("Enter the number:"))
	for i in range(0,n):
		ele=int(input())
		
		lst.append(ele)
		
	return lst

number=inputList()
count=0
for num in number:
	if num == 4:
		count=count+1
		
		

print("The count of 4 in list is: "+str(count))		
