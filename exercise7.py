#! /usr/bin/env python3
filename=input()
filenamewithoutExtn=filename.split(".")
print(filenamewithoutExtn[0])
print(filenamewithoutExtn[1])
print(repr(filenamewithoutExtn[-1]))