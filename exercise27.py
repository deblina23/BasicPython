#!/usr/bin/env python3
def inputLst():
	lst=list(input("Enter the list elements with comma seperated: ").split(","))
	return lst
	
	

sum=""
for i in inputLst():
	sum=sum+i
	
print(sum)
