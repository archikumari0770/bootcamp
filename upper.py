# convert a number to the upper and floor without using the function
target=7
floor=-1
ciel=-1
arr=[10,7,3,12,15]
for nums in arr:
    if nums==target :
        if floor==-1 or nums>floor:
            floor=nums
        
    if nums>target:
        if ciel==-1 or nums<ciel:
            ciel=nums
    
