#!/usr/bin/env python3
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
		
		
25
print("The count of 4 in list is: "+str(count))		
