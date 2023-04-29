# /**
# * author:Hisoka-TheMagician
# * created: 29/04/2023 17:08 Chennai, India
# **/
        

'''

editorial

'''



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
    
    

    
def solve():
    n=ii()
    graph =defaultdict(list)
    ans=[-1]*(n-1)

    f=0
    for i in range(n-1):
        x,y=mii()

        graph[x]+=[(y,i)]
        graph[y]+=[(x,i)]

        if len(graph[x])>2 or len(graph[y])>2:
            f=1
    if f:
        print(-1)
        return
    
    

    
    cur=0
    prev=None

    for node in graph:
        if len(graph[node])==1:
            cur=node
            break
    
    for p in range(n-1):
        for x,i in graph[cur]:
            if x!=prev:
                ans[i]=[2,3][p%2]
                cur,prev=x,cur
                break
    
    print(*ans)





    
    
    
    
t=ii()
for _ in range(t):
    solve()