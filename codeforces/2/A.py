from sys import stdin
input = lambda: stdin.readline().rstrip('\r\n')

n=int(input())

p,q=[],{}

for _ in range(n):
    a,b = input().split()
    q[a] = q.get(a,0)+int(b)
    p.append([a,q[a]])

maxi  = max(q.values())

for i,j in p:
    if q[i]==maxi and j>=maxi:
        print(i)
        break
