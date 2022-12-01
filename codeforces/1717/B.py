import sys, threading
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
 
 
# # # # # # # # # # # # # # # #
#       JAI SHREE RAM         #
# # # # # # # # # # # # # # # #
 
##CodeforcesAssemble : GoodImplementation

def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
 
si= lambda:str(input())
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')
    
    
def solve(t):
    n,k,r,c = mii()

    ar=[['.' for i in range(n)] for j in range(n)]

    r,c=r-1,c-1 
    ar[r][c]='X'

    x=r
    y=c

    while x>=0:
        for i in range(y,n,k):
            ar[x][i]='X'
        for i in range(y,-1,-k):
            ar[x][i]='X'
        x,y=x-1,y+1
        if y>=n:
            y=0
    
    x=r
    y=c

    while x<n:
        for i in range(y,n,k):
            ar[x][i]='X'
        for i in range(y,-1,-k):
            ar[x][i]='X'
        x,y=x+1,y-1
        if y<0:
            y=n-1

        
    for i in range(n):
        for j in range(n):
            print(*ar[i][j],end="")
        print()
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        solve(i+1)
 
 
if __name__ == '__main__':
    main()