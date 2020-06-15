#!  /usr/bin/env  python3
print("Problem:")
print("   Write a Python program to display the examination schedule. (extract the date from exam_st_date). ")
print("Solution:")
a = tuple(input().split(","))
ab=(12,10,2014)
print (a[0]+'/'+a[1]+'/'+a[2])

print("%i/%i/%i"%ab)
