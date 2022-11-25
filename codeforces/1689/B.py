# nice approach, took editorial help
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
 
 
def solve(t):
    n=int(input())
    A=list(map(int, input().split()))
    if n==1:
        print(-1)
        return
    B=[(i+1) for i in range(n)]

    for i in range(n-1):
        if A[i]==B[i]:
            B[i],B[i+1]=B[i+1],B[i]

    if A[n-1]==B[n-1]:
        B[n-1],B[n-2]=B[n-2],B[n-1]

    print(*B) 
    return
 
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