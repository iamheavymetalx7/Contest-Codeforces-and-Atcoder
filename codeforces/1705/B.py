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
    cnt=0
    total=0
    j=0
    while j<n and A[j]==0:
        j=j+1
        
    for i in range(j,n-1):
        total+=A[i]
        if A[i]==0:
            total+=1
    
    return(total)
 
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