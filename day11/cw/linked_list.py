# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#creating the node
head=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
#storing the address of the next element
head.next=second
second.next=third
third.next=fourth

#traverse
temp =head
while temp is not None:
    print(temp.data,end=' ')
    temp=temp.next
#counting the number of elements in the linked list
count=0
temp =head
while temp is not None:
    count+=1
    temp=temp.next
print("\n the nnumber of elements are ",count)
#searching i n the linked list
key=30
temp =head
while temp is not None:
    if temp.data==key:
        print("yes the key is present")
        break
        
    else:
        temp=temp.next
        
#inserting at the first and last position
#at first
five=Node(50)
five.next=head
head=five
temp =head
while temp is not None:
    print(temp.data,end=' ')
    temp=temp.next
#at last
print("\n")
six=Node(60)
six.next=None
temp=head
while temp.next is not None:
    temp=temp.next
temp.next=six
temp =head
while temp is not None:
    print(temp.data,end=' ')
    temp=temp.next
print("\n")
#inserting at a particular position
seven =Node(70)
index=3
temp=head
for i in range(index-1):
    if temp is not None:
        temp=temp.next

if temp is  not None:
    seven.next=temp.next
    temp.next=seven
temp=head
while temp is not None:
    print(temp.data,end=' ')
    temp=temp.next
#Deleting the elements from starting ,ending and from a particular position
