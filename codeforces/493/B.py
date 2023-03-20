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
    
    
# if(os.path.exists("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt")):
#     sys.stdin = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/input.txt", 'r')
#     sys.stdout = open("/Users/nitishkumar/Documents/Template_Codes/Python/CP/Codeforces/output.txt", 'w') 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    
def solve():
    t = int(input())
    
    p,n = [],[]
    c = 0
    for i in range(t):
        tmp = int(input())
        c += tmp
        if tmp < 0:
            n.append(abs(tmp))
            f = False
        else:
            p.append(tmp)
            f = True
            
    if c == 0:
        if p == n:
            if f:
                print("first")
            else:
                print("second")
        elif p > n:
            print("first")
        else:
            print("second")
    elif c > 0:
        print("first")
    else:
        print("second")



    # n=ii()
    # s=0
    # fir=""
    # sec=""
    # for i in range(n):
    #     a=ii()
    #     # print(a)
    #     s+=a
    #     if a>0:
    #         fir+=str(a)

    #     else:
    #         sec+=str(abs(a))
    # # print(fir)
    # # print(sec)
    # if s>0:
    #     print("first")
    #     return
    # elif s<0:
    #     print("second")
    #     return
    # else:
    #     i=0
    #     while i<min(len(fir),len(sec)):
    #         if int(fir[i])>int(sec[i]):
    #             print("first")
    #             return

    #         elif int(sec[i])>int(fir[i]):
    #             print("second")
    #             return
            
    #         else:
    #             i+=1
    #     if len(fir)>len(sec):
    #         print("first")
    #     elif len(sec)>len(fir):
    #         print("second")
    #     else:
    #         if a>0:
    #             print("first")
    #             return
    #         else:
    #             # print("yaha aaya")
    #             print("second")
    #             return


    
    
    
solve()