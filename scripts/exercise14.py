#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to calculate number of days between two dates.Sample dates : (2014, 7, 2), (2014, 7, 11) ")
print("Solution:")
from datetime import datetime

d1=datetime(1985,10,23)
d2=datetime(2020,5,26)
delta=relativedelta.relativedelta(d2,d1)
print(delta.years)
print(delta.months)

print(delta.days)
