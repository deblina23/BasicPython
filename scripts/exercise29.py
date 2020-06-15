#!/usr/bin/env python3
print("Problem:")
print("   Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. ")
print("Solution:")
def lstCompare(lst1,lst2):
	
	return lst1-(lst1.intersection(lst2))
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(lstCompare(color_list_1,color_list_2))

print(color_list_1.difference(color_list_2))
