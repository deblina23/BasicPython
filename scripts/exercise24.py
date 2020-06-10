#!/usr/bin/env python3
def checkVowel(letter):
	vowel=['a','e','i','o','u']
	for char in vowel:
		if letter.lower()==char:
			return True
			
	return False		
15
print(checkVowel(input("Enter the char: ")))