#!/usr/bin/env python3
def intTypeCheck(a,b):
	
	if type(a) is int and type(b) is int:
		print(a+b)
	else:
		print("Non-integer value")
		
intTypeCheck(2,3)

intTypeCheck(2,'hello')
