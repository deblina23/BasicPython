#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. ")
print("Solution:")

amt = 10000
int = 3.5
years = 7

future_value  = amt*((1+(0.01*int)) ** years)

print(round(future_value,2))
