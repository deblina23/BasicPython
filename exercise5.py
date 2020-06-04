#! /usr/bin/env python3
def rev(name):

  revname=''
  for c in name:
	  revname=c+revname
  return revname
  
print(rev(input()))
	