def solve():
    n=int(input())
    a=list(map(int, input().split()))

    a.sort()

    for i in range(n-1):
        if a[i]<a[i+1]:
            continue
        else:
            print("NO")
            return
    print("YES")



t=int(input())
for _ in range(t):
    solve()