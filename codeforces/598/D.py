from collections import defaultdict as dd, deque as dq, Counter as ctr

from re import finditer,search

import sys


input = lambda: sys.stdin.buffer.readline().decode('utf-8').rstrip('\r\n')
 
from bisect import bisect_left as bl
from bisect import bisect_right as br
from array import array

inp = lambda: int(input())
mi = lambda x=int : map(x, input().split())
arr= lambda d='i',x=int: array(d,mi(x))
li = lambda x=int: list(mi(x))
lb = lambda x=int: list(map(x, input()))
ls = lambda: list(input())
bi = lambda n: bin(n).replace("0b", "")



yn = ['No', 'Yes']
YN = ['NO', 'YES']
YY = "YES"
NN = "NO"
yy = "Yes"
nn = "No"
alp='#abcdefghijklmnopqrstuvwxyz'
inf= sys.maxsize
mod=1000000007

import heapq as hq

mod=998244353

from math import ceil,gcd,fabs



def main(kase):
    n,m,k=mi()
    grd=[input() for i in range(n)]

    vstd=[[False for i in range(m)] for j in range(n) ]
    ans=[[False]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grd[i][j]=='.' and not vstd[i][j]:
                t=[0]
                q=[(i,j)]
                
                vstd[i][j]=True
                while q:
                    x,y=q.pop()
                    ans[x][y]=t
                    for u,v in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if 0<=u<n and 0<=v<m:
                            if grd[u][v]=='.' and not vstd[u][v]:
                                vstd[u][v]=True
                                q.append((u,v))
                            elif grd[u][v]=='*':
                                t[0]+=1
    # for x in ans: print(x)
    for _ in range(k):
        u,v=mi()
        print(*ans[u-1][v-1])

if __name__ == "__main__":
    test_Cases=1
    # test_Cases=inp()
    for i in range(1,test_Cases+1):
        main(i)
    