'''
By AyuAnchor, contest: Codeforces Round 824 (Div. 2), problem: (C) Phase Shift, Accepted, #, Copy
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
    t=si()
    a = 'abcdefghijklmnopqrstuvwxyz'
    baap={}
    beta={}

    for i in range(n):
        if t[i] in beta:
            continue

        j=0
        ct=0
        x=t[i]

        while x in baap:
            x=baap[x]
            ct+=1

        while a[j] in baap or a[j]==t[i] or (x==a[j] and ct!=25):
            j=(j+1)%26

        beta[t[i]] = a[j]
        baap[a[j]] = t[i]
    # print(baap)
    # print(beta)
    for i in t:
        print(beta[i],end="")
    print()




























    # j=0
    # seen=set()
    # ans=""
    # map=defaultdict(int)
    # for i in range(n):
        
    #     if s[i] not in map:

    #         map[s[i]]=chr(j+97)
    #         seen.add(j)
    #         j+=1
    #         ans+=map[s[i]]
    #     else:
    #         ans+=map[s[i]]
    
    # print(ans)

    
    
    
t=ii()
for _ in range(t):
    solve()