'''
Editorial :
There are only two options, move right or move down,
and hence the solution
'''
    
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
    
    
# if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
#     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
#     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    
def solve():
    n=ii()
    arr=[]
    for _ in range(2):
        arr.append(lmii())
    
    suff=[0]*n
    suff[-1]=arr[0][-1]

    for i in range(n-2,-1,-1):
        suff[i]=suff[i+1]+arr[0][i]
    
    pref=[0]*n

    pref[0]=arr[1][0]
    for i in range(1,n):
        pref[i]=pref[i-1]+arr[1][i]

    ans=int(1e18)

    for i in range(n):
        tans=0

        if i!=n-1:
            tans=suff[i+1]
        if i!=0:
            tans=max(tans,pref[i-1])
        ans=min(ans,tans)
    print(ans)





    
    
    
    
t=ii()
for _ in range(t):
    solve()