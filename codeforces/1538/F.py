for _ in range(int(input())):
    L,R = map(int, input().split())

    ans=0

    while (L!=0 or R!=0):
        ans+=R-L
        L//=10
        R//=10
    
    print(ans)