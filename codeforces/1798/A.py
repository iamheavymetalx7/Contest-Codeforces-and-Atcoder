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
    b=lmii()

    # aa=a.copy()
    # bb=b.copy()
    # maxia=max(a)
    # maxib=max(b)

    # if maxia==a[-1] and maxib==b[-1]:
    #     print("Yes")
    #     return
    # for i in range(n):
    #     if b[i]==maxib:
    #         b[i]=a[i]
    #         a[i]=maxib

    
    # # print("-"*10)
    # maxiaa=max(aa)
    # maxibb=max(bb)
    # for i in range(n):
    #     if aa[i]==maxiaa:
    #         aa[i]=bb[i]
    #         bb[i]=maxiaa
    #     # print(aa,bb)
    
    # maxinewa=max(a)
    # maxinewb=max(b)

    # maxinewaa=max(aa)
    # # print(maxinewaa,"this is maxi")
    # maxinewbb=max(bb)

    # if maxinewa==a[-1] and maxinewb==b[-1]:
    #     print("Yes")
    #     return
    # # print(aa[-1],"huh")
    # if maxinewaa==aa[-1] and maxinewbb==b[-1]:
    #     # print("this")
    #     # print("Yes")
    #     return

    # print("No")
    ans=True
    for i in range(n):
        if a[i]<=a[n-1] and b[i]<=b[n-1] or b[i]<=a[n-1] and a[i]<=b[n-1]:
            continue
        else:
            ans=False
            break

    if ans:
        print("Yes")
    else:
        print("No")

    
    
    
    
t=ii()
for _ in range(t):
    solve()