t = int(input())
for i in range(t):
    a,n = map(int,input().split())
    x=1;
    ans = 0;
    for j in range(18):
        p = a%10;
        q = n%10;
        if(p>q):
            ans+=(10**j) * (10+q - p)
            n=n//10;
            if (n%10 != 1):
                ans = -1
                break
        else:
            ans+=(10**j) * (q-p)
        n=n//10
        a=a//10
    print(ans)
