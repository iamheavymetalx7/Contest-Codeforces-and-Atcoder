# import os,sys,io, threading
# if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
#     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
#     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    

def solve():
    n=int(input())
    a=list(map(int, input().split()))

    
    diffs=[]

    for i in range(n-1):
        if a[i]>a[i+1]:
            diffs.append((a[i]-a[i+1],i+1))
    
    diffs.sort()

    s=1
    ans=[]
    for ele in diffs:
        x=ele[0]
        while x>0:
            x-=s
            s+=1
            ans.append(ele[1]+1)

    
    if len(ans)!=n:
        ans.extend([n]*(n-len(ans)))

    print(*ans)



t = int(input())
for _ in range(t):
    solve()