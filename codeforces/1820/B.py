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
    s=si()
    n=len(s)

    t=s[-1]+s[:-1]


    if s=="0"*n:
        print(0)
        return

    cnt=0
    for i in range(n):
        if s[i]==t[i] and t[i]=='1':
            cnt+=1
    
    
    if cnt==n:
        print(cnt**2)

    else:
        max_ones=0
        i=0
        cnt=0

        f= True
        while f:
            if s[i%n]=="1":
                cnt+=1
            else:
                max_ones=max(max_ones,cnt)
                cnt=0
            i+=1
            if i>=n and s[i%n]=="0":
                f=False
        max_ones=max(max_ones,cnt)
        print(((max_ones+1)**2)//4)

        



    
    
t=ii()
for _ in range(t):
    solve()