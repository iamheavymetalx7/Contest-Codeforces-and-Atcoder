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
 
 
def solve():
    n,l=map(int,input().split())
    pos=list(map(int,input().split()))
    pos.sort()
    left,right=-1,-1
    if 0 not in pos:
        left=pos[0]-0
    if l not in pos:
        right=l-pos[-1]
    
    if n==1:
        return(max(pos[0]-0,l-pos[0]))
    maxi=-1
    for i in range(len(pos)-1):
        maxi=max(pos[i+1]-pos[i],maxi)
    
    maxi=max(pos[-1]-pos[-2],maxi)

    return(max(left,right, maxi/2))



 
 
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
    z = solve()
    print(z)
 
if __name__ == '__main__':
    main()