#count the number of zeroes in a sorted binary array
l=[1,1,1,1,1,0,0,0]
count=0
n=len(l)
for (i=0;i<n;i++){
    if (l[i]==0){
        count++;
    }
}
return count;