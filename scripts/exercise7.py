#! /usr/bin/env python3
print("Problem:")
print("  Write a Python program to accept a filename from the user and print the extension of that. ")
print("Solution:")
filename=input()
filename=input()
filenamewithoutExtn=filename.split(".")
print(filenamewithoutExtn[0])
print(filenamewithoutExtn[1])
print(repr(filenamewithoutExtn[-1]))
