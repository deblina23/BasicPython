#!/usr/bin/env python3
def inputList():
	lst=[]
	n=int(input("Enter the list range:"))
	for i in range(0,n):
		ele=int(input())
	
		lst.append(ele)
	return lst
	
def checkData(data,lst):

	for i in lst:
		if i==data:
			return True
	
	return False
char=int(input("Enter the data you want to check: "))
25
print(checkData(char,inputList()))