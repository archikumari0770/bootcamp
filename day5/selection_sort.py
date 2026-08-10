'''Implement  selection  sort'''
l=[3,5,8,1,2,7]
n=len(l)
min=l[0]
for i in range(n-1):
    for j in range(n-1):
        if min>l[j]:
            temp=min
            min=l[j]
            l[j]=temp
        elif l[j]>min:
            continue
        else:
            continue
print(l)