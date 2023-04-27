# /**
# * author:Hisoka-TheMagician
# * created: 27/04/2023 13:54 Chennai, India
# **/
        



#By aman_m42, contest: Educational Codeforces Round 108 (Rated for Div. 2), problem: (C) Berland Regional, Accepted, #, Copy

#bisect.bisect_left(a, x, lo=0, hi=len(a)) is the analog of std::lower_bound()
#bisect.bisect_right(a, x, lo=0, hi=len(a)) is the analog of std::upper_bound()
#from heapq import heappop,heappush,heapify #heappop(hq), heapify(list)
#from collections import deque as dq #deque  e.g. myqueue=dq(list)
#append/appendleft/appendright/pop/popleft
#from bisect import bisect as bis #a=[1,3,4,6,7,8] #bis(a,5)-->3
#import bisect #bisect.bisect_left(a,4)-->2 #bisect.bisect(a,4)-->3
#import statistics as stat  # stat.median(a), mode, mean
#from itertools import permutations(p,r)#combinations(p,r)
#combinations(p,r) gives r-length tuples #combinations_with_replacement
#every element can be repeated
        
#Note direct assignment to check somethings doesnt work always
#say there exists s (list) then ss=s and if we edit ss, it edits s as well
#always try to use ss=s.copy() if u wish to make changes to ss and not reflect them in s.
#For example: see **1379A - Acacius and String** for reference
    
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
    a=lmii()
    s=lmii()
    dd=defaultdict(list)
    for i in range(n):
        dd[a[i]].append(s[i])
    
    for ele in dd:
        dd[ele].sort(reverse=True)


    ee=defaultdict(int)

    for k in dd:
        ee[k] = len(dd[k])

        pref=[0]

        # storing prefix sum for each k in dd ( for each uni in dd)
        for el in sorted(dd[k])[::-1]:
            pref.append(pref[-1]+el)
        dd[k] =pref[:]
    
    temp = [0]*n

    ## we make use of the prefix sums to calc the final ans


    for k in dd:
        for l in range(1,ee[k]+1):
            r = ee[k]%l
            temp[l-1]+=dd[k][ee[k]-r]
    
    print(*temp)

    
    # arr=[]
    # for i in range(n):
    #     ans=0

    #     for ele in dd:
    #         idx=(len(dd[ele])//(i+1))*(i+1) if i+1<=len(dd[ele]) else 0
    #         ans+=sum(dd[ele][:idx])
    #     arr.append(ans)
    
    # print(*arr)
    
t=ii()
for _ in range(t):
    solve()