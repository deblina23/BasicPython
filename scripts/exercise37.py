#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to display your details like name, age, address in three different lines. ")
print("Solution:")
def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


personal_details()
