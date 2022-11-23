
import sys


for _ in range(int(input())):
    n,start=map(str,input().split())
    n=int(n)
    string = str(input())
    string=list(string)

    suffix=[0]*n
    
    if string[n-1]=="g":
        suffix[n-1]=n-1
    else:
        suffix[n-1]=-1
##creating a suffix array
    for i in range(n-2,-1,-1):
        if string[i]=="g":
            suffix[i]=i
        else:
            suffix[i]=suffix[i+1]
    ans=0
    for i in range(0,n):
        if string[i]==start:
            if suffix[i]==-1:
    ##note that if suffix[i] is -1, then we have to iterate 
    ##thro the whole string, which is (n-1)-i, then to reach the 
    ##starting point again, it takes one sec, and then the nearst green
    ##can be found by suff[0], hence total time = n-1-i+1+suffix[0]
                ans=max(ans,(n-1)-i+1+suffix[0])

            else:
                ans=max(ans,suffix[i]-i)


    print(ans)
