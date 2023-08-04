import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
s=input().rstrip()
cntx=[0]*3
for i in range(n):
  if s[i]=="X":
    cntx[a[i]]+=1
cntm=[0]*3
ans=0
for i in range(n):
  if s[i]=="M":
    cntm[a[i]]+=1
  elif s[i]=="X":
    cntx[a[i]]-=1
  else:
    for x in range(3):
      for y in range(3):
        se=set()
        se.add(a[i])
        se.add(x)
        se.add(y)
        now=0
        while now in se:
          now+=1
        ans+=now*cntm[x]*cntx[y]
print(ans)