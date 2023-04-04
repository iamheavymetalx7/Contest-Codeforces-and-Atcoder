
def solve():
    n=int(input())
    a=list(map(int, input().split()))


    
    diffs=[]
    ans=[]

    for i in range(n-1):
        if a[i]>a[i+1]:
            diffs.append((a[i]-a[i+1],i+1))
    
    diffs.sort()
    k=1
    for ele in diffs:
        x=ele[0]
        while x>0:
            ans.append(ele[1]+1)
            x-=k
            k+=1
    
    if len(ans)!=n:
        ans.extend([n]*(n-len(ans)))
    

    print(*ans)



t = int(input())
for _ in range(t):
    solve()