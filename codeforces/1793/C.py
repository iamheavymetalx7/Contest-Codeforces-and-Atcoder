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
    
from collections import deque
    
def solve(t):
    n=ii()
    a=lmii()
    q=deque()

    lis = [(i+1) for i in range(n)]
    lis=deque(lis)

    if a==lis:
        print(-1)
        return
    if a[0]!=lis[0] and a[0]!=lis[-1] and a[-1]!=lis[0] and a[-1]!=lis[-1]:
        print(1,n)
        return

    for i in range(n):
        q.append(a[i])

    
    i,j=0,n-1
    ele1,elen=1,n
    while q:
        # print(ele1,elen,"new")
        fir,sec=False,False
        if a[i]==ele1 or a[i]==elen:
            fir=True
        if a[j]==ele1 or a[j]==elen:
            sec=True
        if fir and len(q)>0:
            popped = q.popleft()
            # print(popped,"from frist")
            if popped==ele1:
                ele1+=1
            else:
                elen-=1
            i+=1
        if sec and len(q)>0:
            popped = q.pop()
            # print(popped, "from back")
            if popped==ele1:
                ele1+=1
            else:
                elen-=1
            j-=1
        if not fir and not sec:
            print(i+1,j+1)
            return
    print(-1)
    

        

            
    
    
    
def main():
    t = 1
    # if path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt"):
    #     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
    #     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w')
    #     start_time = time.time()
    #     print("--- %s seconds ---" % (time.time() - start_time))
 
 
    sys.setrecursionlimit(10**5)
 
    t = int(input())
 
    for i in range(t):
        solve(i+1)
 
 
if __name__ == '__main__':
    main()
    
 


