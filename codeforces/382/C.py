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
 
 
input = lambda: sys.stdin.readline().rstrip(
)
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
    
    
if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
    sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
    sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    
def solve():
    n=ii()
    a=lmii()
    a.sort()
    idx=-1
    if n==1:
        print(-1)
        return
    if a==[a[0]]*n:
        print(1)
        print(a[0])
        return
    if n==2:
        arr=[]
        cd=a[1]-a[0]
        if cd%2==0:
            new_m = a[0]+(cd//2)
            arr.append(new_m)
        arr.append(a[0]-cd)
        arr.append(a[1]+cd)

        print(len(arr))
        arr.sort()
        print(*arr)
        return
        
    cd1=a[1]-a[0]
    cd2=a[2]-a[1]
    seen=set()
    # print("here1....")
    arr=[]
    i=0
    f=True
    g=False
    while i < n-1:
        # print(a[i+1],a[i],a[i+1]-a[i],f,g)
        if (a[i+1]-a[i])!=cd1:
            if not f:
                g=True
                break
            idx=i
            a[idx]+=cd1
            i-=1
            f=False
        i+=1
    
    if (not g) and (not f):
        if a[idx] not in seen:
            arr.append(a[idx])
        seen.add(a[idx])

        # print(arr,"added")

    # print("start here2...")
    if idx!=-1:
        a[idx]-=cd1
    # print(a)
    i=0
    f=True
    g=False
    while i < n-1:
        # print(a[i+1],a[i])
        if (a[i+1]-a[i])!=cd2:
            if not f:
                g=True
                break
            idx=i
            a[idx]+=cd2
            i-=1
            f=False
        i+=1
    if (not g) and (not f):
        if a[idx] not in seen:
            arr.append(a[idx])
        seen.add(a[idx])

    
    if f:
        # print("here")
        arr.append(a[0]-cd1)
        arr.append(a[-1]+cd1)
    
    print(len(arr))
    arr.sort()
    print(*arr)
            
    
    
    
    
    
    
solve()