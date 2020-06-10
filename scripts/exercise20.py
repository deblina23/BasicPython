#!/usr/bin/env python3
str=input("Enter the string:")
copy=int(input("Enter the number of copy you want: "))
if len(str)==0:
	print("Empty String")
	
elif copy>=0 and len(str)>0:
	print(str*copy)
else:
16
	print("non negetive integer value required")