#!/usr/bin/env python3
print("Problem:")
print("  Write a Python program to test whether a passed letter is a vowel or not. ")
print("Solution:")
def checkVowel(letter):
	vowel=['a','e','i','o','u']
	for char in vowel:
		if letter.lower()==char:
			return True
			
	return False		

print(checkVowel(input("Enter the char: ")))
