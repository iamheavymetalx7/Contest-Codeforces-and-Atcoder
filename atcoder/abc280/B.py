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
    N=ii()
    S=lmii()

    arr=[0]*N

    arr[0]=S[0]
    add=0
    for i in range(1,N):
        add+=arr[i-1]
        arr[i]=S[i]-add
    print(*arr)

    
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Atcoder/input.txt"):
  
        sys.stdout = open('/Users/nitishkumar/Documents/Template_Codes/Python/CP/AtCoder/output.txt','w')
        sys.stdin = open('/Users/nitishkumar/Documents/Template_Codes/Python/CP/AtCoder/input.txt','r')

        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
    solve()
 
 
if __name__ == '__main__':
    main()