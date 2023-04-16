'''
editorial solution

we keep p >m always so we take p=max(pp,nn) and m=min(pp,nn)
similarly we keep b>a always so we take a=min(x,y).
this ensures that we get the correct relationship at the end which involves inequalities
and we know when dealing with inequalities sign changes will affect out inequality

so to generalise we do this!!
'''

'''

editorial 

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
    s=si()
    cnter = Counter(s)
    pp = cnter["+"]
    nn = cnter["-"]

    p=max(pp,nn)
    m=min(pp,nn)

    q=ii()
    for _ in range(q):
        x,y=mii()
        a=min(x,y)
        b=max(x,y)
 
        if (a==b and m==p) or ((a<b) and ((p-m)*b)%(b-a)==0 and -m<=(((p-m)*b)//(b-a) )<=p):
            print("YES")
        else:
            print("NO")

    
    
    
t=1
for _ in range(t):
    solve()