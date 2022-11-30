import sys, threading
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq

## pure observation based
 
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
    
    
def solve(t):
    n=ii()
    r1,c1,r2,c2,r3,c3=mii()
    x,y=mii()

    x_cnt, y_cnt =defaultdict(int),defaultdict(int)

    x_cnt[r1]+=1
    x_cnt[r2]+=1
    x_cnt[r3]+=1
    y_cnt[c1]+=1
    y_cnt[c2]+=1
    y_cnt[c3]+=1

    if x_cnt[r1]==2:
        r=r1
    if x_cnt[r2]==2:
        r=r2
    if y_cnt[c1]==2:
        c=c1
    if y_cnt[c2]==2:
        c=c2
    
    if abs(x-r)%2==0 or abs(y-c)%2==0:
        if (r==1 or r==n) and (c==1 or c==n):
            if x==r or y==c:
                print("YES")
                return
            print("NO")
            return
        print("YES")
        return
    print("NO")
    return
            


    
    
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