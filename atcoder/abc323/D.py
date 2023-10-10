from bisect import *
from heapq import *
from collections import defaultdict,Counter
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

def solve():
    n=int(input())
    a =[]
    c = Counter()
    for _ in range(n):
        si,ci = map(int, input().split())
        heappush(a,si)
        c[si]+=ci
    ans=0
    while a:
        x = heappop(a)
        k = c[x]
        if k//2>0 and (x*2 not in c):
            heappush(a,x*2)
        
        c[2*x]+=k//2
        ans+=k%2
    print(ans)



def main():
    solve()

if __name__ == "__main__":
    main()