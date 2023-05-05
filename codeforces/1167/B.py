# /**
# * author:Hisoka-TheMagician
# * created: 05/05/2023 12:21 Chennai, India
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
    
    

    
a=[4,8,15,16,23,42]
n=len(a)
squares=[i*i for i in a]
# print(squares)
dic=defaultdict(int)
for i in range(n):
    for j in range(i+1,n):
        dic[a[i]*a[j]] = [a[i],a[j]]

# print(dic)
seen=set(a)

ans=[0,0,0,0,0,0]
print("?",1,1,flush=True)
q=int(input())
idx=squares.index(q)
# print(idx)
ans[0]=a[idx]

print("?",1,6,flush=True)
q=int(input())
val1,val2=dic[q]
ans[-1]=q//(ans[0])
seen.remove(val1)
seen.remove(val2)

arr=[]
print("?",2,5,flush=True)
q=ii()
prev=q
v1,v2=dic[q]
arr.append(v1)
arr.append(v2)
print("?",4,5,flush=True)
q=ii()
v11,v22=dic[q]
arr.append(v11)
arr.append(v22)

cf=Counter(arr)

for k,v in cf.items():
    if v==2:
        ans[-2]=k
ans[-3] = q//(ans[-2])
ans[1] = prev//(ans[-2])

seen.remove(ans[-3])
seen.remove(ans[-2])
seen.remove(ans[1])

rem =list(seen)
# print(rem)
ans[2]=rem[0]


print("!",*ans,flush=True)

