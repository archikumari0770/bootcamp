'''Implement  bubble sort'''
l=[3,5,8,1,2,7]
n=len(l)
for i in range(n-2):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
        else :
            continue
print(l)