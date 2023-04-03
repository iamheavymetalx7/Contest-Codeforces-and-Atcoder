def solve():

    n,m=map(int, input().split())
    n0=n
    cnt2=0;cnt5=0
    k=1

    while n>0 and n%2==0:
        n//=2
        cnt2+=1
    
    while n>0 and n%5==0:
        n//=5
        cnt5+=1
    
    while cnt2<cnt5 and k*2<=m:
        k*=2
        cnt2+=1

    while cnt5<cnt2 and k*5<=m:
        k*=5
        cnt5+=1
    
    while k*10<=m:
        k*=10

    if k==1:
        print(n0*m)
        return
    else:
        k*=(m//k)
        print(n0*k)
        return
    



t=int(input())
for _ in range(t):
    solve()