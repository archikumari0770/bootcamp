
'''Implement  binary search which the elements are in sorted manner'''
l=[1,2,3,4,5,6,7]
n=len(l)
target = 5
left=0
right=n-1
while left<=right:
    mid=(left+right)//2
    if l[mid]==target:
        print("found",target)
        break
    elif l[mid]>target:
        right=mid-1
    elif l[mid]<target:
        left=mid+1
    else:
        print("not found")
