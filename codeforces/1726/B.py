def solve():
    n, m = map(int, input().split())
    if n > m:
        print("NO")
        return
    if n%2:
        print("YES")
        print(*([1]*(n-1)+[m-n+1]))
        return
    if m%2:
        print("NO")
    else:
        print("YES")
        print(*([1]*(n-2)+[(m-n+2)//2]*2))
 
 
 
import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for i in range(t):
    solve()
