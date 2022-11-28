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


## s is in between 0 and 9
## now note that we can go upto 100 characters only (maximum) when each of 0 to 9 have 10 appearances
## because distinct chars can only be 10, but freq can get greater than this after that
## all char freq <= no of distinct chars
## after 100 len subtriing the condition will eventually go false
## so we can work this in O(N*100) time complexity

## so we check all substrings of length <=100

## no use of dictionary

    
def solve(t):
    n=ii()
    s=si()

    ans=0

    for i in range(n):
        dis,maxf =0,0
        c=[0]*10
        for j in range(i,i+100):
            if j>=n:
                break
            c[ord(s[j])-ord('0')]+=1
            if c[ord(s[j])-ord('0')]==1:
                dis+=1
            maxf=max(maxf,c[ord(s[j])-ord('0')])

            if maxf<=dis:
                ans+=1
    print(ans)
            
    
    
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