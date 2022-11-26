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


def solve(t):
    s,t="a","a"
    otherA = False
    otherB = False
    n=int(input())

    cntA=0
    cntB=0


    for i in range(n):
        d,k,x=input().split()
        d=int(d)
        k=int(k)
        for c in x:
            if d==1:
                if c!='a':
                    otherA=1
                else:
                    cntA+=k
            else:
                if c!='a':
                    otherB=1
                else:
                    cntB+=k
        if otherB:
            print("YES")
        elif not otherA and cntA<cntB:
            print("YES")
        else:
            print("NO")



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