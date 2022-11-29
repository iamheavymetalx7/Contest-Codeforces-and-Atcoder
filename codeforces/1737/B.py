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


'''
If x is lying in range n^2 to (n+1)^2 ,
it will give floor(sqrt(x)) = n. 
How many numbers are these?
(n+1)^2 - n^2 = 2*n+1 numbers. 
How many numbers among these are 
divisible by n or you can say how 
many multiples does n have in these
2*n+1 numbers? That is just 
ceil(2*n+1/n) = 3 luxury numbers.
'''
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
 
si= lambda:str(input())
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')



def mySqrt(x):
    l, r = 0, x
    while l <= r:
        mid = l + (r-l)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            r = mid - 1
        else:
            l = mid + 1
    
def solve(t):
    l,r=mii()
    left_sqrt = mySqrt(l)
    right_sqrt=mySqrt(r)

    ans=max(0,right_sqrt-left_sqrt-1)*3

    if left_sqrt*left_sqrt>=l and left_sqrt*left_sqrt<=r:
        ans+=1
    if (left_sqrt+1)*left_sqrt>=l and (left_sqrt+1)*left_sqrt<=r:
        ans+=1
    if (left_sqrt+2)*left_sqrt>=l and (left_sqrt+2)*left_sqrt<=r:
        ans+=1
    
    if left_sqrt!=right_sqrt:
        if right_sqrt*right_sqrt>=l and right_sqrt*right_sqrt<=r:
            ans+=1
        if (right_sqrt+1)*right_sqrt>=l and (right_sqrt+1)*right_sqrt<=r:
            ans+=1
        if (right_sqrt+2)*right_sqrt>=l and (right_sqrt+2)*right_sqrt<=r:
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