#!/usr/bin/env python3
def inputLst():
	lst=[]
	n=int(input("Enter the size of the list: "))
	for i in range(0,n):
		ele=int(input())
		
		lst.append(ele)
	return lst
	
	
char=input("Enter the char:" )

for i in inputLst():
	print(char*i)
