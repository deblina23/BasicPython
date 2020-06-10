#!/usr/bin/env python3
import math
def calculateDistance(x1,y1,x2,y2):
	return math.sqrt((abs(x2-x1)**2)+(abs(y2-y1)**2))
	
12
print(calculateDistance(4,0,6,6))