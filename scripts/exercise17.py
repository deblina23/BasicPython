#!/usr/bin/env python3
number=int(input())
if number>=100 and number<=1000:
	print("the number is between 100 and 1000")
elif number >1000 and number<2000:
	print("number is between 1000 and 2000")
else:
	print("the number is either less than 100 or greater than 2000")
	
print(((abs(1000-number)<=100)or (abs(2000-number)<=100)))