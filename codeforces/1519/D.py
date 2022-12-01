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
 
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
 
si= lambda:str(input())
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')
    
    
def solve():
    n=ii()
    a=lmii()
    b=lmii()

    ans=0
    for i in range(n):
        ans+=a[i]*b[i]

    ##odd

    maxi=ans
    for i in range(n):
        total=ans
        l=i-1
        r=i+1
        while l>=0 and r<=n-1:
            total-=a[l]*b[l]+a[r]*b[r]
            total+=a[l]*b[r]+a[r]*b[l]
            maxi=max(maxi,total)
            
            l-=1
            r+=1

    ## even
    for i in range(n):
        total=ans
        l=i
        r=i+1
        while l>=0 and r<=n-1:
            total-=a[l]*b[l]+a[r]*b[r]
            total+=a[l]*b[r]+a[r]*b[l]

            maxi = max(maxi,total)

            l-=1
            r+=1

    print(maxi)

def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
    solve()
 
 
if __name__ == '__main__':
    main()