#remove all the spaces and convert the string into lower case
#extract all digits 
# replace evry vowel with *
#convert into upper case wihtout using upper function
s1="Python Programming"
s2="abc123xyz567"
s3="PROGRAMMING"
s4="asdfgh"
s11=s1.lower()
p=s11.replace("","")
print(p)
for i in s2:
    if i in("1234567890"):
        continue
    else:
        print(i,end=" ")
print("/n")
for j in s3:
    if j in ("AEIOUaeiou"):
        print("*",end="")
    else:
        print(j,end="")
        
for i in s4:
    l=ord(i)
    b=l+26
    print(chr(b),end=" ")
