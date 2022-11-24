import sys, threading
import math
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
 
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
# note that position of 0 and 1 cannot change
# they have to be the same. Now when we need to check for
# 2, there two possibilities, one that 2 lies inside p[0],p[1] or it lies outside
# if outside, i extend my range, and if inside, the possibilities
# for 2 are r-l+1-2

# similarly if i>=2 lies inside l,r , multiply by r-l+1-i
# else expand the range depending or p[i]....
def solve(t):
    modulo=pow(10,9)+7
    n=int(input())
    A=list(map(int, input().split()))
    pos=[0]*n
    ans=1

    ##storing the position of i
    if len(A)==1:
        print(ans)
        return

    for i in range(n):
        pos[A[i]]=i
    #since position of 0 and 1 are fixed we store it in l and r

    l=min(pos[0],pos[1])
    r=max(pos[0],pos[1])

    for i in range(2,n):
        if pos[i]<r and pos[i]>l:
            ans*=r-l+1-i
            ans%=modulo
        elif pos[i]>r:
            r=pos[i]
        else:
            l=pos[i]
    print(ans)







 
 
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        solve(i+1)
 
 
if __name__ == '__main__':
    main()