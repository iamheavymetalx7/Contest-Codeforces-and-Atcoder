# /**
# * author:Hisoka-TheMagician
# * created: 05/05/2023 15:17 Chennai, India
# **/
        

'''

Observation: (a mod b >>  b mod a) iff (a << b)

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
    


def ask(x,y):
    print("?",x+1,y+1,flush=1)
    c=ii()
    return c

n=ii()
ans =[-1]*n

mx=0


for i in range(1,n):
    a=ask(mx,i)
    b=ask(i,mx)

    if a>b:
        ans[mx]=a
        mx=i
    
    else:
        ans[i]=b
ans[mx]=n

print("!",*ans,flush=1)
print(flush=1)

