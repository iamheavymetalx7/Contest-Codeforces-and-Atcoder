# /**
# * author:Hisoka-TheMagician
# * created: 08/05/2023 18:22 Chennai, India
# **/
        



# By sudmondal2002, contest: Codeforces Round 872 (Div. 2), problem: (C) LuoTianyi and the Show, Accepted, #, Copy
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
    n,k=mii()
    a=lmii()
    cntleft=0
    cntright=0
    cntseats=0

    seats=[]
    # print(a)
    for i in range(n):
        if a[i]==-1:
            cntleft+=1
        elif a[i]==-2:
            cntright+=1
        else: 
            cntseats+=1
            seats.append(a[i])
    
    m=len(set(seats))

    nseats=sorted(list(set(seats)))
    # print(nseats)
    ans=m+max(cntleft,cntright)




    for i in range(m):
        tmp=1
        tmp+=min(nseats[i]-1,cntleft+i)
        tmp+=min(cntright+m-i-1,k-nseats[i])
        ans=max(ans,tmp)
    
    print(min(ans,k))

        




    
xxx=ii()
for _ in range(xxx):
    solve()