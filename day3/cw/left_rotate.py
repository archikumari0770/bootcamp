# left rotate a given array
l=[]
n=int(input("enter the size of the array"))
for i in range(0,n):
    x=int(input("enter the elemt"))
    l.append(x)
temp=l[0]
for i in range(n-1):
    l[i]=l[i+1]

l[n-1]=temp
print(l)