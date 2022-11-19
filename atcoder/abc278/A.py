n,k= map(int,input().split())
arr = list(map(int, input().split()))
for i in range(k):
    arr.pop(0)
    arr.append(0)

print(*arr)
