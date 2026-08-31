'''print from n to 1'''

def rec(n):
    if n<0:
        return
    print(n)
    rec(n-1)
    
        

n=int(input("enter the number"))
rec(n)

'''print from 1 to m'''

def rec1(m):
    if n<0:
        return
    
    rec1(m-1)
    print(m)
    
        
rec1(5)
