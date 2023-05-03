import sys
input = sys.stdin.readline
import bisect


t=int(input())
for tests in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))

    for i in range(1,n):
        B[i]=max(B[i-1],B[i])

    ANS=1<<30

    for i in range(n):
        k=A[i]

        x=bisect.bisect(B,k)

        ANS=min(ANS,x+i)


    print(ANS)

    
