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
 
 
def solve():
    n,m=map(int, input().split())
    A=list(map(int, input().split()))

    ##going right
    val_right=0
    right=[0]*n
    for j in range(1,n):
        if A[j]>A[j-1]:
            right[j]=right[j-1]
        else:
            val_right+=abs(A[j]-A[j-1])
            right[j]=val_right

    val_left=0
    left=[0]*n
    for j in range(n-2,-1,-1):
        if A[j]>A[j+1]:
            left[j]=left[j+1]
        else:
            val_left+=abs(A[j]-A[j+1])
            left[j]=val_left

    for j in range(m):
        p,q=map(int, input().split())
        if p<q:
            print(abs(right[q-1]-right[p-1]))
        else:
            print(abs(left[p-1]-left[q-1]))

 
 
def main():
    t = 1
    if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
        sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
        sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
    sys.setrecursionlimit(10**5)
 
    solve()
 
 
if __name__ == '__main__':
    main()