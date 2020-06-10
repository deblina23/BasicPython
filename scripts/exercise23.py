#!/usr/bin/env python3
def subStrng(pos,strVal):
	subStr=strVal[:pos]
	return subStr
	
str=input("Enter the string:")
copy=int(input("Enter the number of copy:"))
if len(str)>2:
	print("The Substring value is: "+subStrng(2,str)*copy)
else:
17
	print("The length is less than or equal to 2:"+(str*copy))
