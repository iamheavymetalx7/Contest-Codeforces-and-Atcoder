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
    A=list(map(int,input().split()))

    B=defaultdict(int)
    for i in range(n):
        if B.get(A[i]%10,0)>=3:
            continue
        B[A[i]%10]=B.get(A[i]%10,0)+1

    C=[]
    for i,j in B.items():
        C+=[i]*j
    
    for i in range(len(C)):
        for j in range(i+1, len(C)):
            for k in range(j+1,len(C)):
                if (C[i]+C[j]+C[k])%10==3:
                    return ("YES")
    return ("NO")
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        z = solve(i+1)
        print(z)
 
 
if __name__ == '__main__':
    main()