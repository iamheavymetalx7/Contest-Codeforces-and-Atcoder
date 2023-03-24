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
    
'''
Post multiply trying copied from:
By sagarpal1909, contest: Codeforces Round 222 (Div. 1), problem: (A) Maze, Accepted, #, Copy

After Understanding!!

Still can't figure out what's wrong with my code!
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
 
sys.setrecursionlimit(20000)
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
    
# os.read(0, os.fstat(0).st_size)).readline
    
    
def solve():
    n,m,k = mii()

    mat = []

    for i in range(n):
        x = si()
        mat.append(list(x))

    c = 0

    ind1 = -1
    ind2=-1

    for i in range(n):
        for j in range(m):
            if mat[i][j] == ".":
                c += 1
                ind1 = i
                ind2 = j

    if k == 0:
        for i in mat:
            print("".join(i))
    
    elif c-k == 0:
        for i in range(n):
            for j in range(m):
                if mat[i][j] == ".":
                    mat[i][j] = "X"

        for i in mat:
            print("".join(i))
    else:

        vis = set()

        def solve(i,j,rakhlo):
            q = deque()
            q.append((i,j))
            while q:
                i,j = q.popleft()
                vis.add((i,j))
                if len(vis) == rakhlo:
                    return 

                for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    r = x+i
                    c = y+j
                    if 0 <= r < n and 0 <= c < m and mat[r][c] == "." and (r,c) not in vis:
                        q.append((r,c))
                        vis.add((r,c))
                        if len(vis) == rakhlo:
                            return


            return


        solve(ind1,ind2,c-k)


        for i in range(n):
            for j in range(m):
                if mat[i][j] == "." and (i,j) not in vis:
                    mat[i][j] = "X"


        for i in mat:
            print("".join(i))

                                           
solve()