# /**
# * author:Hisoka-TheMagician
# * created: 03/05/2023 13:59 Chennai, India
# **/
        


'''
By * jaglike_makkar, contest: Codeforces Round 762 (Div. 3), problem: (C) Wrong Addition, Accepted, #, Copy

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
    a,s = [list(i) for i in input().strip().split()]
    for i in range (len(a)):
        a[i]=int(a[i])
    for i in range (len(s)):
        s[i]=int(s[i])
    b = []
    try:
        while(len(a)):
            ai = a.pop()
            si = s.pop()
            if si >= ai:
                b.append(si - ai)
            else:
                si1 = s.pop()
                nn = si1*10 + si
                if nn-ai>=10 or nn-ai <0:
                    x = 1/0
                b.append(nn - ai)
        while(len(s)):
            b.append(s.pop())
        while(b[-1]==0):
            b.pop()
        b.reverse()
        for i in b:
            print(i,end="")
        print()
    except:
        print(-1)
        
    
t=ii()
for _ in range(t):
    solve()