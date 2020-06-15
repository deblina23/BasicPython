#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to check whether a file exists. ")
print("Solution:")
from os import path
paths="Important notes.txt"

print(path.exists(paths))
