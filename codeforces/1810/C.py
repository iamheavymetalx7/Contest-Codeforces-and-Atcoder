# By mePranav, contest: CodeTON Round 4 (Div. 1 + Div. 2, Rated, Prizes!), problem: (C) Make It Permutation, Accepted, #, Copy
import sys, threading, os, io 
import math
import time
from os import path
from collections import defaultdict, Counter, deque
from bisect import *
from string import ascii_lowercase
from functools import cmp_to_key
import heapq
from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound
from io import BytesIO, IOBase								
# # # # # # # # # # # # # # # #
#       JAI SHREE RAM         #
# # # # # # # # # # # # # # # #
 
 
def lcm(a, b):
    return (a*b)//(math.gcd(a,b))
 
 
input = lambda: sys.stdin.readline().rstrip()
def lmii():
    return list(map(int,input().split()))

def ii():
    return int(input())

def si():
    return str(input())
def lmsi():
    return list(map(str,input().split()))
def mii():
    return map(int,input().split())

def msi():
    return map(str,input().split())

i2c = lambda n: chr(ord('a') + n)
c2i = lambda c: ord(c) - ord('a')
    
    
if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
    sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
    sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
from collections import Counter
def solve():
    n,c,d=mii()
    a=lmii()

    prev=0
    curr=0
    res=c*n+d   ## deleting all and having 1 as the only element
    
    ans=0
    a.sort()

    for i in range(n):
        if a[i]==prev:
            curr+=c      ## will have to remove this as well
            res=min(res,curr+(n-1-i)*c) ## will delete the others after this
            continue

        if a[i]!=prev+1:
            curr+=(a[i]-prev-1)*d       ## would add all these elements missing
        res=min(res, curr+(n-1-i)*c)    ## removing the other elements

        prev=a[i]
    print(res)



        



    
    
    
    
t=ii()
for _ in range(t):
    solve()