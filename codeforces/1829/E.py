# /**
# * author:Hisoka-TheMagician
# * created: 06/05/2023 20:50 Chennai, India
# **/
        




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
    
    

'''

iterative dfs

'''
    
def solve():
    n,m=mii()
    arr=[]
    for i in range(n):
        a=lmii()
        arr.append(a)
    
    dire=[(1,0),(0,1),(-1,0),(0,-1)]
        
        
    
    maxi=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                volume=arr[i][j]
                arr[i][j]=0
                q=deque()
                q.append((i,j))

                while q:
                    x,y=q.pop()
                    for dx,dy in dire:
                        dx+=x
                        dy+=y
                        if 0<=dx<n and 0<=dy<m and arr[dx][dy]:
                            volume+=arr[dx][dy]
                            arr[dx][dy]=0
                            q.append((dx,dy))
                maxi=max(maxi,volume)
    
    print(maxi)


    
    
    
    
xxx=ii()
for _ in range(xxx):
    solve()