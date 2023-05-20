'''
Idea was correct but getting TLE, due to some non-sense. See the TLE on test case 7
for future, in case you want to solve it. 

Only tight constraints otherwise the question was fine

'''
# # /**
# # * author:Hisoka-TheMagician
# # * created: 20/05/2023 11:13 Chennai, India
# # **/
        




# #bisect.bisect_left(a, x, lo=0, hi=len(a)) is the analog of std::lower_bound()
# #bisect.bisect_right(a, x, lo=0, hi=len(a)) is the analog of std::upper_bound()
# #from heapq import heappop,heappush,heapify #heappop(hq), heapify(list)
# #from collections import deque as dq #deque  e.g. myqueue=dq(list)
# #append/appendleft/appendright/pop/popleft
# #from bisect import bisect as bis #a=[1,3,4,6,7,8] #bis(a,5)-->3
# #import bisect #bisect.bisect_left(a,4)-->2 #bisect.bisect(a,4)-->3
# #import statistics as stat  # stat.median(a), mode, mean
# #from itertools import permutations(p,r)#combinations(p,r)
# #combinations(p,r) gives r-length tuples #combinations_with_replacement
# #every element can be repeated
        
# #Note direct assignment to check somethings doesnt work always
# #say there exists s (list) then ss=s and if we edit ss, it edits s as well
# #always try to use ss=s.copy() if u wish to make changes to ss and not reflect them in s.
# #For example: see **1379A - Acacius and String** for reference
    
# import sys, threading, os, io 
# import math
# import time
# from os import path
# from collections import defaultdict, Counter, deque
# from bisect import *
# from string import ascii_lowercase
# from functools import cmp_to_key
# import heapq
# from bisect import bisect_left as lower_bound
# from bisect import bisect_right as upper_bound
# from io import BytesIO, IOBase								
# # # # # # # # # # # # # # # # #
# #       JAI SHREE RAM         #
# # # # # # # # # # # # # # # # #
 
 
# def lcm(a, b):
#     return (a*b)//(math.gcd(a,b))
 
 
# input = lambda: sys.stdin.readline().rstrip()
# def lmii():
#     return list(map(int,input().split()))

# def ii():
#     return int(input())

# def si():
#     return str(input())
# def lmsi():
#     return list(map(str,input().split()))
# def mii():
#     return map(int,input().split())

# def msi():
#     return map(str,input().split())

# i2c = lambda n: chr(ord('a') + n)
# c2i = lambda c: ord(c) - ord('a')
    
    
# # if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
# #     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
# #     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
# # else:
# #     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    
# def solve():
#     n,m=mii()
#     a=lmii()
#     cf=Counter(a)
#     lis=list(set(a))

#     lis.sort()

#     # print(cf)
#     mod=10**9+7
#     # print(lis)

#     total=0

#     for i,ele in enumerate(lis):
#         ans=1

#         idx=bisect_left(lis,ele+(m))
#         # print(idx,"idxxx")
#         if idx-i<m:
#             break
#         for id in range(i,idx):
#             # print(id)
            
#             ans= (ans * cf[lis[id]]) 
#             ans = ans%mod
        
#         total+=ans
#         total = total%mod
#     print(total%mod)


        



    
    
    
    
# xxx=ii()
# for _ in range(xxx):
#     solve()

from __future__ import print_function
from math import log2
from collections import defaultdict, deque
import os
import random
import sys
from io import BytesIO, IOBase
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
#import time
 
def main():
    pass
 
# region fastio
 
BUFSIZE = 8192
def lcm(a,b):
    return (a*b)//gcd(a,b)
def ceilDiv(a,b):
    if a%b==0:
        return a//b
    else:
        return a//b+1
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

class myDict:
    def __init__(self,func):
        self.RANDOM = random.randint(0,1<<32)
        self.default=func
        self.dict={}
    def __getitem__(self,key):
        myKey=self.RANDOM^key
        if myKey not in self.dict:
            self.dict[myKey]=self.default()
        return self.dict[myKey]
    def __setitem__(self,key,item):
        myKey=self.RANDOM^key
        self.dict[myKey]=item
    def __iter__(self):
        return iter(i^self.RANDOM for i in self.dict)
    def __contains__(self,key):
        return key^self.RANDOM in self.dict
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
#sys.stdin, sys.stdout =open("test.txt","r"),open("result.txt","w")
#ini=time.time()
input = lambda: sys.stdin.readline().rstrip("\r\n")
mod=10**9+7
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) ]))
def invr():
    return(map(int,input().split()))

for _ in range(inp()):
    n,m=invr()
    l=inlt()
    d=myDict(int)
    for i in l:
        d[i]+=1
    x=[]
    for i in d:
        x.append(i)
    x.sort()
    if len(x)<m:
        print(0)
        continue
    ps=[d[i] for i in x]
    ans=0
    cur=1
    for i in range(m):
        cur*=ps[i]
        cur%=mod
    if x[m-1]-x[0]<m:
        ans+=cur
    for i in range(m,len(x)):
        cur*=ps[i]
        cur%=mod
        cur*=pow(ps[i-m],mod-2,mod)
        if x[i]-x[i-m+1]<m:
            ans+=cur
            ans%=mod
    print(ans%mod)