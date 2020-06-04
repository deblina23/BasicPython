#!/usr/bin/env python3
def checkEven(nums):
	lst=[]
	if len(nums)<=237:
		for i in range(len(nums)):
			if nums[i]%2==0:
				lst.append(nums[i])
			
	return lst
	
def checkEvenRange(nums):
	lst=[]
	for value in nums:
		if value==237:
			lst.append("we got 237,break the chain")
			break
		elif value%2==0:
			lst.append(value)
	return lst		
			
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
print(checkEven(numbers))
print (checkEvenRange(numbers))