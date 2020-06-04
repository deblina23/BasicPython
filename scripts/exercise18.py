#!/usr/bin/env python3
number1=int(input("Enter number 1:"))
number2=int(input("Enter number 2:"))
number3=int(input("Enter number 3:"))
if number1==number2==number3:
	print(f'{"number1**3 : "}{number1**3}')
else:
	print("%s%s" %(("number1*number2*number3 : "),(number1*number2*number3)))