import sys, threading
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
 
##got the idea of sorting and greedy

## tried greedy once using (Xi,Yi) and then using (Yi,Xi)

## Ans had to be done using creating new array Yi-Xi, and then sorting (reverse way) and two pointer
 
# # # # # # # # # # # # # # # #
#       JAI SHREE RAM         #
# # # # # # # # # # # # # # # #
 
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
 
def solve(t):
    n=int(input())
    X=list(map(int, input().split()))
    Y=list(map(int, input().split()))

    ar=[0]*n
    for i in range(n):
        ar[i] = Y[i]-X[i]

    ar.sort(reverse=True)

    l,r=0,n-1

    cnt=0
    while l<r:
        if ar[l]+ar[r]>=0:
            cnt+=1
            l+=1
            r-=1
        else:
            r-=1
    print(cnt)




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